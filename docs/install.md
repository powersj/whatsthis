# Install

Below outlines the various ways to obtain and install whatsthis.

## From binary

Download the [latest release](https://github.com/powersj/whatsthis/releases/latest)
of whatsthis for your platform and extract the tarball:

```shell
wget whatsthis_<version>_<os>_<arch>.tar.gz
tar zxvf whatsthis_<version>_<os>_<arch>.tar.gz
```

The tarball will extract the readme, license, and the pre-compiled binary.

## From source

To build and install whatsthis directly from source run:

```shell
git clone https://github.com/powersj/whatsthis
cd whatsthis
make
```

The default make command will run `go build -o whatsthis ./cmd/whatsthis` and
produce a whatsthis binary in the root directory.

## From go

To download using the `go get` command run:

```shell
go get github.com/powersj/whatsthis
```

The executable object file location will exist at `${GOPATH}/bin/whatsthis`

## Architecture support

Releases include binaries for x86-64 (amd64) as well as some initial support
for ARMv8 (arm64). The ARMv8 architecture does not have the same cpuid
capabilities in place as x86-64 does. As such the virtualization detection
on ARMv8 is not functional.

| Architecture   | Support |
| :------------- | :-------|
| x86-64         | yes     |
| ARMv8          | limited |
| ARMv6          | none    |
| ppc64le        | none    |
| s390x          | none    |
| x86            | none    |

## Operating system support

whatsthis was developed with Linux based OSes in mind.

| Operating System   | Support |
| :----------------- | :-------|
| Linux              | yes     |
| Darwin             | none    |
| FreeBSD            | none    |
| Windows            | none    |

FreeBSDs does not mount `/proc` by default and `/sys` is replaced by `sysctl`.
whatsthis could learn how to use `sysctl` down the road. This could also help
enable Darwin support.

Additionally, Windows support could be learned by looking at the Windows
Management Instrumentation (WMI).
