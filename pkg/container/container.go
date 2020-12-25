package container

import (
	"fmt"
	"strings"

	"github.com/powersj/whatsthis/internal/filesystem"
	"github.com/powersj/whatsthis/internal/util"
)

// Probe struct for containres. Used to store the results of the probe and the
// name of the container discovered.
type Probe struct {
	run  filesystem.Run
	proc filesystem.Proc

	Detected bool            `json:"detected"`
	Name     string          `json:"name"`
	Results  map[string]bool `json:"results"`
}

// New initializes new probe struct and probes the system.
func New() (*Probe, error) {
	run := filesystem.Run{}
	proc := filesystem.Proc{}

	probe := &Probe{
		run:      run,
		proc:     proc,
		Detected: false,
		Name:     "",
		Results:  make(map[string]bool),
	}
	if err := probe.probe(); err != nil {
		return nil, err
	}

	return probe, nil
}

// Probe the system.
func (p *Probe) probe() error {
	containers := map[string]func() bool{
		"docker": p.Docker,
		"lxc":    p.LXC,
		"podman": p.Podman,
		"wsl":    p.WSL,
	}

	for container, detect := range containers {
		var result bool = detect()

		p.Results[container] = result
		if result {
			p.Detected = true
			p.Name = container
		}
	}

	return nil
}

// String representation of the struct.
func (p *Probe) String() string {
	if p.Name == "" {
		return "container: not detected"
	}

	return fmt.Sprintf("container: %s", p.Name)
}

// JSON representation of the struct.
func (p *Probe) JSON() string {
	return util.ObjectJSONString(&p)
}

// Docker detects if a system is on the Docker.
func (p *Probe) Docker() bool {
	if p.run.DockerEnv() {
		return true
	} else if strings.Contains(p.proc.CGroup(), "docker") {
		return true
	}

	return false
}

// LXC detects if a system is on the LXC.
func (p *Probe) LXC() bool {
	return strings.HasPrefix(p.proc.Environ(), "container=")
}

// Podman detects if a system is on the Podman.
func (p *Probe) Podman() bool {
	if p.run.ContainerEnv() {
		return true
	} else if strings.HasPrefix(p.proc.Environ(), "container=podman") {
		return true
	}

	return false
}

// WSL detects if a system is on the WSL.
func (p *Probe) WSL() bool {
	var osRelease string = p.proc.OSRelease()
	var version string = p.proc.Version()

	switch {
	case strings.Contains(osRelease, "Microsoft"):
		return true
	case strings.Contains(osRelease, "WSL"):
		return true
	case strings.Contains(version, "Microsoft"):
		return true
	case strings.Contains(version, "WSL"):
		return true
	default:
		return false
	}
}
