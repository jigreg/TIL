# Open STack
## 5 core service
1) Compute Service(CPU,RAM) : Nova, AWS(EC2) - Elastic Compute Cloud
2) Storage Service(SSD, HDD) : Cinder, AWS(EBS) - Elastic Block Storage
                               Swift, AWS(S3) - Simple Storage Service
3) Network Service (G/W, S/W) : Neutron, AWS(VPC) - Virtual Private Cloud
4) Image Service(OS) : Glance, AWS(AMI) - Amazon Machine Image
5) Identitiy Service(AUTH, Keypair) - KeyStone, AWS(IAM) - Identity Access Management
6) Orchestration Service(IaC) - Heat, AWS(CloudFormation)

## Open Stack Setting
- IP : 192.168.0.53/20
- G/W : 192.168.0.1
- Network : extnet
- 보안그룹 : 내보냄 = outbound = egress(오픈스택에서 밖으로 내보냄)
            들어옴 = inbound = ingress(밖에서 오픈스택으로 들어옴)
            http,ssh,icmp 들어옴 추가
- 인스턴스 : 시작 = launch = create , start (poweroff -> start)
- 인스턴스 생성 - 사용자 정의 스크립트 root 권한으로 실행되므로 sudo를 붙일 필요가 없음
```
    #!/bin/bash
    apt udpate
    apt install -y nginx
```
- 볼륨 세팅 : 추가 확장 스토리지 
             attach > mount > umount > detach
             # sudo umount /mnt
             늘어난 볼륨을 줄이지 못함 / 리눅스 절대 규칙
             Scale up : 자원을 수직적 확장 <-> Scle down : 자원을 수직적 축소
             Scale out -> 자원을 수평적 확장