package cmd

import (
	"fmt"

	"github.com/powersj/whatsthis"

	"github.com/pkg/errors"
	"github.com/spf13/cobra"
)

var networkCmd = &cobra.Command{
	Use:   "network",
	Short: "Probe for network",
	RunE:  probeNetwork,
}

func probeNetwork(cmd *cobra.Command, args []string) error {
	probe, err := whatsthis.Network()
	if err != nil {
		return errors.Wrap(err, "error probing network information")
	}

	if jsonOutput {
		fmt.Printf("%v\n", probe.JSON())
	} else {
		fmt.Printf("%s\n", probe)
	}

	return nil
}

func init() {
	rootCmd.AddCommand(networkCmd)
}
