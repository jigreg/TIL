# VMware vSphere ESXi
- 가상 컴퓨터를 배치하고 서비스를 제공할 목적으로 VMware가 개발한 엔터프라이즈 계열 Type1 하이퍼바이저입니다. Type1 하이퍼바이저로서 ESXi는 운영체제에 설치하는 응용 소프트웨어가 아니며, 대신 커널과 같은 중요한 운영체제 구성 요소를 포함,통합하고 있습니다.

# HyperVisor Spec
- CPU : 4
- RAM : 10G(10240MB)
- SSD : 128G
- NET : Bridge
- IMG : VMware_ESXi.iso

# VM Linux Spec
- CPU : 1
- RAM : 1G
- SSD : 100G
- NET :
- IMG : Centos, Ubuntu

# VM Window Spec
- CPU : 1
- RAM : 2G
- SSD : 100G
- NET :
- IMG : Window

# CPU 가상화(HVM)
- CPU에 중첩된 가상화 일 경우 Virtualiztion engine에 체크
- Intel VT-x
- AMD V/RVI

# 접속방법
- Google Chrome
- 192.168.0.254
- root /pw 접속
- 호스트 - 관리 - 스왑 - 데이터 스토어 datastore1
- 호스트 - 관리 - 시간 및 날짜 - NTP서버 등록 후 시작
- 스토리지 - 데이터스토어 브라우저 - 업로드 - iso 파일 업로드
