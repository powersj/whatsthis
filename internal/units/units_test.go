package units

import (
	"fmt"
	"testing"
)

func TestBits2Human(t *testing.T) {
	tests := []struct {
		input  int64
		output string
	}{
		{0, "0K"},
		{1024, "1K"},
		{1900, "1.9K"},
		{1048576, "1M"},
		{200050000, "190.8M"},
		{1073741824, "1G"},
		{256080000000, "238.5G"},
		{1099511627776, "1T"},
		{25600000000000, "23.3T"},
		{1125899906842624, "1P"},
		{5120000000000000, "4.5P"},
		{1152921504606846976, "1E"},
	}
	for _, tc := range tests {
		t.Run(fmt.Sprintf("bits2human=%d", tc.input), func(t *testing.T) {
			var output string = Bits2Human(tc.input)
			if output != tc.output {
				t.Fatalf("got %v; want %v", output, tc.output)
			}
		})
	}
}

func TestKB2Human(t *testing.T) {
	tests := []struct {
		input  int64
		output string
	}{
		{0, "0K"},
		{1, "1K"},
		{100, "100K"},
		{1023, "1023K"},
		{1024, "1M"},
		{2048, "2M"},
	}
	for _, tc := range tests {
		t.Run(fmt.Sprintf("bits2human=%d", tc.input), func(t *testing.T) {
			var output string = KB2Human(tc.input)
			if output != tc.output {
				t.Fatalf("got %v; want %v", output, tc.output)
			}
		})
	}
}

func TestNearestUnits(t *testing.T) {
	tests := []struct {
		input int64
		value int64
		units string
	}{
		{0, 1024, "K"},
		{1, 1024, "K"},
		{1024, 1024, "K"},
		{1900, 1024, "K"},
		{1048576, 1048576, "M"},
		{1050000, 1048576, "M"},
		{1073741824, 1073741824, "G"},
		{1080000000, 1073741824, "G"},
		{1099511627776, 1099511627776, "T"},
		{1100000000000, 1099511627776, "T"},
		{1125899906842624, 1125899906842624, "P"},
		{1130000000000000, 1125899906842624, "P"},
		{1152921504606846976, 1152921504606846976, "E"},
		{1200000000000000000, 1152921504606846976, "E"},
	}
	for _, tc := range tests {
		t.Run(fmt.Sprintf("nearestUnit=%d", tc.input), func(t *testing.T) {
			output, units := nearestUnit(tc.input)
			if output != tc.value {
				t.Fatalf("got %v; want %v", output, tc.value)
			} else if units != tc.units {
				t.Fatalf("got %v; want %v", units, tc.units)
			}
		})
	}
}
