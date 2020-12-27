# KVM

The following describes how to launch a KVM system on Ubuntu in order to test
the KVM detection.

## Multipass

Multipass is a quick way to get an Ubuntu VM up and running. It is available
on Windows, MacOS, and Linux. On Windows it will use the Hyper-V, on
MacOS it will use hyperkit, and on Linux it uses KVM.

To get a Multipass VM on Ubuntu setup to test whatsthis run the following:

```text
snap install multipass
multipass launch focal --name f1
multipass transfer whatsthis f1:/home/ubuntu/whatsthis
multipass exec f1 ./whatsthis
```

## CLI

These instructions are identical to the QEMU instructions except for the
addition of the "-enable-kvm" option used during the launch of the VM.

First, create some user-data to pass the VM that will setup the 'ubuntu' user
with the password of 'password'. Also set your GitHub ID and it will
automatically import your SSH key into the VM:

```shell
export GITHUB_ID=<GITHUB_ID>
sudo apt update
sudo apt install --yes cloud-image-utils
cat > user-data.yaml <<EOF
#cloud-config
password: password
chpasswd:
    expire: False
ssh_pwauth: True
ssh_import_id:
    - gh:$GITHUB_ID
EOF
cloud-localds seed.img user-data.yaml
```

Get the latest Ubuntu 20.04 LTS (Focal) image and launch the VM:

```shell
wget https://cloud-images.ubuntu.com/focal/current/focal-server-cloudimg-amd64.img
qemu-system-x86_64 -enable-kvm -m 2048 -nographic -snapshot \
    -netdev id=net00,type=user,hostfwd=tcp::2222-:22 \
    -device virtio-net-pci,netdev=net00 \
    -drive if=virtio,format=qcow2,file=focal-server-cloudimg-amd64.img \
    -drive if=virtio,format=raw,file=seed.img
```

Once the system has booted, transfer a local test binary run:

```shell
rsync -e "ssh -p 2222" whatsthis ubuntu@0.0.0.0:/home/ubuntu/whatsthis
```

Then either login with `ubuntu` and `password` or SSH to the system using:

```shell
ssh -o "StrictHostKeyChecking no" ubuntu@0.0.0.0 -p 2222
```

When done to close out of the qemu process using the escape sequence:

```shell
Ctrl-a c
(qemu) quit
```
