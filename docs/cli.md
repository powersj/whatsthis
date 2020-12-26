# CLI

To get a full summary of the system run whatsthis and the output will show
a breakdown probe by probe:

```text
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

## Subcommands

To run only one particular probe, run with only that probe name:

```text
$ whatsthis cpu
cpu: AMD Ryzen 9 5950X 16-Core Processor with 16 cores (32 threads) on 1 socket
```

There are subcommands for the following probes:

* cloud
* container
* cpu
* distro
* memory
* network
* platform
* storage
* virt

## JSON output

All commands can take the `--json` flag to produce JSON output:

```json
$ whatsthis cpu --json
{
"model": "AMD Ryzen 9 5950X 16-Core Processor",
"numCore": 16,
"numThread": 32,
"numSocket": 1
}
```
