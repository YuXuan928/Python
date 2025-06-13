USE YSTUDENT;

-- 1. (Ms_My)
SELECT S.SNO AS 學號, T.NAME AS 姓名, Sum(S.SCORE) AS 總分, 
	format( Avg(S.SCORE),1) AS 平均
FROM STUDENT AS T INNER JOIN 
		YSCORE AS S ON T.SNO = S.SNO
GROUP BY S.SNO, T.NAME
ORDER BY Sum(S.SCORE) DESC;

-- 2. (Ms_My)
-- 方法1 92
SELECT S1.SNO AS 學號, T.NAME AS 姓名, S1.SUBJECT AS 科目, S1.SCORE AS 最高分數
FROM (SELECT SNO, Max(SCORE) AS MAX FROM YSCORE AS S2 GROUP BY SNO)  AS SS,
	    YSCORE AS S1 INNER JOIN 
		  STUDENT AS T ON S1.SNO = T.SNO
WHERE (S1.SNO=SS.SNO) AND (S1.SCORE=SS.MAX)
ORDER BY 1 ;

-- 方法2 99;
SELECT S1.SNO AS 學號, T.NAME AS 姓名, S1.SUBJECT AS 科目, S1.SCORE AS 最高分數
FROM  	YSCORE AS S1 INNER JOIN 
		STUDENT AS T using (SNO ) Join
        (SELECT SNO, Max(SCORE) AS MAX FROM YSCORE AS S2 GROUP BY SNO) SS using (sno)
WHERE (S1.SCORE=SS.MAX)
ORDER BY 1;

-- 方法3 依個人作分組之科目排名 Rank() OVER (同分同名,不連續)
SELECT 學號, 姓名, 科目, 最高成績
FROM (
		SELECT T.sno 學號, T.name 姓名, S.subject 科目,	S.score as 最高成績,
			Rank() OVER(PARTITION BY T.name ORDER BY S.score DESC) AS Rank_No
		FROM  student T	JOIN  yscore S ON T.sno = S.sno
	)SUB
WHERE Rank_no=1
ORDER BY  學號 ASC;


-- 3. (Ms_My)
-- 方法1
SELECT S1.SNO AS 學號, T.NAME AS 姓名, S1.SUBJECT AS 科目, S1.SCORE AS 最高分數
FROM (SELECT SUBJECT, Max(SCORE) AS MAX FROM YSCORE GROUP BY SUBJECT)  AS SS, 
	YSCORE AS S1 INNER JOIN 
		STUDENT AS T ON S1.SNO = T.SNO
WHERE (S1.SUBJECT=SS.SUBJECT) And (S1.SCORE=SS.MAX)
ORDER BY 4 DESC;

-- 方法2 使用 CTE
WITH SS (科目,成績) AS
(SELECT SUBJECT,MAX(SCORE) AS 成績 FROM YSCORE GROUP BY SUBJECT)
-- select * from SS;
SELECT S1.SNO 學號, T.NAME 姓名, SS.科目, SS.成績 最高成績
FROM SS JOIN YSCORE S1 ON SS.科目=S1.SUBJECT
		JOIN STUDENT T ON S1.SNO=T.SNO
WHERE  S1.SCORE=SS.成績
ORDER BY 3 DESC;


-- 4. (Ms_My)
-- 方法1 
select sc1.sno AS 學號,st.name as 姓名, sc1.subject as 科目,sc1.score as 分數
  from yscore sc1 inner join student st on sc1.sno=st.sno
  where (select count(distinct score) from yscore sc2 where sc2.subject=sc1.subject
          and sc2.score>=sc1.score)<3
  order by sc1.subject desc ,sc1.score desc;

-- 方法2 使用 RANK() OVER + 子查詢
SELECT 學號, 姓名, 科目, 最高分數 
FROM(
	SELECT S1.SNO AS 學號, T.NAME AS 姓名, S1.SUBJECT AS 科目, S1.SCORE AS 最高分數, 
		RANK() OVER (PARTITION BY S1.SUBJECT ORDER BY S1.SUBJECT, S1.SCORE DESC) 排名
	FROM YSCORE AS S1 INNER JOIN 
		 STUDENT AS T ON S1.SNO = T.SNO ) SUB
WHERE 排名 < 3
order by 3 DESC, 4 DESC;

-- 方法3 使用 RANK() OVER + CTE
with CTE4 (學號, 姓名, 科目, 最高分數, 排名)
as (
	SELECT S1.SNO AS 學號, T.NAME AS 姓名, S1.SUBJECT AS 科目, S1.SCORE AS 最高分數, 
		RANK() OVER (PARTITION BY S1.SUBJECT ORDER BY S1.SUBJECT, S1.SCORE DESC) 排名
	FROM YSCORE AS S1 INNER JOIN 
		 STUDENT AS T ON S1.SNO = T.SNO 
	) 
select * from CTE4
WHERE 排名 < 3
order by 3 DESC, 4 DESC;


-- 5. IIF(Ms) 改成 IF(My) 
-- 方法 1 使用 if
SELECT 學號, 姓名, 國文, 數學, 英文, 國文+數學+英文 AS 總分, CAST((國文+數學+英文)/3.0 as decimal(5,1) ) AS 平均
FROM
(SELECT S.SNO AS 學號, T.NAME AS 姓名, 
	SUM(IF(SUBJECT='國文',SCORE,0)) AS 國文, 
	SUM(IF(SUBJECT='數學',SCORE,0)) AS 數學,
	SUM(IF(SUBJECT='英文',SCORE,0)) AS 英文
	FROM STUDENT AS T INNER JOIN 
		YSCORE AS S ON T.SNO = S.SNO 
GROUP BY S.SNO, T.NAME ) AS SUB
ORDER BY 6 DESC;

-- 方法2 使用 case when
SELECT 學號, 姓名, 國文, 數學, 英文,國文+數學+英文 AS 總分,  CAST((國文+數學+英文)/3.0 as decimal(5,1) ) AS 平均 
FROM
	(SELECT S.SNO AS 學號, T.NAME AS 姓名, 
		SUM(CASE 
			WHEN SUBJECT = '國文' THEN (SCORE)	ELSE 0
		END) AS 國文, 
		SUM(CASE 
			WHEN SUBJECT ='數學' THEN (SCORE)	ELSE 0
		END) AS 數學, 
		SUM(CASE 
			WHEN SUBJECT ='英文' THEN (SCORE)	ELSE 0
		END) AS 英文 
	 FROM STUDENT AS T INNER JOIN 
		YSCORE AS S ON T.SNO = S.SNO 
	 GROUP BY S.SNO, T.NAME
	)AS SUB
ORDER BY 6 DESC;


-- 6. (Ms_My)
SELECT S.SUBJECT AS 科目, format(Avg(S.SCORE),1) AS 科目平均 
FROM YSCORE AS S 
GROUP BY S.SUBJECT
ORDER BY S.SUBJECT;


-- 7.1 方法一  (My) (MariaDB現在支援CTE 。MySql8.0版之前不支援)
-- 方法1 先取所有學生英文(子查詢)，再作排名
SELECT *, RANK() OVER( ORDER BY SUB.英文 DESC) AS 排名
FROM 
  (SELECT S.SNO AS 學號, T.NAME AS 姓名, SUM(IF(SUBJECT='英文',SCORE,0)) AS 英文
		FROM STUDENT AS T INNER JOIN YSCORE AS S ON T.SNO = S.SNO
		GROUP BY S.SNO, T.NAME)  AS SUB
ORDER BY 3 DESC, 1 ;

-- 7.2 方法二 使用 RANK() OVER 排名
SELECT S1.SNO AS 學號, T.NAME AS 姓名,  S1.SCORE AS 英文, 
	RANK() OVER ( ORDER BY S1.SCORE DESC) 排名
FROM YSCORE AS S1 INNER JOIN 
	 STUDENT AS T ON S1.SNO = T.SNO 
where SUBJECT="英文" 
ORDER BY 3 DESC, 1 ;

-- 7.3 方法三 CTE+自排名
WITH CTE7 (學號, 姓名, 英文)
AS	(SELECT T.SNO, NAME,   SCORE as 英文 
		 FROM STUDENT T inner join YSCORE S ON T.SNO = S.SNO
		 WHERE      SUBJECT = '英文'
	)
SELECT *, (SELECT COUNT(*) FROM CTE7 WHERE  英文>SUB2.英文)+1 AS 排行
FROM CTE7 SUB2 
ORDER BY 3 DESC, 1 ;


-- 7.4 方法三 (My) (使用@rank變數) 使用變數排名 (Rank() Over)
-- http://fellowtuts.com/mysql/query-to-obtain-rank-function-in-mysql/
SELECT sno 學號,  st.name 姓名, score 英文, rank1 排名
from (
		select sc1.sno , sc1.score ,
			@rank :=IF( @temp_score = score, @rank, @rank_incr ) rank1 , 
            -- 同分同名次,其他(較小)名次使用已加1的預設名次@rank_incr
			@rank_incr := @rank_incr + 1,	-- 下一個名次(同分與否，預設名次@rank_incr皆加1
			@temp_score := score 			-- 當前分數指派給@temp_score
		FROM yscore sc1,
			(SELECT @rank := 0, @temp_rank := NULL,@rank_incr := 1 ) q -- 初始化3個變數 
		WHERE sc1.subject="英文"
		order by sc1.score desc
     )sub 							-- 本段Table sub 內有 sc1, q, 
     join student st using (sno)	-- 本段 sub join st
where  sub.sno=st.sno
order by 3 DESC, 1;

-- 8. (Ms_My)
-- 方法1 
select sc1.sno AS 學號,st.name as 姓名, sc1.subject as 科目,sc1.score as 分數
from yscore sc1 inner join student st on sc1.sno=st.sno
where (select count(distinct score) from yscore sc2 where sc2.subject=sc1.subject
					and sc2.score>=sc1.score)>1 
    and (select count(distinct score) from yscore sc2 where sc2.subject=sc1.subject
					and sc2.score>=sc1.score)<4 
    and  sc1.subject='數學'    
order by sc1.score desc;  

-- 方法2 使用 Rank() Over 
SELECT *
FROM (
	SELECT  SC1.SNO 學號,ST.NAME 姓名,SUBJECT AS 科目, SC1.SCORE 分數, RANK() OVER(order by sc1.SCORE DESC) 排名
	FROM YSCORE SC1 INNER JOIN STUDENT ST
	ON SC1.SNO = ST.SNO
	WHERE SUBJECT = '數學'  
	) SUB
WHERE  排名>1 AND  排名<4
ORDER BY 1;

-- 方法3 使用 CTE + RANK() OVER
with CTE8 ( 學號, 姓名, 科目, 分數, 排名 )
as (
	SELECT  SC1.SNO 學號,ST.NAME 姓名,SUBJECT AS 科目, SC1.SCORE 分數, RANK() OVER(order by sc1.SCORE DESC) 排名
	FROM YSCORE SC1 INNER JOIN STUDENT ST
	ON SC1.SNO = ST.SNO
	WHERE SUBJECT = '數學'  
	)
select * from CTE8    
WHERE  排名 between 2 and 3  -- (同) 排名>1 AND  排名<4 
ORDER BY 1;


-- 9. (Ms_My) 
-- 方法1 子查詢當欄位值
SELECT S.SUBJECT AS 科目, 
	(SELECT COUNT(*)  FROM YSCORE WHERE SUBJECT=S.SUBJECT AND SCORE<60  ) AS 不及格,
	(SELECT COUNT(*)  FROM YSCORE WHERE SUBJECT=S.SUBJECT AND SCORE>=60 AND SCORE<81 ) AS 良好,
	(SELECT COUNT(*)  FROM YSCORE WHERE SUBJECT=S.SUBJECT AND SCORE>=81 AND SCORE<=100 ) AS 優秀
FROM STUDENT AS T INNER JOIN
	 YSCORE AS S ON T.SNO = S.SNO
GROUP BY S.SUBJECT
ORDER BY S.SUBJECT ;

-- 方法2  sum(iif.., .., ..)
SELECT
	SUBJECT AS 科目,
	SUM(if(SCORE BETWEEN  0 AND  59, 1 ,0) ) AS '不及格',
	SUM(if(SCORE BETWEEN 60 AND  80, 1 ,0) ) AS '良好',
	SUM(if(SCORE BETWEEN 81 AND 100 ,1 ,0) ) AS '優秀'
FROM YSCORE
GROUP BY SUBJECT
ORDER BY 1;

-- 方法3 使用 case when
SELECT
	SUBJECT AS 科目,
	SUM(CASE WHEN SCORE BETWEEN 0 AND 59 THEN 1 ELSE 0 END) AS '不及格',
	SUM(CASE WHEN SCORE BETWEEN 60 AND 80 THEN 1 ELSE 0 END) AS '良好',
	SUM(CASE WHEN SCORE BETWEEN 81 AND 100 THEN 1 ELSE 0 END) AS '優秀'
FROM YSCORE
GROUP BY SUBJECT
ORDER BY 1;

-- 10.1 方法一 (Ms_My)
SELECT S.SNO AS 學號, T.NAME AS 姓名, SCORE AS 數學
   FROM STUDENT AS T 
	INNER JOIN YSCORE AS S ON T.SNO = S.SNO 
   WHERE SUBJECT='數學' AND RIGHT(S.SNO,1)  IN (2,5,6,9)
   ORDER BY S.SNO ASC;

-- 10.2 方法二 (Ms_My)
SELECT 學號, 姓名, 數學
FROM
 (SELECT S.SNO AS 學號, T.NAME AS 姓名, SCORE AS 數學 FROM STUDENT AS T 
	INNER JOIN YSCORE AS S ON T.SNO = S.SNO  WHERE SUBJECT='數學')  AS SUB
WHERE  RIGHT(學號,1)  IN (2,5,6,9)
ORDER BY 學號 ;


--10.2 方法二 (Ms_My)
SELECT 學號, 姓名, 數學
FROM
 (SELECT S.SNO AS 學號, T.NAME AS 姓名, SCORE AS 數學 FROM STUDENT AS T 
	INNER JOIN YSCORE AS S ON T.SNO = S.SNO  WHERE SUBJECT='數學')  AS SUB
WHERE  RIGHT(學號,1)  IN (2,5,6,9)
ORDER BY 學號 ;


-- 10.3 方法三 (Ms_My)
with CTE10 (學號, 姓名, 數學)
as (SELECT S.SNO AS 學號, T.NAME AS 姓名, SCORE AS 數學 FROM STUDENT AS T 
	INNER JOIN YSCORE AS S ON T.SNO = S.SNO  
	WHERE SUBJECT='數學'
	) 
select * from CTE10
WHERE  RIGHT(學號,1)  IN (2,5,6,9)
ORDER BY 學號 ;


-- 11.1 方法一 IIF(Ms) 改 IF(My) 
SELECT S.SNO AS 學號, T.NAME AS 姓名, 
	SUM(IF(SUBJECT='國文',SCORE,0)) AS 國文, 
	SUM(IF(SUBJECT='數學',SCORE,0)) AS 數學,
	SUM(IF(SUBJECT='英文',SCORE,0)) AS 英文, 
	FORMAT( (SUM(IF(SUBJECT='國文',SCORE,0))+SUM(IF(SUBJECT='數學',SCORE,0))
		+SUM(IF(SUBJECT='英文',SCORE,0)))/3.0 ,2) AS 平均
FROM STUDENT AS T INNER JOIN
	 YSCORE AS S ON T.SNO = S.SNO
GROUP BY S.SNO, T.NAME
HAVING SUM(IF(SUBJECT='國文',SCORE,0))>=60 AND  
		SUM(IF(SUBJECT='數學',SCORE,0))>=60 AND 
		SUM(IF(SUBJECT='英文',SCORE,0)) >=60

UNION

SELECT '總平均', COUNT(*) ,NULL, NULL, NULL, CAST( SUM(SUB.平均)*1.0/COUNT(*) AS decimal (5,2))
FROM 
(
	SELECT S.SNO AS 學號, T.NAME AS 姓名, 
		SUM(IF(SUBJECT='國文',SCORE,0)) AS 國文, 
		SUM(IF(SUBJECT='數學',SCORE,0)) AS 數學, 
		SUM(IF(SUBJECT='英文',SCORE,0)) AS 英文, 
		CAST((SUM(IF(SUBJECT='國文',SCORE,0))+SUM(IF(SUBJECT='數學',SCORE,0))
			+SUM(IF(SUBJECT='英文',SCORE,0)))/3.0 AS decimal(5,2)) AS 平均
	FROM STUDENT AS T INNER JOIN 
		YSCORE AS S ON T.SNO = S.SNO
	GROUP BY S.SNO, T.NAME
	 HAVING SUM(IF(SUBJECT='國文',SCORE,0))>=60 AND  
	 		SUM(IF(SUBJECT='數學',SCORE,0))>=60 AND 
	 		SUM(IF(SUBJECT='英文',SCORE,0)) >=60 
) AS SUB
ORDER BY 1;


-- 11.2 方法二 
SELECT 學號, 姓名, 國文, 數學, 英文,  FORMAT((國文+數學+英文)/3,2) 平均
FROM 
(
	SELECT S.SNO AS 學號, T.NAME AS 姓名, 
		SUM(IF(SUBJECT='國文',SCORE,0)) AS 國文, 
		SUM(IF(SUBJECT='數學',SCORE,0)) AS 數學,
		SUM(IF(SUBJECT='英文',SCORE,0)) AS 英文 
        
	FROM STUDENT AS T INNER JOIN
		YSCORE AS S ON T.SNO = S.SNO
	GROUP BY S.SNO, T.NAME
    ) SUB
WHERE 國文>=60 AND 數學>=60 AND 英文>=60 

UNION	
SELECT '總平均', COUNT(*) ,NULL, NULL, NULL, FORMAT(SUM(FORMAT((國文+數學+英文)/3,2))/COUNT(*) ,2) 平均 
FROM 
(
	SELECT S.SNO AS 學號, T.NAME AS 姓名, 
		SUM(IF(SUBJECT='國文',SCORE,0)) AS 國文, 
		SUM(IF(SUBJECT='數學',SCORE,0)) AS 數學,
		SUM(IF(SUBJECT='英文',SCORE,0)) AS 英文 
        
	FROM STUDENT AS T INNER JOIN
		YSCORE AS S ON T.SNO = S.SNO
	GROUP BY S.SNO, T.NAME
    ) SUB2
WHERE 國文>=60 AND 數學>=60 AND 英文>=60 

ORDER BY 1;


-- 11.3 方法三
WITH CTE11 (學號, 姓名, 國文, 數學, 英文, 平均)
AS (
	SELECT 學號, 姓名, 國文, 數學, 英文, format((國文+數學+英文)/3.0, 2) AS 平均
	FROM
		(SELECT S.SNO AS 學號, T.NAME AS 姓名, 
			SUM(IF(SUBJECT='國文',SCORE,0)) AS 國文, 
			SUM(IF(SUBJECT='數學',SCORE,0)) AS 數學,
			SUM(IF(SUBJECT='英文',SCORE,0)) AS 英文
		FROM STUDENT AS T INNER JOIN 
			YSCORE AS S ON T.SNO = S.SNO 
		GROUP BY S.SNO, T.NAME 
        ) AS SUB
	Where  國文>59 AND 數學>59 AND 英文>59
	)

SELECT * FROM CTE11 
union	-- -- 暫存表只能開啟一次，不能使用union開同一個暫存表，但CTE可以。
select '總平均', COUNT(*), null, null, null , format(avg(平均),2)
from CTE11 ;

-- 11.方法4 建立暫時資料表
-- drop table temp11 
CREATE TEMPORARY TABLE temp11 AS
	SELECT 學號, 姓名, 國 國文, 數 數學, 英 英文, (國+數+英)/3.0 平均  -- format((國文+數學+英文)/3.0, '0.00') AS 平均
	FROM
	(SELECT S.SNO AS 學號, T.NAME AS 姓名, 
		SUM(IF(SUBJECT='國文',SCORE,0)) AS 國, 
		SUM(IF(SUBJECT='數學',SCORE,0)) AS 數,
		SUM(IF(SUBJECT='英文',SCORE,0)) AS 英
		FROM STUDENT AS T INNER JOIN 
			YSCORE AS S ON T.SNO = S.SNO 
		
		GROUP BY S.SNO, T.NAME 
    ) AS SUB
    Where  國>59 AND 數>59 AND 英>59;

select ifnull(學號,'總平均')學號, if(學號 is null, null, 姓名)姓名, 
	if(學號 is null, null, 國文)國文, if(學號 is null, null, 數學)數學, 
    if(學號 is null, null, 英文)英文, format(avg(平均),2)
from temp11  -- 暫存表只能開啟一次，不能使用union開同一個暫存表，但CTE可以。
group by 學號 with RollUp


-- 11.方法5 CTE + with Rollup + 各科平均
WITH CTE11 (學號, 姓名, 國文, 數學, 英文, 平均)
AS (
	SELECT 學號, 姓名, 國文, 數學, 英文, format((國文+數學+英文)/3.0, 2) AS 平均
	FROM
		(SELECT S.SNO AS 學號, T.NAME AS 姓名, 
			SUM(IF(SUBJECT='國文',SCORE,0)) AS 國文, 
			SUM(IF(SUBJECT='數學',SCORE,0)) AS 數學,
			SUM(IF(SUBJECT='英文',SCORE,0)) AS 英文
		FROM STUDENT AS T INNER JOIN 
			YSCORE AS S ON T.SNO = S.SNO 
		GROUP BY S.SNO, T.NAME 
        having  國文>59 AND 數學>59 AND 英文>59
        ) AS SUB
	)
select ifnull(學號, '科平均') 學號, if(學號 is null, null, 姓名)姓名, 
	format(avg(國文),1)國文, format(avg(數學),1)數學, format(avg(英文),1)英文, format(avg(平均),2) 平均 from CTE11
group by 學號 with Rollup ;

-- 12.1 自排序Rank() Over() 
-- 方法1 使用 CTE + 自排名
WITH SUB (學號, 姓名, 國文)
AS	(SELECT S.SNO AS 學號, T.NAME AS 姓名, SUM(IF(SUBJECT='國文',SCORE,0)) AS 國文
	FROM STUDENT AS T INNER JOIN YSCORE AS S ON T.SNO = S.SNO
	GROUP BY S.SNO, T.NAME
	)
SELECT * , (SELECT COUNT(*) FROM SUB WHERE  國文>SUB2.國文)+1 AS 排行
FROM SUB SUB2 
-- where 學號 = ('1002')
ORDER BY 3 DESC, 1 ;

-- 方法2 使用 變數排名
-- 12.2 RANK() (My) [本題套用第7題作科目更改，並且條件設學號為 1002 ]
SELECT  學號,  name as 姓名, 分數, rank1 as 排名 
FROM
  (SELECT p.sno as 學號, subject as 科目, score as 分數,
		@curRank := IF(@prevRank = score, @curRank, @incRank) AS rank1,
		@incRank := @incRank + 1, 
		@prevRank := score
	FROM yscore p ,
 (SELECT @curRank :=0, @prevRank := NULL, @incRank := 1) r  
	 WHERE p.subject='國文' ORDER BY score desc) s, 
	student t
WHERE 學號=t.sno   -- and 學號="1002"  
order by 3 DESC;

-- 12.3 使用 子查詢 RANK() OVER
SELECT SNO AS 學號,  NAME AS 姓名,  SUBJECT AS 科目,  RANK1 AS 排名
FROM 
    ( SELECT T.SNO, NAME,  SUBJECT,  SCORE,  RANK() OVER (ORDER BY SCORE DESC) AS RANK1
    FROM STUDENT T inner join YSCORE S ON T.SNO = S.SNO
    WHERE  SUBJECT = '國文'
	) as Sub
WHERE SNO = '1002';


-- 13.1 (使用7.3 加科目及條件)
-- 方法1 使用 變數排名
SELECT sub.sno 學號,  st.name 姓名, '英文' 科目, score 英文, rank1 排名
from (
	select sc1.sno , sc1.score ,
		@rank :=IF( @temp_score = score, @rank, @rank_incr ) rank1 , 
		@rank_incr := @rank_incr + 1,
		@temp_score := score 
	FROM yscore sc1,
		(SELECT@rank := 0,@temp_rank := NULL,@rank_incr := 1 ) q 
	WHERE sc1.subject="英文"
	order by sc1.score desc
     )sub , student st 
where  sub.sno=st.sno -- and  rank1>1 AND rank1<5 
order by 4 DESC; -- rank1;

-- 方法2 使用RANK() OVER+子查詢
select SNO 學號, NAME 姓名, '英文' as 科目, 分數, 排名 from 
(
SELECT T.SNO, NAME,   SCORE as 分數,  RANK() OVER (ORDER BY SCORE DESC) AS 排名
    FROM STUDENT T inner join YSCORE S ON T.SNO = S.SNO
    WHERE      SUBJECT = '英文' 
	) as Sub
where 排名>1 AND 排名<5
order by 5;

-- 方法3 使用RANK() OVER+CTE (CTE MySql8.0版之前不支援, MariaDb支援)
WITH SUB (學號, 姓名, 科目, 分數, 排名)
AS (
SELECT T.SNO, NAME, SUBJECT, SCORE as 分數,  RANK() OVER (ORDER BY SCORE DESC) AS 排名
    FROM STUDENT T inner join YSCORE S ON T.SNO = S.SNO
    WHERE  SUBJECT = '英文' 
   ) 
select 學號, 姓名, 科目, 分數, 排名 from SUB
where 排名 in (2,3,4);

-- 方法4 建立暫時資料表
CREATE TEMPORARY TABLE temp13 AS
select 學號, 姓名, 科目, 分數, 排名 
From (
SELECT T.SNO 學號, NAME 姓名, SUBJECT 科目, SCORE as 分數,  RANK() OVER (ORDER BY SCORE DESC) AS 排名
    FROM STUDENT T inner join YSCORE S ON T.SNO = S.SNO
    WHERE  SUBJECT = '英文' 
   ) sub
where 排名 in (2,3,4);
-----------------------
select * from temp13 



