# Alibaba Cloud

## Alibaba ECS(Elastic Compute Service)

- 인스턴스 만들기
  - 지역 : 중국(홍콩)
  - 사용 가능한 영역 : 홍콩 영역 B
  - 인스턴스 : 1CPU 1GiB
  - OS : Alibaba Cloud Linux 3
  - Disk : SSD 40GB
  - 네트워크 유형 : VPC
- Connect - 보안적인 방법
  - Send Remote Commands
  - `yum install -y httpd`
  - `systemctl enable --now httpd`
- SSH Key Pairs
  - SSH 접근 키페어 만들기 
  - 이름 : alibaba-key
  - Auto-create
  - 인스턴스에 bind 하기

## Alibaba Object Storage Service

- Alibaba Cloud에서 제공하는 안전하고 비용 효율적이며 내구성이 뛰어난 클라우드 스토리지
- OSS는 99.99999999 데이터 내구성 및 99.995% 서비스 가용성을 위해 설계
- 버킷 만들기
  - 버킷 이름 : seojun2022
  - 리전 : South Korea(Seoul)
  - Storage Class : Standard
  - Access Control List : Public Read
  - Encryption Method : None
- 파일 업로드

## Alibaba File Storage NAS

- File Storage NAS
- 리소스 요금제 유형 : 익스트림 NAS 리소스 요금제
- 지역 - 중국(홍콩)
- 용량 : 100GiB
- File System
  - General NAS
  - 리전 : 중국(홍콩)
  - 영역 : Hongkong Zone B
  - 스토리지 유형 : NAS 성능
  - 프로토콜 유형 : NFS
- 마운트
  - Mount on ECS
  - ECS Instances : ECS 선택
  - Mount Path : /mnt
- WEB UI 에서 마운트 가능 (다른 클라우드 X) 

## Alibaba DNS

- 일반 트래픽 해상도 활성화
- 도메인 등록
- 가비아에서 네임서버 등록

## Alibaba Image Service

- ECS 인스턴스 생성 후 소프트웨어 설치 및 애플리케이션 환경 배포
- 이미지를 통해서 VM 생성

## Alibaba Database

- ApsaraDB RDS는 Alibaba Cloud의 Apsara 분산 파일 시스템 및 고성능 SSD를 기반으로 구축된 안정적이고 확장 가능한 온라인 데이터베이스 서비스
- MySQL, SQL Server, PostgreSQL 및 MariaDB TX 데이터베이스 엔진
- 재해 복구, 백업, 복원, 모니터링 및 마이그레이션 지원
- MySQL
  - 리전 : Hongkong
  - Database Type : MySQL
  - Engine Version : 5.7
  - Node Type : Basic
  - Storage Type : Enhanced SSD
  - Zone : Hong Kong Zone B
- Database
  - DB Name : wordpress 
- Account
  - Create Account
- Database Connection
  - Change Endpoint
  - Internal Network으로 바꾸기
  - DB 주소 확인하기
- DB 연결 하기
  - Data Security - Create Whitelist
  - IP Address 에 인스턴스 내부 ip 추가해주기  
