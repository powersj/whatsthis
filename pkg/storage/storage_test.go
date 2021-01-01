package storage

import (
	"encoding/json"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestStorage(t *testing.T) {
	probe, _ := New()
	assert.Contains(t, probe.String(), "storage:")

	var newProbe Probe
	assert.NoError(t, json.Unmarshal([]byte(probe.JSON()), &newProbe))
}
