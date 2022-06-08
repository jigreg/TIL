# GCP

## GCP IAM
- 프로젝트 구성원 추가
  - 기본 - 편집자 : 대부분의 Google Cloud 리소스를 확인, 생성, 업데이트, 삭제
                    Root 계정 삭제만 못하고 Root 계정에 준하는 권한
  - 추가된 구성원으로 접속 : 콘솔로 이동

## GCP Compute Service

- Compute Engine 인스턴스(GCE)에서는 Google에서 제공하는 Linux 및 Winodws Server 용 공개 이미지, 사용자가 만든 커스텀 이미지를 실행
- Container-Optimized OS (CoreOS)로 Docker 컨테이너를 배포, Kubernetes 특화
- Provisioning - CPU, RAM, SSD, OS, NET 
- 머신 유형
  - E2 범용
  - N2, N2D, N1 범용
  - M1, M2 메모리 최적화
  - C2 컴퓨팅 최적화
  - A2 가속기 최적화
- Compute Engine API - 사용
  - 인스턴스 만들기
    - 이름 : web01
    - 리전 : asia-northeast3(서울)
    - 영역 : asia-northeast3-a
    - 머신 구성 : E2
    - 머신 유형 : e2-micro(vCPU 2개, 1GB 메모리)
    - 컨피덴셜 VM 서비스 : 보안 강화 기능 => 사용설정 X
    - 컨테이너 : Docker 환경 만들기
    - 부팅 디스크 : CentOS 7 /Debian(Ubuntu와 비슷함)
    - 액세스 범위 : 모든 Cloud API에 대한 전체 액세스 허용  - 접근 자유로움
    - 방화벽 : HTTP 트래픽 허용 / SSH는 기본적으로 허용
    - 네트워크 : Default
    - 보안 : 액세스 관리 - 수동으로 생성된 SSH 키 추가
        - id_rsa.pub 키 메모장으로 열어서 SSH 복사 
        - user name : SSH 뒷부분에 r2com - Mobaxterm에서 접속할 때 사용하니 기억 
    - 관리 : 자동화(사용자 데이터)
    - 방화벽 변천사(OS 수준의 방화벽) : netfilter -> iptables -L(All Accept) -> firewalld(All Block)
```bash
 #!/bin/bash
yum install -y httpd
systemctl enable --now httpd
echo "<h1>WEB01</h1>" > /var/www/html/index.html
```
- 메타데이터
  - SSH키 추가 : 키가 없는 모든 VM 인스턴스에 전파
  - id_rsa.pub 키 복사하여 추가하기
  - 키를 따로 지정해주지 않아도 모든 VM 접속 가능

## GCP LoadBalancing

- 단순 로드밸런싱 -> 같은 영역에 만듬
- stateless, stateful 은 Autoscaling 을 통하여 멀티 영역 로드밸런싱 가능
- 단순 로드 밸런싱은 단일 영역으로 세팅 unmanaged instance group
- 인스턴스 그룹 (target group) New unmanaged instance group
  - 이름 : instance-group-1
  - 위치 : asia-northeast3 / asia-northeast3-a
  - 네트워크 : default
  - VM 인스턴스 : web01, web02
- 네트워크 서비스 
  - 부하 분산
    - HTTP(S) 부하 분산 - Application Load Balancer Layer 7 부하 분산
    - TCP 부하 분산 - Network Load Balancer Layer 4 부하 분산
  - 이름 : my-slb
  - 백엔드 구성 - 백엔드 서비스 만들기
    - 이름 : bk-svc
    - 백엔드 유형 : 인스턴스 그룹
    - 상태 확인 : health check
      - 이름 : my-health
      - 프로토콜 : http
      - 상태 기준 : 4가지이면 자세히 설정 가능 (AWS 4개, Azure 3개) 
  - 프런트엔드 구성
    - 이름 : frontend 

## GCP Storage Service

- 객체 스토리지(Cloud Storage) : 기업용 객체 스토리지, 모든 유형의 데이터를 저장하고 원할 때마다 데이터 검색 가능 서비스 = AWS S3, Azure blob
  - Cloud Storage
  - 버킷 만들기
    - 이름 : seojun2022
    - 위치 : Region asia-northeast3(서울)
    - 스토리지 클래스 : Standard
    - 액세스 제어 : 균일한 액세스 제어
    - 객체 보호 도구 : 없음
  - 버킷 권한 주기
    - 권한 추가
      - 새 주 구성원 : allUsers
      - 역할 : 저장소 기존 개체 리더 
- 블록 스토리지(Persistent Disk) : Compute Engine 및 GKE와 같은 Google Cloud 제품과 완전히 통합된 서비스 = AWS EBS, Azure Disk
  - Compute Engine - 스토리지
  - 디스크 만들기
    - 이름 : web01-add
    - 위치 : 단일 영역 asia-northeast3-a
  - 디스크 마운트
    - vm 인스턴스에서 web01 수정
    - 추가 디스크 - 기존 디스크 연결
    - web01add
  - 디스크 포맷 & 마운트
    - `sudo mkfs -t ext4 /dev/sdb`
    - `sudo mount /dev/sdb /mnt`
- 파일 스토리지(Filestore) : 파일 마이그레이션과 스토리지를 지원하는 완전 관리형 서비스 = AWS EBS, Azure files, NFS(Network File Storage), SAMBA