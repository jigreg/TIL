# Ansible

## Master / Node Server Setting

### Ubuntu18
- VM Spec
  - 메모리 2GB
  - VDI(VirtualBox 디스크 이미지)
  - 동적 할당 - 씬 프로비저닝 (실무에선 고정 크기 - 씩 프로비저닝)
  - 디스크 128GB
  - CPU 1Core
  - 저장소 - 광학 드라이브 - IDE 세컨더리 마스터 - Ubuntu18.04.iso
  - 네트워크 - 어댑터에 브릿지
- Setting
  ```
  sudo vi /etc/ssh/sshd_config
  PermitRootLogin yes
  sudo su -
  passwd kosa0401
  sudo systemctl restart sshd
  ```

### CentOS7
- VM Spec
  - 메모리 1GB
  - VDI(VirtualBox 디스크 이미지)
  - 동적 할당 - 씬 프로비저닝 (실무에선 고정 크기 - 씩 프로비저닝)
  - 디스크 128GB
  - CPU 1Core
  - 저장소 - 광학 드라이브 - IDE 세컨더리 마스터 - CentOS7Minimal.iso
  - 네트워크 - 어댑터에 브릿지

## Ansible

### Vagrant
```
C:\Users\r2com>cd c:\HashiCorp
c:\HashiCorp>vagrant init
# 안될 시에 환경변수 편집 %SYSTEMROOT%\System32\WindowsPowerShell\v1.0\ 추가 
https://app.vagrantup.com/boxes/search?provider=virtualbox
c:\HashiCorp>notepad Vagrantfile
config.vm.box = "centos/7"
config.vm.network "public_network"
c:\HashiCorp>vagrant up
c:\HashiCorp>vagrant ssh
c:\HashiCorp>vagrant destroy
```

### Ansible Server Setting
- ansible-server 1c 1g
- centos-node01 1c 1g
- centos-node02 1c 1g
- ubuntu-node01 1c 1g
- ubuntu-node02 1c 1g

### Ansible ansible-server Setting
```
ip = 192.168.0.180
# yum install epel-release -y
# yum --enablerepo=epel -y install ansible
# ansible --version
```
문서 사이트 : https://docs.ansible.com/ansible/latest/index.html
모듈 사이트 : https://docs.ansible.com/ansible/2.9/modules/list_of_all_modules.html

### Ansible AD-HOC
```
# vi /etc/ansible/hosts
[centos]
192.168.0.235
192.168.0.237

[ubuntu]
192.168.0.207
192.168.0.244
```
- IaC 도구 중에 Ansible은 agent가 없음 (Python이 agent 역할)
- 대상서버에 다른 프로그램을 설치 안해도됨
- module ping => python이 잘 작동하는지 확인
- -k => ask password
```
# ansible all -m ping
# ansible all -m ping -k
# ansible centos -m ping -k
# ansible ubuntu -m ping -k
# echo "192.168.0.235" >> inventory.list
# echo "192.168.0.207" >> inventory.list
# ansible all -i inventory.list -m ping -k
# ansible 192.168.0.235 -i inventory.list -m ping -k
# ansible all --list-hosts
# ansible all -m shell -a "uptime" -k
# ansible all -m shell -a "df -h" -k
# ansible all -m shell -a "free -h" -k
# ansible all -m user -a "name=kosa" -k
# ansible all -m shell -a "tail -n 1 /etc/passwd" -k
# ansible all -m user -a "name=kosa state=absent" -k
# ansible all -m shell -a "tail -n 1 /etc/passwd" -k
```

### Ansible CentOS Apache AD-HOC
- 앤서블은 멱등성(Idempotency)이란 특징을 가집니다. 이는 여러 번 적용해도 결과가 바뀌지 않으며, 수정된 부분이 있다면 그 부분만 새롭게 반영되는 특징이 있습니다.
- shell module은 멱등성 없음
- copy,service,yum module은 멱등성 있음
```
# ansible centos -m yum -a "name=httpd state=present" -k
# curl https://www.nginx.com/ -o index.html
# ansible centos -m copy -a "src=index.html dest=/var/www/html/index.html" -k
# ansible centos -m service -a "name=httpd state=started" -k
# ansible centos -m shell -a "systemctl status firewalld" -k
# ansible centos -m shell -a "systemctl start firewalld" -k
# ansible centos -m shell -a "firewall-cmd --permanent --zone=public --add-service=http" -k
# ansible centos -m shell -a "firewall-cmd --reload" -k
# ansible centos -m service -a "name=httpd state=stopped" -k
# ansible centos -m shell -a "systemctl stop firewalld" -k
# ansible centos -m yum -a "name=httpd state=absent" -k
```

### Ansible Ubuntu Apache AD-HOC
```
# ansible ubuntu -m apt -a "name=apache2 state=present" -k
# curl https://www.nginx.com/ -o index.html
# ansible ubuntu -m copy -a "src=index.html dest=/var/www/html/index.html" -k
# ansible ubuntu -m service -a "name=apache2 state=stopped" -k
# ansible ubuntu -m service -a "name=apache2 state=started" -k
# ansible ubuntu -m apt -a "name=apache2 state=absent" -k
```

### Ansible SSH Key 전송
- -k 를 사용하여 암호 입력을 하지 않고 SSH 키로 바로 로그인 되도록
```
# ssh-keygen -t rsa
# ssh-copy-id root@192.168.0.235
# ssh-copy-id root@192.168.0.237
```