# IaC(Infrastructure as Code) - 구성 및 설정 자동화

## IaC
- 코드를 작성 및 실행하여 인프라를 생성, 배포, 수정, 정리하는 것
- 서버, DB, Network, logfile, 애플리케이션 구성, 문서, 자동화된 테스트, 배포 프로세스 등 거의 모든 것을 코드로 관리
1. 애드혹 스크립트
   - 수행할 작업을 단계별로 나누고 bash와 같은 언어를 사용하여 코드 정의 및 스크립트 작성
   - 사용자 데이터
2. 구성 관리 도구(Configuration) 
   - ansible
   - 코딩 규칙
   - 멱등성 - 같은 일 반복 X
   - 분산형 구조
3. 서버 템플릿 도구
   - Docker, 베이그런트와 같은 서버 템플릿 도구
   - 스냅샷을 이미지를 생성하여 모든 서버에 이미지를 설치
4. 오케스트레이션 도구 = 쿠버네티스 = 클러스터
   - 관리부분 (쿠버네티스, 도커 스웜)
   - VM과 컨테이너 배포, 효율적 업데이트 및 `롤백`, 자동 복구(치유), 자동 확장(조정), 로드 밸런싱, 서로 식별하고 통신할 수 있게 서비스 검색 기능 제공
5. 프로비전 도구
   - Terraform
   - 테라폼, 클라우드포메이션, 오픈스택 히트와 같은 프로비전 도구는 서버 자체를 생성
   - 인프라에 관한 거의 모든 부분을 프로비저닝
- 장점
  - 자급식 배포
  - 속도와 안정성
  - 문서화
  - 버전관리
  - 유효성 검증
  - 재사용성

## AWS CLI & CloudFormation

### CentOS7 
- VM Spec
  - 메모리 4GB
  - VDI(VirtualBox 디스크 이미지)
  - 동적 할당 - 씬 프로비저닝 (실무에선 고정 크기 - 씩 프로비저닝)
  - 디스크 128GB
  - CPU 2Core
  - 저장소 - 광학 드라이브 - IDE 세컨더리 마스터 - CentOS7 Minimal.iso
  - 네트워크 - 어댑터에 브릿지
- CentOS7 설정
```
# yum install -y bash-completion wget unzip rdate
# rdate -s time.bora.net
# setenforce 0
# sed -i s/^SELINUX=.*$/SELINUX=disabled/ /etc/selinux/config
# cd /tmp
# systemctl disable --now firewalld
# yum update -y
# reboot
```

### AWS CLI 

- AWS CLI 설치
```
# curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
# unzip awscliv2.zip
# ./aws/install
# vi .bash_profile
$ complete -C '/usr/local/bin/aws_completer' aws
# aws --version
# aws s3 ls # aws login 여부 파악
# aws configure
# Access Key, Region : ap-northeast-2, filetype : json
```
- AWS VPC & Subnet 만들기
```
# aws ec2 create-vpc --cidr-block 192.168.0.0/16 --tag-specification "ResourceType=vpc,Tags=[{Key=Name,Value=NEW-VPC}]" --output text
# NEW_VPC=vpc-0b86b4b6ab0bce886
# echo $NEW_VPC
# aws ec2 create-subnet --vpc-id $NEW_VPC --cidr-block 192.168.0.0/20 --availability-zone ap-northeast-2a --tag-specification "ResourceType=subnet,Tags=[{Key=Name,Value=NEW-PUBLIC-SUBNET-2A}]"
# aws ec2 create-subnet --vpc-id $NEW_VPC --cidr-block 192.168.16.0/20 --availability-zone ap-northeast-2b --tag-specification "ResourceType=subnet,Tags=[{Key=Name,Value=NEW-PUBLIC-SUBNET-2B}]"
# aws ec2 create-subnet --vpc-id $NEW_VPC --cidr-block 192.168.32.0/20 --availability-zone ap-northeast-2c --tag-specification "ResourceType=subnet,Tags=[{Key=Name,Value=NEW-PUBLIC-SUBNET-2C}]"
# aws ec2 create-subnet --vpc-id $NEW_VPC --cidr-block 192.168.48.0/20 --availability-zone ap-northeast-2d --tag-specification "ResourceType=subnet,Tags=[{Key=Name,Value=NEW-PUBLIC-SUBNET-2D}]"
# aws ec2 describe-subnets --filters "Name=vpc-id,Values=$NEW_VPC" --query 'Subnets[*].{AZ:AvailabilityZone,CIDR:CidrBlock}'
```
- 서브넷을 퍼블릭 서브넷으로 만들기
```
# aws ec2 create-internet-gateway --tag-specification "ResourceType=internet-gateway,Tags=[{Key=Name,Value=NEW-IGW}]" --output text
# NEW_IGW=igw-07bcf6f436dc7df46
# aws ec2 attach-internet-gateway --vpc-id $NEW_VPC --internet-gateway-id $NEW_IGW
# aws ec2 describe-internet-gateways --output table
# aws ec2 describe-route-tables --filter "Name=vpc-id,Values=$NEW_VPC"
# NEW_RTB=rtb-0c92dd389865be7e3
# aws ec2 create-route --route-table-id $NEW_RTB --destination-cidr-block 0.0.0.0/0 --gateway-id $NEW_IGW
# aws ec2 create-tags --resources $NEW_RTB --tags "Key=Name,Value=NEW-PUBLIC-SUBNET-RTB"
# aws ec2 describe-route-tables --route-table-id $NEW_RTB --output table
# aws ec2 describe-subnets --filters "Name=vpc-id,Values=$NEW_VPC" --query 'Subnets[*].{ID:SubnetId,CIDR:CidrBlock}'
# NEW_SID1=subnet-0378a9a32f00d1a52
# NEW_SID2=subnet-04c1079a3501166e1
# NEW_SID3=subnet-0454c51cfbf6b303a
# NEW_SID4=subnet-0e90af0e60dae58b2
# aws ec2 associate-route-table  --subnet-id $NEW_SID1 --route-table-id $NEW_RTB
# aws ec2 associate-route-table  --subnet-id $NEW_SID2 --route-table-id $NEW_RTB
# aws ec2 associate-route-table  --subnet-id $NEW_SID3 --route-table-id $NEW_RTB
# aws ec2 associate-route-table  --subnet-id $NEW_SID4 --route-table-id $NEW_RTB
# aws ec2 modify-subnet-attribute --subnet-id $NEW_SID1 --map-public-ip-on-launch
# aws ec2 modify-subnet-attribute --subnet-id $NEW_SID2 --map-public-ip-on-launch
# aws ec2 modify-subnet-attribute --subnet-id $NEW_SID3 --map-public-ip-on-launch
# aws ec2 modify-subnet-attribute --subnet-id $NEW_SID4 --map-public-ip-on-launch
# aws ec2 modify-vpc-attribute --vpc-id $NEW_VPC --enable-dns-hostnames
```
- 키페어, 보안그룹 만들기
```
# aws ec2 create-key-pair --key-name new-key --query 'KeyMaterial' --output text > new-key.pem
# chmod 400 new-key.pem
# aws ec2 create-security-group --group-name NEW-SG-WEB --description "Security group for HTTP_SSH access" --vpc-id $NEW_VPC
# NEW_SG=sg-0d3a7a4ddd609d7eb
# aws ec2 authorize-security-group-ingress --group-id $NEW_SG --protocol tcp --port 22 --cidr 0.0.0.0/0
# aws ec2 authorize-security-group-ingress --group-id $NEW_SG --protocol tcp --port 80 --cidr 0.0.0.0/0
# aws ec2 authorize-security-group-ingress --group-id $NEW_SG --protocol icmp --port -1 --cidr 0.0.0.0/0
```
- 볼륨 및 인스턴스 만들기
```
# vi mapping.json
[
    {
        "DeviceName": "/dev/xvda",
        "Ebs": {
            "VolumeSize": 8
        }
    },
    {
        "DeviceName": "/dev/xvdb",
        "Ebs": {
            "VolumeSize": 8
        }
    }
]

# vi my_script.txt
#!/bin/bash
yum install -y httpd
systemctl enable --now httpd
echo "<h1>Hello AWS CLI</h1>" > /var/www/html/index.html

# aws ec2 run-instances \
--image-id ami-0fd0765afb77bcca7 \
--count 1 \
--instance-type t2.micro \
--key-name new-key \
--security-group-ids $NEW_SG \
--subnet-id $NEW_SID1 \
--block-device-mappings file://mapping.json \
--user-data file://my_script.txt \
--tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=NEW-WEB}]' 'ResourceType=volume,Tags=[{Key=Name,Value=NEW-ROOT}]'

# NEW_IID=i-0b9703fde068dd76c
# aws ec2 describe-instances --instance-id $NEW_IID | grep PublicIp
# ssh -i "new-key.pem" ec2-user@3.38.165.0
# curl 3.38.165.0
```
- 인스턴스 정리 및 삭제하기
```
# aws ec2 terminate-instances --instance-id $NEW_IID
# aws ec2 delete-security-group --group-id $NEW_SG
# aws ec2 delete-subnet --subnet-id $NEW_SID1
# aws ec2 delete-subnet --subnet-id $NEW_SID2
# aws ec2 delete-subnet --subnet-id $NEW_SID3
# aws ec2 delete-subnet --subnet-id $NEW_SID4
# aws ec2 delete-internet-gateway --internet-gateway-id $NEW_IGW
# aws ec2 delete-vpc --vpc-id $NEW_VPC
```
### AWS CloudFormation(Azure Resource Manager,GCP Deployment Manager)

- 주요 섹션
  - Resources(생성) : AWS 인프라의 실질적인 섹션, EC2 인스턴스, S3 버킷, ELB등과 같은 클라우드 포메이션을 이용해 AWS 웹 콘솔에서 실행하는 것으로 거의 모든 리소스 유형 생성. 리소스에는 기본 반환값 존재, `Ref`를 이용해 이 반환값을 얻어올 수 있고 템플릿의 다른 위치에 사용
  - Parameters(입력) : 명령줄 도구에 입력하는 매개변수와 동일하게 스택을 만들거나 업데이트 할 때 정의하는 입력 값. 템플릿의 변경 없이도 스택을 커스터마이즈
  - Output(출력) : 스택이 완료된 후에 결과물을 출력, ELB의 퍼블릭 도메인이나 EC2의 퍼블릭 IP를 출력
  - Mapping(지정) : 리전의 특화된 템플릿에서 어떠한 요소 참조, 템플릿에 EC2 AMI ID에 대한 매핑 지정, AMI ID가 리전에 특화된 리소스이기 떄문에 유효한 AMI ID를 리전별로 지정

- VPC yaml
```yaml
AWSTemplateFormatVersion: 2010-09-09
Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 192.168.0.0/16
      EnableDnsSupport: true
      EnableDnsHostnames: true
      InstanceTenancy: default
      Tags:
        - Key: Name
          Value: NEW-VPC
  SubnetA:
    Type: AWS::EC2::Subnet
    Properties:
      AvailabilityZone: ap-northeast-2a
      VpcId: !Ref VPC
      CidrBlock: 192.168.0.0/20
      MapPublicIpOnLaunch: true
      Tags:
        - Key: Name
          Value: NEW-PUBLIC-SUBNET-2A
  SubnetB:
    Type: AWS::EC2::Subnet
    Properties:
      AvailabilityZone: ap-northeast-2b
      VpcId: !Ref VPC
      CidrBlock: 192.168.16.0/20
      MapPublicIpOnLaunch: true
      Tags:
        - Key: Name
          Value: NEW-PUBLIC-SUBNET-2B
  SubnetC:
    Type: AWS::EC2::Subnet
    Properties:
      AvailabilityZone: ap-northeast-2c
      VpcId: !Ref VPC
      CidrBlock: 192.168.32.0/20
      MapPublicIpOnLaunch: true
      Tags:
        - Key: Name
          Value: NEW-PUBLIC-SUBNET-2C
  SubnetD:
    Type: AWS::EC2::Subnet
    Properties:
      AvailabilityZone: ap-northeast-2d
      VpcId: !Ref VPC
      CidrBlock: 192.168.48.0/20
      MapPublicIpOnLaunch: true
      Tags:
        - Key: Name
          Value: NEW-PUBLIC-SUBNET-2D
  InternetGateway:
    Type: AWS::EC2::InternetGateway
    Properties:
      Tags:
        - Key: Name
          Value: NEW-IGW
  VPCGatewayAttachment:
    Type: AWS::EC2::VPCGatewayAttachment
    Properties:
      VpcId: !Ref VPC
      InternetGatewayId: !Ref InternetGateway
  RouteTableA:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref VPC
      Tags:
        - Key: Name
          Value: NEW-PUBLIC-RTB
  InternetRoute:
    Type: AWS::EC2::Route
    DependsOn: InternetGateway
    Properties:
      DestinationCidrBlock: 0.0.0.0/0
      GatewayId: !Ref InternetGateway
      RouteTableId: !Ref RouteTableA
  SubnetARouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId: !Ref RouteTableA
      SubnetId: !Ref SubnetA
  SubnetBRouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId: !Ref RouteTableA
      SubnetId: !Ref SubnetB
  SubnetCRouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId: !Ref RouteTableA
      SubnetId: !Ref SubnetC
  SubnetDRouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId: !Ref RouteTableA
      SubnetId: !Ref SubnetD
```
- EC2 yaml
```yaml
AWSTemplateFormatVersion: 2010-09-09
Mappings:
  RegionMap:
    ap-northeast-2:
      AMIID: ami-0fd0765afb77bcca7
    ap-northeast-1:
      AMIID: ami-0b7546e839d7ace12
Parameters:
  InstanceTypeParameter:
    Type: String
    Default: t2.micro
    Description: Enter instance size. Default is t2.micro
  VPC:
    Type: String
    Default: vpc-01a276b266db7833b
    Description: VPC ID.
  Subnet:
    Type: String
    Default: subnet-01132b9dddcf71d3d
    Description: Subnet ID.
  AMI:
    Type: String
    Default: AMIID
    Description: The Linux AMI to use.
  Key:
    Type: String
    Default: new-key
    Description: The key used to access the instance.
Resources:
  InstanceSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupName: "NEW-SG-WEB"
      GroupDescription: "SSH and web traffic in, all traffic out."
      VpcId: !Ref VPC
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: '80'
          ToPort: '80'
          CidrIp: 0.0.0.0/0
        - IpProtocol: tcp
          FromPort: '22'
          ToPort: '22'
          CidrIp: 0.0.0.0/0
        - IpProtocol: icmp
          FromPort: '-1'
          ToPort: '-1'
          CidrIp: 0.0.0.0/0
      SecurityGroupEgress:
        - IpProtocol: -1
          CidrIp: 0.0.0.0/0
  Linux:
    Type: 'AWS::EC2::Instance'
    Properties:
      SubnetId: !Ref Subnet
#      ImageId: !Ref AMI
      ImageId: !FindInMap [ RegionMap, !Ref "AWS::Region", !Ref AMI ]
      InstanceType:
        Ref: InstanceTypeParameter
      KeyName: !Ref Key
      SecurityGroupIds:
        - Ref: InstanceSecurityGroup
      BlockDeviceMappings:
        - DeviceName: /dev/xvda
          Ebs:
            VolumeSize: 8
      Tags:
        - Key: Name
          Value: NEW-EC2

      UserData:
        Fn::Base64: |
          #cloud-boothook
          #!/bin/bash
          yum install -y httpd
          systemctl enable --now httpd
          echo "Hello World!" > /var/www/html/index.html
Outputs:  
  PublicIp:    
    Description: PublicIp Output    
    Value: {"Fn::GetAtt": ["Linux","PublicIp"]}
```
- ALL yaml
```yaml
AWSTemplateFormatVersion: 2010-09-09
Mappings:
  RegionMap:
    ap-northeast-2:
      AMIID: ami-0fd0765afb77bcca7
    ap-northeast-1:
      AMIID: ami-0b7546e839d7ace12
Parameters:
  InstanceTypeParameter:
    Type: String
    Default: t2.micro
    Description: Enter instance size. Default is t2.micro
  AMI:
    Type: String
    Default: AMIID
    Description: The Linux AMI to use.
  Key:
    Type: String
    Default: new-key
    Description: The key used to access the instance.
Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 192.168.0.0/16
      EnableDnsSupport: true
      EnableDnsHostnames: true
      InstanceTenancy: default
      Tags:
        - Key: Name
          Value: NEW-VPC
  SubnetA:
    Type: AWS::EC2::Subnet
    Properties:
      AvailabilityZone: ap-northeast-2a
      VpcId: !Ref VPC
      CidrBlock: 192.168.0.0/20
      MapPublicIpOnLaunch: true
      Tags:
        - Key: Name
          Value: NEW-PUBLIC-SUBNET-2A
  SubnetB:
    Type: AWS::EC2::Subnet
    Properties:
      AvailabilityZone: ap-northeast-2b
      VpcId: !Ref VPC
      CidrBlock: 192.168.16.0/20
      MapPublicIpOnLaunch: true
      Tags:
        - Key: Name
          Value: NEW-PUBLIC-SUBNET-2B
  SubnetC:
    Type: AWS::EC2::Subnet
    Properties:
      AvailabilityZone: ap-northeast-2c
      VpcId: !Ref VPC
      CidrBlock: 192.168.32.0/20
      MapPublicIpOnLaunch: true
      Tags:
        - Key: Name
          Value: NEW-PUBLIC-SUBNET-2C
  SubnetD:
    Type: AWS::EC2::Subnet
    Properties:
      AvailabilityZone: ap-northeast-2d
      VpcId: !Ref VPC
      CidrBlock: 192.168.48.0/20
      MapPublicIpOnLaunch: true
      Tags:
        - Key: Name
          Value: NEW-PUBLIC-SUBNET-2D
  InternetGateway:
    Type: AWS::EC2::InternetGateway
    Properties:
      Tags:
        - Key: Name
          Value: NEW-IGW
  VPCGatewayAttachment:
    Type: AWS::EC2::VPCGatewayAttachment
    Properties:
      VpcId: !Ref VPC
      InternetGatewayId: !Ref InternetGateway
  RouteTableA:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref VPC
      Tags:
        - Key: Name
          Value: NEW-PUBLIC-RTB
  InternetRoute:
    Type: AWS::EC2::Route
    DependsOn: InternetGateway
    Properties:
      DestinationCidrBlock: 0.0.0.0/0
      GatewayId: !Ref InternetGateway
      RouteTableId: !Ref RouteTableA
  SubnetARouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId: !Ref RouteTableA
      SubnetId: !Ref SubnetA
  SubnetBRouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId: !Ref RouteTableA
      SubnetId: !Ref SubnetB
  SubnetCRouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId: !Ref RouteTableA
      SubnetId: !Ref SubnetC
  SubnetDRouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId: !Ref RouteTableA
      SubnetId: !Ref SubnetD
  InstanceSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupName: "NEW-SG-WEB"
      GroupDescription: "SSH and web traffic in, all traffic out."
      VpcId: !Ref VPC
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: '80'
          ToPort: '80'
          CidrIp: 0.0.0.0/0
        - IpProtocol: tcp
          FromPort: '22'
          ToPort: '22'
          CidrIp: 123.142.252.25/32
        - IpProtocol: icmp
          FromPort: '-1'
          ToPort: '-1'
          CidrIp: 0.0.0.0/0
      SecurityGroupEgress:
        - IpProtocol: -1
          CidrIp: 0.0.0.0/0
  Linux:
    Type: 'AWS::EC2::Instance'
    Properties:
      SubnetId: !Ref SubnetA
#      ImageId: !Ref AMI
      ImageId: !FindInMap [ RegionMap, !Ref "AWS::Region", !Ref AMI ]
      InstanceType:
        Ref: InstanceTypeParameter
      KeyName: !Ref Key
      SecurityGroupIds:
        - Ref: InstanceSecurityGroup
      BlockDeviceMappings:
        - DeviceName: /dev/xvda
          Ebs:
            VolumeSize: 8
      Tags:
        - Key: Name
          Value: NEW-EC2

      UserData:
        Fn::Base64: |
          #cloud-boothook
          #!/bin/bash
          yum install -y httpd
          systemctl enable --now httpd
          echo "Hello World!" > /var/www/html/index.html
Outputs:  
  PublicIp:    
    Description: PublicIp Output    
    Value: {"Fn::GetAtt": ["Linux","PublicIp"]}
```