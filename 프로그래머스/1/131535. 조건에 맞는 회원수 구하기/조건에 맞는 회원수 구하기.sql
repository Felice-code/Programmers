-- 코드를 입력하세요
SELECT COUNT(1)
FROM USER_INFO 
WHERE DATE_FORMAT(JOINED,'%Y') = 2021 AND AGE BETWEEN 20 AND 29