package system

import (
	"fmt"

	"github.com/pkg/errors"
	"github.com/powersj/whatsthis/internal/util"
	"github.com/powersj/whatsthis/pkg/cloud"
	"github.com/powersj/whatsthis/pkg/container"
	"github.com/powersj/whatsthis/pkg/cpu"
	"github.com/powersj/whatsthis/pkg/distro"
	"github.com/powersj/whatsthis/pkg/memory"
	"github.com/powersj/whatsthis/pkg/network"
	"github.com/powersj/whatsthis/pkg/platform"
	"github.com/powersj/whatsthis/pkg/storage"
	"github.com/powersj/whatsthis/pkg/virt"
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
		return nil, errors.Wrap(err, "error probing cloud information")
	}
	container, err := container.New()
	if err != nil {
		return nil, errors.Wrap(err, "error probing container information")
	}
	cpu, err := cpu.New()
	if err != nil {
		return nil, errors.Wrap(err, "error probing cpu information")
	}
	distro, err := distro.New()
	if err != nil {
		return nil, errors.Wrap(err, "error probing distro information")
	}
	memory, err := memory.New()
	if err != nil {
		return nil, errors.Wrap(err, "error probing memory information")
	}
	network, err := network.New()
	if err != nil {
		return nil, errors.Wrap(err, "error probing network information")
	}
	platform, err := platform.New()
	if err != nil {
		return nil, errors.Wrap(err, "error probing platform information")
	}
	storage, err := storage.New()
	if err != nil {
		return nil, errors.Wrap(err, "error probing storage information")
	}
	virt, err := virt.New()
	if err != nil {
		return nil, errors.Wrap(err, "error probing virt information")
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

// String representation of the struct.
func (s *System) String() string {
	return fmt.Sprintf(
		"%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s",
		s.Cloud.String(),
		s.Container.String(),
		s.Virt.String(),
		s.Distro.String(),
		s.Platform.String(),
		s.CPU.String(),
		s.Memory.String(),
		s.Storage.String(),
		s.Network.String(),
	)
}

// JSON representation of the struct.
func (s *System) JSON() string {
	return util.ObjectJSONString(&s)
}
