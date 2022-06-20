# Hybrid Cloud

## Hybrid Cloud (Public 와 Private Cloud 연결) - AWS Storage를 활용하는 방법

- AWS <-VPN-> Openstack
- AWS <-Storage Gateway-> ESXi(On-Pem) 

### VPN Site to Site

- Site to Site (S2S)
- VPC - 가상 사설 네트워크
- 고객 게이트웨이 생성
  - 이름 : MY-CGW
  - 내 IP 검색해서 나온것 입력 : 123.142.252.25
- 가상 프라이빗 게이트웨이 생성 
  - 이름 : MY-VGW
  - Amazon 기본 ASN
  - 작업 - VPC에 연결 - MY-VPC
- Site-to-Site VPN 연결
  - 이름 : MY-VPN 
  - 대상 게이트웨이 유형 : 가상 프라이빗 게이트웨이 / MY-VGW
  - 고객 게이트웨이 : 기존 / MY-CGW
  - 라우팅 옵션 : 정적 (동적은 기업용)
  - 고정 IP 접두사 : 192.168.0.0/20 (사설 IP 네트워크)
  - 로컬 IPv4 네트워크 CIDR : 192.168.0.0/20 (로컬 IP 대역/ 고정 IP와 같음)
  - 원격 IPv4 네트워크 CIDR : 10.26.0.0/16 (MY-VPC IP 대역)
  - 구성 다운로드
    - 공급 업체 : Openswan
    - 플랫폼 : Openswan
    - 소프트웨어 : Openswan 2.6.38+
    - IKE 버전 : ikev1
    - 다운로드 하면 아래와 같은 Tunnel 세부 세팅 값 나옴
- OpenStack VM
  - Libreswan
    - Libreswan은 "IPsec" 및 인터넷 키 교환 ( "IKE" ) 을 사용하여 가장 널리 지원되고 표준화된 VPN 프로토콜의 무료 소프트웨어 구현입니다 . 이러한 표준은 IETF ( Internet Engineering Task Force )에서 생성 및 유지 관리합니다.
  - IKE
    - IKE란 ISAKMP와 IPSec에서 사용되는 키 관리 프로토콜이다. IKE는 상호 개체간에 인증된 보안 통신 채널을 생성한다. 이 과정을 수행하기 위해서는 상호간에 서로를 인증하고 필요한 키를 교환해야 한다. IKE를 통한 협상 과정은 IKE 1단계(ISAKMP SA-Security Association)와 IKE 2단계(IPSec SA)로 구성된다. 이렇게 두단계의 SA가 생성되면 두 개체간에 전송되는 패킷들은 IPSec을 통하여 암호화와 인증 기능을 보장받게 된다
``` bash
# dnf install -y libreswan
# systemctl enable --now ipsec

# vi /etc/sysctl.conf
net.ipv4.ip_forward = 1
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.default.accept_redirects = 0
net.ipv4.conf.all.send_redirects = 0
net.ipv4.conf.default.rp_filter = 0
net.ipv4.conf.default.accept_source_route = 0
net.ipv4.conf.default.send_redirects = 0
net.ipv4.icmp_ignore_bogus_error_responses = 1
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1

for vpn in /proc/sys/net/ipv4/conf/*;
do echo 0 > $vpn/accept_redirects;
echo 0 > $vpn/send_redirects;
done

# sysctl -p

# 가용성을 위해 터널 2개 , left = 혜화 , right = aws
# vi /etc/ipsec.d/aws.conf
conn Tunnel1
	authby=secret
	auto=start
	left=%defaultroute
	leftid=123.142.252.25
	right=13.124.202.55
	type=tunnel
	ikelifetime=8h
	keylife=1h
	phase2alg=aes128-sha1;modp1024
	ike=aes128-sha1;modp1024
	keyingtries=%forever
	keyexchange=ike
	leftsubnet=192.168.0.0/20
	rightsubnet=10.26.0.0/16
	dpddelay=10
	dpdtimeout=30
	dpdaction=restart_by_peer
  overlapip=yes

conn Tunnel2
	authby=secret
	auto=start
	left=%defaultroute
	leftid=123.142.252.25
	right=54.180.47.146
	type=tunnel
	ikelifetime=8h
	keylife=1h
	phase2alg=aes128-sha1;modp1024
	ike=aes128-sha1;modp1024
	keyingtries=%forever
	keyexchange=ike
	leftsubnet=192.168.0.0/20
	rightsubnet=10.26.0.0/16
	dpddelay=10
	dpdtimeout=30
	dpdaction=restart_by_peer
  overlapip=yes

# vi /etc/ipsec.d/aws.secrets
123.142.252.25 13.124.202.55: PSK "psk-key"
123.142.252.25 54.180.47.146: PSK "Pre Shared Key / 구성 다운로드 하면 주어짐"

# systemctl restart ipsec
``` 
- MY-VPC 라우팅 편집
  - MY-PUBLIC-SUBNET-RTB 라우팅 편집
  - 192.168.0.0/20 가상 프라이빗 네트워크 vgw 추가
  - MY-PRIVATE-SUBNET-RTB 라우팅 편집
  - 192.168.0.0/20 가상 프라이빗 네트워크 vgw 추가
- Openstack 라우터 추가
  - 정적 경로 추가
  - 대상 CIDR : MY-VPC IP 추가 10.26.0.0/16 
  - 다음 홉 : Openstack IP 
  - Openstack이 AWS VGW 역할을 하므로 다음 홉을 Openstack ip


### GSLB(Global Server Load Balancing) - 무중단 서비스

- Cross Region
- VRRP : 이중화
- Fail Over : Active
- Passive : inactive, standby
- AWS EC2 만들기 (Seoul)
  - 인스턴스명 : Seoul
  - Region : Seoul
  - 사용자 데이터
```bash
#!/bin/bash
yum install -y httpd
systemctl enable --now httpd
echo "<h1>SEOUL</h1>" > /var/www/html/index.html
```
- Azure 가상머신 만들기 (London)
  - 리소스 그룹 만들기
    - RG-TEST
    - Region : UK South
  - 가상 머신 만들기
    - 리소스 그룹 : RG-TEST
    - 이름 : london
    - 지역 : UK South
    - 가용성 옵션 : 가용성 영역 / 영역 1
    - 관리 - 사용자 지정 데이터 및 Cloud-init
```bash
#!/bin/bash
yum install -y httpd
systemctl enable --now httpd
echo "<h1>LONDON</h1>" > /var/www/html/index.html
```
- GCP 가상 머신 만들기 (Oregon)
  - 이름 : oregon
  - 지역 : us-west1(오리건) / us-west1-b
  - CPU : E2 e2-micro
  - 부팅디스크 : CentOS 7
  - 액세스 범위 : 모든 Cloud API에 대한 전체 액세스 허용
  - 관리 - 자동화
```bash
#!/bin/bash
sed -i 's/^SELINUX=enforcing$/SELINUX=disabled/' /etc/selinux/config
yum install -y httpd
systemctl enable --now httpd
echo "<h1>OREGON</h1>" > /var/www/html/index.html

```
- 알리바바 인스턴스 켜기(Hongkong)
- 서울리전에서 ACM 받기
  - SSL 인증서 받기
  - Route 53에 등록
- 서울 리전에서 HAproxy를 위한 인스턴스 만들기
  - 인스턴스는 항상 만들어 온대로 진행
  - HA-seoul
  - 사용자 데이터 기입 X
```
# sudo yum install -y haproxy
# sudo vi /etc/haproxy/haproxy.cfg
global
    daemon

defaults
    mode               http

frontend  http-in
    bind *:80
    default_backend    backend_servers

backend backend_servers
    balance            roundrobin
#    cookie  SVID insert indirect nocache maxlife 3m
    server             seoul 3.36.122.217:80 cookie w1 check
    server             london 20.117.241.211:80 cookie w2 check
    server             oregon 35.247.86.177:80 cookie w3 check
    server             hongkong 47.242.248.113:80 cookie w4 check

# sudo systemctl start haproxy
# sudo systemctl enable haproxy
# sudo systemctl enable --now haproxy
# firewall-cmd --permanent --zone=external --add-service=http
# firewall-cmd --reload
```
- 도쿄 리전에서 HAproxy를 위한 인스턴스 만들기 
  - HA-seoul 이미지 생성
  - 서울 리전 EC2 작업-이미지 생성
    - MY-AMI
    - 재부팅 안함
  - 서울에서 만든 이미지 도쿄로 보내기 
    - AMI - 작업 - AMI 복사 (아시아 태평양 도쿄)
    - 인스턴스 만들기
      - HA-tokyo
      - 나머지 Default
- HOT Standby
- 이중화
- vrrp  
- 서울 리전에서 로드밸런서 생성
  - Application Load Balancer 생성
    - 이름 : seoul-alb
    - 네트워크 매핑 : MY-VPC
    - ap-northeast-2a / ap-northeast-2c
    - 보안그룹 : SG-ALB
    - 대상그룹 생성
      - TG-Seoul
      - 프로토콜 : HTTP 80
- 도쿄 리전에서 로드밸런서 생성
  - Application Load Balancer 생성
    - 이름 : tokyo-alb
    - 네트워크 매핑 : default VPC
    - ap-northeast-1a / ap-northeast-1c
    - 보안그룹 : SG-ALB
      - HTTPS / HTTP
    - 대상그룹 생성
      - TG-TOKYO
      - 프로토콜 : HTTP 80
- 단순 라우팅
  - ip 4개 넣었을 때 랜덤으로 접속 
- Route 53에서 상태검사
  - 상태 검사 생성
    - 이름 : active
    - 엔드포인트 지정 기준 : 도메인 이름
    - 프로토콜 : HTTPS
    - 도메인 이름 : seoul.seojun.shop
    - 고급 구성
      - 표준(30초)
      - 실패 임계값 : 1
    - 상태 검사 생성
    - 이름 : passive
    - 엔드포인트 지정 기준 : 도메인 이름
    - 프로토콜 : HTTPS
    - 도메인 이름 : tokyo.seojun.shop
    - 고급 구성
      - 표준(30초)
      - 실패 임계값 : 1
- Route 53에서 레코드 생성
  - 레코드 이름 : gslb
  - 레코드 유형 : A
  - 트래픽 라우팅 대상 : Application/Classic Load Balancer
  - 라우팅 정책 : 장애조치 
  - 장애 조치 레코드 유형 : 기본
  - 상태 확인 ID : active
  - 레코드 ID : Seoul-Actice
- 다른 레코드 추가 
  - 레코드 이름 : gslb
  - 레코드 유형 : A
  - 트래픽 라우팅 대상 : Application/Classic Load Balancer
  - 라우팅 정책 : 장애조치 
  - 장애 조치 레코드 유형 : 보조
  - 상태 확인 ID : passive
  - 레코드 ID : Tokyo-Active