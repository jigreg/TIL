# Open Stack
---

## 5 core service
1) Compute Service(CPU,RAM) : Nova, AWS(EC2) - Elastic Compute Cloud
2) Storage Service(SSD, GoogleDrive, NFS, NAS) : Cinder, Block Storage, AWS(EBS) - Elastic Block Store
                                                 Swift, Object Storage, AWS(S3) - Simple Storage Service
                                                 Manila, File Storage, AWS(EFS) - Elastic File System
3) Network Service (IP, Subnet) : Neutron, AWS(VPC) - Virtual Private Cloud
4) Image Service(OS) : Glance, AWS(AMI) - Amazon Machine Image
5) Identitiy Service(User(ID/PW), Group, Role) - KeyStone, AWS(IAM) - Identity Access Management

Optional Service 
6) Orchestration Service(IaC - Infra as a Code) - Heat, AWS(CloudFormation)

## VM Setting
- SSD : 128GB
- CPU : 4C (Virtualize Intel VT-x/EPT or AMD-v/RVI)
- RAM : 12GB (12,288MB)
- OS : CentOS8 - Stream
- Net : Bridged
- Sec : 
- SWAP : 12GB
- 파티션 Setting : /home 삭제 후 swap 메모리에 추가 할당 (12GB)
- Software Selection : Minimal Install

### Openstack VM 최소사양 & 권장사양
- CPU : 4C(시스템 8C)        24C (Baremetal)
- RAM : 8GB(시스템 16GB)     24GB (Baremetal)

## Open Stack Setting
- IP : 192.168.0.99/20
- G/W : 192.168.0.1
- 인증 : 프로젝트 생성, 사용자 생성
- 관리 - 네트워크 
  - 네트워크 생성 (External-Network)
  - 공급자 네트워크 유형 : Flat
  - 물리적인 네트워크 : extnet
  - 외부네트워크 ,DHCP 사용 체크 해제
  - SUBNET 생성 : EXTERNAL-SUBNET , 192.168.0.0/20 , 192.168.0.1
  - Pools 할당 192.168.10.129,192.168.10.254
- Compute - Flavor
  - Flavor 생성
  - m1.micro, ID : 6, VCPUs : 1, RAM : 1024, Root Disk : 10GB
- 보안그룹 : 내보냄 = outbound = egress(오픈스택에서 밖으로 내보냄) all allow
             들어옴 = inbound = ingress(밖에서 오픈스택으로 들어옴) all deny(block)
             http,ssh,icmp 들어옴 추가
             출발지 = source(src); src ip, src port
             목적지 = destination(dst); dst ip, dst port (dest)
- 인스턴스 : 시작 = launch = create , start (poweroff -> start)
- 인스턴스 생성 - 사용자 정의 스크립트 root 권한으로 실행되므로 sudo를 붙일 필요가 없음
- 오브젝트 스토리지 - 컨테이너
  - 컨테이너 이름 부여, 접근 공용
  - wordpress-4.8.2-ko_KR.zip 업로드
  - http://192.168.0.126:8080/v1/AUTH_6aa303d06fe9453d86086ddb32940b0e/files/wordpress-4.8.2-ko_KR.zip
- WEBSERVER를 경유지로 하는 것을 Bastion(요새) 호스트 
```shell
#!/bin/bash
setenforce 0
sed -i 's/^SELINUX=enforcing$/SELINUX=disabled/' /etc/selinux/config # 치환 명령어
yum install -y httpd php php-mysql php-gd php-mbstring wget unzip
cd /home/centos
wget http://192.168.0.126:8080/v1/AUTH_6aa303d06fe9453d86086ddb32940b0e/files/wordpress-4.8.2-ko_KR.zip
cd /var/www/html
unzip /home/centos/wordpress-4.8.2-ko_KR.zip
mv ./wordpress/* .
chown -R apache:apache wordpress
systemctl enable --now httpd
```
- 볼륨 세팅 : 추가 확장 스토리지 
             attach > mount > umount > detach
             # sudo umount /mnt
             늘어난 볼륨을 줄이지 못함 / 리눅스 절대 규칙
             Scale up : 자원을 수직적 확장 <-> Scle down : 자원을 수직적 축소
             Scale out -> 자원을 수평적 확장

## Openstack 싱글 노드 설치
Openstack ip : 192.168.0.99/20
Gateway : 192.168.0.1
```
# vi /etc/sysconfig/network-scripts/ifcfg-ens160
TYPE=Ethernet
BOOTPROTO=none
NAME=ens160
DEVICE=ens160
ONBOOT=yes
IPADDR=192.168.0.99
NETMASK=255.255.240.0
GATEWAY=192.168.0.1
DNS1=192.168.0.66
DNS2=8.8.4.4
```
```
# vi /etc/selinux/config
SELINUX=disabled
```
```
# dnf install network-scripts -y
# systemctl disable --now firewalld
# systemctl disable --now NetworkManager
# systemctl enable --now network
# systemctl start network
# reboot
# dnf update -y
# dnf config-manager --enable powertools
# dnf install -y centos-release-openstack-yoga
# dnf update -y
# dnf install -y openstack-packstack
# packstack --gen-answer-file /root/answers.txt
# vi /root/answers.txt
CONFIG_DEFAULT_PASSWORD=Test1234!
CONFIG_KEYSTONE_ADMIN_PW=Test1234!
CONFIG_CINDER_VOLUMES_SIZE=100G
CONFIG_NTP_SERVERS=0.kr.pool.ntp.org
CONFIG_CEILOMETER_INSTALL=n
CONFIG_AODH_INSTALL=n
CONFIG_HEAT_INSTALL=y
CONFIG_NEUTRON_L2_AGENT=openvswitch
CONFIG_NEUTRON_ML2_TYPE_DRIVERS=vxlan,flat
CONFIG_NEUTRON_ML2_TENANT_NETWORK_TYPES=vxlan
CONFIG_NEUTRON_ML2_MECHANISM_DRIVERS=openvswitch
CONFIG_NEUTRON_OVS_BRIDGE_MAPPINGS=extnet:br-ex
CONFIG_NEUTRON_OVS_BRIDGE_IFACES=br-ex:ens160
CONFIG_PROVISION_DEMO=n
```
```
# packstack --answer-file /root/answers.txt 
```
## 볼륨 추가 명령어
```
$ lsblk
$ df -h
$ sudo mkfs -t xfs /dev/vdb
$ sudo mount /dev/vdb /mnt/
$ df -h
```
## 오브젝트 스토리지 활용 및 웹서버 설치
```
$ sudo yum install -y httpd wget
$ wget http://192.168.0.58:8080/v1/AUTH_b945e8b7c1e84a628c1e3776c5323093/web-store/openstack.tar
$ sudo tar -xvf openstack.tar -C /var/www/html/
$ sudo systemctl enable --now httpd
```
## 템플릿 생성기 활용
```
heat_template_version: "2021-04-16"
description: "version 2017-09-01 created by HOT Generator at Thu, 24 Mar 2022 06:33:11 GMT."
resources: 
  Server_1: 
    type: "OS::Nova::Server"
    properties: 
      security_groups: 
        - "9b873b26-b28b-41fa-9879-5643e41e697a"
      networks: 
        - subnet: "837fdb7b-f531-44d4-941f-ef4a82b00813"
      name: WEB03
      flavor: "m1.micro"
      image: "ab3427b3-fdbe-4972-816c-391dc7178286"
      availability_zone: nova
      key_name: "web-key"
```
## CLI 작업(ad-hoc)
Project
```
# source keystonerc_admin
# openstack project create --domain Default --description "cli-project" cli-project
# openstack project list
```
User
```
# openstack user create --domain Default --project cli-project --password-prompt cli-user
# openstack role add --project cli-project --user cli-user _member_
# openstack user list
```
Image
```
# openstack image create --file CentOS-7-x86_64-GenericCloud-2111.qcow2 --disk-format qcow2 --container-format bare CentOS7 
# openstack image create --file bionic-server-cloudimg-amd64.img --disk-format qcow2 --container-format bare Ubuntu18 --public
```
Flavor
```
# openstack flavor create --id 6 --vcpus 1 --ram 1024 --disk 10 m1.micro
# openstack flavor list
# openstack flavor delete m1.micro //flavor 지우기
```
External Network
```
# openstack network create --project cli-project --provider-network-type flat \
--provider-physical-network extnet --external External-Network
# openstack subnet create --network External-Network \
--project cli-project --subnet-range 192.168.0.0/20 \
--allocation-pool start=192.168.10.129,end=192.168.10.254 \
--gateway 192.168.0.1 --no-dhcp External-Subnet
# openstack subent show External-Subnet //자세히 보기
```

Token
```
# vi keystonerc_cli-user
unset OS_SERVICE_TOKEN
    export OS_USERNAME=cli-user
    export OS_PASSWORD='Test1234!'
    export OS_REGION_NAME=RegionOne
    export OS_AUTH_URL=http://192.168.0.126:5000/v3
    export PS1='[\u@\h \W(keystone_cli-user)]\$ '

export OS_PROJECT_NAME=cli-project
export OS_USER_DOMAIN_NAME=Default
export OS_PROJECT_DOMAIN_NAME=Default
export OS_IDENTITY_API_VERSION=3

# source keystonerc_cli-user
```
Internal Network
```
# vi /etc/neutron/policy.yaml
"create_network:provider:network_type": "role:admin or project_id:%(project_id)s"
"create_floatingip:floating_ip_address": "role:admin or project_id:%(project_id)s"
# projectID=$(openstack project list | grep cli-project | awk '{print $2}')
# openstack network create --project $projectID --provider-network-type vxlan Internal-Network
# openstack subnet create --network Internal-Network --subnet-range 10.26.0.0/20 --gateway 10.26.0.1 \
--dhcp --dns-nameserver 192.168.0.66 --dns-nameserver 8.8.8.8 Internal-Subnet
# openstack subnet delete Internal-subnet
```

Router
```
# openstack router create Router
# openstack router set --external-gateway External-Network Router
# openstack router add subnet Router Internal-Subnet
```
Security Group
```
# openstack security group create SG-WEB
# openstack security group rule create --protocol icmp --ingress SG-WEB
# openstack security group rule create --protocol tcp --dst-port 22:22 SG-WEB
# openstack security group rule create --protocol tcp --dst-port 80:80 SG-WEB
# openstack security group create SG-DB
# openstack security group rule create --protocol icmp --ingress SG-DB
# openstack security group rule create --protocol tcp --dst-port 22:22 SG-DB
# openstack security group rule create --protocol tcp --dst-port 3306:3306 SG-DB
```
KeyPair
```
# openstack keypair create --public-key ~/.ssh/id_rsa.pub cli-key
# openstack keypair create --private-key my-key.pem my-key
```
Floating IP
```
# openstack floating ip create External-Network
# openstack floating ip create --floating-ip-address 192.168.10.130 External-Network
# openstack server create --flavor m1.micro --image CentOS7 --security-group SG-WEB --network Internal-Network --boot-from-volume 10 --key-name cli-key --user-data httpd.file WEBSERVER
# openstack server create --flavor m1.micro --image Ubuntu18 --security-group SG-DB --network Internal-Network --boot-from-volume 10 --key-name cli-key DBSERVER
# openstack server list
# openstack floating ip list
# openstack server add floating ip WEBSERVER 192.168.10.130
# ssh -i .ssh/id_rsa centos@192.168.10.130
```

Volume
```
# openstack volume create --size 8 WEB01-ADD
# openstack volume list
# openstack server list
# openstack server add volume WEB01 WEB01-ADD
```