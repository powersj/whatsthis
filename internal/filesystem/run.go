package filesystem

import (
	"github.com/powersj/whatsthis/internal/file"
)

// Run represents the /run filesystem
type Run struct{}

// ContainerEnv bool if /run/.containerenv exists
func (*Run) ContainerEnv() bool {
	return file.Exists("/run/.containerenv")
}

// DockerEnv bool if /run/.dockerenv exists
func (*Run) DockerEnv() bool {
	return file.Exists("/run/.dockerenv")
}
