package distro

import (
	"encoding/json"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDistro(t *testing.T) {
	probe, _ := New()
	assert.Contains(t, probe.String(), "distro:")

	var newProbe Probe
	assert.NoError(t, json.Unmarshal([]byte(probe.JSON()), &newProbe))
}
