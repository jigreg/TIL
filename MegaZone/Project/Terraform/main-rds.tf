terraform {
 required_providers {
  aws = {
   source = "hashicorp/aws"
  }
 }
}
resource "aws_iam_role" "eks-iam-role" {
 name = "terraform-eks-iam-role"

 path = "/"

 assume_role_policy = <<EOF
{
 "Version": "2012-10-17",
 "Statement": [
  {
   "Effect": "Allow",
   "Principal": {
    "Service": "eks.amazonaws.com"
   },
   "Action": "sts:AssumeRole"
  }
 ]
}
EOF

}
data "aws_vpc" "FINAL-VPC" {
  tags = {
    Name = "FINAL-VPC"
  }
}

data "aws_subnet" "private1" {
  tags = {
    Name = "FINAL-PRIVATE-SUBNET-2A"
  }
}

data "aws_subnet" "private2" {
  tags = {
    Name = "FINAL-PRIVATE-SUBNET-2C"
  }
}

resource "aws_iam_role_policy_attachment" "AmazonEKSClusterPolicy" {
 policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
 role    = aws_iam_role.eks-iam-role.name
}
resource "aws_iam_role_policy_attachment" "AmazonEC2ContainerRegistryReadOnly-EKS" {
 policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
 role    = aws_iam_role.eks-iam-role.name
}
resource "aws_eks_cluster" "terraform-eks" {
 version = "1.21"
 name = "terraform-cluster"
 role_arn = aws_iam_role.eks-iam-role.arn

 vpc_config { 
  subnet_ids = [data.aws_subnet.private1.id, data.aws_subnet.private2.id]
 }
depends_on = [
  aws_iam_role.eks-iam-role,
 ]
}
resource "aws_iam_role" "workernodes" {
  name = "eks-node-group-example"

  assume_role_policy = jsonencode({
   Statement = [{
    Action = "sts:AssumeRole"
    Effect = "Allow"
    Principal = {
     Service = "ec2.amazonaws.com"
    }
   }]
   Version = "2012-10-17"
  })
 }

resource "aws_iam_role_policy_attachment" "AmazonEKSWorkerNodePolicy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy"
  role    = aws_iam_role.workernodes.name
}

resource "aws_iam_role_policy_attachment" "AmazonEKS_CNI_Policy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy"
  role    = aws_iam_role.workernodes.name
}

resource "aws_iam_role_policy_attachment" "EC2InstanceProfileForImageBuilderECRContainerBuilds" {
  policy_arn = "arn:aws:iam::aws:policy/EC2InstanceProfileForImageBuilderECRContainerBuilds"
  role    = aws_iam_role.workernodes.name
}

resource "aws_iam_role_policy_attachment" "AmazonEC2ContainerRegistryReadOnly" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
  role    = aws_iam_role.workernodes.name
}

resource "aws_eks_node_group" "worker-node-group" {
  cluster_name  = aws_eks_cluster.terraform-eks.name
  node_group_name = "terraform-workernodes"
  node_role_arn  = aws_iam_role.workernodes.arn
  subnet_ids   = [data.aws_subnet.private1.id, data.aws_subnet.private2.id]
  instance_types = ["t2.small"]

  scaling_config {
   desired_size = 3
   max_size   = 5
   min_size   = 2
  }

  depends_on = [
   aws_iam_role_policy_attachment.AmazonEKSWorkerNodePolicy,
   aws_iam_role_policy_attachment.AmazonEKS_CNI_Policy,
   #aws_iam_role_policy_attachment.AmazonEC2ContainerRegistryReadOnly,
  ]
}

resource "aws_security_group" "rds-sg" {
  name        = "terraform_rds_security_group"
  description = "Terraform example RDS MySQL server"
  vpc_id      = data.aws_vpc.FINAL-VPC.id
  # Keep the instance private by only allowing traffic from the web server.
  ingress {
    from_port       = 3306
    to_port         = 3306
    protocol        = "tcp"
    self            = "true"
  }
  ingress {
    from_port       = 3306
    to_port         = 3306
    protocol        = "tcp"
    cidr_blocks = ["112.221.225.165/32"]
  }
  ingress {
    from_port       = 22
    to_port         = 22
    protocol        = "tcp"
    cidr_blocks = ["112.221.225.165/32"]
  }
  # Allow all outbound traffic.
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_db_subnet_group" "rds-subnet"{
  name = "rds-subnet"
  subnet_ids = [data.aws_subnet.private1.id,data.aws_subnet.private2.id]
  tags = {
    Name = "db subnet group"
  }
}

resource "aws_db_instance" "conference" {
  identifier                = "conference"
  allocated_storage         = 20
  engine                    = "mysql"
  engine_version            = "8.0.27"
  instance_class            = "db.t2.micro"
  db_name                   = "conference"
  username                  = "admin"
  password                  = "kosa0401"
  db_subnet_group_name      = "rds-subnet"
  vpc_security_group_ids    = [aws_security_group.rds-sg.id]
  skip_final_snapshot       = true
  final_snapshot_identifier = "Ignore"
  parameter_group_name = "test-param-group"
}


resource "aws_db_parameter_group" "test" {
  name        = "test-param-group"
  description = "Terraform example parameter group for mysql5.6"
  family      = "mysql8.0"
  parameter {
    name  = "character_set_server"
    value = "utf8mb4"
  }
  parameter {
    name  = "character_set_client"
    value = "utf8mb4"
  }
  parameter {
    name  = "character_set_connection"
    value = "utf8mb4"
  }
  parameter {
    name  = "character_set_database"
    value = "utf8mb4"
  }
  parameter {
    name  = "character_set_filesystem"
    value = "utf8mb4"
  }
  parameter {
    name  = "character_set_results"
    value = "utf8mb4"
  }
  parameter {
    name  = "collation_connection"
    value = "utf8mb4_general_ci"
  }
  parameter {
    name  = "collation_server"
    value = "utf8mb4_general_ci"
  }
  parameter {
    name  = "max_connections"
    value = "150"
  }
}