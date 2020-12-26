// +build amd64

package cpuid

// cpuid assembly to get the CPUID low level leaf values.
func cpuid(arg1, arg2 uint32) (eax, ebx, ecx, edx uint32)
