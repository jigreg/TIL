# helm 설치

```
# curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
# chmod 700 get_helm.sh
# ./get_helm.sh
# curl -L https://git.io/get_helm.sh | bash -s -- --version v3.8.2
```

# eks 설치

```
# curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
# sudo mv /tmp/eksctl /usr/local/bin
# eksctl version
# eksctl utils associate-iam-oidc-provider \
--cluster terraform-cluster \
--approve
# curl -o iam-policy.json https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.4.3/docs/install/iam_policy.json
# aws iam create-policy \
--policy-name AWSLoadBalancerControllerIAMPolicy \
--policy-document file://iam-policy.json
# eksctl create iamserviceaccount --cluster=terraform-cluster \
--namespace=kube-system \
--name=aws-load-balancer-controller \
--attach-policy-arn=arn:aws:iam::941161943134:policy/AWSLoadBalancerControllerIAMPolicy \
--override-existing-serviceaccounts \
--approve
# helm repo add eks https://aws.github.io/eks-charts
# helm repo update
# helm install aws-load-balancer-controller eks/aws-load-balancer-controller \
-n kube-system \
--set clusterName=terraform-cluster \
--set serviceAccount.create=false \
--set image.repository=602401143452.dkr.ecr.ap-northeast-2.amazonaws.com/amazon/aws-load-balancer-controller \
--set region=ap-northeast-2 \
--set vpcId=vpc-07e0432d93af09d7b
# kubectl get deployment -n kube-system aws-load-balancer-controller
# kubectl apply -f deployment.yaml
# kubectl apply -f ingress.yaml
```
