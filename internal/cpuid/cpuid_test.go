package cpuid

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestInt32sToString(t *testing.T) {
	assert.Equal(t, "WHATSTHIS", int32sToString(1413564503, 1229476947, 83))
}
