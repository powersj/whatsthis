package network

import (
	"fmt"
	"os"
	"path"
	"path/filepath"
	"sort"
	"strings"

	"github.com/pkg/errors"
	"github.com/powersj/whatsthis/internal/filesystem"
	"github.com/powersj/whatsthis/internal/util"
)

// Probe struct for storage. Splits adapters by physical adapters, virtual
// adapters, and bridges.
type Probe struct {
	sys filesystem.Sys

	Physical []Adapter `json:"physical"`
	Bridges  []Bridge  `json:"bridges"`
	Virtual  []Virtual `json:"virtual"`
}

// Adapter captures a physical adapter.
type Adapter struct {
	Name   string `json:"name"`
	MAC    string `json:"mac"`
	Speed  int    `json:"speed"`
	MTU    int    `json:"mtu"`
	Driver string `json:"driver"`
	Path   string `json:"path"`
}

// Bridge captures bridge devices.
type Bridge struct {
	Name string `json:"name"`
	MAC  string `json:"mac"`
	MTU  int    `json:"mtu"`
	Path string `json:"path"`
}

// Virtual captures non-bridge devices that are virtual.
type Virtual struct {
	Name string `json:"name"`
	MAC  string `json:"mac"`
	MTU  int    `json:"mtu"`
	Path string `json:"path"`
}

// New initializes new probe struct and probes the system.
func New() (*Probe, error) {
	sys := filesystem.Sys{}

	probe := &Probe{sys: sys}
	if err := probe.probe(); err != nil {
		return nil, err
	}

	sort.Slice(probe.Physical, func(i, j int) bool {
		return probe.Physical[i].Name < probe.Physical[j].Name
	})
	sort.Slice(probe.Virtual, func(i, j int) bool {
		return probe.Virtual[i].Name < probe.Virtual[j].Name
	})
	sort.Slice(probe.Bridges, func(i, j int) bool {
		return probe.Bridges[i].Name < probe.Bridges[j].Name
	})

	return probe, nil
}

// Probe the system.
func (p *Probe) probe() error {
	for _, path := range p.sys.ListNetwork() {
		if strings.Contains(path, "/sys/class/net/lo") {
			continue
		}

		if p.regularFile(path) {
			continue
		}

		virtualDev, err := p.isVirtual(path)
		if err != nil {
			return errors.Wrap(err, "error determining virtual device")
		}

		var uevent map[string]string = p.sys.UEvent(path)
		var name string = uevent["INTERFACE"]
		if name == "" {
			name = filepath.Base(path)
		}

		switch {
		case uevent["DEVTYPE"] == "bridge":
			var bridge Bridge = Bridge{
				Name: name,
				MAC:  p.MAC(path),
				MTU:  p.MTU(path),
				Path: path,
			}

			p.Bridges = append(p.Bridges, bridge)
		case virtualDev:
			var virtual Virtual = Virtual{
				Name: name,
				MAC:  p.MAC(path),
				MTU:  p.MTU(path),
				Path: path,
			}

			p.Virtual = append(p.Virtual, virtual)
		default:
			var adapter Adapter = Adapter{
				Name:   name,
				MAC:    p.MAC(path),
				Speed:  p.Speed(path),
				MTU:    p.MTU(path),
				Driver: p.Driver(path),
				Path:   path,
			}

			p.Physical = append(p.Physical, adapter)
		}
	}

	return nil
}

// String representation of the struct.
func (p *Probe) String() string {
	var result strings.Builder

	result.WriteString("network:")

	if len(p.Physical) > 0 {
		result.WriteString("\n  physical:")
		for _, adapter := range p.Physical {
			result.WriteString(fmt.Sprintf("\n    - %s", adapter.String()))
		}
	}

	if len(p.Bridges) > 0 {
		result.WriteString("\n  bridges:")
		for _, bridge := range p.Bridges {
			result.WriteString(fmt.Sprintf("\n    - %s", bridge.String()))
		}
	}

	if len(p.Virtual) > 0 {
		result.WriteString("\n  virtual:")
		for _, virtual := range p.Virtual {
			result.WriteString(fmt.Sprintf("\n    - %s", virtual.String()))
		}
	}

	return result.String()
}

// JSON representation of the struct.
func (p *Probe) JSON() string {
	return util.ObjectJSONString(&p)
}

// Driver returns the device driver.
func (p *Probe) Driver(target string) string {
	var uevent map[string]string = p.sys.UEvent(path.Join(target, "device"))
	return uevent["DRIVER"]
}

// MAC returns the physical MAC address.
func (p *Probe) MAC(target string) string {
	return p.sys.ReadString(path.Join(target, "address"))
}

// MTU returns the device MTU.
func (p *Probe) MTU(target string) int {
	return p.sys.ReadInt(path.Join(target, "mtu"))
}

// Speed returns the speed of the adapter.
func (p *Probe) Speed(target string) int {
	return p.sys.ReadInt(path.Join(target, "speed"))
}

func (p *Probe) isVirtual(target string) (bool, error) {
	dest, err := os.Readlink(target)
	if err != nil {
		return false, errors.Wrap(err, "error reading readlink")
	}

	return strings.Contains(dest, "devices/virtual/net"), nil
}

func (p *Probe) regularFile(target string) bool {
	fi, _ := os.Lstat(target)
	return fi.Mode().IsRegular()
}

// String representation of the struct.
func (a *Adapter) String() string {
	return fmt.Sprintf("%s %s %d mtu %d (%s)", a.Name, a.MAC, a.Speed, a.MTU, a.Driver)
}

// String representation of the struct.
func (b *Bridge) String() string {
	return fmt.Sprintf("%s %s mtu %d", b.Name, b.MAC, b.MTU)
}

// String representation of the struct.
func (v *Virtual) String() string {
	return fmt.Sprintf("%s %s mtu %d", v.Name, v.MAC, v.MTU)
}
