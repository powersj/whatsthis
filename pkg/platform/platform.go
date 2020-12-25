package platform

import (
	"fmt"

	"github.com/powersj/whatsthis/internal/filesystem"
	"github.com/powersj/whatsthis/internal/util"
)

// Probe struct for platform. Captures the BIOS and Board values.
type Probe struct {
	sys filesystem.Sys

	BIOS  BIOS  `json:"bios"`
	Board Board `json:"board"`
}

// BIOS captures the platform BIOS values.
type BIOS struct {
	Date    string `json:"date"`
	Vendor  string `json:"vendor"`
	Version string `json:"version"`
}

// Board captures the platform Board values.
type Board struct {
	Name   string `json:"Name"`
	Vendor string `json:"Vendor"`
}

// New initializes new probe struct and probes the system.
func New() (*Probe, error) {
	var sys filesystem.Sys = filesystem.Sys{}

	probe := &Probe{sys: sys}
	if err := probe.probe(); err != nil {
		return nil, err
	}

	return probe, nil
}

// Probe the system.
func (p *Probe) probe() error {
	p.BIOS = BIOS{
		Date:    p.sys.BIOSDate(),
		Vendor:  p.sys.BIOSVendor(),
		Version: p.sys.BIOSVersion(),
	}

	p.Board = Board{
		Name:   p.sys.BoardName(),
		Vendor: p.sys.BoardVendor(),
	}

	return nil
}

// String representation of the struct.
func (p *Probe) String() string {
	return fmt.Sprintf(
		"board: %s %s\nbios: %s BIOS %s (%s)",
		p.Board.Vendor, p.Board.Name, p.BIOS.Vendor, p.BIOS.Version, p.BIOS.Date,
	)
}

// JSON representation of the struct.
func (p *Probe) JSON() string {
	return util.ObjectJSONString(&p)
}
