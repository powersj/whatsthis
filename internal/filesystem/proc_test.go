package filesystem

import (
	"testing"

	"github.com/powersj/whatsthis/internal/file"
	"github.com/stretchr/testify/assert"
)

func TestCGroup(t *testing.T) {
	file.RootDir = "testdata"
	var proc Proc = Proc{}

	assert.Contains(t, proc.CGroup(), "1:name=systemd:/user.slice/user-1000.slice")
}

func TestCPUInfo(t *testing.T) {
	file.RootDir = "testdata"
	var proc Proc = Proc{}

	assert.Contains(t, proc.CPUInfo(), "vendor_id       : AuthenticAMD")
}

func TestEnviron(t *testing.T) {
	file.RootDir = "testdata"
	var proc Proc = Proc{}

	assert.Contains(t, proc.Environ(), "HOME=/init=/sbin/initNETWORK_SKIP_ENSLAVED=TERM=linux")
}

func TestMemInfo(t *testing.T) {
	file.RootDir = "testdata"
	var proc Proc = Proc{}

	var cpuInfo map[string]int64 = proc.MemInfo()
	assert.Equal(t, int64(32856760), cpuInfo["MemTotal"])
}

func TestProcOSRelease(t *testing.T) {
	file.RootDir = "testdata"
	var proc Proc = Proc{}

	var osRelease string = "5.8.0-31-generic"
	assert.Equal(t, osRelease, proc.OSRelease())
}

func TestProcInfo(t *testing.T) {
	file.RootDir = "testdata"
	var proc Proc = Proc{}

	var procInfo string = proc.Procinfo()
	assert.Equal(t, "", procInfo)
}

func TestVersion(t *testing.T) {
	file.RootDir = "testdata"
	var proc Proc = Proc{}

	assert.Contains(t, proc.Version(), "Linux version 5.8.0-31-generic (buildd@lgw01-amd64-038)")
}
