package main

import (
	"fmt"
	"os"
	"runtime"

	"github.com/powersj/whatsthis/app/whatsthis/cmd"
)

func main() {
	var distro string = runtime.GOOS
	var arch string = runtime.GOARCH

	if distro != "linux" {
		fmt.Println("Executable not implemented for " + distro)
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
