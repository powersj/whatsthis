package network

import (
	"fmt"
	"os"
	"path"
	"sort"
	"strings"

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

	return probe, nil
}

// Probe the system.
func (p *Probe) probe() error {
	for _, path := range p.sys.ListNetwork() {
		if strings.Contains(path, "/sys/class/net/lo") {
			continue
		}

		var uevent map[string]string = p.sys.UEvent(path)
		var virtualDev bool = false

		dest, _ := os.Readlink(path)
		if strings.Contains(dest, "devices/virtual/net") {
			virtualDev = true
		}

		switch {
		case uevent["DEVTYPE"] == "bridge":
			var bridge Bridge = Bridge{
				Name: uevent["INTERFACE"],
				MAC:  p.MAC(path),
				MTU:  p.MTU(path),
				Path: path,
			}

			p.Bridges = append(p.Bridges, bridge)
		case virtualDev:
			var virtual Virtual = Virtual{
				Name: uevent["INTERFACE"],
				MAC:  p.MAC(path),
				MTU:  p.MTU(path),
				Path: path,
			}

			p.Virtual = append(p.Virtual, virtual)
		default:
			var adapter Adapter = Adapter{
				Name:   uevent["INTERFACE"],
				MAC:    p.MAC(path),
				Speed:  p.Speed(path),
				MTU:    p.MTU(path),
				Driver: p.Driver(path),
				Path:   path,
			}

			p.Physical = append(p.Physical, adapter)
		}
	}

	sort.Slice(p.Physical, func(i, j int) bool {
		return p.Physical[i].Name < p.Physical[j].Name
	})
	sort.Slice(p.Virtual, func(i, j int) bool {
		return p.Virtual[i].Name < p.Virtual[j].Name
	})
	sort.Slice(p.Bridges, func(i, j int) bool {
		return p.Bridges[i].Name < p.Bridges[j].Name
	})

	return nil
}

// String representation of the struct.
func (p *Probe) String() string {
	var result strings.Builder

	result.WriteString("network:")

	if len(p.Physical) > 0 {
		result.WriteString("\n- physical:")
		for _, adapter := range p.Physical {
			result.WriteString(
				fmt.Sprintf(
					"\n  - %s %s %d mtu %d (%s)",
					adapter.Name, adapter.MAC, adapter.Speed,
					adapter.MTU, adapter.Driver,
				),
			)
		}
	}

	if len(p.Bridges) > 0 {
		result.WriteString("\n- bridges:")
		for _, bridge := range p.Bridges {
			result.WriteString(
				fmt.Sprintf(
					"\n  - %s %s mtu %d", bridge.Name, bridge.MAC, bridge.MTU,
				),
			)
		}
	}

	if len(p.Virtual) > 0 {
		result.WriteString("\n- virtual:")
		for _, virtual := range p.Virtual {
			result.WriteString(
				fmt.Sprintf(
					"\n  - %s %s mtu %d", virtual.Name, virtual.MAC, virtual.MTU,
				),
			)
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
