# TODO

Random notes about things to work on.

## Cloud
* AWS
  * curl --silent http://169.254.169.254/latest/dynamic/instance-identity/document
  * imageId
  * region
  * instanceType

## Network
* Driver (ethtool + modinfo)
    ethtool -i eth0 | grep driver | cut -d' ' -f2
* Offload info
    sudo ethtool -k eth0
* Device speed
    # doesn't always show something
    sudo ethtool eth0

## kernel info
* version
    /proc/sys/kernel/osrelease
