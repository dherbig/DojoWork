CREATE DATABASE  IF NOT EXISTS `twitter` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `twitter`;
-- MySQL dump 10.13  Distrib 5.6.19, for osx10.7 (i386)
--
-- Host: 127.0.0.1    Database: twitter
-- ------------------------------------------------------
-- Server version	5.5.38

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
-- Table structure for table `faves`
--

DROP TABLE IF EXISTS `faves`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `faves` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `tweet_id` int(11) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_faves_users1_idx` (`user_id`),
  KEY `fk_faves_tweets1_idx` (`tweet_id`),
  CONSTRAINT `fk_faves_tweets1` FOREIGN KEY (`tweet_id`) REFERENCES `tweets` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_faves_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faves`
--

LOCK TABLES `faves` WRITE;
/*!40000 ALTER TABLE `faves` DISABLE KEYS */;
INSERT INTO `faves` VALUES (1,2,1,'2010-02-01 00:00:01','2010-02-01 00:00:01'),(2,2,2,'2010-02-01 00:00:01','2010-02-01 00:00:01'),(3,3,4,'2010-02-01 00:00:01','2010-02-01 00:00:01'),(4,4,3,'2010-02-01 00:00:01','2010-02-01 00:00:01'),(5,1,9,'2010-02-01 00:00:01','2010-02-01 00:00:01'),(6,1,10,'2010-02-01 00:00:01','2010-02-01 00:00:01'),(7,1,11,'2010-02-01 00:00:01','2010-02-01 00:00:01');
/*!40000 ALTER TABLE `faves` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `follows`
--

DROP TABLE IF EXISTS `follows`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `follows` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `followed_id` int(11) NOT NULL,
  `follower_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_follows_users_idx` (`followed_id`),
  CONSTRAINT `fk_follows_users` FOREIGN KEY (`followed_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `follows`
--

LOCK TABLES `follows` WRITE;
/*!40000 ALTER TABLE `follows` DISABLE KEYS */;
INSERT INTO `follows` VALUES (1,1,2,'2010-02-01 00:00:01','2010-02-01 00:00:01'),(2,1,3,'2010-02-01 00:00:01','2010-02-01 00:00:01'),(3,1,4,'2010-02-01 00:00:01','2010-02-01 00:00:01'),(4,1,5,'2010-02-01 00:00:01','2010-02-01 00:00:01'),(5,3,4,'2010-02-01 00:00:01','2010-02-01 00:00:01'),(6,3,5,'2010-02-01 00:00:01','2010-02-01 00:00:01'),(7,2,4,'2010-02-01 00:00:01','2010-02-01 00:00:01');
/*!40000 ALTER TABLE `follows` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tweets`
--

DROP TABLE IF EXISTS `tweets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tweets` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tweet` varchar(140) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_tweets_users1_idx` (`user_id`),
  CONSTRAINT `fk_tweets_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tweets`
--

LOCK TABLES `tweets` WRITE;
/*!40000 ALTER TABLE `tweets` DISABLE KEYS */;
INSERT INTO `tweets` VALUES (1,'There is power in understanding the journey of others to help create your own',1,'2002-02-01 00:00:01','2002-02-01 00:00:01'),(2,'Congrats Coach K! Amazing accomplishment #1KforCoachK #Duke',1,'2005-02-01 00:00:01','2005-02-01 00:00:01'),(3,'This is what happens when I pass too much! #ShoulderShock thank u all for ur thoughts and prayers #team @DrinkBODYARMOR @Lakers #oneluv',1,'2004-02-01 00:00:01','2004-02-01 00:00:01'),(4,'Feeling a mix of emotions I haven\'t felt in 18yrs of being a pro #journey #19th',1,'2012-02-01 00:00:01','2012-02-01 00:00:01'),(5,'Thank you everyone for the birthday wishes. I appreciate you all.',2,'2011-02-01 00:00:01','2011-02-01 00:00:01'),(6,'I\'d like to wish everyone a very Merry Christmas. 1 love to all \"Be Safe\"',2,'2009-02-01 00:00:01','2009-02-01 00:00:01'),(7,'Thanks to all who helped with the Christmas food baskets today. Your time is greatly appreciated. Love & Respect!! ',2,'2008-02-01 00:00:01','2008-02-01 00:00:01'),(8,'I took on the ALS Challenge from Monta Ellis. I challenge @coolkesh42 Jameer Nelson, Dionne Calhoun ... http://tmi.me/1eFAxT ',2,'2003-02-01 00:00:01','2003-02-01 00:00:01'),(9,'Well done lil bro, you deserve it!! @KingJames',3,'2006-02-01 00:00:01','2006-02-01 00:00:01'),(10,'For my basketball clinic with @manilacone 11/4/14, we still have a few slots left for the main game. See you all 11/5/14 Philippines',3,'2001-02-01 00:00:01','2001-02-01 00:00:01'),(11,'Always have a great time with my big little brother. ',4,'2011-02-01 00:00:01','2011-02-01 00:00:01'),(12,'Happy Labor Day..',4,'2014-02-01 00:00:01','2014-02-01 00:00:01');
/*!40000 ALTER TABLE `tweets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `handle` varchar(255) DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Kobe','Bryant','kobebryant','1978-08-23','2010-02-01 00:00:01','2011-07-01 00:00:01'),(2,'Vince','Carter','mrvincecarter15','1977-01-26','2007-08-11 00:00:01','2010-01-01 00:00:01'),(3,'Allen','Iverson','alleniverson','1975-06-07','2005-09-01 00:00:01','2011-04-21 00:00:01'),(4,'Tracy','McGrady','Real_T_Mac','1979-05-24','2002-12-01 00:00:01','2005-11-21 00:00:01'),(5,'Rajon','Rondo','RajonRondo','1986-02-22','2001-02-01 00:00:01','2002-01-01 00:00:01');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-03-19 16:48:20
