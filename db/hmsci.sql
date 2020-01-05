-- MySQL dump 10.13  Distrib 8.0.18, for osx10.14 (x86_64)
--
-- Host: localhost    Database: hmsci
-- ------------------------------------------------------
-- Server version	8.0.18

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
-- Table structure for table `hms_hostel`
--

DROP TABLE IF EXISTS `hms_hostel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hms_hostel` (
  `hostelId` int(11) NOT NULL AUTO_INCREMENT COMMENT 'The unique Id of hostel.',
  `hostelName` varchar(40) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT 'Hostel name of the student.',
  `hostelWarden` varchar(40) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT 'Name of hostel warden.',
  `hostelGender` varchar(1) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT 'Gender of Hostel M or F.',
  PRIMARY KEY (`hostelId`),
  UNIQUE KEY `hstl_UNIQUE` (`hostelId`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hms_hostel`
--

LOCK TABLES `hms_hostel` WRITE;
/*!40000 ALTER TABLE `hms_hostel` DISABLE KEYS */;
INSERT INTO `hms_hostel` VALUES (1,'Sukhoi','Ashutosh','M'),(2,'Mirage','Ayushi','F');
/*!40000 ALTER TABLE `hms_hostel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hms_hostel_room_map`
--

DROP TABLE IF EXISTS `hms_hostel_room_map`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hms_hostel_room_map` (
  `hrmid` int(11) NOT NULL AUTO_INCREMENT,
  `hostelid` int(11) NOT NULL,
  `roomnumbers` int(11) DEFAULT NULL,
  `available` int(11) DEFAULT '0',
  PRIMARY KEY (`hrmid`),
  UNIQUE KEY `hrmid_UNIQUE` (`hrmid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hms_hostel_room_map`
--

LOCK TABLES `hms_hostel_room_map` WRITE;
/*!40000 ALTER TABLE `hms_hostel_room_map` DISABLE KEYS */;
INSERT INTO `hms_hostel_room_map` VALUES (1,1,1,1),(2,1,2,0),(3,2,1,1),(4,2,2,0);
/*!40000 ALTER TABLE `hms_hostel_room_map` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hms_students`
--

DROP TABLE IF EXISTS `hms_students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hms_students` (
  `stuid` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique student id for student.',
  `stuEnrollment` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `stuName` varchar(40) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `stuGender` varchar(1) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT 'Gender of student M or F.',
  `stuDept` varchar(40) COLLATE utf8mb4_general_ci NOT NULL COMMENT 'Department Name of Student',
  `stuYear` varchar(10) COLLATE utf8mb4_general_ci NOT NULL COMMENT 'Year of the student',
  `stuHostel` varchar(40) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT 'Hostel Id of the student.',
  `stuRoom` int(11) DEFAULT NULL COMMENT 'Room number of the student.',
  PRIMARY KEY (`stuid`),
  UNIQUE KEY `stuid_UNIQUE` (`stuid`),
  UNIQUE KEY `stuEnrollment_UNIQUE` (`stuEnrollment`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hms_students`
--

LOCK TABLES `hms_students` WRITE;
/*!40000 ALTER TABLE `hms_students` DISABLE KEYS */;
INSERT INTO `hms_students` VALUES (1,'0701CS101013','ASHUTOSH','M','CSE','1','Sukhoi',1),(2,'0701CS101015','AYUSHI','F','CSE','1','Mirage',1);
/*!40000 ALTER TABLE `hms_students` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-01-05 18:47:11
