# AWS

## 리전(Region)

- ap-northeast-2 서울 리전
- ap-northeast-2a 가용 영역(Availability Zone: AZ) 추상적 개념
  - 2개 이상의 데이터 센터 존재(100KM 이내) 2a,2b,2c,2d
  - 가용 영역 별로 Subnet 존재
- 기본 VPC 172.31.0.0/16
- 2a subnet - 172.31.0.0/20
- 2b subnet - 172.31.16.0/20
- 2c subnet - 172.31.32.0/20
- 2d subnet - 172.31.48.0/20 

## IAM(Identity and Access Management)

- 사용자 그룹 
  - 사용자들이 많을 시 사용자들 마다 권한 부여가 어려움, 그룹에 권한 부여
  - Admin Group 생성
  - 권한 정책 연결 - administrator 검색
  - AdministratorAccess(Root 권한에 준하는 권한) - Root 계정 권한 X, 결제 대시보드 X
- 사용자
  - 사용자 추가
  - AWS 액세스 유형 선택
    - 액세스 키 - Token , CLI에서 접근
    - 암호 - GUI에서 접근할 때 입력할 PW
  - 자동 생성된 비밀번호, 비밀번호 재설정 필요 
  - 그룹에 사용자 추가
  - `.csv` 파일 매우 중요! ID/PW 중요 정보 파일, Public 공간에 절대로 업로드 X
- 보안 설정
  - 멀티 팩터 인증
  - 가상 MFA 디바이스 

### EC2(AWS Elastic Compute Cloud)

- 클라우드에서 확장 가능 컴퓨팅 용량을 제공
- VM = Instance
- CPU 와 RAM 설정
- VM에서 Public ip 확인하기
```bash
curl http://169.254.169.254/latest/meta-data/public-ipv4
# meta data 확인하기
curl http://169.254.169.254/latest/meta-data/security-groups
```
- 인스턴스 밑에 스팟요청 - Saving plans - 예약 인스턴스 - 용량 예약 까지 결제 될 수 있음
- 인스턴스 시작
  - AMI 선택 : Amazon Linux 2 Kernel 5.1(AL2) -> Centos7, Redhat7, Fedora 와 닮음
  - 인스턴스 유형(Flavor) : t2.micro
  - 인스턴스 세부 정보 구성
    - 네트워크 : vpc default 
    - 서브넷 : ap-northeast-2a 4091개 IP 주소 사용 가능 (프리티어는 2a와 2c에서만 생성)
    - 퍼블릭 IP 자동 할당 : Floating IP(유동 IP) 
    - 용량 예약 : 예약을 통해서 항상 켜두지 않는 서버의 용량을 확보
    - 도메인 조인 디렉터리 : AD(Active Directory) 와 같은 인증서버를 통해서 접근제어
    - IAM 역할 : 서비스 권한, 보안 역할 세팅 중요! 
    - 종료 방식(Power off) : 중지(stop), 종료(terminate/delete)
    - 최대 절전 중지 동작 : 부팅속도 빨라짐, 윈도우 절전 모드
    - 종료/중지 방지 기능 활성화 : 쉽게 종료/중지 안되도록 설정
    - 모니터링 : NMS(Network Managment Service)등 모니터링 도구 5분마다 1회 (Cloud Watch)
    - 테넌시 : 데이터센터 내의 하드웨어 독점할지 공유 할지 설정
    - 크레딧 사양 : 갑자기 접속자가 많아져서 CPU 성능 up 자동으로 Scale up 시켜줌
    - 파일 시스템 : EFS, 즉 NFS와 같은 디렉토리를 mount 설정
    - 네트워크 인터페이스(NI) : 랜카드 설정, 대부분 보안 장비 세팅 할때 사용
    - 고급 세부 정보 - 사용자 데이터 : #!/bin/bash 와 같은 사용자 데이터 추가 가능
  - 스토리지 추가
    - EBS 세팅 (프리티어는 30GB까지 사용 가능)
    - 볼륨 확장을 통해 스토리지 확장 가능 
    - 스냅샷 : AMI에 선택한 이미지를 의미, `이미지와 스냅샷과의 관계`
    - 볼륨 유형 
      - 범용 SSD(gp2)/General Purpose SSD(gp3) : IOPS(Input Output Per Second) 성능 차이
      - 프로비저닝된 IOPS(io1)/ Provisioned IOPS(io2) : 성능 차이/ io2가 SSD에서 제일 빠름
      - 마그네틱 : 옛날 방식의 HDD
      - 볼륨 추가 후 mobaxterm 에서 포매팅
  - 태그 추가 : 인스턴스의 태그는 꼭 달기
    - 키 : Name / 값 : WEB01
  -  보안 그룹 구성
     -  이름 : SG-WEB
     -  소스 : 출발지 포트/ 보안적으로 중요 , 0.0.0.0/0(ipv4 anywhere), ::/0(ipv6 anywhere)
     -  유형 : SSH, HTTP, ALL ICMP(ipv4)
  - 키페어 생성 
  - Amazon Linux 2 사용자 데이터 ec2-user
```bash
#!/bin/bash
yum install -y httpd
systemctl enable --now httpd
echo "<h1>WEB01</h1>" > /var/www/html/index.html
```
  - ubuntu18 사용자 데이터 ubuntu
```bash
#!/bin/bash
apt update 
apt install -y apache2
```

### EC2 시작 템플릿

### ELB(Elastic Load Balancing)

- 가용성을 높임, High Availability(HA) 고 가용성
- 무중단 서비스
- Application Load Balancer(ALB)
  - L7 Switch 유사
  - Port, Contents 부하 분산 시스템
- Network Load Balancer(NLB) 
  - L4 Switch 유사
  - Port로만 부하 분산 시스템
- 기본구성
  - 로드밸런서 이름
  - 체계 : 접속하는 방식
    - 인터넷 경계
  - IP 주소 유형
    - IPv4  
- 네트워크 매핑
  - VPC : 기본 VPC 172.31.0.0/16
  - 매핑 : ap-northeast-2a, ap-northeast-2c
- 리스너 및 라우팅
  - Frontend
    - TCP
    - 80
  - Backend
    - Target Group (다음으로 전달(Foward))   
    - 대상 그룹(Target Group) - 인스턴스 - 대상 그룹 이름(TG-NLB)
    - 상태 검사(Health Check) - Fail 일어날 시 회로 차단(Circuit breaker)
- NLB 로드 밸런서 알고리즘이 Round Robin이 아님 
- HTTP 상태 코드 
- ALB 로드 밸러서 알고리즘은 Round Robin
- 보안그룹은 특정 IP/특정 보안그룹등 허용 가능
- 경로기반라우팅 abc.com/food -> web01, abc.com/sale -> web02
  - 대상그룹 각각 만들어주기
  - 로드밸런서 ALB 리스너 규칙 보기/편집
  - 규칙 추가 - `규칙 우선순위 고려!`(L7 스위치 우선순위 까다로움)
    - if 경로 - 확장 - /food* 
    - then 전달 대상 - 대상 그룹에서 TG-FOOD 선택
- 서울 리전 웹서버와 도쿄 리전 웹서버 ELB 불가 -> Route 53으로 해결 가능
- 서울 리전 에서의 2개의 가용영역 2a, 2c를 ELB를 통해 부하 분산 하는 것
- `Multi AZ` 가능
- `Cross Region` 불가능 
- Route53은 글로벌 세팅

### AMI(Amazon Machine Image)

- 스냅샷을 이미지로 만들기
  - Root 스냅샷 생성
  - 스냅샷을 이미지 만들기에서 도쿄로 지정
  - 리전을 도쿄로 이동 후에 이미지 생성 된거 확인
  - EC2에서 생성된 이미지로 인스턴스 만들기
  - AMI 등록 취소 
  - AMI 등록 취소를 해야만 스냅샷 삭제 가능
  - 복사라는 기능은 전송 기능 포괄
- 인스턴스를 이미지로 만들기
  - ROOT 볼륨으로 스냅샷과 이미지를 동시에 만드는 것
  - EC2 작업에서 이미지 및 템플릿 - 이미지 생성
  - 재부팅 안함 - 활성화

### EBS(Elastic Block Store)

- 블록 스토리지
  - 볼륨 포매팅 및 마운트, 파티션 확장
  - 스냅샷과 함께 사용
    - 스냅샷을 볼륨으로 생성
    - 스냅샷을 이미지로 생성
```bash
# 볼륨 포매팅 후 마운트
sudo mkfs -t ext4 /dev/xvdb
sudo mount /dev/xvdb /mnt
#파티션 확장
sudo growpart /dev/xvda 1
lsblk
#XFS 파일 시스템 확장
df -Th
sudo xfs_growfs -d /
df -Th
```

### EFS(Elastic File System)

- 파일 스토리지
- 파일 시스템 생성
  - 일종의 인스턴스이므로 VPC가 필요
  - 가용성 및 내구성 (리전 : 똑같은 내용을 여러 AZ에 저장 비용 ↑, One Zone : 단일 AZ에 저장 비용 ↓)
- 네트워크에 들어가서 다중 AZ에서 사용가능 되었는지 확인
- 연결에서 도메인 접근 방법
  - EFS 탑재 헬퍼 사용 : EFS라는 도구를 설치
    - 보안 그룹 새로 생성 SG-EFS NFS 인바운드 규칙 오픈
    - 보안그룹 재설정
```bash
sudo yum install -y amazon-efs-utils
sudo mkdir efs
sudo mount -t efs -o tls fs-cdfwer38:/ efs
```
  - NFS 클라이언트 사용 : 전통적인 방법의 NFS 프로토콜 사용
- IP를 통한 탑재
  - 하이브리드 서버 구축 할 때 사용 

### S3(Simple Storage Service)

- 객체 스토리지
- Google Drive, Opnestack Swift와 닮은 Storage
- URL 생성 가능
- VPC안에 없음, 글로벌에 있음 
- 인터넷 연결을 통해서 접속 가능
- ACL(Access Control List) : 접근 제어 목록 - 차단 및 허용에 권한 정책
  - 비활성됨 : S3를 만든 사람, 소유자만 접근 가능, 가장 강력한 보안
  - 활성화됨 : Public Access를 허용하는 것
- 모든 퍼브릭 액세스 차단 해제 - 보통 3,4번만 체크
- 버전관리 활성화 => 복원(Rollback)
- 기본 암호화 서버측 암호화 SSE(Server Side Encryption) / SSE-KMS
- 객체 잠금 - 비활성화
- 파일 업로드
- 업로드 후에 작업에서 ACL을 사용하여 퍼블릭으로 설정 => 누구나 접속 가능
- 객체 스토리지의 특징 => Google Drive 공유 링크는 wget 명령어 다운로드 불가능하지만 S3 링크로는 wget 다운 가능, 링크 끝에가 파일명

### S3 Glacier

- 객체 스토리지
- 클라우드의 아카이브 스토리지
- HOT 는 빠름, COLD는 느림
- 저렴하면서 대용량의 서비스를 제공, 한 번 업로드된것을 SEARCH하고 DOWNLOAD하는데 오래 걸림
- 빠르게 자주 빈번하게 접근할 데이터는 GLACIER 저장 X

### VPC(Virtual Private Cloud)

- VPC, SUBNET, ROUTING TABLE, INTERNET GATEWAY
- VPC 생성
  - VPC만 - MY-VPC - IPV4 CIDR 10.26.0.0/16
  - 자동으로 생성 : DHCP, 라우팅 테이블, 네트워크 ACL
- SUBNET 생성
  - MY-VPC 선택
  - 서브넷 이름 :  MY-PUBLIC-SUBNET-2A
  - 가용 영역 : ap-northeast-2a
  - IPV4 CIDR : 10.26.0.0/20
  - 같은 방법으로 2b,2c,2d 가용영역으로 생성
- IGW 생성
  - 인터넷 게이트 웨이 생성 MY-IGW
  - VPC와 IGW 연결하여 인터넷과 통신 
- 라우팅 테이블
  - 라우팅 편집 - 라우팅 추가
  - Destination - 0.0.0.0/0 , Target - 인터넷 게이트웨이(MY-IGW) 
  - 서브넷 연결 편집 - 명시적 서브넷 연결