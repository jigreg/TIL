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

### 서비스 배포 전략

1. Recreate
   - 가장 단순한 배포 전략
   - 기존 버전의 서버를 모두 삭제한 다음 새로운 버전의 서버를 생성
   - 서비스에 대한 일시적인 DownTime(중단 시간) 존재 - 무중단 배포 X
   - ![Recreate](https://images.contentstack.io/v3/assets/blt300387d93dabf50e/blt2bcee413a9844e96/5ccb571c43283e8d640ed147/recreate-deployment-ww.png)
2. Rolling Update
   - 기존 버전의 서버를 하나씩 죽이고 새로운 버전의 서버를 하나씩 띄우면서 순차적으로 교체하는 방법
   - 서버를 하나하나씩 버전을 업그레이드 하는 방식
   - 배포 중 추가 자원을 요구하지만, 서비스 DownTime 시간이 없음 - 무중단 배포
   - `이전 버전과 새로운 버전이 공존하는 시간이 발생`
   - ![Rolling update](https://images.contentstack.io/v3/assets/blt300387d93dabf50e/blt6743d826f9bc314f/5ccb56f2887e04ba691710fa/rolling-deployment-ww.png)
3. Blue/Green
   - 구 버전과 새로운 버전의 2가지를 서버에 마련하고, 이를 한꺼번에 교체하는 방법
   - 서비스 DownTime이 존재하지 않고, 롤백이 쉬움
   - 이전 버너과 새로운 버전의 공존하는 시간이 존재하는 Rolling Update의 문제를 해결
   - 운영 환경에 영향을 주지 않고 실제 서비스 환경으로 새 버전 테스트가 가능
   - 배포 시 시스템 자원의 2배를 사용하는 단점
   - ![Blue/Green](https://images.contentstack.io/v3/assets/blt300387d93dabf50e/blt3bd39fbb7a30f3f6/5ccb574ce8ec6ef265db8001/blue-green-deployment-ww.png)
4. Canary
   - 어원 처럼 위험을 빠르게 감지할 수 있는 배포 기법
   - 구버전의 서버와 새로운 버전의 서버들을 구성하고 일부 트래픽을 새 버전으로 분산시켜 테스트 진행
   - 새 버전을 프로덕션 서버로 사용될 수 있고, 문제가 있으면 다시 구버전으로 돌갈 수 있음
   - A/B 테스트 가능
   - ![Canary](https://images.contentstack.io/v3/assets/blt300387d93dabf50e/blt1942369a1c20bf82/5ccb56d2683c75ef6553878b/canary-deployment-ww.png)

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

- Deployment = ReplicaSet + Pod + history이며 ReplicaSet 을 만드는 것보다 더 윗 단계의 선언(추상표현)이다.
- Deployment 사용 이유는 애플리케이션의 업데이트와 배포를 더욱 편하게 만들기 위해
- 컨테이너 애플리케이션을 배포하고 관리하는 역할

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

#### NFS-Volume

```
# yum install -y nfs-utils.x86_64
# mkdir /nfs_shared
# chmod 777 /nfs_shared
# echo '/nfs_shared 192.168.0.0/20(rw,sync,no_root_squash)' >> /etc/exports
# systemctl enable --now nfs
# vi nfs-pv.yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: nfs-pv
spec:
  capacity:
    storage: 100Mi
  accessModes:
    - ReadWriteMany #RWX
  persistentVolumeReclaimPolicy: Recycle
  nfs:
    server: 192.168.1.186
    path: /nfs_shared

# kubectl apply -f nfs-pv.yaml
# kubectl get pv
# vi nfs-pvc.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: nfs-pvc
spec:
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 100Mi

# kubectl apply -f nfs-pvc.yaml
# kubectl get pvc
# kubectl get pv
# vi nfs-pvc-deploy.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nfs-pvc-deploy
spec:
  replicas: 4
  selector:
    matchLabels:
      app: nfs-pvc-deploy
  template:
    metadata:
      labels:
        app: nfs-pvc-deploy
    spec:
      containers:
      - name: nginx
        image: nginx
        volumeMounts:
        - name: nfs-vol
          mountPath: /usr/share/nginx/html
      volumes:
      - name: nfs-vol
        persistentVolumeClaim:
          claimName: nfs-pvc

# kubectl apply -f nfs-pvc-deploy.yaml
# kubectl get pod
# kubectl exec -it nfs-pvc-deploy-76bf944dd5-6j9gf -- /bin/bash
# kubectl expose deployment nfs-pvc-deploy --type=LoadBalancer --name=nfs-pvc-deploy-svc1 --external-ip 192.168.1.186 --port=80
```

### metallb (DHCP)

- ip 충돌을 방지하기 위하여 어댑터 1 NAT Network 어댑터 2 호스트 전용 어댑터로 설정
- hosts 파일 수정

#### kubeadm 초기화

```
# kubeadm reset
# kubeadm init --apiserver-advertise-address=192.168.56.103 --pod-network-cidr=10.244.0.0/16
# mkdir -p $HOME/.kube
# cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
# chown $(id -u):$(id -g) $HOME/.kube/config
# kubectl apply -f https://raw.githubusercontent.com/flannel-io/flannel/master/Documentation/kube-flannel.yml
```

#### metallb

```
# yum install -y git
# git clone https://github.com/hali-linux/_Book_k8sInfra.git
# kubectl apply -f /root/_Book_k8sInfra/ch3/3.3.4/metallb.yaml
# kubectl get pods -n metallb-system -o wide
# vi metallb-l2config.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  namespace: metallb-system
  name: config
data:
  config: |
    address-pools:
    - name: nginx-ip-range
      protocol: layer2
      addresses:
      - 192.168.56.200-192.168.56.250

# kubectl apply -f metallb-l2config.yaml
# kubectl describe configmaps -n metallb-system

- docker 이미지 풀로 받아서 태그 변경 후 사설 레포지토리에 업로드
metallb/speaker:v0.8.2
metallb/controller:v0.8.2

# vi metallb-test.yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  labels:
    app: nginx-pod
spec:
  containers:
  - name: nginx-pod-container
    image: 192.168.56.103:5000/nginx:latest
---
apiVersion: v1
kind: Service
metadata:
  name: loadbalancer-service-pod
spec:
  type: LoadBalancer
#  externalIPs:
#  -
  selector:
    app: nginx-pod
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80

# kubectl apply -f metallb-test.yaml
```

### multi-container

```
# vi multipod.yaml
apiVersion: v1
kind: Pod
metadata:
 name: multipod
spec:
 containers:
 - name: nginx-container        #1번째 컨테이너
   image: nginx:1.14
   ports:
   - containerPort: 80
 - name: centos-container       #2번째 컨테이너
   image: centos:7
   command:
   - sleep
   - "10000"
# kubectl apply -f multipod.yaml
```

#### Multi-Container-Wordpress

```
# vi wordpress-pod-svc.yaml
apiVersion: v1
kind: Pod
metadata:
  name: wordpress-pod
  labels:
    app: wordpress-pod
spec:
  containers:
  - name: mysql-container
    image: mysql:5.7
    env:
    - name: MYSQL_ROOT_HOST
      value: '%' # wpuser@%
    - name: MYSQL_ROOT_PASSWORD
      value: kosa0401
    - name: MYSQL_DATABASE
      value: wordpress
    - name: MYSQL_USER
      value: wpuser
    - name: MYSQL_PASSWORD
      value: wppass
    ports:
    - containerPort: 3306
  - name: wordpress-container
    image: wordpress
    env:
    - name: WORDPRESS_DB_HOST
      value: wordpress-pod:3306
    - name: WORDPRESS_DB_USER
      value: wpuser
    - name: WORDPRESS_DB_PASSWORD
      value: wppass
    - name: WORDPRESS_DB_NAME
      value: wordpress
    ports:
    - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: loadbalancer-service-deployment-wordpress
spec:
  type: LoadBalancer
  externalIPs:
  - 192.168.56.103
  selector:
    app: wordpress-pod
  ports:
  - protocol: TCP
    port: 80
```

### ConfigMap

- ConfigMap은 키-값 쌍으로 기밀이 아닌 데이터를 저장하는 데 사용한 API 오브젝트
- Pod는 볼륨에서 환경 변수, 커맨드-라인 인수 또는 구성 파일로 ConfigMap 사용
- 컨테이너 이미지에서 환경별 구성을 분리하여, 애플리케이션을 쉽게 이식

```
# vi configmap-dev.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: config-dev
  namespace: default
data:
  DB_URL: localhost
  DB_USER: myuser
  DB_PASS: mypass
  DEBUG_INFO: debug
# kubectl apply -f configmap-dev.yaml

# vi deployment-config01.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: configapp
  labels:
    app: configapp
spec:
  replicas: 1
  selector:
    matchLabels:
      app: configapp
  template:
    metadata:
      labels:
        app: configapp
    spec:
      containers:
      - name: testapp
        image: nginx
        ports:
        - containerPort: 8080
        env: # DEBUG_LEVEL=debug
        - name: DEBUG_LEVEL # 컨테이너 안에서의 변수 명
          valueFrom:
            configMapKeyRef:
              name: config-dev
              key: DEBUG_INFO
---
apiVersion: v1
kind: Service
metadata:
  labels:
    app: configapp
  name: configapp-svc
  namespace: default
spec:
  type: NodePort
  ports:
  - nodePort: 30800
    port: 8080
    protocol: TCP
    targetPort: 80
  selector:
    app: configapp

# kubectl exec -it configapp-64d4554b68-v55g5 -- bash
# env
```

### ImagePullError 해결

```
# kubectl create secret generic jigreg --from-file=.dockerconfigjson=/root/.docker/config.json --type=kubernetes.io/dockerconfigjson
# kubectl patch -n default serviceaccount/default -p '{"imagePullSecrets":[{"name": "jigreg"}]}'
# kubectl describe serviceaccount default -n default
```

#### Configmap Wordpress 적용

- Configmap 설정

```
# vi configmap-wordpress.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: config-wordpress
  namespace: default
data:
  MYSQL_ROOT_HOST: '%'
  MYSQL_ROOT_PASSWORD: kosa0401
  MYSQL_DATABASE: wordpress
  MYSQL_USER: wpuser
  MYSQL_PASSWORD: wppass

# kubectl apply -f configmap-wordpress.yaml
# kubectl describe configmaps config-wordpress

```

- DB, Wordpress SVC,POD 설정

```
# vi mysql-wordpress-pod-svc.yaml
apiVersion: v1
kind: Pod
metadata:
  name: mysql-pod
  labels:
    app: mysql-pod
spec:
  containers:
  - name: mysql-container
    image: mysql:5.7
    envFrom: # configmap 설정 전체를 한꺼번에 불러와서 사용
    - configMapRef:
        name: config-wordpress
    ports:
    - containerPort: 3306
---
apiVersion: v1
kind: Service
metadata:
  name: mysql-svc
spec:
  type: ClusterIP
  selector:
    app: mysql-pod
  ports:
  - protocol: TCP
    port: 3306
    targetPort: 3306
---
apiVersion: v1
kind: Pod
metadata:
  name: wordpress-pod
  labels:
    app: wordpress-pod
spec:
  containers:
  - name: wordpress-container
    image: wordpress
    env:
    - name: WORDPRESS_DB_HOST
      value: mysql-svc:3306
    - name: WORDPRESS_DB_USER
      valueFrom:
        configMapKeyRef:
          name: config-wordpress
          key: MYSQL_USER
    - name: WORDPRESS_DB_PASSWORD
      valueFrom:
        configMapKeyRef:
          name: config-wordpress
          key: MYSQL_PASSWORD
    - name: WORDPRESS_DB_NAME
      valueFrom:
        configMapKeyRef:
          name: config-wordpress
          key: MYSQL_DATABASE
    ports:
    - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: wordpress-svc
spec:
  type: LoadBalancer
  externalIPs: # metallb 설정해서 따로 안줘도 댐 주석처리 가능
  - 192.168.2.0
  selector:
    app: wordpress-pod
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
```

#### Configmap-wordpress-deployment

```
# vi mysql-deploy-svc.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mysql-deploy
  labels:
    app: mysql-deploy
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mysql-deploy
  template:
    metadata:
      labels:
        app: mysql-deploy
    spec:
      containers:
      - name: mysql-container
        image: mysql:5.7
        envFrom:
        - configMapRef:
            name: config-wordpress
        ports:
        - containerPort: 3306
---
apiVersion: v1
kind: Service
metadata:
  name: mysql-svc
spec:
  type: ClusterIP
  selector:
    app: mysql-deploy
  ports:
  - protocol: TCP
    port: 3306
    targetPort: 3306
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: wordpress-deploy
  labels:
    app: wordpress-deploy
spec:
  replicas: 1
  selector:
    matchLabels:
      app: wordpress-deploy
  template:
    metadata:
      labels:
        app: wordpress-deploy
    spec:
      containers:
      - name: wordpress-container
        image: wordpress
        env:
        - name: WORDPRESS_DB_HOST
          value: mysql-svc:3306
        - name: WORDPRESS_DB_USER
          valueFrom:
            configMapKeyRef:
              name: config-wordpress
              key: MYSQL_USER
        - name: WORDPRESS_DB_PASSWORD
          valueFrom:
            configMapKeyRef:
              name: config-wordpress
              key: MYSQL_PASSWORD
        - name: WORDPRESS_DB_NAME
          valueFrom:
            configMapKeyRef:
              name: config-wordpress
              key: MYSQL_DATABASE
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: wordpress-svc
spec:
  type: LoadBalancer
#  externalIPs:
#  - 192.168.2.0
  selector:
    app: wordpress-deploy
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
```

### namespace

- 쿠버네티스 클러스터 하나를 여러 개 논리적인 단위로 나눠서 사용하는 것
- 쿠버네티스 클러스터 하나를 여러 개 팀이나 사용자가 함께 공유
- 클러스터 안에서 용도에 따라 실행해야 하는 앱을 구분
- 네임스페이스별 별도의 쿼터를 설정해서 특정 네임스페이스의 사용량을 제한

```
# kubectl get namespaces
# kubectl config get-contexts kubernetes-admin@kubernetes
# kubectl config set-context kubernetes-admin@kubernetes --namespace=kube-system
# kubectl config get-contexts kubernetes-admin@kubernetes
# kubectl config set-context kubernetes-admin@kubernetes --namespace=default
# kubectl create namespace test-namespace
# kubectl get namespace
--- default 네임 스페이스로 설정
# kubectl config set-context kubernetes-admin@kubernetes --namespace=test-namespace
# kubectl config set-context kubernetes-admin@kubernetes --namespace=default
```

### ResourceQuota

- 각 네임스페이스마다, 가상 쿠버네티스 클러스터마다 사용 가능한 리소스 제한
- 생성이나 변경으로 그 시점에 제한이 걸린 상태가 되어도 이미 생성된 리소스에는 영향 X
- '생성 가능한 리소스 수 제한'과 리소스 사용량 제한'으로 나눌 수 있음

```
# vi sample-resourcequota.yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: sample-resourcequota
  namespace: my-ns
spec:
  hard:
    count/pods: 5

# kubectl describe resourcequotas sample-resourcequota
# kubectl run pod new-nginx --image=nginx

# vi sample-resourcequota-usable.yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: sample-resourcequota-usable
  namespace: default
spec:
  hard:
    requests.memory: 2Gi
    requests.storage: 5Gi
    sample-storageclass.storageclass.storage.k8s.io/requests.storage: 5Gi
    requests.ephemeral-storage: 5Gi
    requests.nvidia.com/gpu: 2
    limits.cpu: 4
    limits.ephemeral-storage: 10Gi
    limits.nvidia.com/gpu: 4

# vi sample-pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: sample-pod
spec:
  containers:
  - name: nginx-container
    image: nginx:1.16
    resources:
       requests:
          memory: "64Mi"
          cpu: "50m" # m -> milicore 1000 milicore = 1C
       limits:
          memory: "128Mi"
          cpu: "100m"


# vi sample-resource.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: sample-resource
spec:
  replicas: 3
  selector:
    matchLabels:
      app: sample-app
  template:
    metadata:
      labels:
        app: sample-app
    spec:
      containers:
      - name: nginx-container
        image: nginx:1.16
        resources:
          requests:
            memory: "64Mi"
            cpu: "50m" # m -> milicore 1000 milicore = 1C
          limits:
            memory: "128Mi"
            cpu: "100m"
```

### LimitRange

- Pod에 대해 CPU나 메모리 리소스의 최솟값과 최대값, 기본값 등을 설정 할 수 있음
- Namesapce에 제한을 주려면 네임스페이스마다 설정
- 기본 Pod에 영향 X

```
# vi sample-limitrange-container.yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: sample-limitrange-container
  namespace: default
spec:
  limits:
  - type: Container
    default:
      memory: 512Mi
      cpu: 500m
    defaultRequest:
      memory: 256Mi
      cpu: 250m
    max:
      memory: 1024Mi
      cpu: 1000m
    min:
      memory: 128Mi
      cpu: 125m
    maxLimitRequestRatio:
      memory: 2
      cpu: 2

# vi sample-pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: sample-pod
spec:
  containers:
  - name: nginx-container
    image: nginx:1.16

# vi sample-pod-overrequest.yaml
apiVersion: v1
kind: Pod
metadata:
  name: sample-pod-overrequest
spec:
  containers:
  - name: nginx-container
    image: nginx:1.16
    resources:
      requests:
        cpu: 100m # 최소가 125m 인데 제안을 100으로 하면 안됨
      limits:
        cpu: 100m

# vi sample-pod-overratio.yaml
apiVersion: v1
kind: Pod
metadata:
  name: sample-pod-overratio
spec:
  containers:
  - name: nginx-container
    image: nginx:1.16
    resources:
      requests:
        cpu: 125m
      limits:
        cpu: 500m # 250m 비율이 2배 초과되면 안됨
```
