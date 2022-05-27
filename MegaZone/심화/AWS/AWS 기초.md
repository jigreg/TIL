# AWS

## 리전(Region)

- ap-northeast-2 서울 리전
- ap-northeast-2a 가용 영역(Availability Zone: AZ) 추상적 개념
  - 2개 이상의 데이터 센터 존재(100KM 이내) 2a,2b,2c,2d
  - 가용 역역 별로 Subnet 존재
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
- 파일 스토리지
- 객체 스토리지

### AMI(Amazon Machine Image)

- Root 스냅샷 생성
- 스냅샷을 이미지 만들기에서 도쿄로 지정
- 리전을 도쿄로 이동 후에 이미지 생성 된거 확인
- EC2에서 생성된 이미지로 인스턴스 만들기
- AMI 등록 취소 
- AMI 등록 취소를 해야만 스냅샷 삭제 가능
- 복사라는 기능은 전송 기능 포괄