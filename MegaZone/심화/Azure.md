# Azure

## Azure 지오그래피

- Regional Pair : 대한민국
- Region 2개 : 중부(추천), 남부(예비)
- Azure subscription - Resource Group - Resource(VM, NET, Storage)

## Azure IAM

- 사용자 하나 만들기
- 구독 - IAM - 추가 - 역할 할당 추가
- 소유자 => Root 계정 / 기여자 => ID/PW 기능을 뺀 Root 계정
- 기여자 - 구성원 선택 - 아까 만든 사용자 선택 

## Azure Compute Service

- 가상 머신 만들기
- 리소스 그룹 
  - RG-TEST
- 인스턴스 정보
  - 가상 머신 이름 : WEB01 , WEB02 , WEB03
  - 지역 : KOREA CENTRAL
  - 가용성 옵션 : 가용성 영역 : 영역 1 , 2 , 3
  - 보안 유형 : 표준
  - 이미지 :  CentOS-based 7.9 - Gen2 / Ubuntu Server 18.04 LTS - Gen2 / smalldisk Windows Server 2012 R2 Datacenter -Gen2
  - 크기 : Standard_B1s
  - 인바운드 포트 : HTTP, SSH / HTTP, RDP
- 디스크 
  - 프리미엄 SSD : 프로덕션(최종 운영 환경) 및 성능에 중요한 워크로드 
- 네트워크
  - 가상 네트워크 : RG-TEST-vnet 10.0.0.0/16
  - 서브넷 : default 10.0.0.0/24
  - 공용 IP : WEB01-ip
- 사용자 `지정` 데이터
```bash
#!/bin/bash
yum install -y httpd
systemctl enable --now httpd
echo "<h1>WEB01</h1>" > /var/www/html/index.html
``` 

## Azure Load Balancing(부하분산)

- 인스턴스 정보
  - MY-SLB(Server Load Balancer)
  - SKU - 표준
  - 형식 - 공개
  - 계층 - 지역
- 프런트 엔드 IP 구성
  - FT-IP - Domain 있으면 Domain으로 설정
  - IPv4
  - 공용 IP 주소 : 새로 만들기 PUBLIC-IP 
  - 가용 영역 : 영역 중복
  - 라우팅 기본 설정 : Microsoft 네트워크
- 백 엔드 풀
  - AWS에서는 Target Group
  - 백 엔드 풀 추가
    - 이름 : BK-POOL
    - 가상 네트워크 : RG-TEST-vnet
    - 가상 머신 : WEB01, WEB02, WEB03 추가
    - Virtual Machine Scale Sets => Auto Scaling 
- 인바운드 규칙
  - 부하 분산 규칙 
    - SLB-RULE
    - IPv4 
    - 프로토콜 TCP => L4 스위치
    - 프런트 엔드 IP 주소 :  FT-IP
    - 백엔드 풀 : BK-POOL
    - 포트 : 80 
    - 백엔드 포트 : 80
    - 상태 프로브 : health-check / HTTP
  - 인바운드 NAT 규칙
    - Bastion 호스트 없이 포트 포워딩방식으로 접속 가능 
    - NAT-RULE,2,3
    - 형식 : Azure 가상 머신
    - 대상 가상머신 : WEB01, WEB02, WEB03
    - 프런트 엔드 IP : FT-IP
    - 프런트 엔드 포트 : 221,222,3389
    - 백엔드 포트 : 22,22,3389

## Azure Storage

- 객체 스토리지 : Azure Blob, 텍스트 및 이진 데이터에 대한 확장성이 뛰어남
  - 스토리지 계정
    - 인스턴스 정보
      - 스토리지 계정 이름 : seojun2022
      - 지역 : Korea Central
      - 성능 : 표준
      - 중복 : GRS(Global Region Storage, 지역 중복 스토리지)
  - 컨테이너 (Blob)
    - 이름 : seojun-blob
    - 공용 액세스 : 프라이빗
    - 액세스 수준 변경 : Blob(Blob에 대한 익명 읽기 전용 액세스)
- 파일 스토리지 : Azure Files, 클라우드 또는 온-프레미스 배포를 위한 관리
  - 파일 공유(Azure Files)
    - 이름 : seojun-share
    - 계층 : 트랜잭션 최적화됨
    - WEB01 에서 Powershell ise 실행
    - 스토리지 연결 스크립트 붙여넣기
- 블록 스토리지 : Azure 디스크, azure vm에 대한 블록 수준 저장소 볼륨

## Azure image

- 가상머신에서 캡쳐
- 이미지 만들기
  - 가상머신 중지하고 만들어짐
- 이미지로 가상머신 만들기
  - 인스턴스를 새로 만들 때 이미지를 참고해서 만듬
  - 키를 분실했거나 아이디, 암호를 분실했을 때 사용할 수 있는 방법
  - 이름 : WEB03
  - 가용성 영역 : Zone 3 (디스크와 다르게 가용성 영역이 자유로움) 

## Azure Virtual Network

- 가상 네트워크 AWS VPC
- 가상 네트워크 만들기
  - 이름 : MY-VPC
  - IPv4 : 10.26.0.0/16
  - 서브넷 : 10.26.0.0/20 , 10.26.16.0/20, 10.26.32.0/20
- DNS 영역
  -  Nameserver 가비아 도메인에 입력
  -  레코드 집합 추가
  -  별칭 레코드 집합 : 예
     -  Azure 리소스에서 웹서버 ip 선택 가능

## Azure Database for MariaDB

- 서버 정보
  - 이름 : seojun2022
  - 데이터 원본 : 없음
  - 위치 : Korea Central
  - 버전 : 10.3
  - 컴퓨팅 + 스토리지 : vCore 1 , RAM 2 , Storage 5GB
- 접속 방법
```
mysql.exe -h mydemoserver.mariadb.database.azure.com -u Username@mydemoserver -p --ssl-ca=c:\ssl\BaltimoreCyberTrustRoot.crt.pem
``` 