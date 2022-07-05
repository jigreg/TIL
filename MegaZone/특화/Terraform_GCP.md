# Terraform GCP 

## GCP CLI Setup
```
# mkdir gcp_cli && cd $_
# tee -a /etc/yum.repos.d/google-cloud-sdk.repo << EOM
[google-cloud-cli]
name=Google Cloud CLI
baseurl=https://packages.cloud.google.com/yum/repos/cloud-sdk-el8-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=0
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
       https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
EOM
# yum install -y google-cloud-cli
# gcloud --version
# gcloud init --console-only
asia-northeast3-a [50]
```

## GCP CLI VPC/VM Create
```
# gcloud compute networks create new-vpc
# gcloud compute networks subnets create new-subnet --network=new-vpc --range=192.168.0.0/16 --region=asia-northeast3
# gcloud compute firewall-rules list
# gcloud compute firewall-rules create new-vpc-allow-ssh --allow=tcp:22 --description="Allow incoming traffic on TCP port 22" --direction=INGRESS --network=new-vpc --source-ranges 0.0.0.0/0
# gcloud compute firewall-rules create new-vpc-allow-http --allow=tcp:80 --description="Allow incoming traffic on TCP port 80" --direction=INGRESS --network=new-vpc --source-ranges 0.0.0.0/0
# gcloud compute images list
# gcloud compute images describe centos-7-v20220621 \
    --project=centos-cloud
# gcloud compute machine-types list --filter="zone:( asia-northeast3-a )"
# vi httpd-gcp.txt
#!/bin/bash
yum install -y httpd
systemctl enable --now httpd
echo "Hello GCP CLI" > /var/www/html/index.html

# gcloud compute instances create web01 \
    --image=centos-7-v20220621 \
    --image-project=centos-cloud \
    --machine-type=e2-micro \
    --network=new-vpc \
    --subnet=new-subnet \
    --tags http-server,https-server \
    --zone=asia-northeast3-a \
    --metadata-from-file=startup-script=httpd-gcp.txt

# ssh-keygen -t rsa -f /root/.ssh/johnlee -C johnlee -b 2048
# vi /root/.ssh/johnlee.pub
johnlee:ssh-rsa
# gcloud compute os-login ssh-keys add \
    --key-file=/root/.ssh/johnlee.pub \
    --project=gcp-seojun \
    --ttl=365d
# gcloud compute instances add-metadata web01 --metadata-from-file ssh-keys=/root/.ssh/johnlee.pub
# gcloud compute instances describe web01
# curl 34.64.150.44
# ssh -i /root/.ssh/johnlee johnlee@34.64.150.44
# gcloud compute instances delete web01
# gcloud compute firewall-rules list
# gcloud compute firewall-rules delete new-vpc-allow-http
# gcloud compute firewall-rules delete new-vpc-allow-ssh
# gcloud compute networks subnets delete new-subnet
# gcloud compute networks delete new-vpc
```

## GCP Terraform VPC/VM Create
- provider.tf, credentials 재 세팅해야함
```
# vi provider.tf
provider "google" {
  credentials = file("credentials.json")
  project = "gcp-seojun"
  region = "asia-northeast3"
  zone = "asia-northeast3-a"
}

# vi main.tf
resource "google_compute_network" "custom-test" {
  name                    = "new-vpc"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "network-with-private-ip-ranges" {
  name          = "new-subnet"
  ip_cidr_range = "192.168.0.0/16"
  region        = "asia-northeast3"
  network       = google_compute_network.custom-test.id
}

resource "google_compute_instance" "default" {
  name         = "vm-from-terraform"
  machine_type = "e2-micro"
  zone         = "asia-northeast3-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-9"
    }
  }

  network_interface {
    network = google_compute_network.custom-test.name
    subnetwork = "new-subnet"

    access_config {
      // Include this section to give the VM an external ip address
    }
  }

    metadata_startup_script = file("/root/gcp_set/script.txt")

    // Apply the firewall rule to allow external IPs to access this instance
    tags = ["http-server"]
}

resource "google_compute_firewall" "http-server" {
  name    = "default-allow-http-terraform"
  network = "new-vpc"

  allow {
    protocol = "tcp"
    ports    = ["80"]
  }

  // Allow traffic from everywhere to instances with an http-server tag
  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["http-server"]
}

resource "google_compute_firewall" "ssh-server" {
  name    = "default-allow-ssh-terraform"
  network = "new-vpc"
  allow {
    protocol = "tcp"
    ports    = ["22"]
  }
  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["ssh-server"]
}


# vi output.tf
output "ip" {
  value = "${google_compute_instance.default.network_interface.0.access_config.0.nat_ip}"
}
# terraform init
# terraform plan
# terraform apply
# terraform output ip
```