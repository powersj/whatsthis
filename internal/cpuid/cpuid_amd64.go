// +build amd64

package cpuid

// cpuid assembly to get the CPUID low level leaf values.
func cpuid(arg1, arg2 uint32) (eax, ebx, ecx, edx uint32)

// ReadCPUID check CPUID leaf
func (p *Probe) ReadCPUID() string {
	_, ebx, ecx, edx := cpuid(0x40000000, 0)
	return int32sToString(ebx, ecx, edx)
}

// IsHypervisor returns whether the hypervisor present bit is set
func (p *Probe) IsHypervisor() bool {
	var hypervisorPresent uint32 = 0x80000000
	_, _, ecx, _ := cpuid(0x1, 0)
	return (ecx & hypervisorPresent) == hypervisorPresent
}
