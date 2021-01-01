package network

import (
	"encoding/json"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestNetwork(t *testing.T) {
	probe, _ := New()
	assert.Contains(t, probe.String(), "network:")

	var newProbe Probe
	assert.NoError(t, json.Unmarshal([]byte(probe.JSON()), &newProbe))
}
