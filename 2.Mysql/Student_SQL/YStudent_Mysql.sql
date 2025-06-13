-- 導出 YSTUDENT 的資料庫結構
DROP DATABASE IF EXISTS `YSTUDENT`;
CREATE DATABASE IF NOT EXISTS `YSTUDENT` /*!40100 DEFAULT CHARACTER SET utf8 */;

use `YSTUDENT`;

DROP TABLE IF EXISTS `STUDENT`;

CREATE TABLE `STUDENT` (
  `SNO` smallint(6) DEFAULT NULL,
  `NAME` varchar(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Dumping data for table `STUDENT`
--

LOCK TABLES `STUDENT` WRITE;
INSERT INTO `STUDENT` VALUES (1001,'王玉治'),(1002,'林鳳春'),(1003,'葉秀珠'),(1004,'陳曉蘭'),(1005,'吳美成'),(1006,'莊國雄'),(1007,'向大鵬'),(1008,'陳詔芳'),(1009,'陳雅賢'),(1010,'吳國信');
UNLOCK TABLES;


DROP TABLE IF EXISTS `YSCORE`;
CREATE TABLE `YSCORE` (
  `SNO` smallint(6) DEFAULT NULL,
  `SUBJECT` varchar(2) DEFAULT NULL,
  `SCORE` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


--
-- Dumping data for table `YSCORE`
--

LOCK TABLES `YSCORE` WRITE;
INSERT INTO `YSCORE` VALUES (1001,'國文',96),(1002,'國文',66),(1003,'國文',95),(1004,'國文',54),(1005,'國文',98),(1006,'國文',52),(1007,'國文',56),(1008,'國文',96),(1009,'國文',84),(1010,'國文',66),(1001,'英文',74),(1002,'英文',74),(1003,'英文',79),(1004,'英文',77),(1005,'英文',70),(1006,'英文',70),(1007,'英文',97),(1008,'英文',54),(1009,'英文',72),(1010,'英文',56),(1001,'數學',98),(1002,'數學',80),(1003,'數學',52),(1004,'數學',51),(1005,'數學',95),(1006,'數學',81),(1007,'數學',69),(1008,'數學',87),(1009,'數學',73),(1010,'數學',91);
UNLOCK TABLES;

