-- 1 
select student.SNO as 學號, student.NAME as 姓名, round(sum(yscore.score),1) as 總分, round(avg(yscore.score),1) as 平均
from student
join yscore on student.SNO = yscore.SNO
group by student.SNO, student.NAME
order by  round(sum(yscore.score),1) DESC;

-- 2 
select student.SNO as 學號, student.NAME as 姓名, yscore.SUBJECT as 科目, yscore.score as 最高成績
from student
join yscore on student.SNO = yscore.SNO
where yscore.SCORE = (select MAX(SCORE) from yscore where SNO = student.SNO)
order by student.SNO ASC;


