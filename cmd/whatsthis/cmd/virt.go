package cmd

import (
	"fmt"

	"github.com/powersj/whatsthis"

	"github.com/pkg/errors"
	"github.com/spf13/cobra"
)

var virtCmd = &cobra.Command{
	Use:   "virt",
	Short: "Probe for virt",
	RunE:  probeVirt,
}

// probeVirt used to probe for possible virt types
func probeVirt(cmd *cobra.Command, args []string) error {
	probe, err := whatsthis.Virt()
	if err != nil {
		return errors.Wrap(err, "error probing virt information")
	}

	if jsonOutput {
		fmt.Printf("%v\n", probe.JSON())
	} else {
		fmt.Printf("%s\n", probe)
	}

	return nil
}

func init() {
	rootCmd.AddCommand(virtCmd)
}
