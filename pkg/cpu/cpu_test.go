package cpu

import (
	"encoding/json"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCPU(t *testing.T) {
	probe, _ := New()
	assert.Contains(t, probe.String(), "cpu:")

	var newProbe Probe
	assert.NoError(t, json.Unmarshal([]byte(probe.JSON()), &newProbe))
}
