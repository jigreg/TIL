# IaC(Infrastructure as Code) - 구성 및 설정 자동화

## Terraform

### CentOS7 
- VM Spec
  - 메모리 4GB
  - VDI(VirtualBox 디스크 이미지)
  - 동적 할당 - 씬 프로비저닝 (실무에선 고정 크기 - 씩 프로비저닝)
  - 디스크 128GB
  - CPU 2Core
  - 저장소 - 광학 드라이브 - IDE 세컨더리 마스터 - CentOS7 Minimal.iso
  - 네트워크 - 어댑터에 브릿지
- CentOS7 설정
```bash
# yum install -y bash-completion wget unzip rdate
# rdate -s time.bora.net
# setenforce 0
# sed -i s/^SELINUX=.*$/SELINUX=disabled/ /etc/selinux/config
# cd /tmp
# systemctl disable --now firewalld
# yum update -y
# reboot
``` 
- AWS CLI 설치
```bash
# curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
# unzip awscliv2.zip
# ./aws/install
# vi .bash_profile
$ complete -C '/usr/local/bin/aws_completer' aws
# aws --version
# aws s3 ls # aws login 여부 파악
# aws configure
# Access Key, Region : ap-northeast-2, filetype : json
```
- AWS VPC & Subnet 만들기
```bash
# aws ec2 create-vpc --cidr-block 192.168.0.0/16 --tag-specification "ResourceType=vpc,Tags=[{Key=Name,Value=NEW-VPC}]" --output text
# NEW_VPC=vpc-0b86b4b6ab0bce886
# echo $NEW_VPC
# aws ec2 create-subnet --vpc-id $NEW_VPC --cidr-block 192.168.0.0/20 --availability-zone ap-northeast-2a --tag-specification "ResourceType=subnet,Tags=[{Key=Name,Value=NEW-PUBLIC-SUBNET-2A}]"
# aws ec2 create-subnet --vpc-id $NEW_VPC --cidr-block 192.168.16.0/20 --availability-zone ap-northeast-2b --tag-specification "ResourceType=subnet,Tags=[{Key=Name,Value=NEW-PUBLIC-SUBNET-2B}]"
# aws ec2 create-subnet --vpc-id $NEW_VPC --cidr-block 192.168.32.0/20 --availability-zone ap-northeast-2c --tag-specification "ResourceType=subnet,Tags=[{Key=Name,Value=NEW-PUBLIC-SUBNET-2C}]"
# aws ec2 create-subnet --vpc-id $NEW_VPC --cidr-block 192.168.48.0/20 --availability-zone ap-northeast-2d --tag-specification "ResourceType=subnet,Tags=[{Key=Name,Value=NEW-PUBLIC-SUBNET-2D}]"
# aws ec2 describe-subnets --filters "Name=vpc-id,Values=$NEW_VPC" --query 'Subnets[*].{AZ:AvailabilityZone,CIDR:CidrBlock}'
```
- 서브넷을 퍼블릭 서브넷으로 만들기
```bash
# aws ec2 create-internet-gateway --tag-specification "ResourceType=internet-gateway,Tags=[{Key=Name,Value=NEW-IGW}]" --output text
# NEW_IGW=igw-07bcf6f436dc7df46
# aws ec2 attach-internet-gateway --vpc-id $NEW_VPC --internet-gateway-id $NEW_IGW
# aws ec2 describe-internet-gateways --output table
# aws ec2 describe-route-tables --filter "Name=vpc-id,Values=$NEW_VPC"
# NEW_RTB=rtb-0c92dd389865be7e3
# aws ec2 create-route --route-table-id $NEW_RTB --destination-cidr-block 0.0.0.0/0 --gateway-id $NEW_IGW
# aws ec2 create-tags --resources $NEW_RTB --tags "Key=Name,Value=NEW-PUBLIC-SUBNET-RTB"
# aws ec2 describe-route-tables --route-table-id $NEW_RTB --output table
# aws ec2 describe-subnets --filters "Name=vpc-id,Values=$NEW_VPC" --query 'Subnets[*].{ID:SubnetId,CIDR:CidrBlock}'
# NEW_SID1=subnet-0378a9a32f00d1a52
# NEW_SID2=subnet-04c1079a3501166e1
# NEW_SID3=subnet-0454c51cfbf6b303a
# NEW_SID4=subnet-0e90af0e60dae58b2
# aws ec2 associate-route-table  --subnet-id $NEW_SID1 --route-table-id $NEW_RTB
# aws ec2 associate-route-table  --subnet-id $NEW_SID2 --route-table-id $NEW_RTB
# aws ec2 associate-route-table  --subnet-id $NEW_SID3 --route-table-id $NEW_RTB
# aws ec2 associate-route-table  --subnet-id $NEW_SID4 --route-table-id $NEW_RTB
# aws ec2 modify-subnet-attribute --subnet-id $NEW_SID1 --map-public-ip-on-launch
# aws ec2 modify-subnet-attribute --subnet-id $NEW_SID2 --map-public-ip-on-launch
# aws ec2 modify-subnet-attribute --subnet-id $NEW_SID3 --map-public-ip-on-launch
# aws ec2 modify-subnet-attribute --subnet-id $NEW_SID4 --map-public-ip-on-launch
# aws ec2 modify-vpc-attribute --vpc-id $NEW_VPC --enable-dns-hostnames
```
- 키페어, 보안그룹 만들기
```bash
# aws ec2 create-key-pair --key-name new-key --query 'KeyMaterial' --output text > new-key.pem
# chmod 400 new-key.pem
# aws ec2 create-security-group --group-name NEW-SG-WEB --description "Security group for HTTP_SSH access" --vpc-id $NEW_VPC
# NEW_SG=sg-0d3a7a4ddd609d7eb
# aws ec2 authorize-security-group-ingress --group-id $NEW_SG --protocol tcp --port 22 --cidr 0.0.0.0/0
# aws ec2 authorize-security-group-ingress --group-id $NEW_SG --protocol tcp --port 80 --cidr 0.0.0.0/0
# aws ec2 authorize-security-group-ingress --group-id $NEW_SG --protocol icmp --port -1 --cidr 0.0.0.0/0
```
- 볼륨 및 인스턴스 만들기
```bash
# vi mapping.json
[
    {
        "DeviceName": "/dev/xvda",
        "Ebs": {
            "VolumeSize": 8
        }
    }
]

# vi my_script.txt
#!/bin/bash
yum install -y httpd
systemctl enable --now httpd
echo "<h1>Hello AWS CLI</h1>" > /var/www/html/index.html

# aws ec2 run-instances \
--image-id ami-0fd0765afb77bcca7 \
--count 1 \
--instance-type t2.micro \
--key-name new-key \
--security-group-ids $NEW_SG \
--subnet-id $NEW_SID1 \
--block-device-mappings file://mapping.json \
--user-data file://my_script.txt \
--tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=NEW-WEB}]' 'ResourceType=volume,Tags=[{Key=Name,Value=NEW-ROOT}]'

# NEW_IID=i-0c49036485c1ce2bd
# aws ec2 describe-instances --instance-id $NEW_IID | grep PublicIp
# ssh -i "new-key.pem" ec2-user@3.38.165.0
# curl 3.38.165.0
```
## Ansible

# Container 기술 및 오케스트레이션

## Docker

## Kubernetes

# CI/CD (Continuous Integration / Continuous Deployment , Delivery)

## Jenkins

## Git 