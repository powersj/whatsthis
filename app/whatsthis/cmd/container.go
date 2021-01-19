package cmd

import (
	"fmt"

	"github.com/powersj/whatsthis"

	"github.com/pkg/errors"
	"github.com/spf13/cobra"
)

var containerCmd = &cobra.Command{
	Use:   "container",
	Short: "Probe for container",
	RunE:  probeContainer,
}

func probeContainer(cmd *cobra.Command, args []string) error {
	probe, err := whatsthis.Container()
	if err != nil {
		return errors.Wrap(err, "error probing container information")
	}

	if jsonOutput {
		fmt.Printf("%v\n", probe.JSON())
	} else {
		fmt.Printf("%s\n", probe)
	}

	return nil
}

func init() {
	rootCmd.AddCommand(containerCmd)
}
