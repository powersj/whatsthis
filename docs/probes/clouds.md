# Clouds

## Detection

whatsthis attempts to identify if the system is running on a cloud based on
various heuristics.

## Supported

### Amazon Web Services

Amazon Web Services (AWS) has three types of instance platforms:

* Bare metal
* Nitro (KVM)
* HVM (Xen)

Bare metal and Nitro (KVM) based instances will report "Amazon EC2" as the
system vendor.

The older Xen based systems (e.g t2) will report Xen. To further identify these
systems the Hypervisor UUID will start with "ec2". These heuristics come from
[Amazon's website](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/identify_ec2_instances.html)

### Alibaba Cloud

Alibaba instances report the product name as "Alibaba Cloud ECS".

### CloudSigma

CloudSigma instances report the product name as "CloudSigma".

### CloudStack

CloudStack instances reported product name will start with "CloudStack".

### Digital Ocean

Digital Ocean instances report the system vendor as "DigitalOcean".

### Exoscale

Exoscale instances report the product name as "Exoscale".

### Google Cloud Platform

Google Cloud Platform instances report the product name as "Google Compute
Engine".

### Hetzner

Hetzner instances report the system vendor as "Hetzner".

### Microsoft Azure

Microsoft Azure instances report the chassis asset tag as the hard-coded
value of "7783-7084-3265-9085-8269-3286-77".

### OpenStack

OpenStack instances report system vendor as "OpenStack Foundation".

### Oracle Cloud

Oracle cloud report the chassis asset tag as "OracleCloud.com".

### SmartOS

SmartOS reports the product name start with "SmartDC".

## Other

Other clouds that could be added at a future date include:

* IBM Cloud
