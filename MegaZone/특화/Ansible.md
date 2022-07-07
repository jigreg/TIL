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

### Ansible Env Setting Playbook
- KeyScan 설정 - 서버가 400개일시 items에 400개 추가해야댐
```
# vi keyscan.yml
- name: Setup for the Ansible's Environment
  hosts: localhost
  gather_facts: no
  
  tasks:
    - name: Generate sshkey
      shell: "{{ item }}"
      with_items:
        - "ssh-keyscan 192.168.0.235 >> ~/.ssh/known_hosts"
        - "ssh-keyscan 192.168.0.237 >> ~/.ssh/known_hosts"
        - "ssh-keyscan 192.168.0.207 >> ~/.ssh/known_hosts"
        - "ssh-keyscan 192.168.0.244 >> ~/.ssh/known_hosts"

# ansible-playbook keyscan.yml
# ansible all -m ping -k
```
- KeyPair 등록 - 위와같은 상황일 때 사용
```
# vi keypair_new.yml
- name: Create known_hosts between server and nodes
  hosts: all # 인벤토리 안의 모든 hosts 불러오기
  connection: local
  serial: 1 # 하나씩만 순차적으로 가져오기 / 누락 발생할 수 있음
  gather_facts: no

  tasks:
    - name: ssh-keyscan for known_hosts file
      command: /usr/bin/ssh-keyscan -t ecdsa {{ ansible_host }} # 매직 변수 ansible_host 활용하여 hosts ip 호출
      register: keyscan

    - name: input key
      lineinfile:
        path: ~/.ssh/known_hosts
        line: "{{ item }}"
        create: yes
      with_items:
        - "{{ keyscan.stdout_lines }}"

- name: Create authorized_keys between server and nodes
  hosts: all
  connection: local
  gather_facts: no
  vars:
    ansible_password: kosa0401

  tasks:
    - name: ssh-keygen for authorized_keys file
      openssh_keypair: 
        path: ~/.ssh/id_rsa
        size: 2048
        type: rsa
        force: False 
        # overwrite하지 않는다는 False라고 값을 넣거나 아니면 삭제

    - name: input key for each node
      connection: ssh
      authorized_key:
        user: root
        state: present
        key: "{{ lookup('file', '~/.ssh/id_rsa.pub') }}"

# anp keypair.yml
```
- 환경 설정 등록 hosts file & Alias 등록
```
# vi ansible_env.yml
- name: Setup for the Ansible's Environment
  hosts: localhost
  gather_facts: no
  
  tasks:
    - name: Add "/etc/ansible/hosts"
      blockinfile: 
        path: /etc/ansible/hosts
        block: |
          [centos]
          192.168.0.235
          192.168.0.237

          [ubuntu]
          192.168.0.207 ansible_python_interpreter=/usr/bin/python3
          192.168.0.244 ansible_python_interpreter=/usr/bin/python3

    - name: Configure Bashrc
      lineinfile:   
        path: /root/.bashrc
        line: "{{ item }}"
      with_items:
        - "alias ans='ansible'"
        - "alias anp='ansible-playbook'"

# ansible-playbook ansible_env.yml -k
# Session 재접속
```

### Ansible Playbook apache Install
```
# vi apache_install.yml
- name: Install apache on centos
  hosts: centos
  gather_facts: no

  tasks:
    - name: install apache web server
      yum: name=httpd state=present
    - name: upload default index.html for web server
      get_url: url=https://www.nginx.com dest=/var/www/html/ mode=0644
    - name: start apache web server
      service: name=httpd state=started
    - name: enable apache web server
      service: name=httpd enabled=yes

- name: Install apache on ubuntu
  hosts: ubuntu
  gather_facts: no

  tasks:
    - name: install apache web server
      apt: name=apache2 state=present
    - name: upload default index.html for web server
      get_url: url=https://www.nginx.com dest=/var/www/html/ mode=0644
    - name: start apache web server
      service: name=apache2 state=started

# ansible-playbook apache_install.yml -k
```

### Ansible Playbook apache Remove
```
# vi apache_remove.yml
- name: Remove apache on centos
  hosts: centos
  gather_facts: no

  tasks:
    - name: remove apache web server
      yum: name=httpd state=absent

- name: Remove apache on ubuntu
  hosts: ubuntu
  gather_facts: no

  tasks:
    - name: remove apache web server
      apt: name=apache2 state=absent

# ansible-playbook apache_remove.yml -k
```

### Ansible Playbook nginx Install
```
# vi nginx_install.yml
- name: Install nginx on centos
  hosts: centos
  gather_facts: no

  tasks:
    - name: install epel-release
      yum: 
        name: epel-release
        state: latest
    - name: install nginx web server
      yum: name=nginx state=present
    - name: upload default index.html for web server
      get_url: url=https://www.nginx.com dest=/usr/share/nginx/html/ mode=0644
    - name: start nginx web server
      service: name=nginx state=started

- name: Install nginx on ubuntu
  hosts: ubuntu
  gather_facts: no

  tasks:
    - name: install nginx web server
      apt: pkg=nginx state=present update_cache=yes
    - name: Upload default index.html for web server
      get_url: url=https://www.nginx.com dest=/var/www/html/
               mode=0644 validate_certs=no

# ansible-playbook nginx_install.yml
```

### Ansible Playbook nginx Remove
```
# vi nginx_remove.yml
- name: Remove nginx on centos
  hosts: centos
  gather_facts: no

  tasks:
    - name: remove nginx web server
      yum: 
        name: nginx 
        state: absent

- name: Remove nginx on ubuntu
  hosts: ubuntu
  gather_facts: no

  tasks:
    - name: remove nginx web server
      apt: 
       pkg: nginx* 
       state: absent

# ansible-playbook nginx_remove.yml
```

### Ansible Playbook NFS Install
```
# vi nfs.yml
- name: Setup for nfs server
  hosts: localhost
  gather_facts: no

  tasks:
    - name: make nfs_shared directory
      file:
        path: /root/nfs_shared
        state: directory
        mode: 0777

    - name: configure /etc/exports
      lineinfile:
        path: /etc/exports
        line: /root/nfs_shared 192.168.0.0/20(rw,sync)

    - name: Install NFS
      yum:
        name: nfs-utils
        state: present

    - name: nfs service start
      service:
        name: nfs-server
        state: restarted
        enabled: yes

- name: Setup for nfs clients CentOS
  hosts: centos
  gather_facts: no

  tasks:
    - name: make nfs_client directory
      file:
        path: /root/nfs
        state: directory

    - name: Install NFS
      yum:
        name: nfs-utils
        state: present

    - name: mount point directory as client
      mount:
        path: /root/nfs
        src: 192.168.0.180:/root/nfs_shared #Ansible-Server ip
        fstype: nfs
        state: mounted

- name: Setup for nfs clients Ubuntu
  hosts: ubuntu
  gather_facts: no

  tasks:
    - name: make nfs_client directory
      file:
        path: /root/nfs
        state: directory

    - name: Install NFS
      apt:
        pkg: nfs-common
        state: present
        update_cache: yes

    - name: mount point directory as client
      mount:
        path: /root/nfs
        src: 192.168.0.180:/root/nfs_shared
        fstype: nfs
        opts: nfsvers=3
        state: mounted

# ansible-playbook nfs.yml 
```

### Ansible Playbook Wordpress 
```
# vi wordpress.yml
- name: Setup for webserver
  hosts: webserver
  gather_facts: no

  tasks:
    - name: Install http
      yum:
        name: "{{ item }}"
        state: present
      with_items:
        - httpd
        - php
        - php-mysql
        - php-gd
        - php-mbstring
        - wget
        - unzip

    - name: Unarchive a file that needs to be downloaded (added in 2.0)
      ansible.builtin.unarchive:
        src: https://ko.wordpress.org/wordpress-4.8.2-ko_KR.zip
        dest: /var/www/html
        remote_src: yes

    - name: chown
      file:
        path: /var/www/html/wordpress
        owner: "apache"
        group: "apache"
        recurse: "yes"

    - name: web service restart
      service:
        name: httpd
        state: restarted

- name: Setup for dbserver
  hosts: dbserver
  gather_facts: no

  tasks:
    - name: Install mariadb
      apt:
        pkg: mariadb-server
        state: present
        update_cache: yes

    - name: Install pymysql
      apt:
        pkg: python-pymysql
        state: present

    - name: Install pymysql
      apt:
        pkg: python3-pymysql
        state: present

    - name: set root password
      mysql_user:
        name: 'root'
        password: '{{ mysql_root_password }}'
        login_unix_socket: /var/run/mysqld/mysqld.sock
        state: present

    - name: edit file
      replace:
        path: /etc/mysql/mariadb.conf.d/50-server.cnf
        regexp: "bind-address"
        replace: "#bind-address"

    - name: db service restart
      service:
        name: mysql
        state: restarted

    - name: Create database
      mysql_db:
        db: wordpress
        login_unix_socket: /var/run/mysqld/mysqld.sock
        state: present

    - name: Create database user
      mysql_user:
        user: wpuser
        password: wppass
        priv: "wordpress.*:ALL,GRANT"
        host: '%'
        login_unix_socket: /var/run/mysqld/mysqld.sock
        state: present

# anp wordpress.yml --extra-vars "mysql_root_password=kosa0401"
```