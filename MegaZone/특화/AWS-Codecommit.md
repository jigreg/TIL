cloud9(소스코드작성) -> codecommit(소스코드관리) -> codebuild(빌드) -> codedeploy(배포) -> codepipeline(자동화)

## Cloud9 실습

1. 파이썬 간단 실습
   hello.py

```py
import sys
print('Hello, World!')
print('The sum of 2 and 3 is 5.')
sum = int(sys.argv[1]) + int(sys.argv[2])
print('The sum of {0} and {1} is {2}.'.format(sys.argv[1], sys.argv[2], sum))
```

2. 파이썬 AWS SDK (Boto3) 활용 S3 다루기

```shell
curl -O https://bootstrap.pypa.io/get-pip.py
python get-pip.py
python -m pip --version
rm get-pip.py
python -m pip install boto3
python -m pip show boto3
```

s3.py

```py
import sys
import boto3
from botocore.exceptions import ClientError

def get_s3(region=None):
    """
    Get a Boto 3 Amazon S3 resource with a specific AWS Region or with your
    default AWS Region.
    """
    return boto3.resource('s3', region_name=region) if region else boto3.resource('s3')

def list_my_buckets(s3):
    print('Buckets:\n\t', *[b.name for b in s3.buckets.all()], sep="\n\t")

def create_and_delete_my_bucket(bucket_name, region, keep_bucket):
    s3 = get_s3(region)

    list_my_buckets(s3)

    try:
        print('\nCreating new bucket:', bucket_name)
        bucket = s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': region
            }
        )
    except ClientError as e:
        print(e)
        sys.exit('Exiting the script because bucket creation failed.')


    bucket.wait_until_exists()
    list_my_buckets(s3)

    if not keep_bucket:
        print('\nDeleting bucket:', bucket.name)
        bucket.delete()

        bucket.wait_until_not_exists()
        list_my_buckets(s3)
    else:
        print('\nKeeping bucket:', bucket.name)


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('bucket_name', help='The name of the bucket to create.')
    parser.add_argument('region', help='The region in which to create your bucket.')
    parser.add_argument('--keep_bucket', help='Keeps the created bucket. When not '
                                              'specified, the bucket is deleted '
                                              'at the end of the demo.',
                        action='store_true')

    args = parser.parse_args()

    create_and_delete_my_bucket(args.bucket_name, args.region, args.keep_bucket)


if __name__ == '__main__':
    main()
```

- s3.py s3.seojun.shop ap-northeast-2 --keep_bucket

## CodeCommit 실습

1. 계정 생성 및 Git HTTP 접속을 위한 자격 증명 생성
   사용자 추가 > AWSCodeCommitFullAccess 체크 > csv 다운로드 > 생성된 사용자 클릭 > 보안자격증명 > 자격증명 생성 > 자격증명 다운로드

2. Cloud9과 CodeCommit를 활용한 코드 버전 관리
   CodeCommit 리포지토리 생성 > Cloud9 으로 이동 > 하단 명령어 수행

```
sudo -s
aws --version
git --version

aws configure

git config --global credential.helper '!aws codecommit credential-helper $@'
git config --global credential.useHttpPath true
exit

git clone https://git-codecommit.ap-northeast-2.amazonaws.com/v1/repos/my-repo

cd my-repo
vi index.html
git add .
git status
git commit -m "Uploading New File"
git push
```

3. Github 소스를 CodeCommit로 옮기기

```
mkdir git-migration
git clone --mirror https://github.com/jigreg/hello-world.git git-migration
cd git-migration/
git push -uf https://git-codecommit.ap-northeast-2.amazonaws.com/v1/repos/my-repo --all
```

## CodeBuild 실습

1. Cloud9, CodeCommit, CodeBuild, S3를 활용한 Vue.js 설치

```
npm install vue
npm install --global vue-cli
vue
```

Codecommit에서 codebuild-repo 생성
git clone https://git-codecommit.ap-northeast-2.amazonaws.com/v1/repos/codebuild-repo

```
vue init webpack codebuild-repo
cd codebuild-repo
git add .
git status
git commit -m "Uploading New File"
git push
```

2. S3 정적 호스팅 구성
   정책 편집 > 정책 생성기 > S3 Bucket policy > Allow > \* > Action(GetObject) > arn:aws:s3:::s3.seojun.shop/\*

3. CodeBuild와 S3 정적 웹사이트 구현

buildspec.yml

```yaml
version: 0.2

phases:
install:
runtime-versions:
nodejs: 16
commands: - npm i npm@latest -g
pre_build:
commands: - npm install
build:
commands: - npm run build
post_build:
commands: - aws s3 sync ./dist s3://s3.alibaba9.shop
```

```
git add .
git commit -m "codebuild test commit"
git push
```

## CodeDeploy

1. 서비스 역할 및 IAM 인스턴스 프로파일 생성
   IAM > 역할만들기 > CodeDeploy 사용 사례 선택 > AWSCodeDeployRole 권한 추가 > 생성한 역할 클릭 > 신뢰 정책(위임) 편집(아래 내용 붙여넣기)

```
   {
   "Version": "2012-10-17",
   "Statement": [
   {
   "Sid": "",
   "Effect": "Allow",
   "Principal": {
   "Service": [
   "codedeploy.us-east-2.amazonaws.com",
   "codedeploy.us-east-1.amazonaws.com",
   "codedeploy.us-west-1.amazonaws.com",
   "codedeploy.us-west-2.amazonaws.com",
   "codedeploy.eu-west-3.amazonaws.com",
   "codedeploy.ca-central-1.amazonaws.com",
   "codedeploy.eu-west-1.amazonaws.com",
   "codedeploy.eu-west-2.amazonaws.com",
   "codedeploy.eu-central-1.amazonaws.com",
   "codedeploy.ap-east-1.amazonaws.com",
   "codedeploy.ap-northeast-1.amazonaws.com",
   "codedeploy.ap-northeast-2.amazonaws.com",
   "codedeploy.ap-southeast-1.amazonaws.com",
   "codedeploy.ap-southeast-2.amazonaws.com",
   "codedeploy.ap-south-1.amazonaws.com",
   "codedeploy.sa-east-1.amazonaws.com"
   ]
   },
   "Action": "sts:AssumeRole"
   }
   ]
   }
```

정책 > 정책 생성 > JSON > 아래 내용 붙여넣기

```
{
"Version": "2012-10-17",
"Statement": [
{
"Effect": "Allow",
"Action": [
"s3:Get*",
"s3:List*"
],
"Resource": [
"arn:aws:s3:::replace-with-your-s3-bucket-name/*",
"arn:aws:s3:::aws-codedeploy-us-east-2/*",
"arn:aws:s3:::aws-codedeploy-us-east-1/*",
"arn:aws:s3:::aws-codedeploy-us-west-1/*",
"arn:aws:s3:::aws-codedeploy-us-west-2/*",
"arn:aws:s3:::aws-codedeploy-ca-central-1/*",
"arn:aws:s3:::aws-codedeploy-eu-west-1/*",
"arn:aws:s3:::aws-codedeploy-eu-west-2/*",
"arn:aws:s3:::aws-codedeploy-eu-west-3/*",
"arn:aws:s3:::aws-codedeploy-eu-central-1/*",
"arn:aws:s3:::aws-codedeploy-ap-east-1/*",
"arn:aws:s3:::aws-codedeploy-ap-northeast-1/*",
"arn:aws:s3:::aws-codedeploy-ap-northeast-2/*",
"arn:aws:s3:::aws-codedeploy-ap-southeast-1/*",
"arn:aws:s3:::aws-codedeploy-ap-southeast-2/*",
"arn:aws:s3:::aws-codedeploy-ap-south-1/*",
"arn:aws:s3:::aws-codedeploy-sa-east-1/*"
]
}
]
}
```

역할 만들기 > EC2 선택 > AmazonS3FullAccess, CodeDeployEC2 추가

2. EC2 Auto Scaling 그룹 구성(codedeploy 에이전트 설정)
   ami-01711d925a1e4cc3a
   시작 구성 > 고급 세부 정보(아래 내용 붙여넣기)

```
#!/bin/bash
yum update -y
yum install -y ruby
curl -O https://aws-codedeploy-ap-northeast-2.s3.amazonaws.com/latest/install
chmod +x ./install
sudo ./install auto
```

3. Cloud9을 활용한 웹 페이지와 appspec.yml 생성

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Sample Deployment</title>
    <style>
      body {
        color: #ffffff;
        background-color: #0188cc;
        font-family: Arial, sans-serif;
        font-size: 14px;
      }
      h1 {
        font-size: 500%;
        font-weight: normal;
        margin-bottom: 0;
      }
      h2 {
        font-size: 200%;
        font-weight: normal;
        margin-bottom: 0;
      }
    </style>
  </head>
  <body>
    <div align="center">
      <h1>Congratulations</h1>
      <h2>This application was deployed using AWS CodeDeploy.</h2>
      <p>
        For next steps, read the
        <a href="http://aws.amazon.com/documentation/codedeploy"
          >AWS CodeDeploy Documentation</a
        >.
      </p>
    </div>
  </body>
</html>
```

```
vi appspec.yml
version: 0.0
os: linux
files:

- source: /index.html
  destination: /var/www/html/
  hooks:
  BeforeInstall: - location: scripts/install_dependencies
  timeout: 300
  runas: root - location: scripts/start_server
  timeout: 300
  runas: root
  ApplicationStop: - location: scripts/stop_server
  timeout: 300
  runas: root
```

```
mkdir scripts
cd scripts
vi install_dependencies
#!/bin/bash
yum install -y httpd
```

```
vi start_server
#!/bin/bash
systemctl start httpd
```

```
vi stop_server
#!/bin/bash
isExistApp = `pgrep httpd`
if [[-n $isExistApp]]; then
systemctl stop httpd
fi
```

```
zip -r codedeploy-sample.zip \*
aws s3 cp codedeploy-sample.zip s3://johnlee0405
```

4. CodeDeploy 구성 및 EC2 Auto Scaling 소스 배포
   애플리케이션 생성 > 배포 그룹 생성 > 배포 생성 > ALB 접속 테스트

5. 변경된 소스 및 Auto Scaling 그룹 추가 인스턴스에 대한 배포
   vi index.html

```html
<h1>My Second CodeDeploy</h1>
```

```
rm -rf codedeploy-sample.zip
zip -r codedeploy-sample-v2.zip *
aws s3 cp codedeploy-sample-v2.zip s3://s3.alibaba9.shop
```

## CodePipeLine

1. 서비스 역할 및 IAM 인스턴스 프로파일 생성
   사용자 추가 > 기존 정책 직접 연결 > csv 다운로드 > 생성된 사용자 클릭 > 보안 자격 증명 > 자격 증명 생성 > 자격 증명 다운로드

2. Cloud9과 CodeCommit 설정 및 소스 등록
   CodeCommit 리포지토리 생성 > HTTPS 복제 > index.html과 appspec.yml 파일 작성(아래 내용 붙여넣기)
   vi index.html
   ```html
   <!DOCTYPE html>
   <html>
     <head>
       <meta charset="utf-8" />
       <title>Sample Deployment</title>
       <style>
         body {
           color: #ffffff;
           background-color: #0188cc;
           font-family: Arial, sans-serif;
           font-size: 14px;
         }
         h1 {
           font-size: 500%;
           font-weight: normal;
           margin-bottom: 0;
         }
         h2 {
           font-size: 200%;
           font-weight: normal;
           margin-bottom: 0;
         }
       </style>
     </head>
     <body>
       <div align="center">
         <h1>Congratulations</h1>
         <h2>This application was deployed using AWS CodePipeline.</h2>
         <p>
           For next steps, read the
           <a href="http://aws.amazon.com/documentation/codedeploy"
             >AWS CodeDeploy Documentation</a
           >.
         </p>
       </div>
     </body>
   </html>
   ```

```

```

vi appspec.yml
version: 0.0
os: linux
files:

- source: /index.html
  destination: /var/www/html/
  hooks:
  BeforeInstall: - location: scripts/install_dependencies
  timeout: 300
  runas: root - location: scripts/start_server
  timeout: 300
  runas: root
  ApplicationStop: - location: scripts/stop_server
  timeout: 300
  runas: root

```

```

mkdir scripts
cd scripts
vi install_dependencies

```

```

#!/bin/bash
yum install -y httpd

vi start_server
#!/bin/bash
systemctl start httpd

vi stop_server
#!/bin/bash
isExistApp = `pgrep httpd`
if [[-n $isExistApp]]; then
systemctl stop httpd
fi

cd ..
git add .
git status
git commit -m "Uploading New File"
git push

```
3. EC2 생성과 CodeDeploy 배포 그룹 생성
   EC2 생성(AL2) > IAM 역할 선택 > 사용자 데이터(아래 내용 붙여넣기)
```

#!/bin/bash
yum update -y
yum install -y ruby
curl -O https://aws-codedeploy-ap-northeast-2.s3.amazonaws.com/latest/install
chmod +x ./install
sudo ./install auto

```
CodeDeploy 애플리케이션 생성 > EC2/온프레미스 선택 > 배포 그룹 생성 > IAM 역할 선택 > 환경 구성 태그 그룹 설정

4. CodePipeline과 CodeDeploy를 활용한 배포 파이프라인 구현
   CodePipeLine 생성 > 파이프라인 설정 선택 > 소스 스테이지 추가 > 빌드 스테이지 추가(건너뛰기) > 배포 스테이지 추가
```
