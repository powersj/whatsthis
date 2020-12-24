package memory

import (
	"fmt"

	"whatsthis/internal/filesystem"
	"whatsthis/internal/units"
	"whatsthis/internal/util"
)

// Probe struct for memory.
type Probe struct {
	proc filesystem.Proc

	Total     string `json:"total"`
	SwapTotal string `json:"swapTotal"`
}

// New initializes new probe struct and probes the system.
func New() (*Probe, error) {
	proc := filesystem.Proc{}

	probe := &Probe{proc: proc}
	if err := probe.probe(); err != nil {
		return nil, err
	}

	return probe, nil
}

// Probe the system
func (p *Probe) probe() error {
	var memInfoMap map[string]int64 = p.proc.MemInfo()

	p.Total = units.KB2Human(memInfoMap["MemTotal"])
	p.SwapTotal = units.KB2Human(memInfoMap["SwapTotal"])

	return nil
}

// String representation of the struct
func (p *Probe) String() string {
	return fmt.Sprintf("memory: %s", p.Total)
}

// JSON representation of the struct
func (p *Probe) JSON() string {
	return util.ObjectJSONString(&p)
}
