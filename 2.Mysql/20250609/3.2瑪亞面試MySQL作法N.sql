use MaDb;
-- 職位：CLERK 秘書、SALESMAN 售貨員、MANAGER 經理、ANALYST 分析師、PRESIDENT 負責人
-- 定義：所有員工＝所有僱員；　辦事員：(不含負責人、經理)

-- 1. 列出薪資低於40000的所有員工
select * from Emp where sal<40000;

-- 02. 列出部門30中的所有雇員 
select * from Emp where DeptNo=30;

-- 03. 列出所有辦事員的姓名、編號和部門 (不含負責人、經理)
select ENAME 姓名, EMPNO 員工編號, DNAME 部門名稱 from Emp E inner join Dept D on E.DeptNo=D.DeptNO 
	 where JOB<>'PRESIDENT' and JOB!='MANAGER';

# 04. 找出佣金高於(超過)薪資的雇員
select * from Emp where  COMM>SAL ;

# 05. 找出佣金高於(超過)薪資的60%之雇員
select * from Emp where  COMM>SAL*0.6;

-- 06. 找出部門10中所有經理
select * from Emp where DeptNo=10 and JOB='MANAGER';

-- 07. 找出部門20中不是經理但是薪資大於80000的所有僱員資料
select * from Emp where DeptNo=20 and JOB<>'MANAGER' and SAL>80000;

-- 08. 找出有收到佣金的雇員及其職務
select Ename 姓名, JOB 職務, COMM 傭金 from Emp where  COMM>0;

-- 09. 找出不收取佣金或者佣金小於300的僱員
select * from Emp where COMM<12000 or COMM is null;

-- 10. 找出到職日大於13年以上僱員 
select *, Date_Add(HIREDATE, INTERVAL 13 year) from Emp where Date_Add(HIREDATE, INTERVAL 13 year)<now() ;	
/*
#但如果題目MILLER的生日是1984-03-02；計算日期「now()」是去年2024-02-29 則使用 datediff(...)會有問題
select *, Date_Add(HIREDATE, INTERVAL 13 year) from Emp where Date_Add(HIREDATE, INTERVAL 13 year)<'2024/02/29';	
 */

-- 11. 找出早於2012年以前到職員工
select * from Emp where HIREDATE<cast('2012/01/01' as date);	
-- SELECT * FROM Emp WHERE YEAR(HIREDATE)<2012;		-- 同上

-- 12. 找出姓名為五個字的員工
select * from Emp  where Length(EName)=5;
-- select * from Emp where ename like '_____' 		-- 同上

-- 13. 找出僱員姓名中不帶有"A"的員工
select EMPNO 員工編號, Ename 姓名不帶A from Emp E  where EName not like '%A%' ;

-- 14.(1) 顯示所有僱員姓名的前三個字元
--    (2) 顯示所有僱員姓名的前三個字元，其餘字數使用’*’替代，以符合個資保護作法。
-- 14.1作法
select  EName 姓名, SubString(EName,1,3) 前3字元 from Emp ; 
select  EName 姓名, LEFT(EName,3) 前3字元 from Emp ;			-- 同上
-- 14.2作法
select  EName 姓名, concat(LEFT(EName,3), rpad('',Length(Ename)-3,'*'))  姓名2 from Emp; -- 3碼後補'*'

-- 15. 顯示"SALESMAN"銷售員的姓名，第一個字替換成"B"
select Ename 原姓名, Replace(EName,Left(EName,1), 'B') 調整後姓名, 
 JOB 職務 from Emp where JOB='SALESMAN';
-- select Ename 原姓名, CONCAT('B',SubString(EName,2,Length(Ename)-1)) 調整後姓名, 
-- JOB 職務 from Emp where JOB='SALESMAN';

-- 16. 顯示僱員的詳細資料，按照姓名排序(由小而大)
select  * from Emp Order by EName;

-- 17. 顯示僱員姓名，按照到職日進行排序，將最老的僱員排列在最前面
select  ENAme 姓名, HIREDATE 到職日 from Emp Order by HIREDATE; -- 因為沒有生日欄位，僅依到職日;

-- 18. 顯示所有僱員的姓名，職務，跟薪資，按照職務降序排列，職務相同時按薪資升序排列
select  ENAme 姓名, JOB 職務, SAL 薪資  from Emp  order by 2 DESC, 3 ; -- Order by JOB DESC, SAL ;

-- 19. 顯示所有僱員一個月以30天為情況下計算僱員日薪
select  ENAme 姓名, SAL 薪資, CAST(SAL/30 as decimal(6,1) ) as 日薪  from Emp ;
SELECT ENAME 姓名, SAL 薪資, FORMAT((SAL/30),1) 日薪 from Emp;	-- 同上

-- 20. 找出不含傭金最高薪資員工名稱。
-- 方法一
select  Ename 姓名, SAL 薪資  from Emp order by SAL DESC limit 1; 	
-- 方法二
select E1.Ename 姓名, SAL 薪資 from Emp E1
	where  E1.sal =  (select Max(sal) from Emp );
-- 方法三
select E1.Ename 姓名, SAL 薪資 from Emp E1, (select Max(sal) Max from Emp) E2
where  E1.sal = E2.Max ;

-- 21. 找出不限制年份，二月受聘的所有僱員
select Ename 姓名, HireDate 到職日 from Emp where month(HIREDATE)=2 ; 

-- 22.顯示所有僱員，從到職日至現在的天數 (到職天數遞減)
select  ENAme 姓名,HireDate 到職日, DATEDIFF(now(), HireDate) 到職天數 from Emp  order by 3 DESC;

-- 23. 查詢姓名中有C的僱員
select EMPNO 員工編號, Ename 姓名有C僱員 from Emp where EName like '%C%' ;

-- 24. 請列出最少有一個僱員的所有部門
select  D.DeptNO 部門編號, DNAME 部門名稱 , E.人數
	from  Dept D 
	inner join (select DEPTNO,Count(*) 人數 from Emp  Group by DEPTNO ) E
    on D.DEPTNO=E.DEPTNO;

-- 25. 列出薪資比SMITH還多的所有僱員(依部門編號排序 ASC)
select DEPTNO 部門編號, ENAME 姓名 ,SAL 薪資  from Emp
where SAL>(select E2.SAL from Emp as E2 where Ename='SMITH')
order by deptno ;
/* 將SMITH的資料列於末列
SELECT LEFT(DEPTNO,4) 部門編號, ENAME 姓名 ,SAL 薪資 
FROM Emp E WHERE SAL > (SELECT SAL FROM Emp WHERE ENAME='SMITH') 
UNION 
SELECT 'SMITH', '薪資',  SAL 薪資  FROM Emp WHERE ENAME='SMITH'	
ORDER BY 部門編號;
*/


-- 26. 列出僱員的姓名與上級主管姓名
select E1.Ename as 僱員,E2.Ename as 主管 from Emp E1 Inner join Emp E2 on  E1.MGR=E2.EMPNO ;

-- **如無主管也要列出(使用left)
select E1.Ename as 姓名,E2.Ename as 主管 from Emp E1 left join Emp E2 on  E1.MGR=E2.EMPNO; 

-- 27. 列出到職日早於上級主管的所有僱員
select E1.Ename 僱員, E1.HireDate 到職日, E2.Ename as 主管, E2.HireDate 到職日 from Emp E1
       Inner join (select Empno,ENAME, Hiredate from Emp) as E2
       on E1.MGR=E2.EMPNO where  E1.HIREDATE<E2.HIREDATE; 
/*方法2
select E1.Ename 僱員, E1.HireDate 到職日, E2.Ename as 主管, E2.HireDate 到職日 
from Emp E1 JOIN Emp E2 ON E1.MGR=E2.EMPNO WHERE E1.HIREDATE<E2.HIREDATE;
*/

-- 28. 列出所有職務為"CLERK"的姓名與其部門名稱
select  Ename 姓名, JOB 職務, DNAME 部門名稱 
from Emp E inner join Dept D on E.DeptNo=D.DeptNO 
where E.JOB='CLERK'; 

-- 29.1 列出各種工作類別的最低薪資(按照職務排序 由小而大)
select JOB 職務, Min(SAL) 最低薪 from Emp group by JOB
	order by 1;
	   
	   
-- 29.2 列出各種工作類別最低薪資的僱員(排序同上)		//如果使用顧員，則會有同一職務，多人同薪的情況
-- 方法一
select E1.JOB 職務, E1.Ename as 僱員, E2.MinSal 最低薪 from Emp E1 , 
       (select JOB, Min(SAL) MinSal from Emp group by JOB) as E2
where  E1.JOB=E2.JOB and E1.SAL=E2.MinSal 
order by 1;
-- 方法二
select E2.職務, E1.Ename as 僱員, E2.最低薪
from   (select JOB 職務, Min(SAL) 最低薪 from Emp group by JOB)  as E2
	inner join Emp E1 on E1.JOB=E2.職務 and E1.SAL=E2.最低薪
order by 1;

-- 方法三
SELECT E2.JOB 職務, E1.Ename 僱員, E1.SAL 最低薪
FROM Emp E1 JOIN (SELECT JOB,MIN(SAL) MIN FROM Emp GROUP BY JOB) E2 
			ON E1.JOB=E2.JOB AND E1.SAL=E2.MIN
order by 1;

-- 30. 列出跟"SCOTT"員工做相同工作的所有僱員(不含"SCOTT")
-- 方法一
select E1.Ename as 僱員,E1.JOB 職務 from Emp E1 
       inner join (select JOB from Emp where Ename='SCOTT') as E2
	   on E1.JOB=E2.JOB 
	   where E1.JOB=E2.JOB and E1.EName<>'SCOTT';
-- 方法二
SELECT E1.Ename as 僱員,E1.JOB 職務 FROM Emp E1 
WHERE E1.ENAME<>'SCOTT' AND JOB= (SELECT JOB FROM Emp WHERE ENAME='SCOTT');


-- 31. 列出某些雇員的姓名和薪資，條件是他們的薪資等於部門30中任何一個僱員的薪資
-- 方法一
select  DISTINCT E1.Ename as 僱員,E1.SAL 薪資 from Emp E1 
       inner join (select SAL from Emp where DeptNo=30) as E2
	   on E1.SAL=E2.SAL ;

-- 方法二子查詢使用Group By，就不需有DISTINCT 	   
select  E1.Ename as 僱員, E1.SAL 薪資 from Emp E1 
       inner join (select SAL from Emp where DeptNo=30 GROUP BY SAL) as E2
	   on E1.SAL=E2.SAL;	 

-- 方法三
SELECT E1.Ename as 僱員,E1.SAL 薪資 FROM Emp E1 
WHERE SAL IN (SELECT SAL FROM Emp WHERE DEPTNO=30) ;


-- 32. 列出有雇員的部門之訊息與該部門中共有多少僱員數量
-- 方法一
select D.DEPTNO 部門編號, Dname 部門名稱, LOC 區域, E.人數 from Dept D
		inner join (select DEPTNO,Count(*) 人數 from Emp Group by DEPTNO ) as E
	    on D.DEPTNO=E.DEPTNO ;
-- 方法二        
select D.DEPTNO 部門編號, Dname 部門名稱, LOC 區域, COUNT(empno) 人數 
	from Dept D   inner join Emp E  on D.DEPTNO=E.DEPTNO  
    Group by D.DEPTNO, Dname, LOC ;  -- 同Group by 部門編號, 部門名稱, 區域 ; MSSQL則不能

-- 33. 列出所有僱員的僱員名稱，部門名稱，跟薪資。
select E.Ename as 僱員, D.Dname 部門名稱, E.SAL 薪資 from Emp E 
       inner join Dept D on E.DEPTNO=D.DEPTNO ;

-- 34. 列出分配所有僱員數量的部門詳細訊息，即使該部門沒有僱員(沒有顧員者為0)。(32題方法一改LEFTJOIN)
-- 方法一
select D.DEPTNO 部門編號, Dname 部門名稱, LOC 區域, ifnull(E.人數,0) 人數 from Dept D
		left join (select DEPTNO,Count(empno) 人數 from Emp Group by DEPTNO ) as E
	    on D.DEPTNO=E.DEPTNO ;
-- 方法二
select D.DEPTNO 部門編號, DNAME 部門名稱, LOC 區域, COUNT(E.DEPTNO) 人數	-- **COUNT()內要使用E.DEPTNO)
from EMP E right join DEPT D ON E.DEPTNO=D.DEPTNO 
Group by  D.DEPTNO, DNAME, LOC;


-- 35. 列出各種工作類別的最高薪資。
-- (1)--顯示欄位：職務, 最高薪 
select JOB 職務, Max(SAL) 最高薪 from Emp group by JOB	order by 1;

-- (2)--顯示欄位：職務, 姓名, 最高薪
-- 方法一
select E1.JOB 職務, Ename 姓名, sub.最高薪 
from Emp E1 Left join 
		(select E2.JOB 職務,  max(Sal) 最高薪
		from Emp E2 group by E2.JOB ) sub 
	on E1.sal=sub.最高薪
where 最高薪 is not null
order by 1;
-- 方法二
select E1.JOB 職務, Ename 姓名, sub.最高薪 
from Emp E1 Left join 
		(select E2.JOB 職務,  max(Sal) 最高薪
		from Emp E2 group by E2.JOB ) sub 
	on E1.sal=sub.最高薪
where 最高薪 is not null
order by 1;

-- 36. 列出各部門的經理最低薪資。
-- 顯示欄位：經理(姓名), 職務, 最低薪
-- 方法一
select E1.Ename as 經理,E1.JOB 職務, E2.MinSal 最低薪 from Emp E1 , 
       (select JOB, Min(SAL) MinSal from Emp group by JOB) as E2
	   where  E1.JOB=E2.JOB and E1.SAL=E2.MinSal  and E1.JOB='MANAGER';
-- 方法二
select Distinct E1.ENAME as 經理, 職務, E2.最低薪 
	from   (select  JOB 職務, Min(SAL) 最低薪 from Emp group by  JOB)  as E2
	join Emp E1 on E1.JOB=E2.職務 and E1.SAL=E2.最低薪  and E1.JOB='MANAGER'
	order by 1;
-- 方法三
SELECT Ename as 經理, JOB 職務, SAL 最低薪 FROM Emp 
WHERE SAL=(SELECT  MIN(SAL) FROM Emp E2  WHERE JOB='MANAGER');
-- 方法三如不加 and job='MANAGER' 答案一樣，但如果有一個薪水同最低薪的經理(他不是經理)，則可能就不合題意(經理)

-- 37. 列出按照年薪降冪排序所有僱員的年薪
select E1.Ename as 僱員,E1.JOB 職務, E1.SAL*12 年薪 from Emp E1 
	order by 3 DESC;


-- 38. 列出薪資等級為4的所有員工
-- 顯示欄位：僱員, 職務, 薪資, 等級
-- 方法1.1 (92)
select E.Ename as 僱員,E.JOB 職務, E.SAL 薪資, G.grade 等級
	from Emp E ,  SALGRADE G
    where E.sal>=LOSAL and E.sal<=HISAL and G.grade=4;

-- 方法1.2 99作法
select Ename as 僱員,JOB 職務, SAL 薪資, grade 等級
from Emp E join  SALGRADE on sal>=LOSAL and sal<=HISAL
where  grade = 4;


-- 方法二 (子查詢)
select * 
from (
	select E.Ename as 僱員,E.JOB 職務, E.SAL 薪資, 
	(select GRADE  from SALGRADE where E.sal>=LOSAL and E.sal<=HISAL) 等級 
	from Emp E 
	) as sub
	where 等級=4;
    
-- 方法三 (CTE) 本法MySql8.0版之前不支援, 但MariaDb支援
WITH CTE381 (僱員, 職務, 薪資, 等級)
AS (
	select E.Ename as 僱員,E.JOB 職務, E.SAL 薪資, 
		(select GRADE  from SALGRADE where E.sal>=LOSAL and E.sal<=HISAL) 等級 
	from Emp E 
	) SELECT * FROM CTE381 WHERE 等級=4;

-- 方法四 (CTE) 使用case when... then end
WITH CTE382 (僱員, 職務, 薪資, 等級)
AS (
	select Ename as 僱員,JOB 職務, SAL 薪資, 
		case  
			when sal>3000 and sal<10000 then 5
			when sal>2000				then 4
			when sal>1400				then 3
			when sal>1200				then 2
			when sal>700				then 1
		end as 等級
	from Emp E 
)
select * from CTE382
where 等級=4;


-- 39. 列出含傭金，薪資等級為2的員工。(IFNULL(,)：2參數，OALESCE(,,,...)　多參數
-- 顯示欄位：僱員, 職務, [薪資+傭金], 等級
-- 方法一 99語法
select Ename as 僱員,JOB 職務, SAL 薪資, grade 等級
from Emp E join  SALGRADE 
	on (sal+ ISNULL(E.COMM,0))>=LOSAL and (sal+ISNULL(E.COMM,0))<=HISAL
where  grade = 2;


-- 方法二 (子查詢)
    Select * 
	From (
	select E.Ename as 僱員,E.JOB 職務, E.SAL + ifnull(E.COMM,0) 薪資_傭金 ,  
	(select S.GRADE  from SALGRADE S where E.sal+COALESCE(E.COMM,0) >= LOSAL and E.sal+COALESCE(E.COMM,0)<=HISAL) 等級 
	from Emp E ) as sub
	where  sub.等級=2;
    
-- 方法三 (CTE)  本法MySql8.0版之前不支援, 但MariaDb支援
WITH CTE39 (僱員, 職務, 薪資_傭金, 等級)
AS (
	select E.Ename as 僱員, E.JOB 職務, E.SAL + IFNULL(E.COMM,0) 薪資_傭金 ,  
	(select S.GRADE  from SALGRADE S 
		where E.sal+IFNULL(E.COMM,0) >=LOSAL and E.sal+IFNULL(E.COMM,0)<=HISAL) 等級 
		from Emp E  
	)
SELECT * FROM CTE39 WHERE 等級=2;


-- 40. 列出每個部門薪資水平為第二的員工。
-- 方法一 (子查詢1)
 select DEPTNO 部門編號, Ename 僱員, JOB 職務, SAL 薪資 
	from Emp E1
	where  (select Count(DISTINCT SAL) from Emp E2 where E1.DEPTNO=DEPTNO and SAL>=E1.SAL) =2
 	order by 1;
-- 方法二(子查詢2)
select E2.deptno as '部門編號', ename as '僱員', job as '職務', sal as '薪資' 
from Emp E2,
(	select E1.DEPTNO,  MAX(SAL) 薪資 
	from emp E1 inner join (select deptno,MAX(sal) as Max  from emp group by deptno )sub on E1.deptno=sub.Deptno 
	where E1.sal!=Max
	group by E1.Deptno
) Sub2
where E2.sal = Sub2.薪資 
order by 1;
-- 方法三(子查詢3)
select E2.DEPTNO 部門編號, E2.Ename 僱員, E2.JOB 職務, E2.Sal 薪資 
From (
		select E1.DEPTNO,  MAX(SAL) 薪資 
		from Emp E1  where sal not in (select Max(SAL) from EMP E2  group by deptno)
		group by E1.DEPTNO 
	) sub , Emp E2 
where E2.Sal =sub.薪資 and E2.DEPTNO=sub.DEPTNO
order by 1;
-- 方法四(採用 Dense_Rank Over() )
select 部門編號, 僱員, 職務, 薪資, 部門排名
from (
 select DEPTNO 部門編號, Ename 僱員, JOB 職務, SAL 薪資, DENSE_RANK() OVER (PARTITION BY  DEPTNO ORDER BY DEPTNO,SAL DESC) AS 部門排名 
 from Emp 
) sub
where 部門排名=2
order by 1;

-- 方法五(採用 Dense_Rank Over() )
select 部門編號, Ename 僱員, job 職務, 薪資, 部門排名
from 
Emp E,
(
 select DEPTNO 部門編號,  SAL 薪資, DENSE_RANK() OVER (PARTITION BY  DEPTNO ORDER BY DEPTNO,SAL DESC) AS 部門排名 
 from Emp 
) sub
where  E.Deptno=部門編號 and sal = 薪資 and 部門排名=2
order by 2;
 

 --------------
-- 方法六 (本法的Group By 不適用 MSSQL)
SELECT DEPTNO 部門編號,ENAME 僱員,JOB 職務, max(SAL) 薪資
FROM emp 
where (SAL not in (SELECT Max(SAL) FROM emp group by DEPTNO) ) 
group by DEPTNO  
order by DEPTNO;

---------
-- 方法七 (本法的Group By 不適用 MSSQL)
select deptno as '部門編號', ename as '僱員', job as '職務', Max(sal) as '薪資' 
from emp inner join (select deptno,MAX(sal) as Max  from emp group by deptno )sub using(deptno) 
where sal != Max 
group by deptno ;
 
 