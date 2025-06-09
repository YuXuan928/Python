use f1180024;
select * from customer
where 行業別='機械' and (縣市='台北市' or '縣市'='台中市') ;


SELECT * FROM CUSTOMER
WHERE 客戶寶號 LIKE '%電機%';

SELECT *
FROM EMPLOYEE
WHERE 姓名 LIKE '林%' OR 姓名 LIKE '陳%';

SELECT *
FROM EMPLOYEE
WHERE 姓名 regexp '^[林陳]';

SELECT * 
FROM EMPLOYEE
WHERE 縣市 NOT LIKE '台北%' AND 現任職稱 LIKE '%工程師'  AND 目前月薪資>=35000;

SELECT *
FROM EMPLOYEE
ORDER BY 目前月薪資 DESC
limit 10;

SELECT *
FROM EMPLOYEE
ORDER BY 目前月薪資 ASC
limit 10;

SELECT CEIL(COUNT(*) * 0.10) AS limit_count
FROM EMPLOYEE;


SELECT *
FROM EMPLOYEE
ORDER BY 目前月薪資 DESC
LIMIT 10;

select  縣市, Count(*) `家數` 
from Customer 
group by 縣市
order by  縣市;

select 縣市 , concat(LEFT(姓名,1) , 'O' , RIGHT(姓名,1)) AS 姓名 
FROM EMPLOYEE
where 縣市='台北市';

select  姓名 , concat(LEFT(身分證號碼,2) , '******' , RIGHT(身分證號碼,2)) AS 身分證號碼 , 畢業國中 
from students
where 畢業國中 like '南投縣%';

SELECT 客戶代號 , 客戶寶號 , 客戶代號 as 交易客戶代號
from customer
where 客戶代號 not in (
select 客戶代號
from sales
where 交易年 = 90)
ORDER BY 客戶代號 ASC;

select 學號, 姓名, date_format( 出生年月日 ,'%m-%d') as 生日,  MONTH(出生年月日) as 出生月
from students
where month(出生年月日) = 3
order by month(出生年月日) desc;



