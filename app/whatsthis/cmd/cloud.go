package cmd

import (
	"fmt"

	"github.com/powersj/whatsthis"

	"github.com/pkg/errors"
	"github.com/spf13/cobra"
)

var cloudCmd = &cobra.Command{
	Use:   "cloud",
	Short: "Probe for cloud",
	RunE:  probeCloud,
}

func probeCloud(cmd *cobra.Command, args []string) error {
	probe, err := whatsthis.Cloud()
	if err != nil {
		return errors.Wrap(err, "error probing cloud information")
	}

	if jsonOutput {
		fmt.Printf("%v\n", probe.JSON())
	} else {
		fmt.Printf("%s\n", probe)
	}

	return nil
}

func init() {
	rootCmd.AddCommand(cloudCmd)
}
