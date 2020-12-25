package util

import (
	"encoding/json"
	"fmt"
)

// ObjectJSONString converts a struct to a JSON object with 2 space indent.
func ObjectJSONString(o interface{}) string {
	b, err := json.MarshalIndent(&o, "", "  ")
	if err != nil {
		fmt.Println("error marshaling JSON:", err)
		return ""
	}

	return string(b)
}

// SliceContainsString returns if a slice contains a particular string.
func SliceContainsString(s []string, str string) bool {
	for _, value := range s {
		if value == str {
			return true
		}
	}

	return false
}

// SliceContainsInt returns if a slice contains a particular string.
func SliceContainsInt(s []int, num int) bool {
	for _, value := range s {
		if value == num {
			return true
		}
	}

	return false
}
