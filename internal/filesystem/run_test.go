package filesystem

import (
	"testing"

	"github.com/powersj/whatsthis/internal/file"
	"github.com/stretchr/testify/assert"
)

func TestContainerEnv(t *testing.T) {
	file.RootDir = "testdata"

	var run Run = Run{}
	assert.True(t, run.ContainerEnv())
}

func TestDockerEnv(t *testing.T) {
	file.RootDir = "testdata"

	var run Run = Run{}
	assert.False(t, run.DockerEnv())
}
