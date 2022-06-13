# AWS Architect 

## Cloud

- CSP(Cloud Service Provider)
- 컴퓨팅 리소스(CPU, RAM, Network, Server, Storage, Application, Service) => Provisioning(설정)

## AWS

---

### 특장점

- 초기 비용 없이 사용한 만큼만 지불하는 종량 과금제 방식, 주문제(On demand), Pay-as-you-go, 물리서버 구축(X)
- 온프레미스 서버 구축 기간과 비교하여 빠른 인프라 구축 속도
- 온프레미스 서버 환경의 리소스 확장 시와 달리 사전 리소스 확보 불필요
- 인스턴스 라이프사이클(start, stop, restart, terminate, hibernate)의 손쉬운 관리
- 고가용성(High Availability) 및 무정지 장애허용 시스템(Fault Tolerance - 내결함성) 구축에 필요한 서비스 제공
- API 제공으로 서비스 관리 자동화 용이

### 비용

1. EC2 인스턴스 시작(launch, create) 유형 -> t(용도- 범용)2(CPU 세대).micro (CPU 1C, RAM 1G)
   - 온 디맨드 인스턴스(On Demand Instance)
     - 사용한 만큼 지불
     - 비용은 가장 높지만 선불 결제 없음
     - 장기 약정 없음
     - 애플리케이션의 작동 방식을 예측할 수 없는 단기 및 중단 없는 워크로드에 권장
   - 예약 인스턴스(Reserved Instance, RI)
     - 주문형(온디맨드)에 비해 최대 75% 할인
     - 선결제
     - 기간은 1년 또는 3년
     - 가변 예약 인스턴스
     - 스케쥴된 예약 인스턴스
   - 스팟 인스턴스
     - 가장 비용 효율적인 인스턴스
     - 주문형에 비해 최대 90% 할인을 받음
     - 경매 방식, 구매 후에 운영 중에도 경매가 진행됨
     - Homepage, DB 서버 구성 X => 짧은 시간동안 보유
     - 장애에 탄력적인 워크로드 병렬
       - Batch 작업
       - 데이터 분석
       - 이미지 처리
    - EKS Cluster - Desired capacity 쿠버네티스와 사용할 때 비용 효율적으로 구성 가능  
   - 전용 호스트
     - 한 사용자를 위한 물리적 전용 EC2 서버
     - EC2 인스턴스 배치를 완전히 제어
     - 3년동안 사용자의 계정에 할당
     - 비쌈
     - 복잡한 라이선싱 모델 있는 소프트웨어, 강력한 규제 또는 규정 준수 요구가 있는 회사


## EC2

- 생성 방식은 예전에 해오던것과 똑같이 진행
- bash 파일만 다시 작성
```
#!/bin/bash
yum install -y httpd git
systemctl enable --now httpd
cd /tmp
git clone https://github.com/hali-linux/html.git
cp -r /tmp/html/* /var/www/html/

```

## VPC

- Virtual Private Cloud(VPC) : 사용자의 AWS 계정 전용 가상 네트워크
- Subnet : 각각의 AZ에 1개씩 네트워크 주소가 할당된 VPC의 IP 주소 범위
- 인터넷 게이트웨이 : VPC의 리소스와 인터넷 간의 통신을 활성화하기 위해 VPC에 연결하는 게이트웨이
- 라우팅 테이블 : 네트워크 트래픽을 전달할 위치를 결정하는데 사용되는 라우팅이라는 규칙 집합
- 사설 IP 대역
  - 10.0.0.0 ~ 10.255.255.255
  - 172.16.0.0 ~ 172.31.255.255
  - 192.168.0.0 ~ 192.168.255.255
- VPC 생성
  - 이름 : NEW-VPC
  - IPv4 : 192.168.0.0/16
  - 작업 : DNS 호스트 이름 체크
- SUBNET 생성
  - Public Subnet
    - 작업-서브넷 설정 편집
    - 자동 할당 ip 설정
  - Private Subnet
- IGW 생성
  - 이름 : NEW-IGW
- 라우팅 테이블
  - 이름 : NEW-PUBLIC-SUBNET-RTB
  - 라우팅 - 편집 : 0.0.0.0/0 인터넷 게이트웨이
  - 서브넷 연결 : 명시적 서브넷 연결 (PUBLIC SUBNET만)
  - 이름 : NEW-PRIVATE-SUBNET-RTB
  - 서브넷 연결 : 명시적 서브넷 연결 (PRIVATE SUBNET만)

### VPC Peering Connection

- 다른 두 VPC간 프라이빗 IP를 통하여 통신
- 사용자가 다른 두 VPC와의 피어링 연결
- 다른 리전간의 VPC 피어링
- VPC를 만드는 이유
  - IP 대역이 같으면 VPC Peering이 충돌남
- 어느 VPC간 요청을 하면 다른 VPC에서 수락을 해줘야함
- 피어링 연결 생성
  - 이름 : MY-PCX
  - 로컬 VPC(요청자) : MY-VPC
  - 피어링 할 다른 VPC 선택(수락자)
    - 계정 : 내 계정
    - 리전 : 다른 리전 / 아시아 태평양(도쿄)
    - VPC ID(수락자) : 다른 리전 VPC ID
- 도쿄 피어링 연결
  - 요청 수락
  - 라우팅 테이블 세팅하기
  - 라우팅 테이블 - 라우팅 편집
  - Destination(대상) : 서울의 MY-VPC 10.26.0.0/16 Target(대상) : 피어링 연결(pcx)
- 서울 라우팅 테이블 세팅
  - 라우팅 테이블 - 라우팅 편집
  - Destination(대상) : 도쿄의 VPC 172.31.0.0/16  Target(대상) : 피어링 연결(pcx)
- 도쿄에서는 외부로는 핑이 안나가고 서울 인스턴스만 핑이 나감
- 도쿄에서 외부로 핑 나가게 하기
  - 탄력적 IP 할당
  - 탄력적 IP 인스턴스 연결