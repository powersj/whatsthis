package cpuid

import (
	"bytes"
	"runtime"
)

// VendorID returns vendor ID string from CPUID.
func VendorID() string {
	if runtime.GOARCH != "amd64" {
		return ""
	}

	var eax uint32 = 0x40000000
	_, ebx, ecx, edx := cpuid(eax, 0)
	return int32sToString(ebx, ecx, edx)
}

// IsHypervisor returns whether the hypervisor present bit is set.
func IsHypervisor() bool {
	if runtime.GOARCH != "amd64" {
		return false
	}

	var eax uint32 = 0x1
	_, _, ecx, _ := cpuid(eax, 0)

	var mask uint32 = 0x80000000
	return (ecx & mask) == mask
}

// int32sToString converts the CPUID registers into a string.
func int32sToString(args ...uint32) string {
	var mask8bit uint32 = 0xFF

	var buffer []byte
	for _, arg := range args {
		buffer = append(buffer,
			byte((arg)&mask8bit),
			byte((arg>>8)&mask8bit),
			byte((arg>>16)&mask8bit),
			byte((arg>>24)&mask8bit))
	}

	return string(bytes.Trim(buffer, "\x00"))
}
