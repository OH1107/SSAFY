-- DDL
CREATE TABLE classmates (
  id INTEGER PRIMARY KEY,
  name TEXT
);

DROP TABLE classmates;

CREATE TABLE classmates (
  name TEXT,
  age INTEGER,
  address TEXT
);

-- DML
INSERT INTO classmates (name, age)
VALUES ('홍길동', 23);

INSERT INTO classmates (name, age, address)
VALUES ('홍길동', 30, '서울');

INSERT INTO classmates
VALUES ('홍길동', 30, '서울');

SELECT rowid, * FROM classmates;

----
DROP TABLE classmates;

CREATE TABLE classmates (
  id PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  address TEXT NOT NULL
);

INSERT INTO classmates (name, age, address)
VALUES ('김영희', 23, '대전');

INSERT INTO classmates
VALUES (2, '홍길동', 30, '서울');

----
DROP TABLE classmates;

CREATE TABLE classmates (
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  address TEXT NOT NULL
);

INSERT INTO classmates VALUES 
  ('홍길동',30,'서울'),
  ('김철수',23,'대전'),
  ('박나래',23,'광주'),
  ('이요셉',33,'구미');

-- SELECT
SELECT * FROM classmates;

SELECT rowid, name FROM classmates;

SELECT rowid, name 
FROM classmates LIMIT 1;

SELECT rowid, name 
FROM classmates 
LIMIT 1 OFFSET 2;

SELECT rowid, name 
FROM classmates
WHERE address='서울';

SELECT DISTINCT age FROM classmates;

-- DELETE
DELETE FROM classmates
WHERE rowid=4;

INSERT INTO classmates (name, age, address)
VALUES ('최철순', 45, '서울');
  -- rowid가 4번으로 추가됨
  -- PK에 `AUTOINCREMENT` 제약조건 추가
  -- rowid가 중복없이 추가됨을 확인할 수 있음

-- UPDATE
UPDATE classmates 
SET name='홍길동', address='제주도' 
WHERE rowid=4;

-- WHERE, expressions

  -- Q. 나이가 30 이상인 사람들은?
SELECT * FROM users
WHERE age >= 30;

  -- Q. 나이가 30 이상인 사람들의 이름은?
SELECT first_name FROM users
WHERE age >= 30;

  -- Q. 나이가 30 이상이면서 김씨인 사람들의 성과 나이는?
SELECT last_name, age 
FROM users
WHERE age >= 30 AND last_name='김';

-- COUNT
  -- Q. 총 레코드 수는?
SELECT COUNT(*) FROM users;

  -- Q. 30살 이상인 사람들의 평균 나이는?
SELECT AVG(age) FROM users
WHERE age >= 30;

  -- Q. 계좌 잔액이 가장 높은 사람과 액수는?
SELECT first_name, MAX(balance) FROM users;

  -- Q. 30살 이상인 사람의 계좌 평균 잔액은?
SELECT AVG(balance) FROM users
WHERE age >= 30;

-- LIKE(wild cards)
  -- Q. 20대인 사람은?
SELECT * FROM users
WHERE age LIKE '2_';

  -- Q. 지역번호가 02인 사람은?
SELECT * FROM users
WHERE phone LIKE '02-%';

  -- Q. 이름이 '준'으로 끝나느 사람은?
SELECT * FROM users
WHERE first_name LIKE '%준';

-- ORDER BY
  -- Q. 나이순으로 오름차순 정렬하여 상위 10개만 뽑으면?
SELECT * FROM users
ORDER BY age 
LIMIT 10;

  -- Q. 나이, 성 순으로 오름차순 정렬하여 상위 10개
SELECT * FROM users
ORDER BY age, last_name
LIMIT 10;

  -- Q. 계좌잔액순으로 내림차순 정렬, 성과 이름 상위 10개
SELECT last_name, first_name FROM users
ORDER BY balance DESC
LIMIT 10;

-- GROUP BY
  -- Q. 성별로 몇명인지 출력
SELECT last_name, COUNT(*) FROM users
GROUP BY last_name;

  -- Q. as 문으로 컬럼명을 변경
SELECT last_name, COUNT(*) AS name_count
FROM users
GROUP BY last_name;

-- ALTER

CREATE TABLE articles (
  title TEXT NOT NULL,
  content TEXT NOT NULL
);

INSERT INTO articles
VALUES ('1번글', '1번내용');

ALTER TABLE articles
RENAME TO news;

ALTER TABLE news
ADD COLUMN created_at TEXT NOT NULL DEFAULT '1999-01-01';

INSERT INTO news
VALUES ('2번글', '2번내용', datetime('now'));