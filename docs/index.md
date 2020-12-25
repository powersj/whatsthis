# whatsthis

*Am I on a cloud, in a container, virtualized, or plain bare metal?*

## Overview

`whatsthis` is a Go-based CLI and library to determine where a system is
running and what makes up the system.

To determine where a system is running, `whatsthis` will attempt to make a
best-effort guess based on a variety of heuristics as to what container,
virtualization, or cloud the system is running on. This is similar to an
all-in-one collection of the `systemd-detect-virt`, `virt-what`, and `cloud-id`
commands.

To summarize the system components, `whatsthis` will scan the filesystem for
known files in `/sys`, `/proc`, or other directories. This data is then used to
create a short summarize of the system in place of running several other
commands (e.g. `lsblk`, `ip`, `dmesg`, `dmidecode`)

## Install

See the [latest release](https://github.com/powersj/whatsthis/releases/latest)
page for the available binary downloads.

### Architecture Support

Releases include binaries for x86_64 (amd64) as well as some initial support
for aarch64 (arm64). The aarch64 architecture does not have the same cpuid
capabilities in place as x86_64 does. As such the virtualization detection
on aarch64 is not functional.

### Operating System Support

`whatsthis` was developed with Linux based OSes in mind.

The *BSDs do not mount `/proc` by default and `/sys` is replaced by `sysctl`.
`whatsthis` could learn how to use `sysctl` down the road. This could also help
enable Darwin support.

## CLI Usage

To get a full summary of the system run `whatsthis` and the output will show
a breakdown module name by module name:

```shell
$ whatsthis
cloud: not detected
virt: not detected
container: not detected
distro: Ubuntu 20.10 (amd64)
kernel: 5.8.0-33-generic
board: ASUSTeK COMPUTER INC. TUF GAMING X570-PRO (WI-FI)
bios: American Megatrends Inc. BIOS 3001 (12/04/2020)
cpu: AMD Ryzen 9 5950X 16-Core Processor with 16 cores (32 threads) on 1 socket
memory: 31.3G
storage:
- nvme0n1 931.5G
  - nvme0n1p1 512M EFI System Partition
  - nvme0n1p2 931G
- nvme1n1 1.9T
  - nvme1n1p4 498M
  - nvme1n1p2 16M Microsoft reserved partition
  - nvme1n1p3 1.9T Basic data partition
  - nvme1n1p1 100M EFI system partition
network:
- adapters:
  - enp6s0 24:4b:fe:9a:a4:fa 1000 mtu 9000 (igc)
- virtual:
  - virbr0-nic 52:54:00:6d:53:f1 mtu 1500
- bridges:
  - docker0 02:42:96:01:ec:70 mtu 1500
  - virbr0 52:54:00:6d:53:f1 mtu 1500
```

To run only one particular module, run with only that module name:

```shell
$ whatsthis cpu
cpu: AMD Ryzen 9 5950X 16-Core Processor with 16 cores (32 threads) on 1 socket
```

Finally, to get the output in JSON add the `--json` flag:

```shell
$ whatsthis cpu --json
{
"model": "AMD Ryzen 9 5950X 16-Core Processor",
"numCore": 16,
"numThread": 32,
"numSocket": 1
}
```

See `whatsthis help` for a full list of modules and more information on
options.

## API Usage

`whatsthis` offers several structs and functions to help determine the cloud,
container, virtualization, and the underlying hardware of a system. Users can
take advantage of these in their own code:

```go
package main

import (
  "fmt"

  "github.com/powersj/whatsthis"
)

func main() {
  cloud, err := whatsthis.Cloud()
  if err != nil {
    fmt.Printf("Error getting cloud info: %v", err)
  }

  if cloud.Detected {
    fmt.Printf(cloud.Name)
  }
}
```

## Support

If you find a bug, have a question, or ideas for improvements please file an
[issue](https://github.com/powersj/whatsthis/issues/new) on GitHub.
