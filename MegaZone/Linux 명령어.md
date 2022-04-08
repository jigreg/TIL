# VirtualBoX 네트워크 종류
1. NAT(같은IP)
2. Natnetwork(직접 만들 수 있음) -> 도커 네트워크와 유사
3. host only(호스트 전용 어댑터) -> 인터넷 사용 불가 IP
4. bridge(외부IP사용가능)
5. 내부네트워크(가상 스위치)

# CentOS7 경량 데스크톱(X-Windows) 설치
## 1. 센토스 7 커널 업데이트
```
# yum -y install yum-plugin-fastestmirror
# yum install epel-release -y
# yum update -y
# yum install kernel-devel kernel-headers -y
# yum install -y install gcc make linux-headers-$(uname -r) dkms
# reboot
```
## 2. 센토스 7 xfce 데스크톱 설치
```
# yum groupinstall "X Window System" Xfce -y
# systemctl set-default graphical.target
# rm -rf /etc/systemd/system/default.target
# ln -s '/usr/lib/systemd/system/graphical.target' '/etc/systemd/system/default.target'
# yum install -y unzip wget
```
## 3. 센토스 7 구글 크롬 설치
```
# vi /etc/yum.repos.d/google-chrome.repo 
[google-chrome] 
name=google-chrome 
baseurl=http://dl.google.com/linux/chrome/rpm/stable/$basearch
enabled=1 
gpgcheck=1 
gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub 
# yum install google-chrome-stable -y
# vi /opt/google/chrome/google-chrome
exec -a "$0" "$HERE/chrome" "$@" --no-sandbox --user-data-dir
#  /usr/bin/google-chrome
```
## 4. 한글 나눔글꼴 설치
```
# mkdir /usr/share/fonts/nanumfont && cd $_
# wget http://cdn.naver.com/naver/NanumFont/fontfiles/NanumFont_TTF_ALL.zip
# unzip NanumFont_TTF_ALL.zip
# rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
# yum install -y perl gcc dkms kernel-devel kernel-headers make bzip2
```

## 5. 화면 사이즈 조절 (Autoresize)
```
# mount /dev/sr0 /mnt
# cd /mnt
# ./VBoxLinuxAdditons.run
# reboot
```
# 리눅스 기본 명령어
## 0.0 user 만들기
```
# adduser 이름
# passwd 비번
```

## 0. 실습 준비
```
# mkdir dir{A,B,C}
# touch dir{A,B,C}/file{X,Y,Z}
# touch file{A,B,C,D}
# ls -F ./ dirA dirB dirC
```
## 1. CLI 구문
```
# Command [options] [Arguments]

# uname -> OS이름 묻기 
# date
# cal
# clear

# uname -a (운영체제 설명 자세히)
# uname -s
# uname -r
# uname -s -r
# uname -sr

# cal 2 2016

~ Tilde(틸드)

# ls -l /etc/hosts

# date; uname
# cal 5 2019; date; uname -a

--- Ctrl + C    Terminates the command currently running.
# sleep 500
# ls 
# locale
  반응이 없다.
<CTRL + C>

--- Ctrl + D    Indicates end-of-file or exit.
# mkdir –p /test	/* 최상위 디렉토리 아래 test 디렉토리 생성 */
# cd /test	      /* 생성한 test 디렉토리로 이동 */
# pwd             /* 현재 작업 디텍토리 확인*/
/test
# cat > file1	    /* 파일에 내용 입력 */
Hello, Linux <Enter>
<CTRL + D>        /*“파일의 끝”의미 */
# cat file1  /* 입력된 파일 내용 확인 */
Hello, Linux

--- Ctrl + U    Erases all characters on the current command line.
# find / -name core -type f <CTRL + U>

--- Ctrl + W    Erase the last word on the command line.
# find / -name core -type f <CTRL + W>
# find / -name core -type <CTRL + W> <CTRL + W>
# find / -name <CTRL + W>
# find / <CTRL + U>

--- Ctrl + S    Stops output to the screen
--- Ctrl + Q    Restarts output to the screen after you have pressed Control-S
# du –a /

<CTRL + S>       /* stop */
<CTRL + Q>       /* quit, 원래 상태로 빠져 나오기 */
<CTRL + S>
<CTRL + Q>
<CTRL + C>       /* 정지와 복귀를 반복해보다가 빠져나온다 */
```

## 2. 메뉴얼 페이지
- 메뉴얼 페이지 보기
```
# man uname
# man -k calendar
```
## 3. 디렉토리 작업
- 현재 작업 디렉토리 확인
```
# pwd
```
- 디렉토리 내용 확인
```
# ls
# ls dirA
# ls /var/log
```
- 숨겨진 파일 보기
```
# ls -a
```
- 디렉토리 내용 자세히 보기
```
# ls -l
# ls -l dirA
```
- 개별 디렉토리 확인
```
# ls -l dirA
# ls -ld dirA
```
- 디렉토리 하위 목록 보기
```
# ls -R
# ls -R dirA
```
- 파일 종류 확인
```
# ls -F
# ls -F /bin/uname

# file dirA
# file /var/log/maillog
# file /bin/uname
```
- 디렉토리 변경
```
# pwd
# cd dirA
# pwd

# ls -a
# pwd
# cd ..
# pwd

# cd dirA
# pwd
# cd ../dirB
# pwd
# cd /root/dirA
# pwd
# cd ~
# pwd
# cd ~/dirA
# pwd
루트 사용자 홈디렉토리 /root
john 사용자 홈디렉토리 /home/john

# pwd
# cd /root/dirA
# pwd
# cd -
# pwd
```

## 4. 파일 작업
```
# cat /etc/hosts
# cat /etc/ssh/sshd_config
# more /etc/ssh/sshd_config
# echo -e "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15" > numbers
# cat numbers
# head numbers
# head -5 numbers
# tail -3 numbers
# wc /etc/ssh/sshd_config
# wc -l /etc/ssh/sshd_config
wc -> 글자수 파악
```
## 5. 복사
- 파일 복사
```
# ls -F
# cp fileA fileAA
# ls -F
# ls -F dirC
# cp fileA fileAA dirC
# ls -F dirC
# cp -i fileA fileAA
```
- 디렉토리 복사
```
# cp dirC dirCC (X)
# cp -r dirC dirCC (o)
# ls -F dirC
# ls -F dirCC
```
## 6. 이동
- 파일 이동
```
# ls -F dirC
# mv fileD dirC
# ls -F dirC
```
- 디렉토리 이동
```
# ls -F
# ls -F dirC
# mv dirCC dirC
# ls -F
# ls -F dirC
```
## 7. 생성
- 빈 파일 생성
```
# touch dirC/touch_file
# ls -F dirC
# touch makeA makeB makeC
# ls -F
```
- 디렉토리 생성
```
# mkdir dirX
# ls -ld dirX
# mkdir dirY/dirZ (x) 상위폴더가 없는 경우
# mkdir -p dirY/dirZ -p를 줘야 없는 폴더 생성 후 만듬
# ls -F
# ls -F dirY
# mkdir dirU dirV
```
## 8. 이름 변경
- 파일 이름 변경
```
# mv fileAA fileF
# ls -F
```
- 디렉토리 이름 변경
```
# mv dirU dirD
# ls -F
```
## 9. 삭제
- 파일 삭제
```
# rm makeA
# rm makeB makeC
```
- 빈 디렉토리 삭제
```
# rmdir dirD
# ls -F
# ls -F dirC
# rmdir dirC
# rm -r dirC
```
## 10. 링크
- 하드 링크(디스크 공유)
```
inode(index)
# ls -il /bin/cd
# ls -il /usr/bin/cd
# ls -il fileA
# ln fileA hardA
# ls -il fileA hardA
# echo test > fileA
# cat hardA
# echo hello > hardA
# cat fileA
# echo world >> hardA
```
- 심볼릭 링크(바로가기)
```
# ln -s fileA symbolA
# ls -il fileA symbolA
# echo aloha > fileA
# cat symbolA
# rm -rf fileA
# ls -il
# cat symbolA
# echo aloha > fileA
# cat symbolA
# rm -rf symbolA
```
## 11. 파일 내용 검색
- grep 명령어
```
# grep 'root' /etc/passwd
# grep -n 'root' /etc/passwd (즐번호 달기)
# grep -v 'root' /etc/passwd (root만 제외하고 보여주기)
# grep -l 'root' /etc/* (root가 있는 파이령 보여주기)
# grep -c 'root' /etc/passwd (root가 있는 줄 갯수 보여주기)
# grep 'root' /etc/passwd
# useradd  johnlee
# useradd  john
# grep 'john' /etc/passwd
# grep -w  'john' /etc/passwd
# grep '^kosa' /etc/passwd (kosa로 시작되는 패턴만 보여주기)
# grep 'j..n' /etc/passwd
# grep 'login$' /etc/passwd (loogin 단어가 그 줄에 끝에 들어가는 것 보여주기)
```
- egrep 명령어
```
# egrep 'N(o|e)+' /etc/passwd
# egrep '(root|john):x' /etc/passwd
# egrep -c '(svm|vmx)' /proc/cpuinfo
```
## 12. 파일 및 디렉토리 검색
```
# find / -name hosts
# find / -name hosts -type f
# find / -name hosts -type d
# find / -name fileA -type f -exec rm {} \;
# find / -name fileC -type f -ok rm {} \;
# find ~ -mtime -2 -ls | more (최근 이틀동안 수정시간이 변경된 파일만 찾아준다)
# find /usr/bin -size +3000000c -ls
```
## 13. vi 편집기 기초
```
# view numbers
# vi numbers
```
'i'키 누른다 -> 글을 입력한다. -> 'esc'키를 누른다. -> ':wq!' 입력한다.
- vi 명령어
  - a 텍스트 뒤에 커서를 위치시키고 입력을 받는다.
  - i 텍스트가 앞에 커서를 위치시키고 입력을 받는다.
  - o 커서가 위치한 줄의 아래에 새로운 줄을 추가하여 커서를 위치시키고 입력을 받는다.
  - G 파일의 제일 마지막 줄로 이동
  - 1G 파일의 제일 첫 번째 줄로 이동
  - nG n번째 줄로 이동
  - x 커서가 위치한 부분의 글자를 삭제한다.
  - dd 커서가 위치한 줄을 삭제한다.
  - u 명령어 실행 전으로 되돌린다.
  - yy 한 줄을 복사하여 임시 버퍼 공간에 저장한다.
  - p 임시 버퍼 공간에 저장된 텍스트를 커서의 아랫줄에 붙여 넣는다.
  - :%s/old/new/g
  - :set nu 화면에 줄 번호를 출력한다.
  - :n,nd n번째 줄부터 n번째 줄까지 삭제한다.
  - :n n번째 줄로 이동
  - :wq 수정한 파일을 디스크에 저장한 후 종료한다.
  - :x 수정한 파일을 디스크에 저장한 후 종료한다.
  - :q! 수정한 파일을 디스크에 저장하지 않고 종료한다.

## 14. 파일과 디렉토리 접근 권한
- 사용자 구분
소유자(user): 파일과 디렉토리의 소유자
그룹(group): 사용자가 속한 논리 그룹
기타(others): 소유자나 그룹에 속하지 않은 사용자

- 퍼미션
읽기(r): 파일의 내용을 확인하거나 복사 할 수 있음, 디렉토리 내용 확인 가능.
쓰기(w): 파일의 내용을 수정할 수 있음, 디렉토리 내에 파일을 추가하거나 삭제 가능.
실행(x): 실행파일의 경우 실행할 수 있음, 디렉토리 접근 및 내용 확인 가능.

- 퍼미션 변경
```
$ echo "Hello World" > test.txt
$ chmod 666 test.txt
$ ls -n
$ vi test.txt
$ chmod g-rw test.txt
$ chmod o-rw test.txt
$ ls -n
$ chmod 400 keypair.pem
```
## 15. 쉘 명령어
- 경로 이름
```
# cd dirA
# cd ~
# pwd

# cd ~johnlee
# cd ~root
# pwd

# cd dirB
# ls ~+
# ls ~-

# cd /usr/bin
# cd -
# cd -
```
- 파일 이름 대체 메타문자
```
# cd
# ls fi*
# ls *A

# ls f???A
# ls dir?

# ls file[AB]
# ls dir[AC]
# ls dir[A-C]
```
- 인용부호 메타문자
```
# echo $USER
# echo '$USER'
# echo "$USER"
# echo "\$USER"

# date
# echo `date`
# echo "The current time is `date`"
```
- 표준 입력(stdin;0) 재지정
```
# cat 0< /etc/hosts
```
- 표준 출력(stdout;1) 재지정
```
# ps 1> process_list
# cat process_list
# echo "---My Proccess List---" > process_list
# ps >> process_list
# cat process_list
```
- 표준 에러(stderr;2) 재지정
```
$ echo "TEST" > /tmp/test.txt
$ find /tmp -type f -exec grep TEST {} \; -print
$ find /tmp -type f -exec grep TEST {} \; -print 2> /dev/null
$ find /tmp -type f -exec grep TEST {} \; -print 1> test 2>&1
$ more /tmp/test
```
- 파이프 문자
```
$ ls -l /etc | wc -l
$ ps -ef | more
$ ps -ef | grep bash
# cat /etc/ssh/sshd_config | grep -n "22"
```
## 16. history 명령어
```
# history
# history 5
# history | head -3
# history | tail -3
# ls
# !!
# !10
```
## 17. 사용자 초기화 파일
```
# MyName="HanGi Lee"
# echo $MyName
# exit
# vi /etc/profile
MyName="HanGi Lee"
# exit
# echo $MyName

$ vi .bash_profile
MyName=James
$ source .bash_profile
$ echo $MyName
```
## 18. 프로세스 확인
```
# ps
# ps -f
# ps -ef
# ps -ef | more
# pstree
# ps -ef | grep bash
# pgrep -x bash
# pgrep -n sh
# pgrep -u 1000
# pgrep -l bash
# pgrep  -lt pts/1
```
## 19.kill 명령어
```
# sleep 1000 &
pgrep -l sleep
# kill 5572
# pgrep -l sleep

# sleep 2000 &
# pgrep -l sleep
# pkill sleep
```

## 20. 작업 관리
```
# sleep 60 &
# jobs
# fg %1

# sleep 60
^z
# bg %1
# jobs
```
## 21. 아카이브(하나의 파일로 모은다.)
- tar 명령어
c: 새로운 tar 파일을 생성
l: tar 파일 내부 내용 확인
x: tar 파일을 해제합니다.
f: 아카이브 파일 지정
v: tar 명령어 수행 과정 출력

- tar 명령어를 이용한 아카이브 생성(jar, war 유사)
```
# tar cvf archive.tar dirA fileD numbers
# tar tvf archive.tar
# mkdir test
# cd test
# tar xvf ../archive.tar
```
## 22. 압축 및 압축 해제
- compress 파일 압축
```
# ls -l
# compress -v process_list
# ls -l
# zcat process_list.Z
# compress -v achive.tar
# zcat achive.tar.Z | tar xvf -
# uncompress -c process_list.Z
```

- uncompress 압축 해제
```
# uncompress -v achive.tar.Z
# uncompress -v process_list.Z
# ls -l
```
- gzip 파일 압축
```
# gzip process_list
# ls -l
# zcat process_list.gz
```
- gunzip 압축 해제
```
# gunzip process_list.gz
# ls -l
```
- 아카이브된 파일 또는 디렉토리 압축 및 해제
```
# tar zcvf test.tar.gz dirB
# ls -l
# tar ztvf test.tar.gz
# rm -rf dirB
# tar zxvf test.tar.gz
# ls -l
```
- bzip2 파일 압축
```
# bzip2 process_list
# ls -l
# bzcat process_list.bz2
```
- bunzip 압축 해제
```
# bunzip2 process_list.bz2
# ls -l
```
- 아카이브된 파일 또는 디렉토리 압축 및 해제
```
# tar jcvf test.tar.bz2 dirB
# ls -l
# tar jtvf test.tar.bz2 dirB
# tar jxvf test.tar.bz2
# ls -l
```

- zip 파일 또는 디렉토리 압축 및 해제
```
# zip test.zip dirB/*
# rm -rf dirB
# unzip test.zip
```
chmod 744
r(4) : read
w(2) : write
x(1) : execute