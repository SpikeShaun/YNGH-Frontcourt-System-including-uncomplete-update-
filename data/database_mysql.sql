-- MySQL dump 10.13  Distrib 9.0.0, for Win64 (x86_64)
--
-- Host: localhost    Database: toubiao_db
-- ------------------------------------------------------
-- Server version	8.0.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `toubiao_db`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `toubiao_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `toubiao_db`;

--
-- Table structure for table `admins`
--

DROP TABLE IF EXISTS `admins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admins` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `password_hash` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(120) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admins`
--

LOCK TABLES `admins` WRITE;
/*!40000 ALTER TABLE `admins` DISABLE KEYS */;
INSERT INTO `admins` VALUES (1,'yngh','scrypt:32768:8:1$ydnSes1P0gEBD2B6$23b31084a4d1fa12651e64b30479be442db610125d4c077b9c9b67bb7614c0390997918d3c6d7f32257746b0a586e1644e8bd9b8fde3adffaac8ce2729d6bcc0','shaun7565@163.com');
/*!40000 ALTER TABLE `admins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bids`
--

DROP TABLE IF EXISTS `bids`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bids` (
  `id` int NOT NULL AUTO_INCREMENT,
  `project_id` int NOT NULL,
  `supplier_name` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `supplier_address` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `legal_person` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `credit_code` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `agent` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `phone` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(120) COLLATE utf8mb4_general_ci NOT NULL,
  `file_method` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `file_time` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `is_paid` tinyint(1) DEFAULT NULL,
  `status` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_supplier_project` (`supplier_name`,`credit_code`,`project_id`),
  KEY `project_id` (`project_id`),
  CONSTRAINT `bids_ibfk_1` FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bids`
--

LOCK TABLES `bids` WRITE;
/*!40000 ALTER TABLE `bids` DISABLE KEYS */;
INSERT INTO `bids` VALUES (1,1,'昆明仲凡教育科技有限公司','大渔街道','于帆','91530103MA6L43XM7J','郑晓峰','13020833009','shaun7565@163.com','现场获取','2025年04月21日11时40分',1,'pending','2025-04-21 11:40:14'),(16,2,'昆明仲凡教育科技有限公司','大渔街道','于帆','91530103MA6L43XM7J','郑晓峰','13020833009','shaun7565@163.com','现场获取','2025年04月21日14时21分',1,'pending','2025-04-21 14:21:59'),(41,1,'新东方','dsvsvd','vssdf','vsvsdv','sdvsd','vvvvv','shaun7565@163.com','现场获取','2025年04月22日11时24分',1,'pending','2025-04-22 11:25:38'),(42,3,'新东方','dsvsvd','vssdf','vsvsdv','sdvsd','vvvvv','shaun7565@163.com','现场获取','2025年04月22日11时25分',1,'pending','2025-04-22 11:26:13'),(46,4,'新东方','dsvsvd','vssdf','vsvsdv','zx','13020833009','shaun7565@163.com','现场获取','2025年04月22日16时04分',1,'pending','2025-04-22 16:04:46'),(48,4,'新东方','dsvsvd','vssdf','vsvsd','zx','13020833009','shaun7565@163.com','现场获取','2025年04月22日16时14分',1,'pending','2025-04-22 16:14:59'),(49,4,'新瀚动','执眠纪','vssdf','xhc','zx','13020833009','shaun7565@163.com','现场获取','2025年04月22日21时58分',1,'pending','2025-04-22 21:58:28'),(51,2,'新瀚动','执眠纪','于帆','91530103MA6L43XM7J','郑晓峰','13020833009','shaun7565@163.com','现场获取','2025年04月23日14时44分',0,'pending','2025-04-23 14:44:58'),(52,4,'新瀚动','执眠纪','于帆','91530103MA6L43XM7J','郑晓峰','13020833009','shaun7565@163.com','现场获取','2025年04月23日15时54分',1,'locked','2025-04-23 15:54:17'),(53,4,'新瀚动xxx','执眠纪','于帆d','kjj,kk,k,,','郑晓峰','13020833003','shaun7565@163.com','现场获取','2025年04月23日16时03分',1,'locked','2025-04-23 16:03:54'),(54,4,'新瀚动xxxdf都护府好地方his对哦好大夫回答搜if','执眠纪','于帆d','LBR','b vcbneeeff','13020833009','shaun7565@163.com','现场获取','2025年04月23日16时08分',1,'pending','2025-04-23 16:08:14'),(58,4,'执眠x','执眠x','xhc','xc','郑晓峰','13020833009','shaun7565@163.com','现场获取','2025年04月23日16时11分',1,'locked','2025-04-23 16:11:54'),(61,6,'百度xxx','白云路','席灏铖','sdhgfdsfjsdgfuids','刘博纯','13020833009','361077078@qq.com','现场获取','2025年04月27日10时10分',1,'confirmed','2025-04-27 10:10:42'),(62,6,'新瀚动23444565757粉红色丢粉红色丢分hisi好哦佛色哈佛色i活动撒','白云路同德广场','席灏铖','HSAFJ2324235TRYRTG','刘博纯x','13020833009','361077078@qq.com','现场获取','2025年04月27日14时12分',0,'confirmed','2025-04-27 14:11:54'),(64,8,'新瀚动234','白云路','席灏铖','wwww','刘博纯','13020833009','shaun7565@163.com','现场获取','2025年04月27日15时02分',1,'confirmed','2025-04-27 15:02:48'),(65,8,'新瀚动7566','白云路','席灏铖','wwwwdf','刘博纯','13020833009','shaun7565@163.com','现场获取','2025年04月27日16时55分',0,'confirmed','2025-04-27 16:55:10'),(66,5,'新瀚动75tfghfthft','白云路','席灏铖','WWWWDF200000000FSD','刘博纯','13020833009','shaun7565@163.com','现场获取','2025年04月28日14时15分',1,'confirmed','2025-04-28 14:16:00'),(67,9,'新瀚动75tfghfthft','白云路','席灏铖','WWWWDF200000000FSD','刘博纯','13020833009','shaun7565@163.com','现场获取','2025年04月29日12时13分',1,'confirmed','2025-04-29 12:13:08'),(68,9,'新东方','白云路','席灏铖','WR115656565RGDFGDF','刘博纯','13020833009','shaun7565@163.com','现场获取','2025年04月29日13时08分',1,'confirmed','2025-04-29 13:08:37');
/*!40000 ALTER TABLE `bids` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `leaders`
--

DROP TABLE IF EXISTS `leaders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `leaders` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(120) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leaders`
--

LOCK TABLES `leaders` WRITE;
/*!40000 ALTER TABLE `leaders` DISABLE KEYS */;
INSERT INTO `leaders` VALUES (1,'郭琼','1730394096@qq.com'),(2,'马爱佳','851502638@qq.com'),(3,'蒋立','1193988365@qq.com'),(4,'张育玮','549839908@qq.com'),(5,'李昂','1215774156@qq.com'),(6,'何云艳','740211471@qq.com'),(7,'张杰','645231114@qq.com'),(8,'袁思猛','1023207130@qq.com'),(9,'朱大洲','2113800357@qq.com'),(10,'高铭','1812651346@qq.com'),(11,'施江艳','2822611109@qq.com'),(12,'赵津仪','122841989@qq.com'),(13,'林艳平','920167135@qq.com'),(14,'何甜甜','2419801535@qq.com'),(15,'房雨雷','1430684282@qq.com'),(16,'张国辉','3330807194@qq.com'),(17,'李锦香','839029321@qq.com'),(18,'陈学敏','450077893@qq.com'),(19,'王云文','2039479437@qq.com'),(20,'张凤阳','2624654686@qq.com'),(21,'杨云鹏','420031465@qq.com'),(22,'武江艳','693549110@qq.com'),(23,'张静楠','1525053382@qq.com'),(24,'苏雪冬','361077078@qq.com'),(25,'常焱茗','1162193179@qq.com'),(26,'周翔丽','20909691@qq.com'),(27,'杨天秀','251400160@qq.com'),(28,'蒋翔','648504278@qq.com'),(29,'王林伟','1457454721@qq.com'),(30,'李灿辉','306626194@qq.com'),(31,'冯丽','763455921@qq.com'),(32,'张正举','30143153@qq.com'),(33,'执眠纪','shaun7565@163.com'),(34,'席灏铖','13020833009@163.com'),(35,'硫花','xihaocheng27@163.com');
/*!40000 ALTER TABLE `leaders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mail_logs`
--

DROP TABLE IF EXISTS `mail_logs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mail_logs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `bid_id` int DEFAULT NULL,
  `project_id` int DEFAULT NULL,
  `status` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `message` text COLLATE utf8mb4_general_ci,
  `sent_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `bid_id` (`bid_id`),
  KEY `project_id` (`project_id`),
  CONSTRAINT `mail_logs_ibfk_1` FOREIGN KEY (`bid_id`) REFERENCES `bids` (`id`),
  CONSTRAINT `mail_logs_ibfk_2` FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mail_logs`
--

LOCK TABLES `mail_logs` WRITE;
/*!40000 ALTER TABLE `mail_logs` DISABLE KEYS */;
INSERT INTO `mail_logs` VALUES (1,NULL,9,'success','发送成功: shaun7565@163.com','2025-04-29 11:55:02'),(2,NULL,9,'success','发送成功: shaun7565@163.com','2025-04-29 12:00:01'),(3,NULL,9,'success','发送成功: shaun7565@163.com','2025-04-29 12:14:01'),(4,NULL,9,'success','发送成功: shaun7565@163.com','2025-04-29 12:15:00'),(5,NULL,9,'success','发送成功: shaun7565@163.com','2025-04-29 12:45:02'),(6,NULL,9,'success','发送成功: shaun7565@163.com','2025-04-29 12:47:01'),(7,NULL,9,'success','发送成功: shaun7565@163.com','2025-04-29 12:51:01'),(8,NULL,9,'success','发送成功: shaun7565@163.com','2025-04-29 13:00:00'),(9,NULL,9,'success','发送成功: shaun7565@163.com','2025-04-29 13:03:01'),(10,NULL,9,'success','发送成功: shaun7565@163.com','2025-04-29 13:07:01'),(11,NULL,9,'success','发送成功: shaun7565@163.com','2025-04-29 13:10:00'),(12,NULL,9,'success','发送成功: shaun7565@163.com','2025-04-29 13:11:00'),(13,NULL,2,'success','发送成功: shaun7565@163.com','2025-04-29 13:13:00'),(14,NULL,5,'success','发送成功: shaun7565@163.com','2025-04-29 13:13:01'),(15,NULL,6,'success','发送成功: shaun7565@163.com','2025-04-29 13:13:01'),(16,NULL,9,'success','发送成功: shaun7565@163.com','2025-04-29 13:13:01'),(17,NULL,2,'success','发送成功: shaun7565@163.com','2025-04-29 17:00:03'),(18,NULL,5,'success','发送成功: shaun7565@163.com','2025-04-29 17:00:05'),(19,NULL,6,'success','发送成功: shaun7565@163.com','2025-04-29 17:00:06'),(20,NULL,9,'success','发送成功: shaun7565@163.com','2025-04-29 17:00:06'),(21,NULL,2,'success','发送成功: shaun7565@163.com','2025-04-29 18:19:02'),(22,NULL,5,'success','发送成功: shaun7565@163.com','2025-04-29 18:19:02'),(23,NULL,6,'success','发送成功: shaun7565@163.com','2025-04-29 18:19:02'),(24,NULL,9,'success','发送成功: shaun7565@163.com','2025-04-29 18:19:03'),(25,NULL,2,'success','发送成功: 361077078@qq.com','2025-04-29 18:21:00'),(26,NULL,5,'success','发送成功: shaun7565@163.com','2025-04-29 18:21:01'),(27,NULL,6,'success','发送成功: shaun7565@163.com','2025-04-29 18:21:01'),(28,NULL,9,'success','发送成功: shaun7565@163.com','2025-04-29 18:21:02'),(29,NULL,5,'success','发送成功: shaun7565@163.com','2025-04-30 00:00:03'),(30,NULL,6,'success','发送成功: shaun7565@163.com','2025-04-30 00:00:03'),(31,NULL,7,'success','发送成功: shaun7565@163.com','2025-04-30 00:00:08'),(32,NULL,9,'success','发送成功: shaun7565@163.com','2025-04-30 00:00:11'),(33,NULL,5,'success','发送成功: shaun7565@163.com','2025-04-30 00:03:01'),(34,NULL,6,'success','发送成功: shaun7565@163.com','2025-04-30 00:03:01'),(35,NULL,9,'success','发送成功: shaun7565@163.com','2025-04-30 00:03:02'),(36,NULL,5,'success','发送成功: shaun7565@163.com','2025-04-30 17:00:02'),(37,NULL,6,'success','发送成功: 361077078@qq.com','2025-04-30 17:00:03'),(38,NULL,9,'success','发送成功: 361077078@qq.com','2025-04-30 17:00:04'),(39,NULL,14,'success','发送成功: 13020833009@163.com','2025-05-14 15:47:03'),(40,NULL,14,'success','发送成功: shaun7565@163.com','2025-05-14 15:47:03'),(41,NULL,14,'success','发送成功: xihaocheng27@163.com','2025-05-14 15:47:03'),(42,NULL,14,'success','发送成功: shaun7565@163.com','2025-05-14 17:00:03'),(43,NULL,14,'success','发送成功: 13020833009@163.com','2025-05-14 17:00:03'),(44,NULL,14,'success','发送成功: xihaocheng27@163.com','2025-05-14 17:00:04');
/*!40000 ALTER TABLE `mail_logs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project_members`
--

DROP TABLE IF EXISTS `project_members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project_members` (
  `project_id` int NOT NULL,
  `leader_id` int NOT NULL,
  PRIMARY KEY (`project_id`,`leader_id`),
  KEY `leader_id` (`leader_id`),
  CONSTRAINT `project_members_ibfk_1` FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`) ON DELETE CASCADE,
  CONSTRAINT `project_members_ibfk_2` FOREIGN KEY (`leader_id`) REFERENCES `leaders` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project_members`
--

LOCK TABLES `project_members` WRITE;
/*!40000 ALTER TABLE `project_members` DISABLE KEYS */;
INSERT INTO `project_members` VALUES (16,33),(14,34),(14,35),(16,35);
/*!40000 ALTER TABLE `project_members` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects`
--

DROP TABLE IF EXISTS `projects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `code` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `deadline` datetime NOT NULL,
  `deposit_amount` float DEFAULT NULL,
  `is_paid` tinyint(1) DEFAULT NULL,
  `file_path` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `leader_email` varchar(120) COLLATE utf8mb4_general_ci NOT NULL,
  `start_time` datetime NOT NULL COMMENT '文件获取开始时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects`
--

LOCK TABLES `projects` WRITE;
/*!40000 ALTER TABLE `projects` DISABLE KEYS */;
INSERT INTO `projects` VALUES (1,'云南师范大学附属世纪金源学校广播系统采购项目','YNGH[2024]-620','2025-04-21 17:00:00',16000,0,'uploads/ePass_280120242336.pdf','2025-04-21 09:58:55','2025-04-21 16:46:08','placeholder@example.com','2025-01-01 00:00:00'),(2,'云南大学信息学院计算机采购项目','YNGH[2025]-816','2025-05-05 17:00:00',18000,0,'static\\uploads\\YNGH[2025]-816 云南大学信息学院计算机采购项目 招标文件.docx','2025-04-21 11:27:57','2025-05-14 17:02:15','shaun7565@163.com','2025-01-01 00:00:00'),(3,'昆明理工大学各学院采购任务','YNGH[2025]-621','2025-04-25 17:00:00',15000,0,'static\\uploads\\YNGH[2025]-621 昆明理工大学各学院采购任务 招标文件.docx','2025-04-22 11:23:14','2025-04-22 11:23:14','placeholder@example.com','2025-01-01 00:00:00'),(4,'云南民族大学扩建任务','YNGH[2025]-813','2025-04-30 17:00:00',27000,0,'static\\uploads\\YNGH[2025]-813 云南民族大学扩建任务 招标文件.doc','2025-04-22 14:31:48','2025-04-22 14:31:48','placeholder@example.com','2025-01-01 00:00:00'),(5,'海南医科大学接送服务','YNGH[2025]-425','2025-04-28 17:00:00',5942100,0,'static\\uploads\\YNGH[2025]-425 海南医科大学接送服务 招标文件.doc','2025-04-25 13:33:32','2025-04-30 17:40:44','361077078@qq.com','2025-01-01 00:00:00'),(6,'云南大学设备采购','YNGH[2025]-556','2025-04-28 17:00:00',6000,0,'static\\uploads\\YNGH[2025]-556 云南大学设备采购 招标文件.doc','2025-04-27 10:06:07','2025-04-30 17:32:37','1193988365@qq.com','2025-01-01 00:00:00'),(7,'云南大学设备采购1','YNGH[2025]-555','2025-04-30 00:00:00',160000,0,'static\\uploads\\--.docx','2025-04-27 14:46:10','2025-04-29 23:59:03','shaun7565@163.com','2025-01-01 00:00:00'),(8,'云南大学dfdf','YNGH[2025]-444','2025-04-21 15:04:00',0,0,'static\\uploads\\评委签到表.docx','2025-04-27 15:01:46','2025-04-30 17:41:35','1193988365@qq.com','2025-01-01 00:00:00'),(9,'西南林业大学采购任务','YNGH[2025]-8848','2025-04-28 17:00:00',20000,0,'static\\uploads\\评标纪律.doc','2025-04-29 10:54:24','2025-04-30 17:40:58','361077078@qq.com','2025-01-01 00:00:00'),(14,'昆明文理学院ddd','YNGH[2025]-97333','2025-04-30 13:46:00',659898,0,'static\\uploads\\结题验收报告CodePearls：面向青少年编程早教的可视化编程平台.doc','2025-05-14 13:47:05','2025-05-14 17:08:50','shaun7565@163.com','2025-03-24 01:46:00'),(16,'昆明文理','YNGH[2025]-9796','2025-05-06 16:03:00',0,0,'static\\uploads\\结题验收报告CodePearls：面向青少年编程早教的可视化编程平台.doc','2025-05-14 16:03:55','2025-05-14 17:01:26','13020833009@163.com','2025-04-29 16:03:00'),(17,'昆明文理sdds','YNGH[2025]-95455','2025-06-07 11:12:00',0,0,'static\\uploads\\2.个人陈述写作材料信息表-本科.docx','2025-05-19 11:12:56','2025-05-19 11:12:56','13020833009@163.com','2025-05-19 11:12:00');
/*!40000 ALTER TABLE `projects` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-19 13:58:19
