package file

import (
	"fmt"
	"os"
	"path"
	"regexp"
	"strconv"
	"strings"
)

// RootDir is used to determine where to run from. Default is of course
// "/", but this can be changed to read from a captured set of files.
var RootDir = "/"

// Exists if a file exists.
func Exists(file string) bool {
	var target string = path.Join(RootDir, file)

	if _, err := os.Stat(target); err == nil {
		return true
	}

	return false
}

// ListDirsWithRegex returns a list of  directories meeting a specific
// regular expression.
func ListDirsWithRegex(basePath string, regularExpression string) []string {
	var values []string
	var rex *regexp.Regexp = regexp.MustCompile(regularExpression)

	file, err := os.Open(path.Join(RootDir, basePath))
	if err != nil {
		fmt.Println("failed opening directory:", err)
		return make([]string, 0)
	}

	list, _ := file.Readdirnames(0)
	for _, name := range list {
		matches := rex.FindStringSubmatch(name)
		if len(matches) > 0 {
			values = append(values, path.Join(basePath, matches[0]))
		}
	}

	return values
}

// Read a file and return value as string.
func Read(file string) string {
	data, err := os.ReadFile(path.Join(RootDir, file))
	if err != nil {
		return ""
	}

	return strings.TrimSpace(strings.TrimSuffix(string(data), "\n"))
}

// ReadInt a file and return value as an int.
func ReadInt(file string) int {
	integer, _ := strconv.Atoi(Read(file))

	return integer
}

// ReadInt64 a file and return value as an int64.
func ReadInt64(file string) int64 {
	integer64, _ := strconv.ParseInt(Read(file), 10, 64)

	return integer64
}

// ParseKeyValue parses a key value file with a specified delimiter.
func ParseKeyValue(file string, delimiter string) map[string]string {
	var results map[string]string = make(map[string]string)

	var output string = Read(file)
	if output == "" {
		return make(map[string]string)
	}

	for _, line := range strings.Split(output, "\n") {
		var values []string = strings.Split(line, delimiter)
		results[values[0]] = strings.TrimSpace(values[1])
	}

	return results
}
