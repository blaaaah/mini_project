-- MySQL dump 10.13  Distrib 5.7.17, for Linux (x86_64)
--
-- Host: localhost    Database: node
-- ------------------------------------------------------
-- Server version	5.7.17-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `node`
--

DROP TABLE IF EXISTS `node`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `node` (
  `id` int(11) NOT NULL,
  `na0` varchar(10) DEFAULT NULL,
  `na1` varchar(10) DEFAULT NULL,
  `na2` varchar(10) DEFAULT NULL,
  `na3` varchar(10) DEFAULT NULL,
  `sa0` varchar(10) DEFAULT NULL,
  `sa1` varchar(10) DEFAULT NULL,
  `sa2` varchar(10) DEFAULT NULL,
  `sa3` varchar(10) DEFAULT NULL,
  `ea0` varchar(10) DEFAULT NULL,
  `ea1` varchar(10) DEFAULT NULL,
  `ea2` varchar(10) DEFAULT NULL,
  `ea3` varchar(10) DEFAULT NULL,
  `wa0` varchar(10) DEFAULT NULL,
  `wa1` varchar(10) DEFAULT NULL,
  `wa2` varchar(10) DEFAULT NULL,
  `wa3` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `node`
--

LOCK TABLES `node` WRITE;
/*!40000 ALTER TABLE `node` DISABLE KEYS */;
INSERT INTO `node` VALUES (1,'0,0,0,1','0,0,0,1','0,0,0,1','0,0,0,1','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,1','0,0,0,0','0,0,0,0','0,0,0,1'),(2,'0,0,0,0','0,0,0,0','0,0,0,1','0,0,0,1','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0'),(3,'0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,1','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0'),(4,'0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,1','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,1','0,0,0,2','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0'),(5,'0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,1','0,0,0,0','0,0,0,0'),(6,'0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,1'),(7,'0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0'),(8,'0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,1','0,0,0,1','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0'),(9,'0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0'),(10,'0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0'),(11,'0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0'),(12,'0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,1','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,1','0,0,0,2','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0'),(13,'0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,1','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,2','0,0,0,3'),(14,'0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,1','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0'),(15,'0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0'),(16,'0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,1','0,0,0,1','0,0,0,2','0,0,0,2','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,1','0,0,0,0','0,0,0,0','0,0,0,0','0,0,0,0');
/*!40000 ALTER TABLE `node` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `selector`
--

DROP TABLE IF EXISTS `selector`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `selector` (
  `id` int(11) NOT NULL,
  `ni` int(11) NOT NULL,
  `si` int(11) DEFAULT NULL,
  `wi` int(11) DEFAULT NULL,
  `ei` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `selector`
--

LOCK TABLES `selector` WRITE;
/*!40000 ALTER TABLE `selector` DISABLE KEYS */;
INSERT INTO `selector` VALUES (1,1,1,1,1),(2,0,0,0,0),(3,0,0,0,0),(4,0,0,0,0),(5,0,0,0,0),(6,0,0,0,0),(7,0,0,0,0),(8,0,0,0,0),(9,0,0,0,0),(10,0,0,0,0),(11,0,0,0,0),(12,0,0,0,0),(13,0,0,0,0),(14,0,0,0,3),(15,3,3,3,3),(16,0,0,0,0);
/*!40000 ALTER TABLE `selector` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-03-27 11:00:14
