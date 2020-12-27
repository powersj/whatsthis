# Containers

## Detection

whatsthis attempts to identify if the system is running in a container based
on a variety of heuristic.

## Supported

### docker

First look for the `/run/.dockerenv` file to identify a Docker container. Then
look for "docker" inside `/proc/cgroups`.

### lxc

Looks for the string "container=" in `/proc/environ`.

### podman

Per a [GitHub issue](https://github.com/containers/podman/issues/3586#issuecomment-661918679)
on the podman project page, there is a guarantee that container environment
variable will be set to "podman".

The environment variable could be overridden by a user or image creator. As
such, this looks for the `/run/.containerenv` file as well.

### wsl

Per a [GitHub issue](https://github.com/Microsoft/WSL/issues/423#issuecomment-221627364)
on the WSL project page, checking for "microsoft" in either of these
two files:

* `/proc/sys/kernel/osrelease`
* `/proc/version`

## Other

For the initial development of the app, platforms were limited to those that
could easily be tested. The are some additional container run-times that could
be added at a later date:

* `bottlerocket`
* `rkt`: however, per [GitHub page](https://github.com/rkt/rkt) no longer under
  development
* `openvz`: the commercial version, Virtuozzo is available, but otherwise
  development appears to have ended
