package cmd

import (
	"fmt"
	"os"

	"whatsthis/internal/file"
	"whatsthis/internal/system"

	"github.com/pkg/errors"
	log "github.com/sirupsen/logrus"
	"github.com/spf13/cobra"
)

const (
	version = "v20.1"
)

var (
	debugOutput     bool
	jsonOutput      bool
	sourceDirectory string
)

// rootCmd represents the base command when called without any subcommands
var rootCmd = &cobra.Command{
	Use:   "whatsthis",
	Short: "Am I in a cloud, on a container, or just plain metal?",
	Long: `Am I in a cloud, on a container, or just plain metal?

This is a Go-based CLI and library to determine where a system is running and
what makes up the system. I found myself wanting a single screen with system
information after SSH'ing onto new systems to debug or test. Additionally, I
started this after wanting to explore /proc and /sys and learn what data are
available in each.

To determine where a system is running, whatsthis is essentially an
all-in-one collection of systemd-detect-virt, virt-what, and cloud-id.
This attempts to do a best effort guess based on a variety of heuristics as to
what container, virtualization, or cloud the system is running on.

To summarize the system components, whatsthis will scan the filesystem
for known files in /sys, /proc, or other directories. This data is then
used to create a short summarize of the system in place of running a number of
other commands (e.g. lsblk, ip, dmesg, dmidecode)`,
	PersistentPreRun: setup,
	RunE:             root,
}

// Called before all commands to setup general run-time settings
func setup(cmd *cobra.Command, args []string) {
	log.SetFormatter(&log.TextFormatter{
		DisableTimestamp: true,
	})

	if debugOutput {
		log.SetLevel(log.DebugLevel)
	}

	file.RootDir = sourceDirectory
}

// Base command operations
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

// CLI function to setup flags
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

// Execute adds all child commands to the root command and sets flags
// appropriately. This is called by main.main(). It only needs to happen once
// to the rootCmd.
func Execute() {
	if err := rootCmd.Execute(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}
