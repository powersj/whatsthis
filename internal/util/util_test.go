package util

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

type test struct {
	Name string `json:"name"`
}

func TestObjectJSONString(t *testing.T) {
	var testStruct test = test{
		Name: "Tester",
	}

	assert.Equal(t, "{\n  \"name\": \"Tester\"\n}", ObjectJSONString(testStruct))
}

func TestSliceContainsString(t *testing.T) {
	var slice = []string{"foo", "bar"}
	assert.True(t, SliceContainsString(slice, "foo"))
	assert.False(t, SliceContainsString(slice, "fake"))
}

func TestSliceContainsInt(t *testing.T) {
	var slice = []int{42, 2021}
	assert.True(t, SliceContainsInt(slice, 42))
	assert.False(t, SliceContainsInt(slice, 1))
}
