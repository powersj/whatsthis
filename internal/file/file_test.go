package file

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestExists(t *testing.T) {
	RootDir = "testdata"

	assert.False(t, Exists("fakefile"))
	assert.True(t, Exists("string"))
}

func TestListDirs(t *testing.T) {
	RootDir = "testdata"

	assert.Equal(t, 3, len(ListDirsWithRegex("dir", `dir\d+`)))
	assert.Equal(t, make([]string, 0), ListDirsWithRegex("blah", `dir\d+`))
}

func TestReadString(t *testing.T) {
	RootDir = "testdata"

	assert.Equal(t, "Test string data", Read("string"))
	assert.Equal(t, "", Read("fakefile"))
}

func TestReadInt(t *testing.T) {
	RootDir = "testdata"

	assert.Equal(t, 42, ReadInt("int"))
	assert.Equal(t, "", Read("fakefile"))
}

func TestReadInt64(t *testing.T) {
	RootDir = "testdata"

	assert.Equal(t, int64(1000000000000), ReadInt64("int64"))
	assert.Equal(t, "", Read("fakefile"))
}

func TestParseKeyValue(t *testing.T) {
	RootDir = "testdata"

	var map1 map[string]string = ParseKeyValue("keyvalue_1", "=")
	assert.Equal(t, "value", map1["key"])
	assert.Equal(t, "bar", map1["foo"])

	var map2 map[string]string = ParseKeyValue("keyvalue_2", ":")
	assert.Equal(t, "value", map2["key"])
	assert.Equal(t, "bar", map2["foo"])

	var map3 map[string]string = ParseKeyValue("fakefile", ":")
	assert.Equal(t, make(map[string]string), map3)
}
