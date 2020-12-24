package distro

import (
	"fmt"
	"os/exec"
	"runtime"
	"strings"

	"github.com/powersj/whatsthis/internal/filesystem"
	"github.com/powersj/whatsthis/internal/util"
)

// Probe struct for distro.
type Probe struct {
	etc filesystem.Etc

	Arch       string `json:"arch"`
	ID         string `json:"id"`
	Name       string `json:"name"`
	PrettyName string `json:"prettyName"`
	Version    string `json:"version"`
	Kernel     string `json:"kernel"`
}

// New initializes new probe struct and probes the system.
func New() (*Probe, error) {
	etc := filesystem.Etc{}

	probe := &Probe{etc: etc}
	if err := probe.probe(); err != nil {
		return nil, err
	}

	return probe, nil
}

// Probe the system
func (p *Probe) probe() error {
	p.Arch = runtime.GOARCH

	var osRelease map[string]string = p.etc.OSRelease()

	p.ID = osRelease["ID"]
	p.Name = strings.ReplaceAll(osRelease["NAME"], "\"", "")
	p.PrettyName = strings.ReplaceAll(osRelease["PRETTY_NAME"], "\"", "")
	p.Version = strings.ReplaceAll(osRelease["VERSION"], "\"", "")

	kernelRelease, _ := exec.Command("uname", "-r").Output()
	p.Kernel = strings.TrimSuffix(string(kernelRelease), "\n")

	return nil
}

// String representation of the struct
func (p *Probe) String() string {
	return fmt.Sprintf(
		"distro: %s (%s)\nkernel: %s", p.PrettyName, p.Arch, p.Kernel,
	)
}

// JSON representation of the struct
func (p *Probe) JSON() string {
	return util.ObjectJSONString(&p)
}
