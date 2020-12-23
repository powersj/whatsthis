package cmd

import (
	"fmt"
	"whatsthis"

	"github.com/pkg/errors"
	"github.com/spf13/cobra"
)

var cpuCmd = &cobra.Command{
	Use:   "cpu",
	Short: "Probe for cpu",
	RunE:  probeCPU,
}

func probeCPU(cmd *cobra.Command, args []string) error {
	probe, err := whatsthis.CPU()
	if err != nil {
		return errors.Wrap(err, "error probing cpu information")
	}

	if jsonOutput {
		fmt.Printf("%v\n", probe.JSON())
	} else {
		fmt.Printf("%s\n", probe)
	}

	return nil
}

func init() {
	rootCmd.AddCommand(cpuCmd)
}
