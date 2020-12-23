package cmd

import (
	"fmt"
	"whatsthis"

	"github.com/pkg/errors"
	"github.com/spf13/cobra"
)

var memoryCmd = &cobra.Command{
	Use:   "memory",
	Short: "Probe for memory",
	RunE:  probeMemory,
}

func probeMemory(cmd *cobra.Command, args []string) error {
	probe, err := whatsthis.Memory()
	if err != nil {
		return errors.Wrap(err, "error probing memory information")
	}

	if jsonOutput {
		fmt.Printf("%v\n", probe.JSON())
	} else {
		fmt.Printf("%s\n", probe)
	}

	return nil
}

func init() {
	rootCmd.AddCommand(memoryCmd)
}
