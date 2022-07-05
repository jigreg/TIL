# Ansible

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
  - 저장소 - 광학 드라이브 - IDE 세컨더리 마스터 - Ubuntu-18.04.iso
  - 네트워크 - 어댑터에 브릿지