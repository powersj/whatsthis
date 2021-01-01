package platform

import (
	"encoding/json"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestPlatform(t *testing.T) {
	probe, _ := New()
	var output string = probe.String()
	assert.Contains(t, output, "board:")
	assert.Contains(t, output, "bios:")

	var newProbe Probe
	assert.NoError(t, json.Unmarshal([]byte(probe.JSON()), &newProbe))
}
