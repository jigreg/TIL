# Hybrid Computer

## OpenStack(Private Cloud) <-> AWS(Public Cloud)

### VPN Site to Site

- Site to Site (S2S)
- VPC - 가상 사설 네트워크
- 고객 게이트웨이 생성
  - 이름 : MY-CGW
  - 내 IP 검색해서 나온것 입력 : 123.142.252.25
- 가상 프라이빗 게이트웨이 생성 
  - 이름 : MY-VGW
  - Amazon 기본 ASN


### GSLB(Global Server Load Balancing)

- AWS EC2 만들기
  - 인스턴스명 : Seoul
  - Region : Seoul
  - 사용자 데이터
```bash
#!/bin/bash
yum install -y httpd
systemctl enable --now httpd
echo "<h1>SEOUL</h1>" > /var/www/html/index.html
```
- Azure 가상머신 만들기
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
- GCP 가상 머신 만들기
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