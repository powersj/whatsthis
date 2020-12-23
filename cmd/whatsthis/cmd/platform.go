package cmd

import (
	"fmt"
	"whatsthis"

	"github.com/pkg/errors"
	"github.com/spf13/cobra"
)

var platformCmd = &cobra.Command{
	Use:   "platform",
	Short: "Probe for platform",
	RunE:  probeSystem,
}

func probeSystem(cmd *cobra.Command, args []string) error {
	probe, err := whatsthis.Platform()
	if err != nil {
		return errors.Wrap(err, "error probing platform information")
	}

	if jsonOutput {
		fmt.Printf("%v\n", probe.JSON())
	} else {
		fmt.Printf("%s\n", probe)
	}

	return nil
}

func init() {
	rootCmd.AddCommand(platformCmd)
}
