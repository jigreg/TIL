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

## Git Lab 설치

```
# curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.rpm.sh | sudo bash
# EXTERNAL_URL="http://192.168.4.214" yum install -y gitlab-ce
# cat /etc/gitlab/initial_root_password # 패스워드 수정
```

### protection 설정

개인 계정 > 프로젝트 > settings > repository > Protected branches > expand > unprotected 클릭

### 간단한 데브옵스 프로젝트

- Continuous Integration (CI)
- Continuous Delivery (CD)
- Continuous Deployment (CD)
