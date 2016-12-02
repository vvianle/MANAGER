-- MySQL dump 10.13  Distrib 5.7.12, for osx10.10 (x86_64)
--
-- Host: localhost    Database: CALENDAR
-- ------------------------------------------------------
-- Server version	5.7.12

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add my user',6,'add_myuser'),(17,'Can change my user',6,'change_myuser'),(18,'Can delete my user',6,'delete_myuser'),(19,'Can add one auth token',7,'add_oneauthtoken'),(20,'Can change one auth token',7,'change_oneauthtoken'),(21,'Can delete one auth token',7,'delete_oneauthtoken'),(22,'Can add holiday',8,'add_holiday'),(23,'Can change holiday',8,'change_holiday'),(24,'Can delete holiday',8,'delete_holiday'),(25,'Can add exceptional lunch day',9,'add_exceptionallunchday'),(26,'Can change exceptional lunch day',9,'change_exceptionallunchday'),(27,'Can delete exceptional lunch day',9,'delete_exceptionallunchday'),(28,'Can add personal default lunch schedule',10,'add_personaldefaultlunchschedule'),(29,'Can change personal default lunch schedule',10,'change_personaldefaultlunchschedule'),(30,'Can delete personal default lunch schedule',10,'delete_personaldefaultlunchschedule'),(31,'Can add daily lunch request',11,'add_dailylunchrequest'),(32,'Can change daily lunch request',11,'change_dailylunchrequest'),(33,'Can delete daily lunch request',11,'delete_dailylunchrequest'),(34,'Can add personal monthly lunch order',12,'add_personalmonthlylunchorder'),(35,'Can change personal monthly lunch order',12,'change_personalmonthlylunchorder'),(36,'Can delete personal monthly lunch order',12,'delete_personalmonthlylunchorder'),(37,'Can add meal price',13,'add_mealprice'),(38,'Can change meal price',13,'change_mealprice'),(39,'Can delete meal price',13,'delete_mealprice'),(40,'Can add month calendar',14,'add_monthcalendar'),(41,'Can change month calendar',14,'change_monthcalendar'),(42,'Can delete month calendar',14,'delete_monthcalendar'),(43,'Can add monthly working schedule',15,'add_monthlyworkingschedule'),(44,'Can change monthly working schedule',15,'change_monthlyworkingschedule'),(45,'Can delete monthly working schedule',15,'delete_monthlyworkingschedule'),(46,'Can add personal working schedule',16,'add_personalworkingschedule'),(47,'Can change personal working schedule',16,'change_personalworkingschedule'),(48,'Can delete personal working schedule',16,'delete_personalworkingschedule'),(49,'Can add working calendar',17,'add_workingcalendar'),(50,'Can change working calendar',17,'change_workingcalendar'),(51,'Can delete working calendar',17,'delete_workingcalendar'),(52,'Can add exceptional working day',18,'add_exceptionalworkingday'),(53,'Can change exceptional working day',18,'change_exceptionalworkingday'),(54,'Can delete exceptional working day',18,'delete_exceptionalworkingday'),(58,'Can add cors model',20,'add_corsmodel'),(59,'Can change cors model',20,'change_corsmodel'),(60,'Can delete cors model',20,'delete_corsmodel'),(61,'Can add cron job log',21,'add_cronjoblog'),(62,'Can change cron job log',21,'change_cronjoblog'),(63,'Can delete cron job log',21,'delete_cronjoblog'),(64,'Can add personal default working request',22,'add_personaldefaultworkingrequest'),(65,'Can change personal default working request',22,'change_personaldefaultworkingrequest'),(66,'Can delete personal default working request',22,'delete_personaldefaultworkingrequest');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_one_users_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_one_users_id` FOREIGN KEY (`user_id`) REFERENCES `one_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2016-07-20 12:53:04.712869','1','vivianle',2,'Changed has_working_schedule.',6,1),(2,'2016-07-20 13:09:18.706904','1','2016-7',3,'',17,1),(3,'2016-07-21 03:37:05.548083','2','linh',1,'Added.',6,1),(4,'2016-07-21 03:37:21.357227','2','linh',2,'Changed sun_morning, tue, wed and thu.',NULL,1),(5,'2016-07-21 07:43:38.718188','1','2016-7',3,'',14,1),(6,'2016-07-21 07:43:56.732773','1','vivianle',2,'Changed mon, tue, wed, thu and fri.',10,1),(7,'2016-07-21 07:44:02.764345','2','linh',2,'Changed mon, tue, wed, thu and fri.',10,1),(8,'2016-07-21 07:46:28.069762','2','2016-7',3,'',14,1),(9,'2016-07-21 07:48:14.880157','3','2016-07-21',3,'',11,1),(10,'2016-07-21 07:49:49.156642','4','2016-07-21',3,'',11,1),(11,'2016-07-21 07:50:23.387865','5','2016-07-21',3,'',11,1),(12,'2016-07-21 07:52:22.316682','6','2016-07-21',3,'',11,1),(13,'2016-07-21 07:55:21.748935','7','2016-07-21',3,'',11,1),(14,'2016-07-21 07:56:22.602514','8','2016-07-21',3,'',11,1),(15,'2016-07-21 07:57:59.649785','10','2016-07-21',3,'',11,1),(16,'2016-07-21 07:59:02.063721','11','2016-07-21',3,'',11,1),(17,'2016-07-21 07:59:16.523036','12','2016-07-21',3,'',11,1),(18,'2016-07-21 08:08:56.510995','13','2016-07-21',3,'',11,1),(19,'2016-07-21 08:10:55.753199','3','2016-7',3,'',14,1),(20,'2016-07-22 01:28:38.821233','4','2016-7',3,'',14,1),(21,'2016-07-22 01:58:32.047430','5','2016-7',3,'',14,1),(22,'2016-07-22 01:58:37.307331','16','2016-07-22',3,'',11,1),(23,'2016-07-27 03:52:47.236121','2','linh',2,'Changed is_admin.',6,1),(24,'2016-07-27 03:52:55.987531','2','linh',2,'Changed is_admin.',6,1),(25,'2016-07-27 04:19:25.321947','2','linh',2,'Changed has_working_schedule.',6,1),(26,'2016-07-27 04:21:18.246130','2','linh',2,'Changed has_working_schedule.',6,1),(27,'2016-07-27 04:21:29.776865','2','linh',2,'Changed has_working_schedule.',6,1),(28,'2016-07-27 04:21:38.713819','2','linh',2,'Changed has_working_schedule.',6,1),(29,'2016-08-02 04:22:51.679355','3','2016-08-02',3,'',15,1),(30,'2016-08-02 04:26:10.972518','4','2016-08-02',3,'',15,1),(31,'2016-08-05 12:49:58.444202','19','thuanlv 2016-7',3,'',16,1),(32,'2016-08-05 12:49:58.446744','18','anhv 2016-7',3,'',16,1),(33,'2016-08-05 12:49:58.448163','17','tuanlm 2016-7',3,'',16,1),(34,'2016-08-05 12:49:58.449773','16','hiepdx 2016-7',3,'',16,1),(35,'2016-08-05 12:49:58.451605','15','linhba 2016-7',3,'',16,1),(36,'2016-08-05 12:49:58.453068','14','cuongbd 2016-7',3,'',16,1),(37,'2016-08-05 12:49:58.454537','13','toantv 2016-7',3,'',16,1),(38,'2016-08-05 12:49:58.456139','12','thuanlv 2016-8',3,'',16,1),(39,'2016-08-05 12:49:58.458370','11','anhv 2016-8',3,'',16,1),(40,'2016-08-05 12:49:58.461280','10','tuanlm 2016-8',3,'',16,1),(41,'2016-08-05 12:49:58.463576','9','hiepdx 2016-8',3,'',16,1),(42,'2016-08-05 12:49:58.466555','8','linhba 2016-8',3,'',16,1),(43,'2016-08-05 12:49:58.470442','7','cuongbd 2016-8',3,'',16,1),(44,'2016-08-05 12:49:58.472629','6','toantv 2016-8',3,'',16,1),(45,'2016-08-05 12:49:58.474070','5','linh 2016-8',3,'',16,1),(46,'2016-08-05 12:49:58.475698','4','vivianle 2016-8',3,'',16,1),(47,'2016-08-05 12:49:58.477367','3','linh 2016-7',3,'',16,1),(48,'2016-08-05 12:49:58.478856','2','vivianle 2016-7',3,'',16,1),(50,'2016-08-08 02:54:55.796471','2','linh',2,'No fields changed.',6,1),(51,'2016-08-08 02:55:19.724897','2','linh',2,'No fields changed.',6,1),(52,'2016-08-08 03:01:43.204690','2','linh',2,'Changed is_active.',6,1),(53,'2016-08-08 03:02:50.496393','2','linh',2,'No fields changed.',6,1),(54,'2016-08-08 03:04:54.841691','2','linh',2,'Changed is_active.',6,1),(55,'2016-08-08 03:08:06.097895','3','1234',3,'',6,1),(56,'2016-08-08 03:08:06.100688','12','abc',3,'',6,1),(57,'2016-08-08 03:26:53.061439','13','abc',3,'',6,1),(62,'2016-08-09 01:20:42.381632','22','2016-08-09',3,'',11,1),(63,'2016-08-09 01:21:34.115202','24','2016-08-09',3,'',11,1),(64,'2016-08-09 01:22:26.082994','10','linh 2016-8',2,'Changed orderDays, numMeal and totalPrice.',12,1),(65,'2016-08-09 01:22:29.951075','9','vivianle 2016-8',2,'No fields changed.',12,1),(66,'2016-08-09 05:11:39.147822','2','2016-7',3,'',17,1),(67,'2016-08-09 05:12:09.282292','8','2016-10',3,'',17,1),(68,'2016-08-09 05:13:56.152391','9','2016-10',3,'',17,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (6,'accounts','myuser'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(20,'corsheaders','corsmodel'),(21,'django_cron','cronjoblog'),(8,'holidays','holiday'),(11,'lunch','dailylunchrequest'),(9,'lunch','exceptionallunchday'),(13,'lunch','mealprice'),(14,'lunch','monthcalendar'),(10,'lunch','personaldefaultlunchschedule'),(12,'lunch','personalmonthlylunchorder'),(7,'one_auth','oneauthtoken'),(18,'schedule','exceptionalworkingday'),(15,'schedule','monthlyworkingschedule'),(22,'schedule','personaldefaultworkingrequest'),(16,'schedule','personalworkingschedule'),(17,'schedule','workingcalendar'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_cron_cronjoblog`
--

DROP TABLE IF EXISTS `django_cron_cronjoblog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_cron_cronjoblog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(64) NOT NULL,
  `start_time` datetime(6) NOT NULL,
  `end_time` datetime(6) NOT NULL,
  `is_success` tinyint(1) NOT NULL,
  `message` longtext NOT NULL,
  `ran_at_time` time(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `django_cron_cronjoblog_code_84da9606_idx` (`code`,`is_success`,`ran_at_time`),
  KEY `django_cron_cronjoblog_code_8b50b8fa_idx` (`code`,`start_time`,`ran_at_time`),
  KEY `django_cron_cronjoblog_code_4fc78f9d_idx` (`code`,`start_time`),
  KEY `django_cron_cronjoblog_c1336794` (`code`),
  KEY `django_cron_cronjoblog_c4d98dbd` (`start_time`),
  KEY `django_cron_cronjoblog_305d2889` (`end_time`),
  KEY `django_cron_cronjoblog_a05e4b70` (`ran_at_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_cron_cronjoblog`
--

LOCK TABLES `django_cron_cronjoblog` WRITE;
/*!40000 ALTER TABLE `django_cron_cronjoblog` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_cron_cronjoblog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2016-07-20 02:58:53.512949'),(2,'contenttypes','0002_remove_content_type_name','2016-07-20 02:58:53.551242'),(3,'auth','0001_initial','2016-07-20 02:58:53.700693'),(4,'auth','0002_alter_permission_name_max_length','2016-07-20 02:58:53.728540'),(5,'auth','0003_alter_user_email_max_length','2016-07-20 02:58:53.736476'),(6,'auth','0004_alter_user_username_opts','2016-07-20 02:58:53.744591'),(7,'auth','0005_alter_user_last_login_null','2016-07-20 02:58:53.751719'),(8,'auth','0006_require_contenttypes_0002','2016-07-20 02:58:53.754093'),(9,'auth','0007_alter_validators_add_error_messages','2016-07-20 02:58:53.761716'),(10,'accounts','0001_initial','2016-07-20 02:58:53.918040'),(11,'accounts','0002_auto_20160718_1144','2016-07-20 02:58:53.961761'),(12,'admin','0001_initial','2016-07-20 02:58:54.039225'),(13,'admin','0002_logentry_remove_auto_add','2016-07-20 02:58:54.081362'),(14,'holidays','0001_initial','2016-07-20 02:58:54.122955'),(15,'holidays','0002_auto_20160720_0958','2016-07-20 02:58:54.184098'),(16,'lunch','0001_initial','2016-07-20 02:58:54.690783'),(17,'lunch','0002_auto_20160720_0958','2016-07-20 02:58:54.721501'),(18,'one_auth','0001_initial','2016-07-20 02:58:54.773273'),(19,'one_auth','0002_auto_20160705_1126','2016-07-20 02:58:54.793790'),(20,'schedule','0001_initial','2016-07-20 02:58:55.420825'),(21,'schedule','0002_auto_20160718_1553','2016-07-20 02:58:55.482987'),(22,'sessions','0001_initial','2016-07-20 02:58:55.517393'),(23,'django_cron','0001_initial','2016-07-21 08:35:57.202819'),(24,'django_cron','0002_remove_max_length_from_CronJobLog_message','2016-07-21 08:35:57.208640'),(25,'holidays','0003_auto_20160802_1125','2016-08-02 04:25:55.560027'),(26,'lunch','0003_auto_20160802_1125','2016-08-02 04:25:55.725166'),(27,'schedule','0003_auto_20160802_1125','2016-08-02 04:25:55.959997'),(28,'holidays','0004_auto_20160808_1723','2016-08-08 10:23:50.589781'),(29,'lunch','0004_auto_20160808_1723','2016-08-08 10:23:50.730790'),(30,'schedule','0004_auto_20160808_1723','2016-08-08 10:23:51.038543'),(31,'schedule','0005_auto_20160808_1733','2016-08-08 10:33:13.021795'),(32,'schedule','0006_auto_20160808_1733','2016-08-08 10:33:49.432215'),(33,'schedule','0007_auto_20160808_1735','2016-08-08 10:35:29.741118'),(34,'schedule','0008_auto_20160808_1736','2016-08-08 10:36:07.405936'),(35,'schedule','0009_auto_20160808_2118','2016-08-08 14:18:37.417810'),(36,'holidays','0005_auto_20160810_0834','2016-08-10 01:34:39.365283'),(37,'lunch','0005_auto_20160810_0834','2016-08-10 01:34:39.509525');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('3ql33l6qdxqfajbxv7ulnq30u3ybztok','NTEyZWI5OTkxOWI3MGNmMDQ4NzI0NTQxY2EyMGU1NmU4NTIyMzc1Mjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiNjRjMmI5NDU3NTRlMzYxYjdkYjc5NTdkM2U4OWI3OTFmNTMzMTBkNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2016-08-22 11:14:37.791788');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `holidays_holiday`
--

DROP TABLE IF EXISTS `holidays_holiday`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `holidays_holiday` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `startDate` date NOT NULL,
  `endDate` date NOT NULL,
  `noLunch` tinyint(1) NOT NULL,
  `noWorking` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `holidays_holiday_startDate_4a057059_uniq` (`startDate`,`endDate`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `holidays_holiday`
--

LOCK TABLES `holidays_holiday` WRITE;
/*!40000 ALTER TABLE `holidays_holiday` DISABLE KEYS */;
/*!40000 ALTER TABLE `holidays_holiday` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lunch_dailylunchrequest`
--

DROP TABLE IF EXISTS `lunch_dailylunchrequest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lunch_dailylunchrequest` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `totalOrders` int(11) NOT NULL,
  `price` int(11) DEFAULT NULL,
  `calendar_id` int(11),
  PRIMARY KEY (`id`),
  UNIQUE KEY `date` (`date`),
  KEY `lunch_dailylunchrequest_df2e10dc` (`calendar_id`),
  CONSTRAINT `lunch_dailylunchr_calendar_id_08f03b1b_fk_lunch_monthcalendar_id` FOREIGN KEY (`calendar_id`) REFERENCES `lunch_monthcalendar` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lunch_dailylunchrequest`
--

LOCK TABLES `lunch_dailylunchrequest` WRITE;
/*!40000 ALTER TABLE `lunch_dailylunchrequest` DISABLE KEYS */;
INSERT INTO `lunch_dailylunchrequest` VALUES (17,'2016-07-22',2,25000,6),(18,'2016-08-08',2,25000,7),(25,'2016-08-09',1,25000,7),(27,'2016-08-10',2,25000,7);
/*!40000 ALTER TABLE `lunch_dailylunchrequest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lunch_dailylunchrequest_users`
--

DROP TABLE IF EXISTS `lunch_dailylunchrequest_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lunch_dailylunchrequest_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dailylunchrequest_id` int(11) NOT NULL,
  `myuser_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `lunch_dailylunchrequest_users_dailylunchrequest_id_1598ad15_uniq` (`dailylunchrequest_id`,`myuser_id`),
  KEY `lunch_dailylunchrequest_users_myuser_id_df6fd74a_fk_one_users_id` (`myuser_id`),
  CONSTRAINT `lunc_dailylunchrequest_id_22dbd65a_fk_lunch_dailylunchrequest_id` FOREIGN KEY (`dailylunchrequest_id`) REFERENCES `lunch_dailylunchrequest` (`id`),
  CONSTRAINT `lunch_dailylunchrequest_users_myuser_id_df6fd74a_fk_one_users_id` FOREIGN KEY (`myuser_id`) REFERENCES `one_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lunch_dailylunchrequest_users`
--

LOCK TABLES `lunch_dailylunchrequest_users` WRITE;
/*!40000 ALTER TABLE `lunch_dailylunchrequest_users` DISABLE KEYS */;
INSERT INTO `lunch_dailylunchrequest_users` VALUES (27,17,1),(28,17,2),(29,18,1),(30,18,2),(33,25,2),(34,27,2),(35,27,4);
/*!40000 ALTER TABLE `lunch_dailylunchrequest_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lunch_exceptionallunchday`
--

DROP TABLE IF EXISTS `lunch_exceptionallunchday`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lunch_exceptionallunchday` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `addDay` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `lunch_exceptionallunchday_user_id_1a3afaff_uniq` (`user_id`,`date`),
  CONSTRAINT `lunch_exceptionallunchday_user_id_3b7aaa7b_fk_one_users_id` FOREIGN KEY (`user_id`) REFERENCES `one_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lunch_exceptionallunchday`
--

LOCK TABLES `lunch_exceptionallunchday` WRITE;
/*!40000 ALTER TABLE `lunch_exceptionallunchday` DISABLE KEYS */;
INSERT INTO `lunch_exceptionallunchday` VALUES (8,'2016-08-17',1,1);
/*!40000 ALTER TABLE `lunch_exceptionallunchday` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lunch_mealprice`
--

DROP TABLE IF EXISTS `lunch_mealprice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lunch_mealprice` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `price` int(11) NOT NULL,
  `inUse` tinyint(1) NOT NULL,
  `startDate` date NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `startDate` (`startDate`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lunch_mealprice`
--

LOCK TABLES `lunch_mealprice` WRITE;
/*!40000 ALTER TABLE `lunch_mealprice` DISABLE KEYS */;
INSERT INTO `lunch_mealprice` VALUES (8,25000,1,'2016-08-10');
/*!40000 ALTER TABLE `lunch_mealprice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lunch_monthcalendar`
--

DROP TABLE IF EXISTS `lunch_monthcalendar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lunch_monthcalendar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` int(11) NOT NULL,
  `month` int(11) NOT NULL,
  `calendar` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `lunch_monthcalendar_year_747035e6_uniq` (`year`,`month`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lunch_monthcalendar`
--

LOCK TABLES `lunch_monthcalendar` WRITE;
/*!40000 ALTER TABLE `lunch_monthcalendar` DISABLE KEYS */;
INSERT INTO `lunch_monthcalendar` VALUES (6,2016,7,'[[\"\", \"\", \"\", \"\", \"\", \"1\", \"2\"], [\"3\", \"4\", \"5\", \"6\", \"7\", \"8\", \"9\"], [\"10\", \"11\", \"12\", \"13\", \"14\", \"15\", \"16\"], [\"17\", \"18\", \"19\", \"20\", \"21\", \"22\", \"23\"], [\"24\", \"25\", \"26\", \"27\", \"28\", \"29\", \"30\"], [\"31\", \"\", \"\", \"\", \"\", \"\", \"\"]]'),(7,2016,8,'[[\"\", \"1\", \"2\", \"3\", \"4\", \"5\", \"6\"], [\"7\", \"8\", \"9\", \"10\", \"11\", \"12\", \"13\"], [\"14\", \"15\", \"16\", \"17\", \"18\", \"19\", \"20\"], [\"21\", \"22\", \"23\", \"24\", \"25\", \"26\", \"27\"], [\"28\", \"29\", \"30\", \"31\", \"\", \"\", \"\"]]');
/*!40000 ALTER TABLE `lunch_monthcalendar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lunch_personaldefaultlunchschedule`
--

DROP TABLE IF EXISTS `lunch_personaldefaultlunchschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lunch_personaldefaultlunchschedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mon` tinyint(1) NOT NULL,
  `tue` tinyint(1) NOT NULL,
  `wed` tinyint(1) NOT NULL,
  `thu` tinyint(1) NOT NULL,
  `fri` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `lunch_personaldefaultlunchsched_user_id_3a18230a_fk_one_users_id` FOREIGN KEY (`user_id`) REFERENCES `one_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lunch_personaldefaultlunchschedule`
--

LOCK TABLES `lunch_personaldefaultlunchschedule` WRITE;
/*!40000 ALTER TABLE `lunch_personaldefaultlunchschedule` DISABLE KEYS */;
INSERT INTO `lunch_personaldefaultlunchschedule` VALUES (1,1,1,0,1,1,1),(2,1,1,1,1,1,2),(4,0,0,1,0,0,4),(5,0,0,0,0,0,5),(6,0,0,0,0,0,6),(7,0,0,0,0,0,7),(8,0,0,0,0,0,8),(9,0,0,0,0,0,9),(10,0,0,0,0,0,10),(11,0,0,0,0,0,11);
/*!40000 ALTER TABLE `lunch_personaldefaultlunchschedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lunch_personalmonthlylunchorder`
--

DROP TABLE IF EXISTS `lunch_personalmonthlylunchorder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lunch_personalmonthlylunchorder` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` int(11) NOT NULL,
  `month` int(11) NOT NULL,
  `orderDays` varchar(400) DEFAULT NULL,
  `numMeal` int(11) NOT NULL,
  `totalPrice` int(11) NOT NULL,
  `calendar_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `lunch_personalmonthlylunchorder_user_id_8f48e087_uniq` (`user_id`,`month`,`year`),
  KEY `lunch_personalmon_calendar_id_53a60085_fk_lunch_monthcalendar_id` (`calendar_id`),
  CONSTRAINT `lunch_personalmon_calendar_id_53a60085_fk_lunch_monthcalendar_id` FOREIGN KEY (`calendar_id`) REFERENCES `lunch_monthcalendar` (`id`),
  CONSTRAINT `lunch_personalmonthlylunchorder_user_id_3db6646b_fk_one_users_id` FOREIGN KEY (`user_id`) REFERENCES `one_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lunch_personalmonthlylunchorder`
--

LOCK TABLES `lunch_personalmonthlylunchorder` WRITE;
/*!40000 ALTER TABLE `lunch_personalmonthlylunchorder` DISABLE KEYS */;
INSERT INTO `lunch_personalmonthlylunchorder` VALUES (7,2016,7,'22',1,25000,6,1),(8,2016,7,'22',1,25000,6,2),(9,2016,8,'8',1,25000,7,1),(10,2016,8,'8,9,10',3,75000,7,2),(11,2016,8,'10',1,25000,7,4);
/*!40000 ALTER TABLE `lunch_personalmonthlylunchorder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `one_authentication`
--

DROP TABLE IF EXISTS `one_authentication`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `one_authentication` (
  `digest` varchar(128) NOT NULL,
  `salt` varchar(16) NOT NULL,
  `created` datetime(6) NOT NULL,
  `expires` datetime(6) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`digest`),
  UNIQUE KEY `salt` (`salt`),
  KEY `one_authen_user_id_9341440b_fk_one_users_id` (`user_id`),
  CONSTRAINT `one_authen_user_id_9341440b_fk_one_users_id` FOREIGN KEY (`user_id`) REFERENCES `one_users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `one_authentication`
--

LOCK TABLES `one_authentication` WRITE;
/*!40000 ALTER TABLE `one_authentication` DISABLE KEYS */;
INSERT INTO `one_authentication` VALUES ('aaea63848847fa4c333bdb0ed95dbe50e4da81eb2a06d13f7bb072def8bbb19a11d7996deb500fa603553dc365b4f44c5c3d378715c221bca5992085402865a0','05ac3e0003e65511','2016-08-10 03:47:40.015213','2016-08-10 13:47:40.013946',1),('c78cf40792aac9e9ec6c4af6dc411bff8bc39e9b4d086b46106b9e1ad25d67c8766aaaab07c2ab0b9b5d5ab02014077dada3d297e1223aee06ff54b8287d2132','5b29969bcb0f1a4f','2016-08-10 02:54:58.221626','2016-08-10 12:54:58.220761',1);
/*!40000 ALTER TABLE `one_authentication` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `one_users`
--

DROP TABLE IF EXISTS `one_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `one_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `email` varchar(255) NOT NULL,
  `username` varchar(100) NOT NULL,
  `fullname` varchar(255) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  `has_working_schedule` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `one_users`
--

LOCK TABLES `one_users` WRITE;
/*!40000 ALTER TABLE `one_users` DISABLE KEYS */;
INSERT INTO `one_users` VALUES (1,'pbkdf2_sha256$24000$GhZX3WOc2NVo$uIk0rY4SVFdKzsL23zkyLVjj6q/MwCfakb0k+geeRt4=','2016-08-10 03:47:40.017357',0,'le27l@mtholyoke.edu','vivianle','bbaaaaa','2016-07-20 03:00:04.403195',1,1,1),(2,'pbkdf2_sha256$24000$YMQC6bKpaYzN$LN/dh8cfNkaAriy4PRDNsT73/iv5CGPNH3/hsxTSwFQ=','2016-08-10 02:04:05.704378',0,'linh@linh.com','linh','hahaha123','2016-07-21 03:37:05.456421',1,0,1),(4,'pbkdf2_sha256$24000$mr6Pvzz9w7eg$6947C6kcncIS/geRVjbGYhAUm/MH2v5Jo5pgH7bv4ds=','2016-08-03 02:06:31.388082',0,'toantv@mvs.vn','toantv','Tong Van Toan','2016-08-03 01:53:00.379486',1,0,1),(5,'pbkdf2_sha256$24000$9sD0Ea9nKmO1$wVQk827quM9Am2pfj7GkE5naFBPBi4Ewyy/tvxGH+M8=',NULL,0,'cuongbd@mvs.vn','cuongbd','Bùi Đình Cường','2016-08-03 02:16:08.731820',1,0,1),(6,'pbkdf2_sha256$24000$XoOaaGVoMo4d$5/vpsFxPcgo7P3983+3ERyMGZi/D7FEJg2u7+ZpcCVk=',NULL,0,'linhba@mvs.vn','linhba','Bùi Anh Linh','2016-08-03 02:16:40.252210',1,0,1),(7,'pbkdf2_sha256$24000$sER6zEmq0H4N$dyaWSUE4KeeoQ3lxYcSm+rZZsnHpZ8O/rn+GESmD9z8=',NULL,0,'hiepdx@mvs.vn','hiepdx','Dương Xuân Hiệp','2016-08-03 02:17:12.918971',1,0,1),(8,'pbkdf2_sha256$24000$RDmGMv0MEry3$GOkSUjW2rZrVVcfuECoOUaLVgklj6bRKxg4SbFiJSis=',NULL,0,'tuanlm@mvs.vn','tuanlm','Lê Minh Tuấn','2016-08-03 02:17:35.428746',1,0,1),(9,'pbkdf2_sha256$24000$4taynlQhPDYO$CTrGQOYHQ696KDh6T0t65xBQwGJmWnT6Uad6cz24ckQ=',NULL,0,'dainc@mvs.vn','dainc','Ngô Cao Đại','2016-08-03 02:51:22.708198',1,0,0),(10,'pbkdf2_sha256$24000$edRIWk8BTpLu$P0UfVbiXlU2uLAN3isTqYTRcxH23GtcVP9R5pc9S3Ls=',NULL,0,'anhv@mvs.vn','anhv','Vũ Anh','2016-08-03 02:53:13.024780',1,0,1),(11,'pbkdf2_sha256$24000$ZCO55KeYITM2$amb2U9yhAsIeOS4ZxeF+mrx8OFinOr56+FijLRLDuTc=',NULL,0,'thuanlv@mvs.vn','thuanlv','Lê Văn Thuần','2016-08-03 02:54:09.089434',1,0,1);
/*!40000 ALTER TABLE `one_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `one_users_groups`
--

DROP TABLE IF EXISTS `one_users_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `one_users_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `myuser_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `one_users_groups_myuser_id_509643a3_uniq` (`myuser_id`,`group_id`),
  KEY `one_users_groups_group_id_bc0b0b9e_fk_auth_group_id` (`group_id`),
  CONSTRAINT `one_users_groups_group_id_bc0b0b9e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `one_users_groups_myuser_id_4be07305_fk_one_users_id` FOREIGN KEY (`myuser_id`) REFERENCES `one_users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `one_users_groups`
--

LOCK TABLES `one_users_groups` WRITE;
/*!40000 ALTER TABLE `one_users_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `one_users_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `one_users_user_permissions`
--

DROP TABLE IF EXISTS `one_users_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `one_users_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `myuser_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `one_users_user_permissions_myuser_id_d5728dda_uniq` (`myuser_id`,`permission_id`),
  KEY `one_users_user_perm_permission_id_c3733b3f_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `one_users_user_perm_permission_id_c3733b3f_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `one_users_user_permissions_myuser_id_bbfe7f04_fk_one_users_id` FOREIGN KEY (`myuser_id`) REFERENCES `one_users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `one_users_user_permissions`
--

LOCK TABLES `one_users_user_permissions` WRITE;
/*!40000 ALTER TABLE `one_users_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `one_users_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schedule_exceptionalworkingday`
--

DROP TABLE IF EXISTS `schedule_exceptionalworkingday`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schedule_exceptionalworkingday` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `addDay` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `schedule_exceptionalworkingday_user_id_66f9b493_uniq` (`user_id`,`date`),
  CONSTRAINT `schedule_exceptionalworkingday_user_id_928b9add_fk_one_users_id` FOREIGN KEY (`user_id`) REFERENCES `one_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schedule_exceptionalworkingday`
--

LOCK TABLES `schedule_exceptionalworkingday` WRITE;
/*!40000 ALTER TABLE `schedule_exceptionalworkingday` DISABLE KEYS */;
INSERT INTO `schedule_exceptionalworkingday` VALUES (3,'2016-08-10',1,1),(4,'2016-08-17',1,1);
/*!40000 ALTER TABLE `schedule_exceptionalworkingday` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schedule_monthlyworkingschedule`
--

DROP TABLE IF EXISTS `schedule_monthlyworkingschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schedule_monthlyworkingschedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `startDate` date DEFAULT NULL,
  `month` int(11),
  `year` int(11),
  `schedule` varchar(1000) DEFAULT NULL,
  `nextStartDate` date DEFAULT NULL,
  `calendar_id` int(11),
  PRIMARY KEY (`id`),
  UNIQUE KEY `schedule_monthlyworkingschedule_month_13e5abe0_uniq` (`month`,`year`),
  KEY `schedule_monthlyworkingschedule_df2e10dc` (`calendar_id`),
  CONSTRAINT `schedule_mon_calendar_id_9dffd6d2_fk_schedule_workingcalendar_id` FOREIGN KEY (`calendar_id`) REFERENCES `schedule_workingcalendar` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schedule_monthlyworkingschedule`
--

LOCK TABLES `schedule_monthlyworkingschedule` WRITE;
/*!40000 ALTER TABLE `schedule_monthlyworkingschedule` DISABLE KEYS */;
INSERT INTO `schedule_monthlyworkingschedule` VALUES (5,'2016-08-02',8,2016,'[[\"\",\"\",\"cuongbd\",\"linh\",\"vivianle\",\"linh\",\"vivianle\"],[\"OPEN | linh\",\"linh\",\"vivianle\",\"linh\",\"vivianle\",\"linh\",\"vivianle\"],[\"vivianle | linh\",\"linh\",\"vivianle\",\"linh\",\"vivianle\",\"linh\",\"vivianle\"],[\"vivianle | linh\",\"linh\",\"vivianle\",\"linh\",\"vivianle\",\"linh\",\"vivianle\"],[\"vivianle | linh\",\"linh\",\"vivianle\",\"linh\",\"\",\"\",\"\"]]','2016-09-01',3),(9,'2016-09-01',9,2016,'[[\"\", \"\", \"\", \"\", \"linhba\", \"anhv\", \"toantv\"], [\"cuongbd | linhba\", \"thuanlv\", \"anhv\", \"hiepdx\", \"toantv\", \"thuanlv\", \"hiepdx\"], [\"tuanlm | anhv\", \"cuongbd\", \"hiepdx\", \"toantv\", \"linhba\", \"tuanlm\", \"thuanlv\"], [\"toantv | cuongbd\", \"hiepdx\", \"thuanlv\", \"anhv\", \"tuanlm\", \"cuongbd\", \"linhba\"], [\"hiepdx | tuanlm\", \"toantv\", \"linhba\", \"thuanlv\", \"tuanlm\", \"cuongbd\", \"anhv\"]]','2016-10-02',7);
/*!40000 ALTER TABLE `schedule_monthlyworkingschedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schedule_monthlyworkingschedule_users`
--

DROP TABLE IF EXISTS `schedule_monthlyworkingschedule_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schedule_monthlyworkingschedule_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `monthlyworkingschedule_id` int(11) NOT NULL,
  `myuser_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `schedule_monthlyworkings_monthlyworkingschedule_id_93dc623f_uniq` (`monthlyworkingschedule_id`,`myuser_id`),
  KEY `schedule_monthlyworkingschedu_myuser_id_0bae5562_fk_one_users_id` (`myuser_id`),
  CONSTRAINT `D8d7c68a2e8ce857f972a34b20a0c95f` FOREIGN KEY (`monthlyworkingschedule_id`) REFERENCES `schedule_monthlyworkingschedule` (`id`),
  CONSTRAINT `schedule_monthlyworkingschedu_myuser_id_0bae5562_fk_one_users_id` FOREIGN KEY (`myuser_id`) REFERENCES `one_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schedule_monthlyworkingschedule_users`
--

LOCK TABLES `schedule_monthlyworkingschedule_users` WRITE;
/*!40000 ALTER TABLE `schedule_monthlyworkingschedule_users` DISABLE KEYS */;
INSERT INTO `schedule_monthlyworkingschedule_users` VALUES (8,5,1),(9,5,2),(10,5,4),(11,5,5),(39,9,4),(40,9,5),(41,9,6),(42,9,7),(43,9,8),(44,9,10),(45,9,11);
/*!40000 ALTER TABLE `schedule_monthlyworkingschedule_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schedule_personaldefaultworkingrequest`
--

DROP TABLE IF EXISTS `schedule_personaldefaultworkingrequest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schedule_personaldefaultworkingrequest` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sun_morning` tinyint(1) NOT NULL,
  `sun_evening` tinyint(1) NOT NULL,
  `mon` tinyint(1) NOT NULL,
  `tue` tinyint(1) NOT NULL,
  `wed` tinyint(1) NOT NULL,
  `thu` tinyint(1) NOT NULL,
  `fri` tinyint(1) NOT NULL,
  `sat` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `schedule_personaldefaultworking_user_id_7713d750_fk_one_users_id` FOREIGN KEY (`user_id`) REFERENCES `one_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schedule_personaldefaultworkingrequest`
--

LOCK TABLES `schedule_personaldefaultworkingrequest` WRITE;
/*!40000 ALTER TABLE `schedule_personaldefaultworkingrequest` DISABLE KEYS */;
INSERT INTO `schedule_personaldefaultworkingrequest` VALUES (1,0,0,1,0,0,0,1,0,1),(2,1,0,0,1,0,1,0,0,2),(4,1,1,1,1,1,1,1,1,4),(5,1,1,1,1,1,1,1,1,5),(6,1,1,1,1,1,1,1,1,6),(7,1,1,1,1,1,1,1,1,7),(8,1,1,1,1,1,1,1,1,8),(9,0,0,0,0,0,0,0,0,9),(10,1,1,1,1,1,1,1,1,10),(11,1,1,1,1,1,1,1,1,11);
/*!40000 ALTER TABLE `schedule_personaldefaultworkingrequest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schedule_personalworkingschedule`
--

DROP TABLE IF EXISTS `schedule_personalworkingschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schedule_personalworkingschedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` int(11) NOT NULL,
  `month` int(11) NOT NULL,
  `personalSchedule` varchar(500) NOT NULL,
  `calendar_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `schedule_personalworkingschedule_user_id_72dcbc11_uniq` (`user_id`,`month`,`year`),
  KEY `schedule_personalworkingschedule_df2e10dc` (`calendar_id`),
  KEY `schedule_personalworkingschedule_e8701ad4` (`user_id`),
  CONSTRAINT `schedule_per_calendar_id_19b9e782_fk_schedule_workingcalendar_id` FOREIGN KEY (`calendar_id`) REFERENCES `schedule_workingcalendar` (`id`),
  CONSTRAINT `schedule_personalworkingschedul_user_id_c8635059_fk_one_users_id` FOREIGN KEY (`user_id`) REFERENCES `one_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schedule_personalworkingschedule`
--

LOCK TABLES `schedule_personalworkingschedule` WRITE;
/*!40000 ALTER TABLE `schedule_personalworkingschedule` DISABLE KEYS */;
INSERT INTO `schedule_personalworkingschedule` VALUES (20,2016,8,'[\"2016-08-03\", \"2016-08-05\", \"2016-08-07 Evening\", \"2016-08-08\", \"2016-08-10\", \"2016-08-12\", \"2016-08-14 Evening\", \"2016-08-15\", \"2016-08-17\", \"2016-08-19\", \"2016-08-21 Evening\", \"2016-08-22\", \"2016-08-24\", \"2016-08-26\", \"2016-08-28 Evening\", \"2016-08-29\", \"2016-08-31\"]',3,2),(21,2016,8,'[\"2016-08-04\", \"2016-08-06\", \"2016-08-09\", \"2016-08-11\", \"2016-08-13\", \"2016-08-14 Morning\", \"2016-08-16\", \"2016-08-18\", \"2016-08-20\", \"2016-08-21 Morning\", \"2016-08-23\", \"2016-08-25\", \"2016-08-27\", \"2016-08-28 Morning\", \"2016-08-30\"]',3,1),(23,2016,8,'[\"2016-08-02\"]',3,5),(51,2016,9,'[\"2016-09-03\", \"2016-09-08\", \"2016-09-14\", \"2016-09-18 Morning\", \"2016-09-26\"]',7,4),(52,2016,9,'[\"2016-09-04 Morning\", \"2016-09-12\", \"2016-09-18 Evening\", \"2016-09-23\", \"2016-09-30\"]',7,5),(53,2016,9,'[\"2016-09-01\", \"2016-09-04 Evening\", \"2016-09-15\", \"2016-09-24\", \"2016-09-27\"]',7,6),(54,2016,9,'[\"2016-09-07\", \"2016-09-10\", \"2016-09-13\", \"2016-09-19\", \"2016-09-25 Morning\"]',7,7),(55,2016,9,'[\"2016-09-11 Morning\", \"2016-09-16\", \"2016-09-22\", \"2016-09-25 Evening\", \"2016-09-29\"]',7,8),(56,2016,9,'[\"2016-09-02\", \"2016-09-06\", \"2016-09-11 Evening\", \"2016-09-21\", \"2016-10-01\"]',7,10),(57,2016,9,'[\"2016-09-05\", \"2016-09-09\", \"2016-09-17\", \"2016-09-20\", \"2016-09-28\"]',7,11);
/*!40000 ALTER TABLE `schedule_personalworkingschedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schedule_workingcalendar`
--

DROP TABLE IF EXISTS `schedule_workingcalendar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schedule_workingcalendar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` int(11) NOT NULL,
  `month` int(11) NOT NULL,
  `calendar` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `schedule_workingcalendar_year_86155328_uniq` (`year`,`month`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schedule_workingcalendar`
--

LOCK TABLES `schedule_workingcalendar` WRITE;
/*!40000 ALTER TABLE `schedule_workingcalendar` DISABLE KEYS */;
INSERT INTO `schedule_workingcalendar` VALUES (3,2016,8,'[[\"\", \"\", \"2016-08-02\", \"2016-08-03\", \"2016-08-04\", \"2016-08-05\", \"2016-08-06\"], [\"2016-08-07\", \"2016-08-08\", \"2016-08-09\", \"2016-08-10\", \"2016-08-11\", \"2016-08-12\", \"2016-08-13\"], [\"2016-08-14\", \"2016-08-15\", \"2016-08-16\", \"2016-08-17\", \"2016-08-18\", \"2016-08-19\", \"2016-08-20\"], [\"2016-08-21\", \"2016-08-22\", \"2016-08-23\", \"2016-08-24\", \"2016-08-25\", \"2016-08-26\", \"2016-08-27\"], [\"2016-08-28\", \"2016-08-29\", \"2016-08-30\", \"2016-08-31\", \"\", \"\", \"\"]]'),(7,2016,9,'[[\"\", \"\", \"\", \"\", \"2016-09-01\", \"2016-09-02\", \"2016-09-03\"], [\"2016-09-04\", \"2016-09-05\", \"2016-09-06\", \"2016-09-07\", \"2016-09-08\", \"2016-09-09\", \"2016-09-10\"], [\"2016-09-11\", \"2016-09-12\", \"2016-09-13\", \"2016-09-14\", \"2016-09-15\", \"2016-09-16\", \"2016-09-17\"], [\"2016-09-18\", \"2016-09-19\", \"2016-09-20\", \"2016-09-21\", \"2016-09-22\", \"2016-09-23\", \"2016-09-24\"], [\"2016-09-25\", \"2016-09-26\", \"2016-09-27\", \"2016-09-28\", \"2016-09-29\", \"2016-09-30\", \"2016-10-01\"]]');
/*!40000 ALTER TABLE `schedule_workingcalendar` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-08-10 10:59:58
