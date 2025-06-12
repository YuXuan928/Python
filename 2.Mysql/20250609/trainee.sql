use madb_n;

select ENAME, JOB, SAL
FROM madb_n.emp
where SAL < 40000;

SELECT ENAME, JOB, DEPTNO
FROM madb_n.emp
where DEPTNO=30;

select ENAME, EMPNO, JOB, DEPTNO
from madb_n.emp
where JOB not in ('MANAGER', 'PRESIDENT');

select ENAME, JOB, SAL, COMM
from madb_n.emp
where COMM > SAL;

select ENAME, JOB, SAL, COMM
from madb_n.emp
where COMM > (SAL*0.6);

select *
from emp
where DEPTNO=10 and JOB like 'MANAGER';

select ENAME, JOB, SAL, DEPTNO
from madb_n.emp
where DEPTNO = 20 and SAL>80000 and JOB not like 'MANAGER';

select ENAME, JOB, COMM
from madb_n.emp
where COMM not in ('null','0') ;

select ENAME, JOB, COMM
from emp
where COMM is null or COMM = '0' ;

select *
from emp
where timestampdiff( year,HIREDATE,curdate())>13;

select *
from emp
where HIREDATE < '2012-01-01';

select *
from emp
where length(ENAME) = 5;

select EMPNO, ENAME as 'No A in ENAME'
from emp
where ENAME not like "%A%" and ENAME not like "%a%";

select ENAME , left(ENAME,3) as '前三個字元'
from emp ;

select ENAME , 
concat ( left ( ENAME , 3 ) , repeat( '*' , char_length(ENAME) -3)) as '前三個字元'
from emp ;

SELECT 
  ENAME, 
  CONCAT('B', SUBSTR(ENAME, 2)) AS 'AFTER CHANGE FIRST WORD', 
  JOB
FROM emp
WHERE JOB = 'SALESMAN';

select *
from emp
ORDER BY ENAME ASC;

select ENAME, HIREDATE
from emp
order by HIREDATE asc;

select ENAME, JOB, SAL
from emp
order by JOB desc , SAL ASC;

select ENAME, SAL, ROUND( SAL / 30, 1) as DailySAL
from emp ;

select ENAME, SAL
from emp
WHERE SAL = (SELECT MAX(SAL) FROM emp);

select ENAME, HIREDATE
from emp
where MONTH(HIREDATE) = 2 ;

select ENAME, HIREDATE, DATEDIFF(curdate( ),HIREDATE) as HIREDAYS
from emp
order by HIREDATE asc;

select EMPNO, ENAME as 'there has c in ENAME'
from emp
where ENAME like '%C%' and ENAME like '%c%';

SELECT emp.DEPTNO , dept.DNAME, count(EMPNO) as People_in_DEPTNO
from dept
join emp on emp.DEPTNO = dept.DEPTNO
GROUP BY DEPTNO, DNAME;

select DEPTNO, ENAME, SAL
from emp
where SAL >(select SAL from emp where ENAME='SMITH')
order by DEPTNO asc;

-- 選取員工姓名（e.ENAME）與對應的主管姓名（m.ENAME），並用別名表示
SELECT e.ENAME AS ENAME,      -- 員工的名字，從 e 表中選出
       m.ENAME AS MGR         -- 員工的主管名字，從 m 表中選出

-- 從 emp 表中取出員工資料，並指定別名 e
FROM emp e                    -- emp 表作為員工資料來源，別名為 e

-- 對 emp 表再次引用，這次當成主管資料來源，別名為 m
-- 把 e 表中的 MGR（主管編號）對應到 m 表中的 EMPNO（主管自己的員工編號）
LEFT JOIN emp m ON e.MGR = m.EMPNO;  -- 使用 LEFT JOIN 可保留沒有主管的人（如 KING）

select e.ENAME as ENAME, e.HIREDATE as HIREDATE, m.ENAME as ENAME, m.HIREDATE as HIREDATE
from emp e
join emp m on e.MGR = m.EMPNO
where e.HIREDATE < m.HIREDATE;

select emp.ENAME, emp.JOB, dept.DNAME as DNAME
from emp
join dept on emp.DEPTNO = dept.DEPTNO 
where JOB like 'CLERK';

select JOB, min(SAL) as min_salary
from emp
group by job 
order by job asc;

select JOB, ENAME, min(SAL) as min_salary
from emp 
group by JOB
order by JOB ASC;

select ENAME, JOB
from emp
where JOB =(select JOB from emp where ENAME = 'SMITH') 
and ENAME <> 'SMITH';

select ENAME, SAL
from emp
where SAL in (SELECT SAL from emp where DEPTNO = 30 );

select emp.DEPTNO, dept.DNAME, dept.LOC, count(ENAME) as People_in_DNAME
from dept
join emp on emp.DEPTNO = dept.DEPTNO
group by emp.DEPTNO, dept.DNAME, dept.LOC;

select emp.ENAME, dept.DNAME, emp.SAL
from emp
join dept on emp.deptno = dept.deptno;

select dept.DEPTNO, dept.DNAME, LOC, count(emp.ENAME) as People_in_each_DNAME
from dept
left join emp on emp.DEPTNO = dept.DEPTNO
group by dept.DEPTNO, dept.DNAME, dept.LOC ;

select JOB, MAX(SAL) as Highest_SAL
from emp
group by job
order by job asc;

select JOB, ENAME, MAX(SAL) as Highest_SAL
from emp
group by JOB
order by JOb asc;

select ENAME as MAG_ENAME, JOB, SAL as LOWEST_SAL
from emp
where JOB = 'MANAGER' and SAL = (select MIN(SAL) from emp where JOB = "MANAGER");