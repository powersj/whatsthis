# Virtualization

## Detection

whatsthis attempts to identify the system's virtualization platforms based
on the result of the CPU identification instruction known as
[cpuid](https://en.wikipedia.org/wiki/CPUID).

The instruction was created to provide a mechanism for programmers to obtain
the system's CPU model. Virtualization providers will set this string to
provide a mechanism to determine what virtualization platfrom a system is
running on.

!!! bug
    As cpuid is only available on x86-64, virtualization support in aarch64 is
    currently non-existant. When running on aarch64, the function will always
    return an emptry string and therefore never detect any virtualization
    platform correctly.

## Supported

Below is a table of the currently known virtualization platforms and their
cooresponding advertised vendor ID found from cpuid:

| Platform   | Vendor ID      |
| :--------- | :------------- |
|  bhyve     | `bhyve bhyve ` |
|  hyper-v   | `Microsoft Hv` |
|  kvm       | ` KVMKVMKVM `  |
|  parallels | ` lrpepyh vr`  |
|  qemu      | `TCGTCGTCGTCG` |
|  vmware    | `VMwareVMware` |
|  xen       | `XenVMMXenVMM` |

!!! note
    Using cpuid on these platforms provides a good first heuristic when
    attempting to determine the platform. However, there are cases where these
    platforms have additional product offerings and using the cpuid alone is
    not enough. Please feel free to file an
    [issue](https://github.com/powersj/whatsthis/issues/new) if you come
    across one of these scenarios.

## Other

Other virtualization detection software like
[virt-what](https://people.redhat.com/~rjones/virt-what/) or
[imvirt](http://micky.ibh.net/~liske/imvirt.html) have detection for other
additional platforms. For the initial development of the app, platforms were
limited to those that could easily be tested. The are some additional
virtualization platforms that could be added at a later date:

* acrn
* bochs
* qnx
* lkvm
* uml
* virtual box
