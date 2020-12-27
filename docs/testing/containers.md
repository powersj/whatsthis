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

TODO
