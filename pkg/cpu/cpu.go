package cpu

import (
	"fmt"
	"regexp"
	"runtime"
	"strings"

	"github.com/powersj/whatsthis/internal/filesystem"
	"github.com/powersj/whatsthis/internal/util"
)

// Probe struct for CPUs.
type Probe struct {
	proc filesystem.Proc
	sys  filesystem.Sys

	Model      string `json:"model"`
	NumCores   int    `json:"numCore"`
	NumThreads int    `json:"numThread"`
	NumSockets int    `json:"numSocket"`
}

// New initializes new probe struct and probes the system.
func New() (*Probe, error) {
	proc := filesystem.Proc{}
	sys := filesystem.Sys{}

	probe := &Probe{proc: proc, sys: sys}
	if err := probe.probe(); err != nil {
		return nil, err
	}

	return probe, nil
}

// Probe the system
func (p *Probe) probe() error {
	if runtime.GOARCH == "amd64" {
		var cpuinfo string = p.proc.CPUInfo()
		rex := regexp.MustCompile(`(?:model name.*: )(.*)`)
		p.Model = rex.FindStringSubmatch(cpuinfo)[1]
	} else {
		p.Model = "ARMv8"
	}

	p.NumCores = len(p.sys.CPUCoreList())
	p.NumThreads = len(p.sys.ListCPU())
	p.NumSockets = p.numSockets()

	return nil
}

// String representation of the struct
func (p *Probe) String() string {
	var result strings.Builder

	result.WriteString(fmt.Sprintf("cpu: %s with ", p.Model))

	if p.NumCores > 1 {
		result.WriteString(fmt.Sprintf("%d cores", p.NumCores))
	} else {
		result.WriteString(fmt.Sprintf("%d core", p.NumCores))
	}

	if p.NumThreads > 1 {
		result.WriteString(fmt.Sprintf(" (%d threads)", p.NumThreads))
	} else {
		result.WriteString(fmt.Sprintf(" (%d thread)", p.NumThreads))
	}

	if p.NumSockets > 1 {
		result.WriteString(fmt.Sprintf(" on %d sockets", p.NumSockets))
	} else {
		result.WriteString(fmt.Sprintf(" on %d socket", p.NumSockets))
	}

	return result.String()
}

// JSON representation of the struct
func (p *Probe) JSON() string {
	return util.ObjectJSONString(&p)
}

// numSockets returns the number of sockets in the system
func (p *Probe) numSockets() int {
	var cpuSocketMap map[string]int = p.sys.CPUSocketMap()

	var uniqueSockets []int = make([]int, 0)
	for _, socketID := range cpuSocketMap {
		if !util.SliceContainsInt(uniqueSockets, socketID) {
			uniqueSockets = append(uniqueSockets, socketID)
		}
	}

	return len(uniqueSockets)
}
