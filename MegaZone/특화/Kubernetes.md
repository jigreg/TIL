# Kubernetes

## 이해

- 컨테이너화된 워크로드와 서비스를 관리하기 위한 이식성, 확장 간으한 오픈소스 플랫폼
- 선언적 구성과 자동화를 모두 용이
- 크고 빠르게 성장하는 생태계

## Architecture

![kubernetes architecture](https://d33wubrfki0l68.cloudfront.net/2475489eaf20163ec0f54ddc1d92aa8d4c87c96b/e7c81/images/docs/components-of-kubernetes.svg)

### Control Plane Component

- 컨트롤 플레인 컴포넌트는 클러스터에 관한 전반적인 결정(ex 스케쥴링)을 수행하고 클러스터 이벤트(ex `deployment`의 replicas 필드에 대한 요구조건이 충족되지 않을 경우 새로운 pod를 구동시키는 것)을 감지하고 반응
- 클러스터 내 어떠한 머신에서든지 동작
- 간결성을 위하여 구성 스크립트는 보통 동일 머신 상에 모든 컨트롤 플레인 컴포넌트를 구동시키고, 사용자 컨테이너는 해당 머신 상에 동작 X
- 고가용성 클러스터 구성

### kube-apiserver

- API 서버는 쿠버네티스 API를 노출하는 쿠버네티스 컨트롤 플레인 컴포넌트
- 쿠버네티스 컨트롤 플레인의 프론트 엔드(관리자 전면부)
- 수평적 확장되도록 디자인(Scale out)
- 더 많은 인스턴스를 배포해서 확장
- 인스턴스를 실행하고, 인스턴스간의 트래픽을 균형있게 조절

### etcd (nosql)

- 모든 클러스터 데이터를 담는 쿠버네티스 뒷단의 저장소
- 일관성, 고가용성 키-값 저장소(KVS; Key Value Storage)
- 데이터를 백업하는 계획은 필수

### kube-scheduler

- 노드가 배정되지 않은 새로 생성된 pod 감지하고, 실행할 노드를 선택하는 컨트롤 플레인 컴포넌트(주로 메모리)
- 스케쥴링 결정을 위해서 고려되는 요소는 리소스에 대한 개별 및 총체적 요구 사항

### kube-controller-manager

- 컨트롤러를 구동하는 마스터 상의 컴포넌트
- 각 컨트롤러는 개별 프로세스, 복잡성을 낮추기 위해 모두 단일 바이너리로 컴파일 되고 단일 프로세스 내에서 실행
- 종류
  - 노드 컨트롤러
  - 레플리케이션 컨트롤러
  - 엔드포인트 컨트롤러
  - 서비스 어카운트 & 토큰 컨트롤러

### cloud-controller-manager

- 클라우드별 컨트롤 로직을 포함하는 쿠버네티스 컨트롤 플레인 컴포넌트
- 클라우드 컨트롤러 매니저를 통해 클러스터를 클라우드 공급자의 API에 연결
- 해당 클라우드 플랫폼과 상호 작용하는 컴포넌트와 클러스터와 상호 작용하는 컴포넌트를 분리

### kubelet - Worker node 구성 요소

- 클러스터의 각 노드에서 실행되는 `에이전트`
- kubelet은 pod에서 컨테이너가 확실하게 동작하도록관리
- pod를 꾸미고 안에 컨테이너를 꾸밈

### kube-proxy - Worker node 구성 요소

- kube-proxy는 클러스터의 각 노드에서 실행되는 네트워크 프록시
- 쿠버네티스의 서비스 개념의 구현부
- 노드의 네트워크 규칙을 유지 관리
- 내부 네트워크 세션이나 클러스터 바깥에서 pod로 네트워크 통신

### container-runtime - Worker node 구성 요소

- 컨테이너 런타임은 컨테이너 실행을 담당하는 소프트웨어
- Docker, containerd,CRI-O, Kubernetes CRI 를 구현한 모든 소프트웨어

### Pod

- 쿠버네티스에서 배포할 수 있는 가장 작은 단위
- 한 개 이상의 컨테이너와 스토리지, 네트워크 속성을 가짐
- pod에 속한 컨테이너는 스토리지와 네트워크를 공유하고 서로 localhost로 접근
- 컨테이너를 하나만 사용하는 경우도 반드시 pod으로 감싸서 관리

## Kubernetes 설치

### Minikube 설치(Single Node: Master Node + Worker Node)

```
# curl -fsSL https://get.docker.com/ | sudo sh
# systemctl enable --now docker
# yum install -y conntrack git
# curl -Lo minikube https://storage.googleapis.com/minikube/releases/v1.23.2/minikube-linux-amd64 && chmod +x minikube
# mkdir -p /usr/local/bin/
# install minikube /usr/local/bin/
# minikube version
# minikube start --driver=none
# minikube status
```

### kubectl 설치

```
# curl -LO https://dl.k8s.io/release/v1.22.2/bin/linux/amd64/kubectl
# install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
# source <(kubectl completion bash)
# echo "source <(kubectl completion bash)" >> ~/.bashrc
# exit
# kubectl version
# kubectl get svc # service
# kubectl get nodes
```

### Multi Node 설치

#### All Node(공통 설치)

```
# cat <<EOF >> /etc/hosts
192.168.1.186 master1
192.168.1.193 worker1
192.168.1.194 worker2
EOF

# hostnamectl set-hostname master
# curl https://download.docker.com/linux/centos/docker-ce.repo -o /etc/yum.repos.d/docker-ce.repo
# sed -i -e "s/enabled=1/enabled=0/g" /etc/yum.repos.d/docker-ce.repo
# yum --enablerepo=docker-ce-stable -y install docker-ce-19.03.15-3.el7
# cat <<EOF | sudo tee /etc/docker/daemon.json
{
  "exec-opts": ["native.cgroupdriver=systemd"],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m"
  },
  "storage-driver": "overlay2"
}
EOF
# systemctl enable --now docker
# systemctl daemon-reload
# systemctl restart docker
# systemctl disable --now firewalld
# setenforce 0
# sed -i 's/^SELINUX=enforcing$/SELINUX=disabled/' /etc/selinux/config

# swapoff -a
# sed -i '/ swap / s/^/#/' /etc/fstab

# cat <<EOF > /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF

# sysctl --system # 커널에 적용
# reboot

# cat <<'EOF' > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-$basearch
enabled=1
gpgcheck=0
repo_gpgcheck=0
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
EOF

# yum -y install kubeadm-1.19.16-0 kubelet-1.19.16-0 kubectl-1.19.16-0 --disableexcludes=kubernetes
# systemctl enable kubelet
```

#### Master

```
# kubeadm init --apiserver-advertise-address=192.168.1.186 --pod-network-cidr=10.244.0.0/16
# mkdir -p $HOME/.kube
# cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
# chown $(id -u):$(id -g) $HOME/.kube/config
# kubectl apply -f https://raw.githubusercontent.com/flannel-io/flannel/master/Documentation/kube-flannel.yml

# kubectl get pods --all-namespaces
# source <(kubectl completion bash)
# echo "source <(kubectl completion bash)" >> ~/.bashrc
# exit
```

#### Node

```
# kubeadm join 192.168.1.186:6443 --token igshg8.21uni3daumxd3i3m \
    --discovery-token-ca-cert-hash sha256:efa1953021daeadd04b92b676933f264040b450f2b6b7c4c63e84c99e18af424
# kubectl get nodes

```

### Pod

```
# mkdir workspace && cd $_
# kubectl run nginx --image=nginx
# kubectl expose pod nginx --name clusterip --type=ClusterIP --port 80
# kubectl expose pod nginx --name nodeport --type=NodePort --port 80
# kubectl expose pod nginx --name loadbalancer --type=LoadBalancer --external-ip 192.168.1.171 --port 80
# kubectl get all
# kubectl exec -it nginx -- bash
# kubectl delete svc --all
# kubectl delete pod nginx
```

### Service

```
# vi nginx-pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  labels:
    app: nginx-pod
spec:
  containers:
  - name: nginx-pod-container
    image: nginx

  - name: mysql-pod-container
    image: mysql
# 하나의 pod에 여러개의 container가 들어갈 수 있음
# kubectl apply -f nginx-pod.yaml
# kubectl get pod -o wide
# kubectl describe pod nginx-pod
```

```
# vi clusterip-pod.yaml
apiVersion: v1
kind: Service
metadata:
  name: clusterip-service-pod
spec:
  type: ClusterIP
  selector:
    app: nginx-pod
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80

# kubectl apply -f clusterip-pod.yaml
# kubectl get svc -o wide
# kubectl describe svc clusterip-service-pod
# kubectl edit svc clusterip-service-pod
```

```
# vi nodeport-pod.yaml
apiVersion: v1
kind: Service
metadata:
  name: nodeport-service-pod
spec:
  type: NodePort
  selector:
    app: nginx-pod
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80 # container port 절대로 바꾸면 안됌
    nodePort: 30080
# kubectl apply -f nodeport-pod.yaml
# kubectl get svc -o wide
# kubectl describe svc nodeport-service-pod
```

```
# vi loadbalancer-pod.yaml
apiVersion: v1
kind: Service
metadata:
  name: loadbalancer-service-pod
spec:
  type: LoadBalancer
  externalIPs:
  - 192.168.56.119
  selector:
    app: nginx-pod
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
# kubectl apply -f loadbalancer-pod.yaml
# kubectl get svc -o wide
# kubectl describe svc loadbalancer-service-pod
```

```
# vi replicaset.yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: nginx-replicaset
spec:
  replicas: 3 # desired state (kube-controller-manager) 선언적 API, 자가치유
  selector:
    matchLabels:
      app: nginx-replicaset

  template:
    metadata:
      name: nginx-replicaset
      labels:
        app: nginx-replicaset
    spec:
      containers:
      - name: nginx-replicaset-container
        image: nginx
        ports:
        - containerPort: 80

# kubectl apply -f replicaset.yaml
# kubectl get replicasets.apps -o wide
# kubectl describe replicasets.apps nginx-replicaset
```

```
# vi clusterip-replicaset.yaml # 클러스터아이피 야믈
apiVersion: v1
kind: Service
metadata:
  name: clusterip-service-replicaset
spec:
  type: ClusterIP
  selector:
    app: nginx-replicaset
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80

# kubectl apply -f clusterip-replicaset.yaml
# kubectl get svc -o wide
# kubectl describe svc clusterip-service-replicaset
```

```
# vi nodeport-replicaset.yaml # 노드포트 야믈
apiVersion: v1
kind: Service
metadata:
  name: nodeport-service-replicaset
spec:
  type: NodePort
  selector:
    app: nginx-replicaset
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
    nodePort: 30080

# kubectl apply -f nodeport-replicaset.yaml
# kubectl get svc -o wide
# kubectl describe svc nodeport-service-replicaset

# vi loadbalancer-replicaset.yaml # 로드밸런서 야믈
apiVersion: v1
kind: Service
metadata:
  name: loadbalancer-service-replicaset
spec:
  type: LoadBalancer
  externalIPs:
    - 172.25.0.137
  selector:
    app: nginx-replicaset
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80

# kubectl apply -f loadbalancer-replicaset.yaml
# kubectl get svc -o wide
# kubectl describe svc loadbalancer-service-replicaset
```

### Deployment

```
# vi deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx-deployment
  template:
    metadata:
      name: nginx-deployment
      labels:
        app: nginx-deployment
    spec:
      containers:
      - name: nginx-deployment-container
        image: nginx
        ports:
        - containerPort: 80

# kubectl apply -f deployment.yaml
# kubectl get deployments.apps -o wide
# kubectl describe deployments.apps nginx-deployment

# vi clusterip-deployment.yaml
apiVersion: v1
kind: Service
metadata:
  name: clusterip-service-deployment
spec:
  type: ClusterIP
  selector:
    app: nginx-deployment
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80

# kubectl apply -f clusterip-deployment.yaml
# kubectl get svc -o wide
# kubectl describe svc clusterip-service-deployment

# vi nodeport-deployment.yaml
apiVersion: v1
kind: Service
metadata:
  name: nodeport-service-deployment
spec:
  type: NodePort
  selector:
    app: nginx-deployment
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
    nodePort: 30080

# kubectl apply -f nodeport-deployment.yaml
# kubectl get svc -o wide
# kubectl describe svc nodeport-service-deployment

# vi loadbalancer-deployment.yaml
apiVersion: v1
kind: Service
metadata:
  name: loadbalancer-service-deployment
spec:
  type: LoadBalancer
  externalIPs:
  - 192.168.1.186
  - 192.168.1.193
  - 192.168.1.194
  selector:
    app: nginx-deployment
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
# kubectl apply -f loadbalancer-deployment.yaml
# kubectl get svc -o wide
# kubectl describe svc loadbalancer-service-deployment

# kubectl get all
# kubectl delete pod,svc --all
# kubectl delete replicaset,svc --all
# kubectl delete deployment,svc --all
```

#### Deployment 롤링 업데이트 제어

```
# kubectl set image deployment.apps/nginx-deployment nginx-deployment-container=nginx:1.9.1
# kubectl get all
# kubectl rollout history deployment nginx-deployment
# kubectl rollout history deployment nginx-deployment --revision=2 # 리비전2 상세보기
# kubectl rollout undo deployment nginx-deployment # 롤백(전 단계로 복원)
# kubectl rollout undo deployment nginx-deployment --to-revision=1 # 특정 리비전 롤백(특정 단계로 복원)
# kubectl get all
# kubectl rollout history deployment nginx-deployment
# kubectl rollout history deployment nginx-deployment --revision=3 # 리비전3 상세보기
```

### Ingress

```
# yum install -y git
# git clone https://github.com/hali-linux/_Book_k8sInfra.git
# kubectl apply -f /root/_Book_k8sInfra/ch3/3.3.2/ingress-nginx.yaml
# kubectl get pods -n ingress-nginx
# mkdir ingress && cd $_
# vi ingress-deploy.yaml
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: foods-deploy
spec:
  replicas: 1
  selector:
    matchLabels:
      app: foods-deploy
  template:
    metadata:
      labels:
        app: foods-deploy
    spec:
      containers:
      - name: foods-deploy
        image: halilinux/test-home:v1.0
---
apiVersion: v1
kind: Service
metadata:
  name: foods-svc
spec:
  type: ClusterIP
  selector:
    app: foods-deploy
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: sales-deploy
spec:
  replicas: 1
  selector:
    matchLabels:
      app: sales-deploy
  template:
    metadata:
      labels:
        app: sales-deploy
    spec:
      containers:
      - name: sales-deploy
        image: halilinux/test-home:v2.0
---
apiVersion: v1
kind: Service
metadata:
  name: sales-svc
spec:
  type: ClusterIP
  selector:
    app: sales-deploy
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: home-deploy
spec:
  replicas: 1
  selector:
    matchLabels:
      app: home-deploy
  template:
    metadata:
      labels:
        app: home-deploy
    spec:
      containers:
      - name: home-deploy
        image: halilinux/test-home:v0.0
---
apiVersion: v1
kind: Service
metadata:
  name: home-svc
spec:
  type: ClusterIP
  selector:
    app: home-deploy
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80

# kubectl apply -f ingress-deploy.yaml
# kubectl get all
# vi ingress-config.yaml
apiVersion: networking.k8s.io/v1beta1
kind: Ingress
metadata:
  name: ingress-nginx
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - http:
      paths:
      - path: /foods
        backend:
          serviceName: foods-svc
          servicePort: 80
      - path: /sales
        backend:
          serviceName: sales-svc
          servicePort: 80
      - path:
        backend:
          serviceName: home-svc
          servicePort: 80

# kubectl apply -f ingress-config.yaml

# vi ingress-service.yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-ingress-controller
  namespace: ingress-nginx
spec:
  ports:
  - name: http
    protocol: TCP
    port: 80
    targetPort: 80
  - name: https
    protocol: TCP
    port: 443
    targetPort: 443
  selector:
    app.kubernetes.io/name: ingress-nginx
  type: LoadBalancer
  externalIPs:
  - 192.168.2.0

# kubectl apply -f ingress-service.yaml
```

## Volume

```
# pv-pvc-pod.yaml
---
apiVersion: v1
kind: PersistentVolume
metadata:
  name: task-pv-volume
  labels:
    type: local
spec:
  storageClassName: manual
  capacity:
    storage: 10Mi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/mnt/data"
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: task-pv-claim
spec:
  storageClassName: manual
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Mi
  selector:
    matchLabels:
      type: local
---
apiVersion: v1
kind: Pod
metadata:
  name: task-pv-pod
  labels:
    app: task-pv-pod
spec:
  volumes:
    - name: task-pv-storage
      persistentVolumeClaim:
        claimName: task-pv-claim
  containers:
    - name: task-pv-container
      image: nginx
      ports:
        - containerPort: 80
          name: "http-server"
      volumeMounts:
        - mountPath: "/usr/share/nginx/html"
          name: task-pv-storage
# kubectl apply -f pv-pvc-pod.yaml
# kubectl get pv
# kubectl get pvc
# worker node 밑에 ls /mnt 하면 data 폴더 보임 echo 명령어로 index.html 만들면 폴더 공유 됨
```
