# SQL 명령어 실습(GUI)

1. 데이터베이스 생성
- shopDB 생성
localhost > 새로 생성 > 테이터베이스 > shopDB 입력 확인

2. 테이블 생성
- memberTBL 생성
shopDB > 새로 생성 > 테이블 > memberTBL

열 이름(한글)          영문이름        데이터 형식    길이         NULL 허용
아이디(Primary Key)    memberID        문자(CHAR)     8글자(영문)  X
회원 이름              memberName      문자(CHAR)     5글자(한글)  X
주소                   memberAddress   문자(CHAR)     20글자(한글) O

- productTBL 생성

shopDB > 새로 생성 > 테이블 > productTBL

열 이름(한글)          영문이름        데이터 형식    길이         NULL 허용
제품이름(Primary Key)  productName     문자(CHAR)     4글자(한글)  X
가격                   cost            숫자(INT)      정수         X
제조일자               makeDate        날짜(DATE)     날짜형       O
제조회사               company         문자(CHAR)     5글자(한글)  O
남은수량               amount          숫자(INT)      정수         X

3. 데이터 입력
- 행 삽입

회원 데이터 ( 아이디 / 이름 / 주소 )
Dang / 당탕이 / 경기 부천시 중동
Jee  / 지운이 / 서울 은평구 중산동
Han  / 한주연 / 인천 남구 주안동
Sang / 상길이 / 경기 성남시 분당구

제품데이터(제품명 / 비용 / 날짜 / 제조사 / 수량)
냉장고 / 5  / 2023-02-01 / 대우 / 22
세탁기 / 20 / 2022-09-01 / LG   / 3
컴퓨터 / 10 / 2021-01-01 / 삼성 / 17

4. 데이터 활용
- 회원의 모든 정보 조회

select * from memberTbl; 

-이름과 주소만 조회

select memberName, memberAddress from memberTbl;

- 지운이 정보만 조회

select * from memberTbl where memberName = '지운이';

- 테이블 생성

create table `my testTBL`(id int);
select * from `my testTBL`;

- 테이블 삭제

drop table `my testTBL`;

5. 데이터베이스 개체 활용
- 인덱스(Index): 대부분의 책의 제일 뒤에 붙어 있는 '찾아보기'와 같은 개념

CREATE TABLE indexTBL (first_name varchar(14), last_name varchar(16) , hire_date date);
INSERT INTO indexTBL 
	SELECT first_name, last_name, hire_date 
	FROM employees.employees
	LIMIT 500;
SELECT * FROM indexTBL;

SELECT * FROM indexTBL WHERE first_name = 'Mary';

EXPLAIN SELECT * FROM indexTBL WHERE first_name = 'Mary';

CREATE INDEX idx_indexTBL_firstname ON indexTBL(first_name);

SELECT * FROM indexTBL WHERE first_name = 'Mary';

EXPLAIN SELECT * FROM indexTBL WHERE first_name = 'Mary';

- 뷰(View): 가상 테이블, 진짜 테이블에 링크된 개념

CREATE VIEW uv_memberTBL 
AS
	SELECT memberName, memberAddress FROM memberTBL ;

SELECT * FROM uv_memberTBL ;

- 스토어드 프로시저(Stored Procedure): SQL문을 하나로 묶어서 편리하게 사용하는 프로그래밍 기능

SELECT * FROM memberTBL WHERE memberName = '당탕이';
SELECT * FROM productTBL WHERE productName = '냉장고';

DELIMITER //
CREATE PROCEDURE myProc()
BEGIN
	SELECT * FROM memberTBL WHERE memberName = '당탕이' ;
	SELECT * FROM productTBL WHERE productName = '냉장고' ;
END // 
DELIMITER ;

CALL myProc() ;

- 트리거(Trigger): 테이블에 부착되어서, 테이블에 INSERT나 UPDATE 또는 DELETE 작업이 발생되면 실행되는 코드

INSERT INTO memberTBL VALUES ('Figure', '연아', '경기도 군포시 당정동');

SELECT * FROM membertbl;

UPDATE memberTBL SET memberAddress = '서울 강남구 역삼동' WHERE memberName = '연아';

SELECT * FROM membertbl;

DELETE FROM memberTBL WHERE memberName = '연아';

SELECT * FROM membertbl;

CREATE TABLE deletedMemberTBL (  -- 백업 테이블
	memberID char(8) ,
	memberName char(5) ,
	memberAddress  char(20),
	deletedDate date  -- 삭제한 날짜
);

DELIMITER // -- 구분자
CREATE TRIGGER trg_deletedMemberTBL  -- 트리거 이름 
	AFTER DELETE -- 삭제 후에 작동하게 지정 
	ON memberTBL -- 트리거를 부착할 테이블 
	FOR EACH ROW -- 각 행마다 적용시킴 
BEGIN 
	-- OLD 테이블의 내용을 백업테이블에 삽입 
	INSERT INTO deletedMemberTBL 
		VALUES (OLD.memberID, OLD.memberName, OLD.memberAddress, CURDATE() ); 
END //
DELIMITER ;

SELECT * FROM memberTBL;

DELETE FROM memberTBL WHERE memberName = '당탕이';

SELECT * FROM memberTBL;

SELECT * FROM deletedMemberTBL;

INSERT INTO memberTBL 
	SELECT memberID, memberName, memberAddress
	FROM deletedMemberTBL;

SELECT * FROM memberTBL;

6. 데이터베이스 백업 및 관리(DBA: DataBase Administrator)
- 백업과 복원: 데이터베이스를 다른 매체에 보관과 문제 발생 시 원상태로 돌려놓는 작업

USE shopDB;

SELECT * FROM productTBL;

-- 데이터베이스를 SQL로 내보내기

DELETE FROM productTBL;

SELECT * FROM productTBL;

USE mysql; -- 일단 다른 DB를 선택함

-- 파일 > SQL 파일 불러오기 > 쿼리 실행

USE shopDB;
SELECT * FROM productTBL;

7. 사용자 관리
- 모든 권한

CREATE USER director@'%' IDENTIFIED BY 'director';
GRANT ALL ON *.* TO director@'%' WITH GRANT OPTION;

- 읽기 권한

CREATE USER ceo@'%' IDENTIFIED BY 'ceo';
GRANT SELECT ON *.* TO ceo@'%';

- shopDB 읽기, 쓰기 권한, employees 읽기 권한

CREATE USER staff@'%' IDENTIFIED BY 'staff';
GRANT SELECT, ALTER ROUTINE, CREATE ROUTINE, INSERT, UPDATE, DELETE ON shopDB.* TO staff@'%';
GRANT SELECT ON employees.* TO staff@'%';

- director 권한 테스트

CREATE DATABASE sampleDB;
DROP DATABASE sampleDB;

- ceo 권한 테스트
USE shopDB;
SELECT * FROM membertbl;
DELETE FROM memberTBL WHERE memberID = 'Dang';

- staff 권한 테스트

USE shopDB;
DELETE FROM memberTBL WHERE memberID = 'Sang';
SELECT * FROM memberTBL;
DROP TABLE memberTBL;

USE employees;
SELECT * FROM employees;

- 사용자 삭제
DROP USER staff;

- 사용자 목록
SELECT USER, HOST FROM USER;

- 사용자 정보 변경
ALTER USER 'director'@'localhost' IDENTIFIED BY 'kosa0401';

- 사용자 권한 보기
SHOW GRANTS FOR root@'%';
SHOW GRANTS FOR director@'%';
SHOW GRANTS FOR ceo@'%';
SHOW GRANTS FOR staff@'%';

--- SQL 명령어 실습(CLI)
1. 데이터베이스 이름, 데이블 이름, 필드 이름이 정확히 기억나지 않거나, 또는 각 이름의 철자가 확실하지 않을 때 찾아서 조회하는 방법을 실습하자. 지금 조회하고자 하는 내용이 employees 데이터베이스에 있는 employees 테이블의 first_name 및 gender 열이라고 가정한다.

- 데이터베이스 조회
SHOW DATABASES;

- 데이터베이스 지정
USE employees;

- 테이블 정보 조회
SHOW TABLE STATUS;

- employees 테이블의 열이 무엇이 있는 확인(first_name과 gender)
DESCRIBE employees; -- 또는 DESC employees;

- 데이터 조회
SELECT first_name, gender FROM employees;

2. 데이터베이스와 테이블 생성

- 데이터베이스 생성
DROP DATABASE IF EXISTS sqlDB;
CREATE DATABASE sqlDB;

- 테이블 생성
USE sqlDB;
CREATE TABLE userTbl -- 회원 테이블
(
userID CHAR(8) NOT NULL PRIMARY KEY, -- 사용자 아이디 (pK)
name VARCHAR(10) NOT NULL, -- 이름
birthYear INT NOT NULL, -- 출생년도
addr CHAR(2) NOT NULL, -- 지역(경기, 서울, 경남 식으로 2글자만 입력)
mobile1 CHAR(3), -- 휴대폰의 국번 (011, 016, 017, 018, 019, 010등)
mobile2 CHAR(8), -- 휴대폰의 나머지 번호 (하이픈제외)
height SMALLINT, -- 키
mDate DATE -- 회원 가입일
);

기본 키 (Primary Key) #
Data-Table에 있는 유일하게 구분되는 Data-Key를 기본 키(Primary Key)라 부른다.
Primary Key는 유일한 값이기 때문에 중복된 값을 가질 수 없다.
Primary Key는 공백을 가질 수 없습니다.

- 테이블 확인
DESCRIBE userTbl; -- 또는 DESC userTbl;

- 데이터 입력
INSERT INTO userTbl VALUES('LSG', '이승기', 1987, '서울', '011', '1111111', 182, '2008-8-8');
INSERT INTO userTbl VALUES('KBS', '김범수', 1979, '경남', '011', '2222222', 173, '2012-4-4');
INSERT INTO userTbl VALUES('KKH', '김경호', 1971, '전남', '019', '3333333', 177, '2007-7-7');
INSERT INTO userTbl VALUES('JYP', '조용필', 1950, '경기', '011', '4444444', 166, '2009-4-4');
INSERT INTO userTbl VALUES('SSK', '성시경', 1979, '서울', NULL , NULL , 186, '2013-12-12');
INSERT INTO userTbl VALUES('LJB', '임재범', 1963, '서울', '016', '6666666', 182, '2009-9-9');
INSERT INTO userTbl VALUES('YJS', '윤종신', 1969, '경남', NULL , NULL , 170, '2005-5-5');
INSERT INTO userTbl VALUES('EJW', '은지원', 1972, '경북', '011', '8888888', 174, '2014-3-3');
INSERT INTO userTbl VALUES('JKW', '조관우', 1965, '경기', '018', '9999999', 172, '2010-10-10');
INSERT INTO userTbl VALUES('BBK', '바비킴', 1973, '서울', '010', '0000000', 176, '2013-5-5');

- 데이터 확인
SELECT * FROM userTbl;

- 테이블 생성
CREATE TABLE buyTbl
(
num INT AUTO_INCREMENT NOT NULL PRIMARY KEY, -- 순번(PK)
userID CHAR(8) NOT NULL, -- 아이디(FK)
prodName CHAR(6) NOT NULL, -- 물품명
groupName CHAR(4), -- 분류
price INT NOT NULL, -- 단가
amount SMALLINT NOT NULL, -- 수량
FOREIGN KEY (userID) REFERENCES userTbl(userID) -- 외래 키 지정
);

외래 키 (Foreign Key) #
한 Table과 참조되는 다른 Table 간의 연결되는 Primary Key Column을 Foreign Key라 합니다.
Foreign Key는 다른 Primary Key를 참조하는 속성 또는 속성들의 집합을 의미한다.
Foreign Key는 참조관계의 기본 키와 같은 속성을 가진다.

- 테이블 확인
DESCRIBE buyTbl; -- 또는 DESC buyTbl;

- 데이터 입력
INSERT INTO buyTbl VALUES(NULL, 'KBS', '운동화', NULL , 30, 2);
INSERT INTO buyTbl VALUES(NULL, 'KBS', '노트북', '전자', 1000, 1);
INSERT INTO buyTbl VALUES(NULL, 'JYP', '모니터', '전자', 200, 1);
INSERT INTO buyTbl VALUES(NULL, 'BBK', '모니터', '전자', 200, 5);
INSERT INTO buyTbl VALUES(NULL, 'KBS', '청바지', '의류', 50, 3);
INSERT INTO buyTbl VALUES(NULL, 'BBK', '메모리', '전자', 80, 10);
INSERT INTO buyTbl VALUES(NULL, 'SSK', '책' , '서적', 15, 5);
INSERT INTO buyTbl VALUES(NULL, 'EJW', '책' , '서적', 15, 2);
INSERT INTO buyTbl VALUES(NULL, 'EJW', '청바지', '의류', 50, 1);
INSERT INTO buyTbl VALUES(NULL, 'BBK', '운동화', NULL , 30, 2);
INSERT INTO buyTbl VALUES(NULL, 'EJW', '책' , '서적', 15, 1);
INSERT INTO buyTbl VALUES(NULL, 'BBK', '운동화', NULL , 30, 2);

- 데이터 확인
SELECT * FROM buyTbl;

- sqlDB 내보내기
mysqldump -u root -p sqlDB > sqlDB.sql

- sqlDB 가져오기
CREATE DATABASE sqlDB;
USE sqlDB;
source sqlDB.sql

3. 특정 조건의 데이터만 조회

- 기본적인 WHERE절(SELECT 열(필드)이름 FROM 테이블이름 WHERE 조건식;)
USE  sqlDB;
SELECT * FROM userTbl;
SELECT * FROM userTbl WHERE name = '김경호';

- 관계 연산자의 사용
SELECT userID, Name FROM userTbl WHERE birthYear >= 1970 AND height >= 182;
SELECT userID, Name FROM userTbl WHERE birthYear >= 1970 OR height >= 182;

- BETWEEN ... AND와 IN() 그리고 LIKE
SELECT Name, height FROM userTbl WHERE height >= 180 AND height <= 183;
SELECT Name, height FROM userTbl WHERE height BETWEEN 180 AND 183;
SELECT Name, addr FROM userTbl WHERE addr='경남' OR  addr='전남' OR addr='경북';
SELECT Name, addr FROM userTbl WHERE addr IN ('경남','전남','경북');
SELECT Name, height FROM userTbl WHERE name LIKE '김%';
SELECT Name, height FROM userTbl WHERE name LIKE '_종신';

- ANY/ALL/SOME 그리고 서브쿼리(SubQUERY, 하위 커리)
SELECT Name, height FROM userTBL WHERE height  > 177;
SELECT Name, height FROM userTbl 
   WHERE height > (SELECT height FROM userTbl WHERE Name = '김경호');
SELECT Name, height FROM userTbl 
   WHERE height >= (SELECT height FROM userTbl WHERE addr = '경남');
SELECT Name, height FROM userTbl 
   WHERE height >= ANY (SELECT height FROM userTbl WHERE addr = '경남');
SELECT Name, height FROM userTbl 
   WHERE height >= ALL (SELECT height FROM userTbl WHERE addr = '경남');
SELECT Name, height FROM userTbl 
   WHERE height = ANY (SELECT height FROM userTbl WHERE addr = '경남');
SELECT Name, height FROM userTbl 
  WHERE height IN (SELECT height FROM userTbl WHERE addr = '경남');

- 원하는 순서대로 정렬하여 출력: ORDER BY
결과물에 대해 영향을 미치지는 않지만, 결과가 출력되는 순서를 조절하는 구문

SELECT Name, mDate FROM userTbl ORDER BY mDate;

SELECT Name, mDate FROM userTbl ORDER BY mDate DESC;

SELECT Name, height FROM userTbl ORDER BY height DESC, name ASC;

- 중복된 것은 하나만 남기는 DISTINCT

SELECT addr FROM userTbl;

SELECT addr FROM userTbl ORDER BY addr;

SELECT DISTINCT addr FROM userTbl;

- 출력하는 개수를 제한하는 LIMIT

USE employees;
SELECT emp_no, hire_date FROM employees 
   ORDER BY hire_date ASC;

USE employees;
SELECT emp_no, hire_date FROM employees 
   ORDER BY hire_date ASC 
   LIMIT 5 ;

- 테이블을 복사하는 CREATE TABLE ... SELECT
USE sqlDB;
CREATE TABLE buyTbl2 (SELECT * FROM buyTbl);
SELECT * FROM buyTbl2;

CREATE TABLE buyTbl3 (SELECT userID, prodName FROM buyTbl);
SELECT * FROM buyTbl3;