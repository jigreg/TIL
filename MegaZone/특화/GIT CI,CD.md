# GIT HUB

## Git Create a new repository

```
https://github.com/jigreg/dev.git
```

### Git을 활용한 GitHub에 소스코드 Push

```
# mkdir git-test && cd $_
# echo "Hello World" > README.txt
# git init
Initialized empty Git repository in /root/git-test/.git/ # 로컬 저장소
# ls -al
# git config --global user.email "test@example.com" # 버전 관리를 위해 내 정보 설정
# git config --global user.name "johnlee"
# git add README.txt
# git commit -m "add site"
[master (root-commit) ee0b2d0] add site
1 file changed, 1 insertion(+)
create mode 100644 README.txt
# echo "Aloha" >> README.txt
# git add README.txt
# git commit -m "add update"
[master 62b4357] add update
1 file changed, 1 insertion(+)
# git log

commit 62b435702d0f51da2c85ac805ca9b10923ca8854
Author: johnlee <test@example.com>
Date: Mon Jan 31 10:46:06 2022 +0900

    add update

commit ee0b2d0c2c7f874e7e7ed63d42a10ecc87cbac73
Author: johnlee <test@example.com>
Date: Mon Jan 31 10:45:36 2022 +0900

    add site

# cat README.txt
Hello World
Aloha

# git checkout 776e5fded06e850941fd79732aa7fc005612ec4d
Note: checking out '776e5fded06e850941fd79732aa7fc005612ec4d'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -b with the checkout command again. Example:

# git checkout -b new_branch_name
HEAD is now at 776e5fd... add site
# cat README.txt
Hello World
# git checkout -
Previous HEAD position was 776e5fd... add site
Switched to branch 'master'
# cat README.txt
Hello World
Aloha
```

## GitHub 원격저장소 커밋

```
# git remote add origin https://github.com/hali-linux/dev.git
# git push origin master
Username for 'https://github.com':
GitHub 원격저장소의 커밋을 로컬저장소에 내려받기
# git clone https://github.com/hali-linux/dev.git
# cd GitTest/
# cat README.txt
# echo "NIHAO" >> README.txt
# git add README.txt
# git commit -m "add list"
# git push origin master
원격저장소의 새로운 커밋을 로컬저장소에 갱신하기
# cd ~
# cd git-test/
# cat README.txt
# git pull origin master
# cat README.txt
```

### 제거

```
# git rm README.txt
# git commit -m "remove README.txt"
# git push origin master
```

### CentOS Git Lab 설치

```
# curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.rpm.sh | sudo bash
# EXTERNAL_URL="http://192.168.4.214" yum install -y gitlab-ce
# cat /etc/gitlab/initial_root_password # 패스워드 수정
```

### EC2(Amazon Linux2)에 Gitlab 설치

```
# sudo yum install -y curl policycoreutils-python openssh-server openssh-clients perl
# curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.rpm.sh | sudo bash
# sudo sed -i "s/\/el\/7/\/amazon\/2/g" /etc/yum.repos.d/gitlab_gitlab*.repo
# sudo yum clean metadata
# sudo yum makecache
# sudo EXTERNAL_URL="http://tomcat.seojun.shop" yum install -y gitlab-ce
# cat /etc/gitlab/initial_root_password
```

### GCP(Debian)에 Gitlab 설치

```
# sudo apt-get update
# sudo apt-get install -y curl openssh-server ca-certificates perl
# curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh | sudo bash
# sudo EXTERNAL_URL="http://gitlab.seojun.shop" apt-get install gitlab-ce
# cat /etc/gitlab/initial_root_password
```

### protection 설정

개인 계정 > 프로젝트 > settings > repository > Protected branches > expand > unprotected 클릭

### 간단한 데브옵스 프로젝트

- Continuous Integration (CI)
- Continuous Delivery (CD)
- Continuous Deployment (CD)

### 젠킨스 설치

```
$ sudo su -
# wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
# rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
# yum install -y fontconfig java-11-openjdk
# amazon-linux-extras install -y java-openjdk11
# yum install -y jenkins
# systemctl enable --now jenkins
# cat /var/lib/jenkins/secrets/initialAdminPassword # 패스워드 수정
```

### Install Git on Jenkins Instance

```
# hostnamectl set-hostname jenkins-server
# yum install -y git
```

### Maven 설치

```
# cd /opt
# wget https://dlcdn.apache.org/maven/maven-3/3.8.6/binaries/apache-maven-3.8.6-bin.tar.gz
# tar -xvzf apache-maven-3.8.6-bin.tar.gz
# mv apache-maven-3.8.6 maven
# cd maven
# cd bin
# cd ~
# find / -name java-11*
# vi .bash_profile
M2_HOME=/opt/maven
M2=/opt/maven/bin
JAVA_HOME=/usr/lib/jvm/java-11-openjdk-11.0.13.0.8-1.amzn2.0.3.x86_64
# User specific environment and startup programs
PATH=$PATH:$HOME/bin:$JAVA_HOME:$M2_HOME:$M2
# echo $PATH
# source .bash_profile
# echo $PATH
# mvn -v
```

### Tomcat 서버 설치

```
# hostnamectl set-hostname tomcat-server
# amazon-linux-extras install -y java-openjdk11
# cd /opt
# wget https://dlcdn.apache.org/tomcat/tomcat-9/v9.0.65/bin/apache-tomcat-9.0.65.tar.gz
# tar -xvzf apache-tomcat-9.0.65.tar.gz
# mv apache-tomcat-9.0.65 tomcat
# cd tomcat/bin/
# ./startup.sh
# cd /opt/tomcat
# find / -name context.xml
# vi /opt/tomcat/webapps/host-manager/META-INF/context.xml
<!--  <Valve className="org.apache.catalina.valves.RemoteAddrValve"
         allow="127\.\d+\.\d+\.\d+|::1|0:0:0:0:0:0:0:1" /> -->
# vi /opt/tomcat/webapps/manager/META-INF/context.xml
<!--  <Valve className="org.apache.catalina.valves.RemoteAddrValve"
         allow="127\.\d+\.\d+\.\d+|::1|0:0:0:0:0:0:0:1" /> -->
# cd tomcat/bin/
# ./shutdown.sh
# ./startup.sh
# /opt/tomcat/conf
# vi tomcat-users.xml
<role rolename="manager-gui"/>
<role rolename="manager-script"/>
<role rolename="manager-jmx"/>
<role rolename="manager-status"/>
<user username="admin" password="kosa0401" roles="manager-gui, manager-script, manager-jmx, manager-status"/>
<user username="deployer" password="kosa0401" roles="manager-script"/>
<user username="tomcat" password="kosa0401" roles="manager-gui"/>

# ln -s /opt/tomcat/bin/startup.sh /usr/local/bin/tomcatup
# ln -s /opt/tomcat/bin/shutdown.sh /usr/local/bin/tomcatdown
# tomcatdown
# tomcatup
```

### Jenkins User-data

```
#!/bin/bash
timedatectl set-timezone Asia/Seoul
wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
yum install -y fontconfig java-11-openjdk
amazon-linux-extras install -y java-openjdk11
yum install -y jenkins git
systemctl enable --now jenkins
cd /opt
wget https://dlcdn.apache.org/maven/maven-3/3.8.6/binaries/apache-maven-3.8.6-bin.tar.gz
tar -xvzf apache-maven-3.8.6-bin.tar.gz
mv apache-maven-3.8.6 maven
cat <<EOF > /root/.bash_profile
# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
        . ~/.bashrc

fi
M2_HOME=/opt/maven
M2=/opt/maven/bin
JAVA_HOME=/usr/lib/jvm/java-11-openjdk-11.0.13.0.8-1.amzn2.0.3.x86_64
# User specific environment and startup programs

PATH=$PATH:$HOME/bin:/usr/lib/jvm/java-11-openjdk-11.0.13.0.8-1.amzn2.0.3.x86_64:/opt/maven:/opt/maven/bin

export PATH
EOF
source /root/.bash_profile
```

```
# 검증 방법
cat /var/lib/jenkins/secrets/initialAdminPassword
echo $PATH
mvn -v
```

### Docker host 환경 설치

```
#!/bin/bash
timedatectl set-timezone Asia/Seoul
hostnamectl set-hostname docker-host
amazon-linux-extras install docker -y
systemctl enable --now docker
curl https://raw.githubusercontent.com/docker/docker-ce/master/components/cli/contrib/completion/bash/docker -o /etc/bash_completion.d/docker.sh
usermod -a -G docker ec2-user
```

### Docker와 Jenkins 통합

```
sudo passwd ec2-user
sudo vi /etc/ssh/sshd_config
PasswordAuthentication yes
#PermitEmptyPasswords no
#PasswordAuthentication no
sudo systemctl restart sshd

sudo mkdir /opt/docker
sudo vi /opt/docker/Dockerfile
FROM tomcat:9
RUN cp -R /usr/local/tomcat/webapps.dist/* /usr/local/tomcat/webapps
COPY ./*.war /usr/local/tomcat/webapps

sudo chown -R ec2-user:ec2-user /opt/docker
```

### Jenkins WEBUI

plugin 설치 - publish over ssh
configure 설정 - SSH Servers
Name - docker host
Hostname - docker.seojun.shop
Username - ec2-user
password - kosa0401
webapp/target/\*.war
webapp/target
//opt//docker

cd /opt/docker;
docker build -t halilinux/mytomcat:v1.0 .;
docker rm -f docker-container;
docker run -d -p 8080:8080 --name docker-container halilinux/mytomcat:v1.0

http://docker.alibaba9.shop:8080/webapp/

```
vi ~/hello-world/webapp/src/main/webapp/index.jsp
git add index.jsp
git commit -m "edit index.jsp"
git push origin master
```
