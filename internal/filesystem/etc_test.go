package filesystem

import (
	"testing"

	"github.com/powersj/whatsthis/internal/file"
	"github.com/stretchr/testify/assert"
)

func TestEtcOSRelease(t *testing.T) {
	file.RootDir = "testdata"
	var etc Etc = Etc{}

	var osRelease map[string]string = etc.OSRelease()
	assert.Equal(t, "heroic", osRelease["VERSION_CODENAME"])
}
