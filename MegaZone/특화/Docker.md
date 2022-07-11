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

## Docker(Docker CE; Community Edition) Ubuntu Install
```
$ sudo apt update
$ sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
$ sudo apt update
$ sudo apt-cache policy docker-ce
$ sudo apt install docker-ce -y
```

## Docker 기본 명령어
```
# docker search nginx
# docker image pull nginx
# docker image ls
# docker image inspect --format="{{ .Os}}" nginx # 상세 정보
# docker container create -p 80:80 --name webserver nginx
# docker container start webserver
# docker container stop webserver
# docker container start webserver
# docker container rm -f webserver
# docker container run -p 80:80 --name webserver nginx # foreground 실행
# docker container run -d -p 80:80 --name webserver nginx # background 실행
# docker container run --name test_cal centos /bin/cal
# docker container run --name test_cal --rm centos /bin/cal # 컨테이너 1회성 실행하고 종료/ 남김 없이 지워지는 것
# docker container run -it --name test_bash centos /bin/bash #it 컨테이너 내부로 들어가기 위한 명령어
# docker container run -d --name test_ping centos /bin/ping localhost
# docker container logs -t test_ping
# docker container run -d -p 8080:80 --name test_port nginx # 중요!!!
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
# docker images # ls와 같은 명령어
# docker container run -d -p 80:80 --name webserver test_commit:v1.0
# docker rm -f $(docker ps -a -q) # container 전부 다 한번에 지우기
# docker image rm nginx # image 지우기 / name, id 입력하여 지우기
# docker rmi centos:latest
# docker rmi $(docker images -q) # image 전부 다 한번에 지우기
# yum install -y iproute # ip a 사용을 위한 패키지 다운
# docker network ls
# docker network create -d bridge --subnet 192.168.123.0/24 --ip-range 192.168.123.128/25 test_bridge
# docker run -d -p 8383:80 --name webserver2 --network test_bridge nginx
# docker network connect test_bridge test_bash
# docker network disconnect bridge test_bash
```

## Wordpress
### dbserver
```
# docker run -d -p 3306:3306 --name dbserver \
-e MYSQL_DATABASE=wordpress \
-e MYSQL_USER=wpuser \
-e MYSQL_PASSWORD=wppass \
-e MYSQL_ROOT_PASSWORD=password --network test_bridge mariadb
```
### webserver
```
# docker run -it -d -p 8888:80 --name apache --network test_bridge centos:7
# docker exec -it apache bash
# yum install -y httpd php php-mysql php-gd php-mbstring wget unzip
# wget https://ko.wordpress.org/wordpress-4.8.2-ko_KR.zip
# cd /var/www/html
# unzip /wordpress-4.8.2-ko_KR.zip
# mv wordpress/* .
# chown -R apache:apache /var/www/*
# httpd &
```

## Docker File
### 개념
- 컨테이너를 생성하는 여러 구성 정보를 하나의 파일로 정리
- 일괄 실행하여 docker build 명령을 통해 Docker 이미지를 작성하는 스크립트
- Docker File 작성시 폴더 하나 만들어서 작성 / vi Dockerfile (D는 대문자)
- Docker file 명령어
![docker](docker.png)
- ADD 는 압축 해제 가능
