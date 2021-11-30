## GIT 용어

___

> #### 저장소 만들기

```bash
$ git init
```

> #### 작업 후 버전 기록

```bash
$ git add .
$ git commit -m '커밋메세지'
```

> #### 상태보기

```bash
$ git status
$ git log
```

> #### 원격저장소

```bash
$ git remote add origin <url>
$ git push origin master /# repository로 업로드
```

### push

```bash
$ git push origin master
To https://github.com/edutak/edutak.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/edutak/edutak.git'
# 거절 원격 변경 != 로컬 변경 (커밋)
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. 
# 너는 먼저 원격 변경사항을 통합
# 다시 push 하기 전에...
# 예) git pull ...
You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

```

#### 해결

##### 1. git pull

```bash
$ git pull origin master
remote: Enumerating objects: 8, done.
remote: Counting objects: 100% (8/8), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 6 (delta 1), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (6/6), 1.29 KiB | 60.00 KiB/s, done.
From https://github.com/edutak/edutak
 * branch            master     -> FETCH_HEAD
   5571b5a..ea3c397  master     -> origin/master
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
```

##### 상황1) 충돌

> 동일한 파일이 수정된 경우

```bash
$ git status
On branch master
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```

* 충돌 예시

  ```bash
  <<<<<<< HEAD
  ## 프로젝트
  
  * 미세먼지 프로젝트
  =======
  ## 기술스택
  * JAVA
  * Python
  
  ## 학력
  >>>>>>> ea3c397205378975b40c233cbf62dd6255132d92
  ```

* conflict 파일을 수정하고, add -> commit

  ```bash
  $ git log --oneline
  58dcf30 (HEAD -> master) Merge branch 'master' of https://github.com/
  ea3c397 (origin/master) Update README.md
  f26b35f Update project
  d91c906 Update README.md
  5571b5a Update README
  691f7a4 Hi
  
  ```

##### 상황2) 충돌 X 반영

> 다른 커밋이 모두 다른 파일이 수정된 경우

* 커밋까지 모두 자동으로 진행됨

#### 3. push

```bash
$ git push origin master
```

