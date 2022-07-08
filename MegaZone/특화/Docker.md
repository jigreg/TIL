# Docker

## 개념
- 컨테이너형 가상화 기술 => 운영체제 수준 가상화
- 컨테이너란 호스트 OS상에 논리적인 구획을 만들고, 애플리케이션을 작동시키기 위해 필요한 라이브러리나 애플리케이션 을 하나로 모아, 별도의 서버인 것처럼 사용할 수 있게 만드는 것
- 가볍고 고속으로 작동
- 애플리케이션의 실행에 필요한 환경을 하나의 이미지로 모아두고 이미지를 사용하여 다양한 환경에서 애플리케이션 실행환경 구축 및 운용
- 3가지 기능
  - Docker 이미지 만듬 : docker image build
  - Docker 이미지 공유 : docker image push/pull
  - Docker 컨테이너 작동 : docker container run
- 구성 요소
  - Docker 이미지 : 파일 시스템과 실행할 애플리케이션 설정을 하나로 합친 것, 컨테이너를 생성하는 템플릿 역할
  - Docker 컨테이너 : 이미지 기반으로 생성, 파일 시스템과 애플리케이션 구체화 되어 실행

## Docker 가상머신
- VM Spec
  - OS : CentOS 7
  - CPU : 2Core
  - RAM : 4GB

## Docker(Docker CE; Community Edition) CentOS Install
```
# curl -fsSL https://get.docker.com/ | sh
# yum -y install bash-completion wget unzip net-tools mysql telnet rdate
# rdate -s time.bora.net && clock -w
# curl https://raw.githubusercontent.com/docker/docker-ce/master/components/cli/contrib/completion/bash/docker -o /etc/bash_completion.d/docker.sh
# systemctl start docker && systemctl enable docker
```

## Docker 기본 명령어
```
# docker search nginx
# docker image pull nginx
# docker image ls
# docker image inspect --format="{{ .Os}}" nginx
# docker container create -p 80:80 --name webserver nginx
# docker container start webserver
# docker container stop webserver
# docker container start webserver
# docker container rm -f webserver
# docker container run -p 80:80 --name webserver nginx # foreground 실행
# docker container run -d -p 80:80 --name webserver nginx # background 실행
# docker container run --name test_cal centos /bin/cal
# docker container run -it --name test_bash centos /bin/bash
# docker container run -d --name test_ping centos /bin/ping localhost
# docker container logs -t test_ping
# docker container run -d -p 8080:80 --name test_port nginx
# docker container stats nginx
# docker container run -d -p 8181:80 --cpus 1 --memory=256m --name test_resource nginx
# docker container run -d -p 8282:80 --cpus 1 --memory=256m -v /tmp:/usr/share/nginx/html --name volume-container nginx 
# docker container ls
# docker container ls -a
# docker container ls -a -f name=test_webserver
# docker container ls -a -f exited=0
# docker container ls -a --format "table {{.Names}}\t{{.Status}}"
# docker container attach test_bash
[root@1689b6318c35 /]# ctrl + p, ctrl +q 를 입력
# docker container ls
# docker container exec -it test_port /bin/echo "Hello world"
# docker container exec -it test_port /bin/bash
# docker container top test_port
# docker container port test_port
# docker container rename test_port webserver
# docker container cp webserver:/usr/share/nginx/html/index.html /root/index.html
# docker container cp ./index.html webserver:/usr/share/nginx/html/index.html
# docker container diff webserver
# docker container commit -a "johnlee<test@example.com>" -m "NICE TO MEET YOU" webserver test_commit:v1.0
# docker image ls
# docker image inspect test_commit:v1.0
# docker image save -o test_commit.tar test_commit:v1.0
# scp test_commit.tar root@192.168.0.207:/root 
# docker image load -i test_commit.tar
# docker image ls
# docker container run -d -p 80:80 --name webserver test_commit:v1.0
```