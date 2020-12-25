package virt

import (
	"fmt"

	"github.com/powersj/whatsthis/internal/cpuid"
	"github.com/powersj/whatsthis/internal/util"
)

// Probe struct for virt.
type Probe struct {
	cpuid cpuid.Probe

	Detected bool            `json:"detected"`
	Name     string          `json:"name"`
	Results  map[string]bool `json:"results"`
}

// New initializes new probe struct and probes the system.
func New() (*Probe, error) {
	cpuid := cpuid.Probe{}

	probe := &Probe{
		cpuid:    cpuid,
		Detected: false,
		Name:     "",
		Results:  make(map[string]bool),
	}
	if err := probe.probe(); err != nil {
		return nil, err
	}

	return probe, nil
}

// New initializes new probe struct and probes the system.
func (p *Probe) probe() error {
	virtTypes := map[string]func() bool{
		"bhyve":      p.Bhyve,
		"hyperv":     p.Hyperv,
		"kvm":        p.KVM,
		"parallels":  p.Parallels,
		"qemu":       p.QEMU,
		"virtualbox": p.VirtualBox,
		"vmware":     p.VMware,
		"xen":        p.Xen,
	}

	for virt, detect := range virtTypes {
		var result bool = detect()

		p.Results[virt] = result
		if result {
			p.Detected = true
			p.Name = virt
		}
	}

	return nil
}

// String representation of the struct.
func (p *Probe) String() string {
	if p.Name == "" {
		return "virt: not detected"
	}

	return fmt.Sprintf("virt: %s", p.Name)
}

// JSON representation of the struct.
func (p *Probe) JSON() string {
	return util.ObjectJSONString(&p)
}

// Bhyve detect if a system is on bhyve hypervisor.
func (p *Probe) Bhyve() bool {
	return p.cpuid.VendorID == "bhyve bhyve"
}

// Hyperv detects if a system is on Hyper-V hypervisor.
func (p *Probe) Hyperv() bool {
	return p.cpuid.VendorID == "Microsoft Hv"
}

// KVM detects if a system is on KVM hypervisor.
func (p *Probe) KVM() bool {
	return p.cpuid.VendorID == "KVMKVMKVM"
}

// Parallels detects if a system is on Parallels hypervisor.
func (p *Probe) Parallels() bool {
	return p.cpuid.VendorID == " lrpepyh vr"
}

// QEMU detects if a system is on QEMU hypervisor.
func (p *Probe) QEMU() bool {
	return p.cpuid.VendorID == "TCGTCGTCGTCG"
}

// VirtualBox detects if a system is on VirtualBox hypervisor.
// TODO: not implemented yet.
func (p *Probe) VirtualBox() bool {
	return false
}

// VMware detects if a system is on VMware hypervisor.
// TODO: there may be additional scenarios that need to be tested for given
// the large number of VMware products.
func (p *Probe) VMware() bool {
	return p.cpuid.VendorID == "VMwareVMware"
}

// Xen detects if a system is on Xen hypervisor.
// TODO: There are a number of other scenarios that need to be covered.
// This currently only covers on of the most basic ones.
func (p *Probe) Xen() bool {
	return p.cpuid.VendorID == "XenVMMXenVMM"
}
