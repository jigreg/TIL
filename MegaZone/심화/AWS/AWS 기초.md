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
    - 범용 SSD(gp2)/General Purpose SSD(gp3) : IOPS 성능 차이
    - 프로비저닝된 IOPS(io1)/ Provisioned IOPS(io2) : 성능 차이/ io2가 SSD에서 제일 빠름
    - 마그네틱 : 옛날 방식의 HDD