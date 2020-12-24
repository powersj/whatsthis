package filesystem

import (
	"strconv"
	"strings"

	"whatsthis/internal/file"
)

// Proc represents the /proc filesystem
type Proc struct{}

// CGroup read from /proc/self/cgroup
func (*Proc) CGroup() string {
	return file.Read("/proc/self/cgroup")
}

// CPUInfo read from /proc/cpuinfo
func (*Proc) CPUInfo() string {
	return file.Read("/proc/cpuinfo")
}

// Environ read from /proc/1/environ
func (*Proc) Environ() string {
	return file.Read("/proc/1/environ")
}

// MemInfo read from /proc/meminfo, strip "kB" from endings and convert
// to int64
func (*Proc) MemInfo() map[string]int64 {
	var parsedMap map[string]string = file.ParseKeyValue("/proc/meminfo", ":")

	var memInfoMap map[string]int64 = make(map[string]int64)
	for key, value := range parsedMap {
		intValue, _ := strconv.ParseInt(strings.ReplaceAll(value, " kB", ""), 10, 64)
		memInfoMap[key] = intValue
	}

	return memInfoMap
}

// OSRelease read from /proc/sys/kernel/osrelease
func (*Proc) OSRelease() string {
	return file.Read("/proc/sys/kernel/osrelease")
}

// Procinfo read from /proc/procinfo
func (*Proc) Procinfo() string {
	return file.Read("/proc/procinfo")
}

// Version read from /proc/version
func (*Proc) Version() string {
	return file.Read("/proc/version")
}
