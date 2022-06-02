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
  - 가상 머신 이름 : WEB01
  - 지역 : KOREA CENTRAL
  - 가용성 옵션 : 가용성 영역 : 영역 1
  - 보안 유형 : 표준
  - 이미지 :  CentOS-based 7.9 - Gen2
  - 크기 : Standard_B1s
  - 인바운드 포트 : HTTP, SSH
- 디스크 
  - 프리미엄 SSD : 프로덕션(최종 운영 환경) 및 성능에 중요한 워크로드 
- 네트워크
  - 가상 네트워크 : RG-TEST-vnet 
  - 서브넷 : default
  - 공용 IP : WEB01-ip
- 사용자 지정 데이터
```bash
#!/bin/bash
yum install -y httpd
systemctl enable --now httpd
echo "<h1>WEB01</h1>" > /var/www/html/index.html
``` 