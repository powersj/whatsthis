package storage

import (
	"fmt"
	"sort"
	"strings"

	"github.com/powersj/whatsthis/internal/filesystem"
	"github.com/powersj/whatsthis/internal/units"
	"github.com/powersj/whatsthis/internal/util"
)

// Probe struct for storage. Captures disks, which capture partitions.
type Probe struct {
	sys filesystem.Sys

	Disks []Disk `json:"disks"`
}

// Disk captures information about physical disks.
type Disk struct {
	Name       string      `json:"name"`
	Size       string      `json:"size"`
	Bytes      int64       `json:"bytes"`
	Path       string      `json:"path"`
	Partitions []Partition `json:"partitions"`
}

// Partition captures information about partitions on disks.
type Partition struct {
	Number      string `json:"number"`
	Name        string `json:"name"`
	Description string `json:"description"`
	Size        string `json:"size"`
	Bytes       int64  `json:"bytes"`
	Path        string `json:"path"`
}

// New initializes new probe struct and probes the system.
func New() (*Probe, error) {
	sys := filesystem.Sys{}

	probe := &Probe{sys: sys}
	if err := probe.probe(); err != nil {
		return nil, err
	}

	return probe, nil
}

// Probe the system.
func (p *Probe) probe() error {
	for _, path := range p.sys.ListBlock() {
		if strings.Contains(path, "/sys/class/block/loop") {
			continue
		}

		var uevent map[string]string = p.sys.UEvent(path)
		if uevent["DEVTYPE"] != "disk" {
			continue
		}

		var bytesSize int64 = p.sys.BlockSize(path)
		var disk Disk = Disk{
			Name:       uevent["DEVNAME"],
			Path:       path,
			Bytes:      bytesSize,
			Size:       units.Bits2Human(bytesSize),
			Partitions: p.Partitions(uevent["DEVNAME"]),
		}

		p.Disks = append(p.Disks, disk)
	}

	sort.Slice(p.Disks, func(i, j int) bool {
		return p.Disks[i].Name < p.Disks[j].Name
	})

	return nil
}

// String representation of the struct.
func (p *Probe) String() string {
	var result strings.Builder

	result.WriteString("storage:")

	for _, disk := range p.Disks {
		result.WriteString(fmt.Sprintf("\n  %s:", disk.String()))

		for _, partition := range disk.Partitions {
			result.WriteString(fmt.Sprintf("\n    - %s", partition.String()))
		}
	}

	return result.String()
}

// JSON representation of the struct.
func (p *Probe) JSON() string {
	return util.ObjectJSONString(&p)
}

// Partitions returns all partitions for a particular device.
func (p *Probe) Partitions(parentDevName string) []Partition {
	var partitions []Partition

	for _, path := range p.sys.ListBlock() {
		var uevent map[string]string = p.sys.UEvent(path)
		if uevent["DEVTYPE"] != "partition" {
			continue
		}
		if !strings.HasPrefix(uevent["DEVNAME"], parentDevName) {
			continue
		}

		var bytesSize int64 = p.sys.BlockSize(path)
		var partition Partition = Partition{
			Name:        uevent["DEVNAME"],
			Description: uevent["PARTNAME"],
			Number:      uevent["PARTN"],
			Path:        path,
			Bytes:       bytesSize,
			Size:        units.Bits2Human(bytesSize),
		}

		partitions = append(partitions, partition)
	}

	sort.Slice(partitions, func(i, j int) bool {
		return partitions[i].Number < partitions[j].Number
	})

	return partitions
}

// String representation of the struct.
func (d *Disk) String() string {
	return fmt.Sprintf("%s %s", d.Name, d.Size)
}

// String representation of the struct.
func (p *Partition) String() string {
	return fmt.Sprintf("%s %s %s", p.Name, p.Size, p.Description)
}
