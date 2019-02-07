-- 모두 가져오기
SELET * FROM classmates;

-- 특정 col 가져오기
SELET id, name FROM classmates;

-- 특정 row(레코드) 의 갯수를 지정하여 가져오기
SELET * FROM classmates LIMIT 3;

-- 특정 row, col가져오기
SELET id, name FROM classmates LIMIT 2;

-- 특정 row(레코드)의 시작점을 지정하기
SELET * FROM classmates OFFSET 2;

-- 특정 row 시작점과 갯수 지정하기(중간값을 빼올 때 주로 사용)
SELET * FROM classmates LIMIT 1; OFFSET 4; --이렇게 되면 4번째 줄에 있는 값 1개만 가져오기

-- 특정 값을 가진 row만 가져오기
SELET * FROM classmates WHERE id = 2;
SELET * FROM classmates WHERE address = '서울';


-- 대전에 사는 사람의 이름은?
SELET name FROM classmates WHERE address = '대전';