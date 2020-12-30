# Containers

Below are the test cases used to confirm container identification. These
assume a user is running on Ubuntu 20.04 LTS or later. Essentially, each
test case is to launch a container, copy the whatsthis binary over, and run it.
Finally, confirm the container is correctly reported.

## Docker

```text
snap install docker
docker run --detach --tty --name test ubuntu
docker cp whatsthis test:/
docker exec -it test /whatsthis
docker container rm --force test
```

## LXC

```text
snap install lxc
lxc launch ubuntu-daily:focal test
lxc file push whatsthis test/root/whatsthis
lxc exec test /root/whatsthis
lxc delete --force test
```

## Podman

```text
snap install podman
podman run --detach --tty --name test ubuntu
podman cp whatsthis test:/
podman exec -it test /whatsthis
podman container rm --force test
```

## WSL

### Enable WSL

Open a PowerShell console as Administrator and run the following to enable WSL
and WSL 2:

```shell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

There is an additional kernel update package required for download
[here](https://docs.microsoft.com/en-us/windows/wsl/install-win10#step-4---download-the-linux-kernel-update-package).
Once installed, reboot the system to begin using WSL.

For more details see these official instructions
[here](https://docs.microsoft.com/en-us/windows/wsl/install-win10#manual-installation-steps).

### WSL Version

To set WSL 2 as the default version run the following as Administrator in a
PowerShell console:

```shell
wsl --set-default-version 2
```

It can be helpful to switch between WSL 1 and WSL 2 during testing. Users can
list all distributions and change the version of any running distribution by
running.

```shell
wsl --list --all
wsl --set-version <distro> [2|1]
```

### Testing

Finally, to test the binary on a WSL distribution, copy it from your local
filesystem by accessing it from `/mnt/c`:

```text
cp /mnt/c/Users/<username>/Documents... whatthis
./whatsthis
```
