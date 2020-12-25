package units

import (
	"fmt"
	"strings"
)

var (
	// KB 1024.
	KB int64 = 1024
	// MB 1,048,576.
	MB int64 = KB * 1024
	// GB 1,073,741,824.
	GB int64 = MB * 1024
	// TB 1,099,511,627,776.
	TB int64 = GB * 1024
	// PB 1,125,899,906,842,624.
	PB int64 = TB * 1024
	// EB 1,152,921,504,606,847,000.
	EB int64 = PB * 1024
)

// Bits2Human converts bits to human readable version.
func Bits2Human(rawValue int64) string {
	denominator, unit := nearestUnit(rawValue)
	var value float64 = float64(rawValue) / float64(denominator)
	return fmt.Sprintf("%s%s", oneDecimal(value), unit)
}

// KB2Human converts KBs to human readable version.
func KB2Human(rawValue int64) string {
	return Bits2Human(rawValue * KB)
}

// oneDecimal returns the value to one decimal.
func oneDecimal(value float64) string {
	s := fmt.Sprintf("%.1f", value)
	return strings.TrimRight(strings.TrimRight(s, "0"), ".")
}

// nearestUnit returns the nearest value and units.
func nearestUnit(size int64) (int64, string) {
	switch {
	case size < MB:
		return KB, "K"
	case size < GB:
		return MB, "M"
	case size < TB:
		return GB, "G"
	case size < PB:
		return TB, "T"
	case size < EB:
		return PB, "P"
	default:
		return EB, "E"
	}
}
