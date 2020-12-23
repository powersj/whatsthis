package main

import (
	"fmt"
	"os"
	"runtime"

	cmd "whatsthis/cmd/whatsthis/cmd"
)

func main() {
	var distro string = runtime.GOOS
	var arch string = runtime.GOARCH

	if distro != "linux" {
		fmt.Println("Executable not implimented for " + distro)
		os.Exit(1)
	}

	if arch != "amd64" {
		if arch != "arm64" {
			fmt.Println("Executable not implemented for " + arch)
			os.Exit(1)
		}
	}

	cmd.Execute()
}
