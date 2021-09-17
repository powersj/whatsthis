package cmd

import (
	"fmt"
	"os"

	"github.com/powersj/whatsthis/internal/file"
	"github.com/powersj/whatsthis/internal/system"

	"github.com/pkg/errors"
	log "github.com/sirupsen/logrus"
	"github.com/spf13/cobra"
)

const (
	version = "v1.3.1"
)

var (
	debugOutput     bool
	jsonOutput      bool
	sourceDirectory string
)

// rootCmd represents the base command when called without any subcommands.
var rootCmd = &cobra.Command{
	Use:   "whatsthis",
	Short: "Am I on a cloud, in a container, virtualized, or plain bare metal?",
	Long: `Am I on a cloud, in a container, virtualized, or plain bare metal?

whatsthis is a Go-based CLI and library to determine where a system is
running and what makes up the system.

To determine where a system is running, whatsthis will attempt to make a
best-effort guess based on a variety of heuristics as to what container,
virtualization, or cloud the system is running on. This is similar to an
all-in-one collection of the systemd-detect-virt, virt-what, and cloud-id
commands.

To summarize the system components, whatsthis will scan the filesystem for
known files in /sys, /proc, or other directories. This data is then used to
create a short summarize of the system in place of running several other
commands (e.g. lsblk, ip, dmesg, dmidecode)`,
	PersistentPreRun: setup,
	RunE:             root,
}

// Called before all commands to setup general run-time settings.
func setup(cmd *cobra.Command, args []string) {
	log.SetFormatter(&log.TextFormatter{
		DisableTimestamp: true,
	})

	if debugOutput {
		log.SetLevel(log.DebugLevel)
	}

	file.RootDir = sourceDirectory
}

// Base command operations.
func root(cmd *cobra.Command, args []string) error {
	system, err := system.Probe()
	if err != nil {
		return errors.Wrap(err, "error getting system info")
	}

	if jsonOutput {
		fmt.Printf("%s\n", system.JSON())
	} else {
		fmt.Printf("%s\n", system)
	}

	return nil
}

// CLI function to setup flags.
func init() {
	rootCmd.Version = version

	rootCmd.PersistentFlags().BoolVar(
		&debugOutput, "debug", false, "debug output",
	)
	rootCmd.PersistentFlags().BoolVar(
		&jsonOutput, "json", false, "enable output in JSON",
	)
	rootCmd.PersistentFlags().StringVar(
		&sourceDirectory, "source", "/", "source directory to read from",
	)
}

// Execute adds all child commands to the root command and sets flags.
//
// This is called by main.main(). It only needs to happen once to the rootCmd.
func Execute() {
	if err := rootCmd.Execute(); err != nil {
		os.Exit(1)
	}
}
