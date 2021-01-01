package system

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestSystem(t *testing.T) {
	system, _ := Probe()

	var output string = system.String()
	assert.Contains(t, output, "cloud: ")
	assert.Contains(t, output, "container: ")
	assert.Contains(t, output, "virt: ")

	var jsonOutput string = system.JSON()
	assert.Contains(t, jsonOutput, "\"cloud\": {")
	assert.Contains(t, jsonOutput, "\"container\": {")
	assert.Contains(t, jsonOutput, "\"virt\": {")
}
