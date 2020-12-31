# Hyper-V

## Enable Hyper-V

Open a PowerShell console as Administrator and run the following and reboot the
system:

`Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All`

For more details and options see the
[Install Hyper-V on Windows 10](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v)
documentation.

## Multipass

Multipass is a quick way to get an Ubuntu VM up and running. It is available
on Windows, MacOS, and Linux. On Windows, if Hyper-V is enabled, it can take
advantage of Hyper-V.

Once downloaded and installed, a user can launch a VM in PowerShell, transfer a
test binary, and test it with:

```text
multipass launch focal --name test
multipass transfer whatsthis test:/home/ubuntu/whatsthis
multipass exec test ./whatsthis
multipass delete --force test
```
