package cmd

import (
	"fmt"
	"whatsthis"

	"github.com/pkg/errors"
	"github.com/spf13/cobra"
)

var storageCmd = &cobra.Command{
	Use:   "storage",
	Short: "Probe for storage",
	RunE:  probeStorage,
}

func probeStorage(cmd *cobra.Command, args []string) error {
	probe, err := whatsthis.Storage()
	if err != nil {
		return errors.Wrap(err, "error probing storage information")
	}

	if jsonOutput {
		fmt.Printf("%v\n", probe.JSON())
	} else {
		fmt.Printf("%s\n", probe)
	}

	return nil
}

func init() {
	rootCmd.AddCommand(storageCmd)
}
