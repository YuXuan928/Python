use yvmenu0;
-- 1.	請列出該公司民國100年1月所有銷貨內容:
-- A.	欄位如右:日期，公司編號，客戶簡稱，性質，成品編號，成品名稱，數量，單價，金額。
-- B.	排序: 日期(遞增)，公司編號(遞增)，金額(遞減)。
select vhdt 日期, M.cono 公司編號, na 客戶簡稱, dc 性質, D.fgno 成品編號, FGNAME 成品名稱, 
		D.QTY 數量, D.PRC 單價, D.QTY*D.PRC 金額
From YFGIO M join YFGIODT D using (VHNO)  -- 同 on M.VHNO=D.VHNO
			 join YCUST C using (CONO)    -- 同 on M.CONO=C.CONO
			 join YFGMAST FG using (FGNO)  -- 同 on D.FGNO=FG.FGNO
where FLOOR(vhdt/100)= 10001 and dc='C'
order by 1, 2, 9 DESC;


-- 2.	請列出該公司民國100年2月所有進貨內容:
-- A.	欄位如右:日期，公司編號，廠商簡稱，進/銷，成品編號，成品名稱，數量，單價，金額。
-- 排序: 日期(遞增)，公司編號(遞增)，金額(遞減)
select vhdt 日期, M.cono 公司編號, C.na 客戶簡稱, dc 性質, D.fgno 成品編號, FG.FGNAME 成品名稱, 
		D.QTY 數量, D.PRC 單價, D.QTY*D.PRC 金額
From YFGIO M join YFGIODT D on M.VHNO=D.VHNO
			 join YCUST C on M.CONO=C.CONO
			 join YFGMAST FG on D.FGNO=FG.FGNO
where FLOOR(vhdt/100)= 10002 and dc='D'
order by 1, 2, 9 DESC;


-- 3.	請列出該公司民國100年1-3月所有訂單內容:
-- A.	欄位如右: 訂單年月，公司編號，客戶簡稱，訂單日期，產品編號，產品名稱，數量，單價，金額。
-- B.	排序: 訂單年月(遞增)，公司編號(遞增)，訂單日期(遞增)，產品編號(遞增)。
select CEILING(ODATE/100) 訂單年月, M.cono 公司編號, C.na 客戶簡稱, ODATE 訂單日期, D.fgno 成品編號, FG.FGNAME 成品名稱, 
		D.QTY 數量, D.PRC 單價, D.QTY*D.PRC 金額
From YODR M join YODRDT D on M.ORDER1=D.ORDER1
			 join YCUST C on M.CONO=C.CONO
			 join YFGMAST FG on D.FGNO=FG.FGNO
where FLOOR(ODATE/100) between 10001 and 10003
order by 1, 2, 4, 5 ;


-- 4.	請列出該公司民國100年1-3月之月庫存總值(單價以YFGMAST之PRC):
-- A.	欄位如右: 庫存年月，庫存總值。
-- B.	排序: 庫存年月(遞增)。
-- ※注：本題為一個月份僅有一個庫存總值，因此總共只有3筆。
select yymm 庫存年月, sum(I.IVQTY*FG.PRC) 庫存總值
from YINVENTORY I join YFGMAST FG on I.FGNO=FG.FGNO
where YYMM between 10001 and 10003
group by  yymm ;



-- 5.	請列出該公司民國100年2月各型號所有進貨、銷貨、存貨內容(請暫使用YFGQTY資料表作本題練習):
-- A.	欄位如右: 資料年月，成品編號，成品名稱，期初數，進貨數，銷貨數，期末數。
-- B.	排序:成品編號(遞增)
select YYMM 資料年月, Q.FGNO 成品編號,  FGNAME 成品名稱,  PMQTY 期初數,  INQTY 進貨數,
		UDQTY 銷貨數, PMQTY+INQTY-UDQTY 期末數 
from YFGQTY Q join YFGMAST F on Q.FGNO=F.FGNO
where yymm =10002 ;