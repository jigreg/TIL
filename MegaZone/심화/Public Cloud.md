# 클라우드 컴퓨팅

## 개념

- 인터넷 기반 컴퓨팅의 일종
- 정보를 자신의 컴퓨터가 아닌 인터넷에 연결된 다른 컴퓨터로 처리하는 기술
- 컴퓨팅 자원
  - NETWORK
  - CPU, RAM
  - SSD, HDD
  - APP

## 종류

### Hybrid Cloud
- Public 과 Private을 연동시킨 Hybrid Cloud
- Public 과 Public 을 연동 Multi Cloud
- 단일 클라우드 호스팅 공급업체(CSP)에 대한 의존도를 줄임
- Public Cloud
  - 대규모/ 불특정 사용자
  - AWS - Azure - GCP - Alibaba
- Private Cloud
  - 중소 규모/ 특정 사용자
  - 보안/ 격리
  - ESXi
  - OpenStack
- Traditional Infrastructure
  - On-Premise

### Public Cloud

- 용이한 IT 인프라 자원 관리
- 빠른 인프라 구축 속도
- 신속한 글로벌 서비스 전개 (Public IP)
- `트래픽에 대한 자동 조정 (Auto Scaling)`
- 다양한 서비스로의 확장성 제공
- 서비스로서의 퍼블릭 클라우드 유형
  - Iaas(Infrastructure as a Service) - AWS EC2, Openstack
  - Paas(Platform as a Service) - AWS Beanstalk
  - Saas(Software as a Service) - MS Office 365, Google Docs, SAP, ERP

## 가상화

- 하이퍼바이저 타입 1 (베어메탈)
- 하이퍼바이저 타입 2 (호스트, 실습)
- OS 수준 컨테이너형 가상화 (도커)

### Scale Up vs Scale Out

- 자동 조정
  - 자원
  - CPU, RAM, SSD
- Scale up <-> Scale down
  - CPU 나 RAM을 업그레이드 해주는 것
  - CPU 2C -> 4C, RAM 4GB -> 8GB
  - 수직적 확장
- Scale out <-> Scale in
  - 개수를 늘리는 것
  - CPU 1C, RAM 1G 1대 -> 5대
  - 대부분 Scale out이 유익
  - 수평적 확장
  - Public Cloud에서는 Scale out으로 Auto Scaling  