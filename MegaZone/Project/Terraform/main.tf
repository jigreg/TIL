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

data "aws_subnet" "apne2_az1" {
  tags = {
    Name = "FINAL-PRIVATE-SUBNET-2A"
  }
}
data "aws_subnet" "apne2_az3" {
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
  subnet_ids = [data.aws_subnet.apne2_az1.id, data.aws_subnet.apne2_az3.id]
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
  subnet_ids   = [data.aws_subnet.apne2_az1.id, data.aws_subnet.apne2_az3.id]
  instance_types = ["t2.micro"]

  scaling_config {
   desired_size = 10
   max_size   = 10
   min_size   = 10
  }

  depends_on = [
   aws_iam_role_policy_attachment.AmazonEKSWorkerNodePolicy,
   aws_iam_role_policy_attachment.AmazonEKS_CNI_Policy,
   #aws_iam_role_policy_attachment.AmazonEC2ContainerRegistryReadOnly,
  ]
 }
