package filesystem

import (
	"fmt"
	"testing"

	"github.com/powersj/whatsthis/internal/file"
	"github.com/stretchr/testify/assert"
)

func TestBIOSDate(t *testing.T) {
	file.RootDir = "testdata"
	var sys Sys = Sys{}

	assert.Equal(t, "12/04/2020", sys.BIOSDate())
}

func TestBIOSVendor(t *testing.T) {
	file.RootDir = "testdata"
	var sys Sys = Sys{}

	assert.Equal(t, "Fake Vendor Inc.", sys.BIOSVendor())
}

func TestBIOSVersion(t *testing.T) {
	file.RootDir = "testdata"
	var sys Sys = Sys{}

	assert.Equal(t, "3001", sys.BIOSVersion())
}

func TestBlockSize(t *testing.T) {
	file.RootDir = "testdata"
	var sys Sys = Sys{}

	assert.Equal(t, int64(1952473088), sys.BlockSizeRaw("/sys/class/block/nvme0n1p2"))
}

func TestBoardName(t *testing.T) {
	file.RootDir = "testdata"
	var sys Sys = Sys{}

	assert.Equal(t, "TUF GAMING X570-PRO (WI-FI)", sys.BoardName())
}

func TestBoardVendor(t *testing.T) {
	file.RootDir = "testdata"
	var sys Sys = Sys{}

	assert.Equal(t, "FAKE VENDOR INC.", sys.BoardVendor())
}

func TestCPUTopology(t *testing.T) {
	file.RootDir = "testdata"
	var sys Sys = Sys{}

	var coreMap map[int][]int = sys.CPUTopology()
	fmt.Println(coreMap)
	assert.Equal(t, 0, len(coreMap[2]))
}

func TestChassisAssetTag(t *testing.T) {
	file.RootDir = "testdata"
	var sys Sys = Sys{}

	assert.Equal(t, "Default string", sys.ChassisAssetTag())
}

func TestHypervisorType(t *testing.T) {
	file.RootDir = "testdata"
	var sys Sys = Sys{}

	assert.Equal(t, "virt", sys.HypervisorType())
}

func TestHypervisorUUID(t *testing.T) {
	file.RootDir = "testdata"
	var sys Sys = Sys{}

	assert.Equal(t, "da0fc1a0-303c-11eb-9c56-575985fe067e", sys.HypervisorUUID())
}

func TestListBlock(t *testing.T) {
	file.RootDir = "testdata"
	var sys Sys = Sys{}

	assert.Equal(t, 3, len(sys.BlockDevices()))
}

func TestListCPU(t *testing.T) {
	file.RootDir = "testdata"
	var sys Sys = Sys{}

	assert.Equal(t, 2, len(sys.CPUs()))
}

func TestListNetwork(t *testing.T) {
	file.RootDir = "testdata"
	var sys Sys = Sys{}

	assert.Equal(t, 2, len(sys.NetworkAdapters()))
}

func TestProductName(t *testing.T) {
	file.RootDir = "testdata"
	var sys Sys = Sys{}

	assert.Equal(t, "System Product Name", sys.ProductName())
}

func TestProductSerial(t *testing.T) {
	file.RootDir = "testdata"
	var sys Sys = Sys{}

	// File does not exist so tests the error branch and the default return
	assert.Equal(t, "", sys.ProductSerial())
}

func TestSysVendor(t *testing.T) {
	file.RootDir = "testdata"
	var sys Sys = Sys{}

	assert.Equal(t, "FAKE VENDOR", sys.SysVendor())
}

func TestUEvent(t *testing.T) {
	file.RootDir = "testdata"
	var sys Sys = Sys{}

	var ueventMap map[string]string = sys.BlockUEvent("/sys/class/net/wlp5s0")
	assert.Equal(t, "wlan", ueventMap["DEVTYPE"])
	assert.Equal(t, "wlp5s0", ueventMap["INTERFACE"])
	assert.Equal(t, "3", ueventMap["IFINDEX"])
}
