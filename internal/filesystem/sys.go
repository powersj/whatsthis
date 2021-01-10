package filesystem

import (
	"path"

	"github.com/powersj/whatsthis/internal/file"
	"github.com/powersj/whatsthis/internal/util"
)

// Sys represents the /sys filesystem.
type Sys struct{}

// BIOSDate read from /sys/class/dmi/id.
func (*Sys) BIOSDate() string {
	return file.Read("/sys/class/dmi/id/bios_date")
}

// BIOSVendor read from /sys/class/dmi/id.
func (*Sys) BIOSVendor() string {
	return file.Read("/sys/class/dmi/id/bios_vendor")
}

// BIOSVersion read from /sys/class/dmi/id.
func (*Sys) BIOSVersion() string {
	return file.Read("/sys/class/dmi/id/bios_version")
}

// BlockSizeBytes reads from a size file for a storage device. The size file
// returns the number of blocks, and is always reported assuming 512-byte
// blocks, so the value returned is multiplied by 512 to return the actual
// number of bytes (a more useful number)
func (s *Sys) BlockSizeBytes(target string) int64 {
	var size int64 = s.BlockSizeRaw(target)
	if size == -1 {
		return -1
	}

	return size * 512
}

// BlockSizeRaw reads the raw number of 512-byte blocks for a device
func (s *Sys) BlockSizeRaw(target string) int64 {
	return file.ReadInt64(path.Join(target, "size"))
}

// BoardName read from /sys/class/dmi/id/.
func (*Sys) BoardName() string {
	return file.Read("/sys/class/dmi/id/board_name")
}

// BoardVendor read from /sys/class/dmi/id/.
func (*Sys) BoardVendor() string {
	return file.Read("/sys/class/dmi/id/board_vendor")
}

// ChassisAssetTag read from /sys/class/dmi/id/.
func (*Sys) ChassisAssetTag() string {
	return file.Read("/sys/class/dmi/id/chassis_asset_tag")
}

// CPUTopology returns a mapping of socket to physical cores.
func (s *Sys) CPUTopology() map[int][]int {
	var cpuCoreMap map[int][]int = make(map[int][]int)

	for _, cpu := range s.CPUs() {
		var socketID int = file.ReadInt(path.Join(cpu, "topology/physical_package_id"))
		var coreID int = file.ReadInt(path.Join(cpu, "topology/core_id"))

		if !util.SliceContainsInt(cpuCoreMap[socketID], coreID) {
			cpuCoreMap[socketID] = append(cpuCoreMap[socketID], coreID)
		}
	}

	return cpuCoreMap
}

// HypervisorType read from /sys/hypervisor/.
func (*Sys) HypervisorType() string {
	return file.Read("/sys/hypervisor/type")
}

// HypervisorUUID read from /sys/hypervisor/.
func (*Sys) HypervisorUUID() string {
	return file.Read("/sys/hypervisor/uuid")
}

// BlockDevices returns lists all block devices in /sys.
func (s *Sys) BlockDevices() []string {
	return file.ListDirsWithRegex("/sys/class/block", `.*`)
}

// CPUs returns a list of all CPUs in /sys.
func (s *Sys) CPUs() []CPU {
	var CPUs []CPU = make([]CPU, 0)
	return file.ListDirsWithRegex("/sys/devices/system/cpu", `cpu\d+`)
}

// NetworkAdapters returns a list of all network adapters in /sys.
func (s *Sys) NetworkAdapters() []string {
	return file.ListDirsWithRegex("/sys/class/net", `.*`)
}

// ProductName read from /sys/class/dmi/id/.
func (*Sys) ProductName() string {
	return file.Read("/sys/class/dmi/id/product_name")
}

// ProductSerial read from /sys/class/dmi/id/.
func (*Sys) ProductSerial() string {
	return file.Read("/sys/class/dmi/id/product_serial")
}

// SysVendor read from /sys/class/dmi/id/.
func (*Sys) SysVendor() string {
	return file.Read("/sys/class/dmi/id/sys_vendor")
}

// NetworkUEvent reads a network adapter's uevent file and parses it.
func (s *Sys) NetworkUEvent(target string) map[string]string {
	return file.ParseKeyValue(path.Join(target, "uevent"), "=")
}

// BlockUEvent reads a block device's uevent file and parses it.
func (s *Sys) BlockUEvent(target string) map[string]string {
	return file.ParseKeyValue(path.Join(target, "uevent"), "=")
}
