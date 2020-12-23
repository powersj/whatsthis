package cpuid

import (
	"bytes"

	"whatsthis/pkg/util"
)

// Probe struct for cpuid.
type Probe struct {
	VendorID string `json:"vendorID"`
}

// New initializes new probe struct and probes the system.
func New() (*Probe, error) {
	probe := &Probe{}
	if err := probe.probe(); err != nil {
		return nil, err
	}

	return probe, nil
}

// Probe the system
// https://lwn.net/Articles/301888/
func (p *Probe) probe() error {
	_, ebx, ecx, edx := cpuid(0x40000000, 0)
	p.VendorID = int32sToString(ebx, ecx, edx)

	return nil
}

// String representation of the struct
func (p *Probe) String() string {
	return p.VendorID
}

// JSON representation of the struct
func (p *Probe) JSON() string {
	return util.ObjectJSONString(&p)
}

// IsHypervisor returns whether the hypervisor present bit is set
func (p *Probe) IsHypervisor() bool {
	var hypervisorPresent uint32 = 0x80000000
	_, _, ecx, _ := cpuid(0x1, 0)
	return (ecx & hypervisorPresent) == hypervisorPresent
}

// cpuid assembly to get the CPUID low level leaf values.
func cpuid(arg1, arg2 uint32) (eax, ebx, ecx, edx uint32)

// int32sToString converts the CPUID registers into a string
func int32sToString(args ...uint32) string {
	var buffer []byte
	for _, arg := range args {
		buffer = append(buffer,
			byte((arg)&0xFF),
			byte((arg>>8)&0xFF),
			byte((arg>>16)&0xFF),
			byte((arg>>24)&0xFF))
	}

	return string(bytes.Trim(buffer, "\x00"))
}
