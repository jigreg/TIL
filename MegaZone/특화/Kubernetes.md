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
  replicas: 3 # desired state (kube-controller-manager)
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
