package cloud

import (
	"fmt"
	"strings"

	"github.com/powersj/whatsthis/internal/filesystem"
	"github.com/powersj/whatsthis/internal/util"
)

// Probe struct for clouds. Used to store the results of the probe and the
// name of the cloud discovered.
type Probe struct {
	sys filesystem.Sys

	Name     string          `json:"name"`
	Detected bool            `json:"detected"`
	Results  map[string]bool `json:"results"`
}

// New initializes new probe struct and probes the system.
func New() (*Probe, error) {
	sys := filesystem.Sys{}

	probe := &Probe{
		sys:      sys,
		Detected: false,
		Name:     "",
		Results:  make(map[string]bool),
	}
	if err := probe.probe(); err != nil {
		return nil, err
	}

	return probe, nil
}

// Probe the system
func (p *Probe) probe() error {
	var clouds = map[string]func() bool{
		"alibaba":      p.Alibaba,
		"aws":          p.AWS,
		"azure":        p.Azure,
		"cloudsigma":   p.CloudSigma,
		"cloudstack":   p.CloudStack,
		"digitalocean": p.DigitalOcean,
		"exoscale":     p.Exoscale,
		"gcp":          p.GCP,
		"hetzner":      p.Hetzner,
		"openstack":    p.OpenStack,
		"oracle":       p.Oracle,
		"smartos":      p.SmartOS,
	}

	for cloud, detect := range clouds {
		var result bool = detect()

		p.Results[cloud] = result
		if result {
			p.Detected = true
			p.Name = cloud
		}
	}

	return nil
}

// String representation of the struct
func (p *Probe) String() string {
	if p.Name == "" {
		return "cloud: not detected"
	}

	return fmt.Sprintf("cloud: %s", p.Name)
}

// JSON representation of the struct
func (p *Probe) JSON() string {
	return util.ObjectJSONString(&p)
}

// Alibaba detects if a system is on the Alibaba Cloud.
func (p *Probe) Alibaba() bool {
	return p.sys.ProductName() == "Alibaba Cloud ECS"
}

// AWS detects if a system is on Amazon Web Services (AWS). Baremetal
// and Nitro (KVM) based instances will have "Amazon EC2" as the sys_vendor.
// The older Xen based systems (e.g t2) will show Xen. To further identify
// these systems the Hypervisor UUID will start with "ec2"
//
// https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/identify_ec2_instances.html
func (p *Probe) AWS() bool {
	var sysVendor string = p.sys.SysVendor()

	if sysVendor == "Amazon EC2" {
		return true
	} else if sysVendor == "Xen" &&
		strings.HasPrefix(p.sys.HypervisorUUID(), "ec2") {
		return true
	}

	return false
}

// Azure detects if a system is on Microsoft Azure. The value assigned
// to the chassis_asset_tag in sys is hard-coded on Azure and is used
// to ID the platform.
//
// https://bugs.launchpad.net/cloud-init/+bug/1693939
func (p *Probe) Azure() bool {
	return p.sys.ChassisAssetTag() == "7783-7084-3265-9085-8269-3286-77"
}

// CloudSigma detects if a system is on CloudSigma.
func (p *Probe) CloudSigma() bool {
	return p.sys.ProductName() == "CloudSigma"
}

// CloudStack detects if a system is on Apache CloudStack.
func (p *Probe) CloudStack() bool {
	return strings.HasPrefix(p.sys.ProductName(), "CloudStack")
}

// DigitalOcean detects if a system is on DigitalOcean.
func (p *Probe) DigitalOcean() bool {
	return p.sys.SysVendor() == "DigitalOcean"
}

// Exoscale detects if a system is on the Apache Exoscale.
func (p *Probe) Exoscale() bool {
	return strings.HasPrefix(p.sys.ProductName(), "Exoscale")
}

// GCP detects if a system is on Google Compute Platform.
//
// Source:
// https://github.com/googleapis/google-cloud-go/blob/master/compute/metadata/metadata.go#L188
func (p *Probe) GCP() bool {
	return p.sys.ProductName() == "Google Compute Engine"
}

// Hetzner detects if a system is on the Hetzner Cloud.
func (p *Probe) Hetzner() bool {
	return p.sys.SysVendor() == "Hetzner"
}

// OpenStack detects if a system is on OpenStack.
func (p *Probe) OpenStack() bool {
	return p.sys.SysVendor() == "OpenStack Foundation"
}

// Oracle detects if a system is on Oracle Cloud.
func (p *Probe) Oracle() bool {
	return p.sys.ChassisAssetTag() == "OracleCloud.com"
}

// SmartOS detects if a system is on SmartOS.
func (p *Probe) SmartOS() bool {
	return strings.HasPrefix(p.sys.ProductName(), "SmartDC")
}
