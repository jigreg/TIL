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

### IAM

- AWS 서비스에 대한 액세스를 안전하게 제어하는 웹 서비스
- IAM을 통해 사용자, 액세스 키와 같은 보안 자격 증명, 사용자와 애플리케이션이 어떤 AWS 리소스에 액세스 할 수 있는지 제어하는 권한을 한 곳에서 관리

### RDS(Relational Database Service)

- 완전 관리형 서비스 - 고가용성, 자동백업, 자동조정
- 데이터 베이스 생성
  - MySQL 5.7.22
  - 개발(Dev) -> 테스트(QA) -> 스테이징 -> 프로덕션(Ops)
- 퍼블릭 액세스는 웬만하면 사용 X
- 굳이 해야된다면 퍼블릭 서브넷으로 연결
- 이미 적용된 서브넷 그룹은 변경 X

### ELB(Elatsic Load Balancing)

- 대상 그룹
  - 인스턴스
  - 이름 : TG-NLB
  - TCP 80
  - 아래에 보류 중인 것으로 포함
  - 대상 그룹 생성
  - 인스턴스
  - 이름 : TG-ALB
  - HTTP 80
  - HTTP1
  - 아래에 보류 중인 것으로 포함
  - 대상 그룹 생성
- Network Load Balancer
  - 이름 : ELB-NLB
  - 체계 : 인터넷 경계
  - IP유형 : IPv4
  - 네트워크 매핑 
    - VPC : MY-VPC
    - 매핑 : ap-northeast-2a / ap-northeast-2c
- Application Load Balancer
  - 이름 : ELB-ALB 
  - 체계 : 인터넷 경계
  - IP유형 : IPv4
  - 네트워크 매핑 
    - VPC : MY-VPC
    - 매핑 : ap-northeast-2a / ap-northeast-2c
  - 보안 그룹 
    - 우회할 수 있는 경로를 차단 방법 존재
    - 우회할 수 있는 경로가 있으므로 alb는 보안그룹이 존재
  - 모바일과 PC 접속 트래픽 분산시키기
    - 대상 그룹에서 각각의 웹서버 대상 그룹 생성
    - TG-CACTUS / TG-RABBIT
    - ALB - 리스너 - 규칙 편집
    - 규칙 삽입
    - IF - HTTP헤더 User-Agent / 확장하는데 `*Mobile*`
    - 규칙 삽입
    - HTTP 헤더 User-Agent / 확장하는데 `*Chrome*`

### AutoScaling

- 하나의 웹서버로 구성하는 것 => 단일 장애 지점(SPOF; Single Point Of Failure)
- 인스턴스 - 작업 - 이미지 생성
- 이미지 - 스냅샷을 빠르게 생성하기 위한 껍데기(?) 같은 느낌
  - 이름 : MY-AMI
  - 재부팅 안함 활성화
- 시작 템플릿
  - 이름 : MY-TEMP
  - Auto Scaling 지침
  - 이미지 - 내 AMI(MY-AMI)
  - 인스턴스 유형 - t2.micro
  - 키페어 : aws-key
  - 네트워크
    - 서브넷 : 시작 템플릿에 포함하지 않음
    - 보안 그룹 : SG-WEB
- Auto Scaling 그룹(ASG)
  - 그룹 생성
  - 그룹 이름 : MY-ASG
  - 시작 템플릿 : MY-TEMP
  - 네트워크 
    - VPC : MY-VPC
    - 서브넷 : MY-PUBLIC-SUBNET-2A / MY-PUBLIC-SUBNET-2C
  - 새 로드밸런서에 연결
    - Application Load Balancer
    - 로드 밸런서 이름 : MY-ASG-ALB
    - 로드 밸런서 체계 : Internet-facing(인터넷 경계)
    - 리스너 및 라우팅 : 대상 그룹 생성 (TG-ASG-ALB)
    - 그룹 크기(Capacity) 
      - 원하는 용량 : 2 
      - 최소 용량 : 1 (실무에서는 원하는 용량과 같이 맞춰줌)
      - 최대 용량 : 4
    - 크기 조정 정책 : 없음 (CloudWatch에서 세팅)
    - 알림 추가 (SNS; Simple Notification Service) - 이메일, SMS
  - 자동 크기 조정
    - 동적 크기 조정 정책
      - Scale OUT 정책
      - 정책 유형 : 단순 크기 조정
      - 정책 이름 : ScaleOutPolicy
      - CloudWatch 경보 - 생성 - ScaleOutAlert
        - 지표 선택
        - EC2 - Auto Scaling 그룹별 - CPUUtilization
        - 조건 : 정적 / 보다 크거나 같음 / 70
        - 알림 : 경보 상태 / MY-SNS
        - 이름 및 설명 - 경보 이름 : ScaleOutAlert
      - 작업 수행 : 추가 1 용량 단위 
      - Scale IN 정책
      - 정책 유형 : 단순 크기 조정
      - 정책 이름 : ScaleInPolicy
      - CloudWatch 경보 - 생성 - ScaleInAlert
        - 지표 선택
        - EC2 - Auto Scaling 그룹별 - CPUUtilization
        - 조건 : 정적 / 보다 작거나 같음 / 30
        - 알림 : 경보 상태 / MY-SNS
        - 이름 및 설명 - 경보 이름 : ScaleInAlert
      - 작업 수행 : 제거 1 용량 단위 
  - CPU 과부하 주기
    - `$top` : CPU 사용량 보기
    - yes > /dev/null &  
    - & 기호는 백그라운드 실행

### 보안 그룹 VS 네트워크 ACL

- 보안 그룹(허용) - 특정 IP만 차단 불가능
  - 인스턴스 레벨
  - 허용 규칙만 지원
  - 상태 저장 : 규칙에 관계 없이 반환 트래픽이 자동 허용
  - 트래픽 허용 여부를 결정하기 전에 모든 규칙을 평가
  - 인스턴스 시작 시 보안그룹 지정, 보안그룹을 인스턴스와 연결하는 경우에만 적용
- 네트워크 ACL(차단)
  - 서브넷 레벨
  - 허용 및 거부 규칙 지원
  - 상태 비저장 : 반환 트래픽이 규칙에 의해 명시적 허용
  - 트래픽 허용 여부를 결정할 때 번호가 낮은 규칙부터 처리
  - 연결된 서브넷의 모든 인스턴스에 자동 적용

### NAT Gateway

- NAT 게이트웨이 생성
  - 이름 : MY-NGW
  - 서브넷 : MY-PUBLIC-SUBNET-2D
  - 탄력적 IP 할당
- 라우팅 테이블 - MY-PRIVATE-SUBNET - 라우팅 편집
  - 0.0.0.0 => NAT 게이트웨이

### EFS

- 파일 시스템 생성
  - 이름 : MY-EFS
  - VPC : MY-VPC
  - 리전 : 리전(여러 AZ)
- VPC 보안그룹 생성 
  - 이름 : SG-EFS
  - 인바운드 규칙 : NFS / SG-ALB
                    NFS / SG-WEB
- EFS 보안 그룹 변경
  - MY-EFS - 네트워크에서 보안그룹을 SG-EFS로 변경 

### IAM

- 사용자 만들기
  - 이름 : s3-user
  - 액세스 유형 선택 : 액세스 키
  - 기존 정책 직접 연결 : AmazonS3FullAccess

### AWS CLI
- aws cli 설치
- CLI 실행 - cmd
  - aws --version
  - aws configure
    - 아까 받은 csv파일에서 Access Key, Secret Access Key 입력
    - 리전명 : ap-northeast2
    - output format : json
- S3에 파일 업로드
  - 버킷 리스트 보기
    - aws s3 ls
  - 폴더를 만들면서 이미지 업로드
    - aws s3 cp two-rabbit.jpg s3://seoul.seojun.shop/images/
  - 버킷에서 파일 리스트 보기
    - aws s3 ls s3://seoul.seojun.shop
  - 폴더 통째로 업로드하기
    - aws s3 sync backup s3://seoul.seojun.shop/backup/
  - 파일 지우기
    - aws s3 rm s3://seoul.seojun.shop/backup/alibaba.tar
  - 폴더 지우기
    - aws s3 rm s3://seoul.seojun.shop/backup/ --recursive 
  - 배치파일로 파일 백업 하기
    - backup.bat 파일 만들어서 명령어 넣기
    - aws s3 sync c:\users\r2com\backup s3://seoul.seojun.shop/backup
    - 작업 스케쥴러
      - 작업 만들기
      - s3 backup
      - 가장 높은 수준의 권한으로 실행
      - 트리거 만들기

### S3(Simple Storage Service)

- 버킷 만들기
  - 버킷 이름 : seoul.seojun.shop
  - 리전 : ap-northeast-2
  - 객체 소유권 : ACL 활성화됨
  - 버킷의 퍼블릭 액세스 차단 설정 : 3,4 번만 체크
  - 버킷 버전 관리 : 활성화
  - 기본 암호화 : 활성화 (Amazon S3 관리형 키)
- 정적 웹 사이트 호스팅
  - 활성화
  - 정적 웹 사이트 호스팅
- 퍼블릭 액세스 권한 주기 
  - 객체에서 파일 선택후 작업 - ACL을 사용하여 퍼블릭으로 설정

### ACM (AWS Certificate Manager)

- SSL 인증서 받기
- HTTPS를 사용하면 누군가 가져가지 못하게함
- 개인정보를 다루는 사이트는 HTTPS를 이용해야함
- 퍼블릭 인증서 요청
  - 도메인 이름 : *.seojun.shop
  - Route53에서 레코드 생성 검증 받기
- ALB 만들기
  - 앞서 만든 로드밸런서와 같이 만듬
  - 리스너 HTTPS 443
  - HTTPS로 바꾸고 대상그룹 만들기
    - 대상 그룹 이름 : TG-ALB
    - 프로토콜 : HTTP 80
    - VPC : MY-VPC
  - 보안 리스너 
    - ACM에서 만든 인증서 선택 
- 보안 그룹 HTTPS 포트 열기
- Route53에서 레코드 생성하기
  - ACM 인증서를 도메인으로 받았기 때문에 DNS주소로는 접속 위험
  - A 레코드
  - 별칭 - Application 로드밸런서
  - 리전 : 아시아 태평양(서울)

### CloudFront

- 원본 도메인 : paulo
- S3 버킷 액세스 : OAI 사용 안함 
- 경로 패턴 : 기본값(*)
- 뷰어 프로토콜 : HTTP and HTTPS
- 설정
  - 가격 분류 : 모든 엣지 로케이션에서 사용(최고의 성능)
  - WAF(Web Application Firewall) : 웹 방화벽 - 이상 징후 감지, 로그, 탐지, 차단
  - 대체 도메인 : cf.seojun.shop
  - SSL 인증서 추가
  - 기본값 루트 객체 - index.html