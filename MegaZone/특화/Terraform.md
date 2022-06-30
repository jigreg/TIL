# Terraform

## 개념
- Terraform은 해시코프사에서 Go언어로 개발한 오픈소스도구입니다. 운영체제마다 바이너리 파일이 존재하는데 Go 코드는 하나의 바이너리 파일로 컴파일되며 Terraform이라는 명령어로 실행할 수 있습니다. 이 Terraform 명령어를 사용하여 노트북, 데스크탑, 빌드 서버 또는 다른 컴퓨터에서든 인프라를 배포할 수 있으며 이를 위해 추가 인프라(마스터, 에이전트)를 생성할 필요가 없습니다. 즉 Terraform 명령어가 AWS, Azure, GCP, Openstack 등의 Provider를 대신해 API를 호출하여 리소스를 생성합니다.
- 테라폼은 생성하려는 인프라 정보가 담겨 있는 텍스트로 이루어진 테라폼 구성 파일을 생성하여 API를 호출합니다. 이러한 구성 값들이 '코드형 인프라'를 만드는 바로 그 '코드'입니다. 팀의 누군가가 인프라를 수정하고자 할 때, 서버에 직접 접속하여 작업하거나 수작업으로 수정하는 대신 테라폼을 사용하여 구성 파일을 수정할 수 있습니다.
- Terraform은 컴퓨팅, 스토리지 및 네트워킹 리소스와 같은 하위 수준 구성 요소는 물론 DNS 항목 및 SaaS 기능과 같은 상위 수준 구성 요소를 관리

## WorkFlow
- 쓰기 : 여러 클라우드 공급자 및 서비스에 걸쳐 있을 수 있는 리소스를 정의 / 보안 그룹 및 로드 밸런서가 있는 Virtual Private Cloud 네트워크의 가상 머신에 애플리케이션을 배포하기 위한 구성을 생성
- 계획 : Terraform은 기존 인프라 및 구성을 기반으로 생성, 업데이트 또는 삭제할 인프라를 설명하는 실행 계획 생성
- 적용 : 승인시 Terraform은 리소스 종속성을 고려하여 제안된 작업을 올바른 순서로 수행

## 주요 명령어
- terraform init : terraform 명령어에는 테라폼의 기본 기능 포함, 모든 공급자(AWS, Azure, GCP등)에 대한 코드 포함 X , init을 실행하여 테라폼에 코드 스캔하도록 지시, 공급자 확인, 필요한 코드 다운로드 => 초기화
- terraform plan : 구성 파일을 사용하여 작업 수행 전 코드의 온전성 검사
- terraform apply : 구성 파일 실행

## Terraform 설치
```linux
# wget https://releases.hashicorp.com/terraform/1.2.3/terraform_1.2.3_linux_amd64.zip
# unzip terraform_1.2.3_linux_amd64.zip
# mv terraform /usr/local/bin/
# terraform -version
```

## AWS Terraform EC2 인스턴스 생성
```linux
# mkdir aws && cd $_
# vi main.tf
provider "aws" {
  region = "ap-northeast-2"
}

resource "aws_instance" "example" {
  ami           = "ami-0fd0765afb77bcca7"
  instance_type = "t2.micro"
}

# terraform init
# terraform plan
# terraform apply
```

## AWS EC2 인스턴스 웹서버 배포
```linux
# vi main.tf
provider "aws" {
  region = "ap-northeast-2"
}

resource "aws_instance" "example" {
  ami                    = "ami-0fd0765afb77bcca7"
  instance_type          = "t2.micro"
  vpc_security_group_ids = [aws_security_group.instance.id]
  key_name  = "aws-key"
  user_data = <<-EOF
              #! /bin/bash
              yum install -y httpd
              systemctl enable --now httpd
              echo "Hello, Terraform" > /var/www/html/index.html
              EOF

  tags = {
    Name = "terraform-example"
  }
}

resource "aws_security_group" "instance" {

  name = var.security_group_name

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    from_port   = -1
    to_port     = -1
    protocol    = "icmp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    Name = "terraform-sg"
  }
}

variable "security_group_name" {
  description = "The name of the security group"
  type        = string
  default     = "terraform-example-instance"
}

output "public_ip" {
  value       = aws_instance.example.public_ip
  description = "The public IP of the Instance"
}

output "public_dns" {
  value       = aws_instance.example.public_dns
  description = "The Public dns of the Instance"
}

output "private_ip" {
  value       = aws_instance.example.private_ip
  description = "The Private_ip of the Instance"
}

# terraform init
# terraform plan
# terraform apply
# terraform output public_ip
# terraform destroy
```