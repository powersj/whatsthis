package system

import (
	"fmt"

	"whatsthis/pkg/cloud"
	"whatsthis/pkg/container"
	"whatsthis/pkg/cpu"
	"whatsthis/pkg/distro"
	"whatsthis/pkg/memory"
	"whatsthis/pkg/network"
	"whatsthis/pkg/platform"
	"whatsthis/pkg/storage"
	"whatsthis/pkg/util"
	"whatsthis/pkg/virt"
)

// System struct for all probes we want to report at once.
type System struct {
	Cloud     *cloud.Probe     `json:"cloud"`
	Container *container.Probe `json:"container"`
	CPU       *cpu.Probe       `json:"cpu"`
	Distro    *distro.Probe    `json:"distro"`
	Memory    *memory.Probe    `json:"memory"`
	Network   *network.Probe   `json:"network"`
	Platform  *platform.Probe  `json:"platform"`
	Storage   *storage.Probe   `json:"storage"`
	Virt      *virt.Probe      `json:"virt"`
}

// Probe initializes all the required structs.
func Probe() (*System, error) {
	cloud, err := cloud.New()
	if err != nil {
		return nil, err
	}
	container, err := container.New()
	if err != nil {
		return nil, err
	}
	cpu, err := cpu.New()
	if err != nil {
		return nil, err
	}
	distro, err := distro.New()
	if err != nil {
		return nil, err
	}
	memory, err := memory.New()
	if err != nil {
		return nil, err
	}
	network, err := network.New()
	if err != nil {
		return nil, err
	}
	platform, err := platform.New()
	if err != nil {
		return nil, err
	}
	storage, err := storage.New()
	if err != nil {
		return nil, err
	}
	virt, err := virt.New()
	if err != nil {
		return nil, err
	}

	return &System{
		Cloud:     cloud,
		Container: container,
		CPU:       cpu,
		Distro:    distro,
		Memory:    memory,
		Network:   network,
		Platform:  platform,
		Storage:   storage,
		Virt:      virt,
	}, nil
}

// String representation of the struct
func (s *System) String() string {
	return fmt.Sprintf(
		"%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s",
		s.Cloud.String(),
		s.Virt.String(),
		s.Container.String(),
		s.Distro.String(),
		s.Platform.String(),
		s.CPU.String(),
		s.Memory.String(),
		s.Storage.String(),
		s.Network.String(),
	)
}

// JSON representation of the struct
func (s *System) JSON() string {
	return util.ObjectJSONString(&s)
}
