package cmd

import (
	"fmt"

	"github.com/powersj/whatsthis"

	"github.com/pkg/errors"
	"github.com/spf13/cobra"
)

var distroCmd = &cobra.Command{
	Use:   "distro",
	Short: "Probe for distro",
	RunE:  probeDistro,
}

func probeDistro(cmd *cobra.Command, args []string) error {
	probe, err := whatsthis.Distro()
	if err != nil {
		return errors.Wrap(err, "error probing distro information")
	}

	if jsonOutput {
		fmt.Printf("%v\n", probe.JSON())
	} else {
		fmt.Printf("%s\n", probe)
	}

	return nil
}

func init() {
	rootCmd.AddCommand(distroCmd)
}
