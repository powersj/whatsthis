package container

import (
	"encoding/json"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestPlatform(t *testing.T) {
	probe, _ := New()
	assert.Contains(t, probe.String(), "container:")

	var newProbe Probe
	assert.NoError(t, json.Unmarshal([]byte(probe.JSON()), &newProbe))
}
