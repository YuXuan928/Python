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