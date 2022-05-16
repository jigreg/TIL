# GO Lang

---

## Go 언어

- 컴파일 언어
- 코드 작성이 효율적인 언어, 구문이 단순하고 컴파일러 빨라야함
- scale up vs scale out 
- Go 작업공간 - GOPATH 환경 변수 set GOPATH
- 작업 공간의 기본 디렉토리 : GOPATH=$Home/go, GOPATH=%USERPROFILE%\go
- Go는 다른 언어와 달리 자신의 코드 저장소를 공유하여 패키지를 직접 다운받고 설치 가능

## GO 명령어

- go run [go 파일... | go 패키지] - 작은 프로그램 테스트, Go를 스크립트 언어처럼 사용
- go build [go 파일... | go 패키지] - 바이너리(실행파일) 생성, 최종 베포본 파일 만들기
  
```
$ go build hello.go
$ go build -o hello_world.exe hello.go
$ go install github.com/rakyll/hey@latest
```
## Code Formatting

- go fmt 
  - 들여쓰기 공백 수정
  - 구조체 항목 정렬
  - 연산자 주변 적절한 공백 사용 체크
- goimports
  - import 문 정리
  - 알파벳 순 정렬
  - 사용되지 않은 import 삭제
  - import 추측 
- 세미클론 삽입 규칙 
  - Go 컴파일러가 자동으로 문장 끝에 세미콜론을 붙여줌
  - 식별자, 기본 리터럴, 토큰들(break, continue, fallthrough, return, '++', '--', ')', '}')

## 개발 도구

- VS Code
- GoLand
- Go Playground

## 데이터 타입

- 불리언
- 숫자
  - 정수 - 주로 int 사용, 경우에 따라 byte
  - 실수 
  - 복소수
- 문자열
- 별칭(Alias) : byte(uint8), rune(int32)
- 제로 값 : 선언되었으나 값이 할당되지 않은 변수에 기본 값 제로(0) 할당

### 리터럴

- 코드에 작성하는 값 그 자체 
- 정수 리터럴
    - 10진수, 8진수, 16진수, 2진수 => 접두사 이용(없음, 0o, 0x, 0b)
    - 밑줄 (underscore) : 정수 리터럴 사이에 1_234
- 부동 소수점 리터럴
  - 점(.)
  - e(E) 지수 표현
  - 밑줄 가능
- 룬 리터럴
  - 작은 따옴표
  - 단일 유니코드 문자, 8비트 8진 숫자, 8비트 16진수 숫자, 16비트 16진수 숫자, 32비트 유니코드
  - 이스케이프 시퀀스: '\n', '\t', ... 