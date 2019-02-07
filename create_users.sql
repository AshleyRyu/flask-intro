CREATE TABLE users  (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    age INT,
    country TEXT,
    phone TEXT ,
    balance INT 
);

-- 컬럼명 표기
.headers on

-- 표처럼 표기
.mode column