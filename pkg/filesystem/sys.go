package filesystem

import (
	"path"

	"whatsthis/pkg/file"
	"whatsthis/pkg/util"
)

// Sys represents the /sys filesystem
type Sys struct{}

// BIOSDate read from /sys/class/dmi/id
func (*Sys) BIOSDate() string {
	return file.Read("/sys/class/dmi/id/bios_date")
}

// BIOSVendor read from /sys/class/dmi/id
func (*Sys) BIOSVendor() string {
	return file.Read("/sys/class/dmi/id/bios_vendor")
}

// BIOSVersion read from /sys/class/dmi/id
func (*Sys) BIOSVersion() string {
	return file.Read("/sys/class/dmi/id/bios_version")
}

// BlockSize reads from a size file for a storage device. The values return the
// number of blocks, so the value returned is multiplied by 512 to return the
// actual size.
func (s *Sys) BlockSize(target string) int64 {
	return file.ReadInt64(path.Join(target, "size")) * 512
}

// BoardName read from /sys/class/dmi/id/
func (*Sys) BoardName() string {
	return file.Read("/sys/class/dmi/id/board_name")
}

// BoardVendor read from /sys/class/dmi/id/
func (*Sys) BoardVendor() string {
	return file.Read("/sys/class/dmi/id/board_vendor")
}

// ChassisAssetTag read from /sys/class/dmi/id/
func (*Sys) ChassisAssetTag() string {
	return file.Read("/sys/class/dmi/id/chassis_asset_tag")
}

// CPUCoreList returns a unique list of CPUs with the same phyiscal core
// file returns a list of cores with the same physical core (e.g. 0, or 0,7)
func (s *Sys) CPUCoreList() []string {
	var cpuCoreList []string

	for _, cpu := range s.ListCPU() {
		var coreID string = file.Read(path.Join(cpu, "topology/core_cpus_list"))
		if !util.SliceContainsString(cpuCoreList, coreID) {
			cpuCoreList = append(cpuCoreList, coreID)
		}
	}

	return cpuCoreList
}

// CPUSocketMap returns a map of CPU to Socket
func (s *Sys) CPUSocketMap() map[string]int {
	var cpuSocketMap map[string]int = make(map[string]int)

	for _, cpu := range s.ListCPU() {
		cpuSocketMap[cpu] = file.ReadInt(path.Join(cpu, "topology/physical_package_id"))
	}

	return cpuSocketMap
}

// HypervisorType read from /sys/hypervisor/
func (*Sys) HypervisorType() string {
	return file.Read("/sys/hypervisor/type")
}

// HypervisorUUID read from /sys/hypervisor/
func (*Sys) HypervisorUUID() string {
	return file.Read("/sys/hypervisor/uuid")
}

// ListBlock returns lists all block devices in /sys
func (s *Sys) ListBlock() []string {
	return file.ListDirsWithRegex("/sys/class/block", `.*`)
}

// ListCPU returns a list of all CPUs in /sys
func (s *Sys) ListCPU() []string {
	return file.ListDirsWithRegex("/sys/devices/system/cpu", `cpu\d+`)
}

// ListNetwork returns a list of all network devices in /sys
func (s *Sys) ListNetwork() []string {
	return file.ListDirsWithRegex("/sys/class/net", `.*`)
}

// ProductName read from /sys/class/dmi/id/
func (*Sys) ProductName() string {
	return file.Read("/sys/class/dmi/id/product_name")
}

// ProductSerial read from /sys/class/dmi/id/
func (*Sys) ProductSerial() string {
	return file.Read("/sys/class/dmi/id/product_serial")
}

// ReadInt returns
func (*Sys) ReadInt(target string) int {
	return file.ReadInt(target)
}

// ReadInt64 TODO
func (*Sys) ReadInt64(target string) int64 {
	return file.ReadInt64(target)
}

// ReadString TODO
func (*Sys) ReadString(target string) string {
	return file.Read(target)
}

// SysVendor read from /sys/class/dmi/id/
func (*Sys) SysVendor() string {
	return file.Read("/sys/class/dmi/id/sys_vendor")
}

// UEvent TOOD
func (s *Sys) UEvent(target string) map[string]string {
	return file.ParseKeyValue(path.Join(target, "uevent"), "=")
}
