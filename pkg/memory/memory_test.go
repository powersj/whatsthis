package memory

import (
	"encoding/json"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMemory(t *testing.T) {
	probe, _ := New()
	assert.Contains(t, probe.String(), "memory:")

	var newProbe Probe
	assert.NoError(t, json.Unmarshal([]byte(probe.JSON()), &newProbe))
}
