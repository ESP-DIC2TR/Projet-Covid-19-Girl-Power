-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: basee
-- ------------------------------------------------------
-- Server version	8.0.22

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
-- Table structure for table `cas_commune`
--

DROP TABLE IF EXISTS `cas_commune`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cas_commune` (
  `id_Communes` int NOT NULL,
  `id_communique` int NOT NULL,
  `Nb_Cas_Communautaires` int NOT NULL,
  PRIMARY KEY (`id_Communes`,`id_communique`),
  KEY `fk_Communes_Cas_communique1_idx` (`id_communique`),
  CONSTRAINT `fk_Communes_Cas_Communes1` FOREIGN KEY (`id_Communes`) REFERENCES `communes` (`idCommunes`),
  CONSTRAINT `fk_Communes_Cas_communique1` FOREIGN KEY (`id_communique`) REFERENCES `communique` (`id_communique`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cas_commune`
--

LOCK TABLES `cas_commune` WRITE;
/*!40000 ALTER TABLE `cas_commune` DISABLE KEYS */;
INSERT INTO `cas_commune` VALUES (3,63,94),(3,64,6),(3,69,1),(3,72,5),(3,73,1),(3,74,1),(3,75,2),(3,77,2),(3,78,24),(3,80,4),(3,81,5),(3,82,1),(3,83,1),(3,85,1),(3,89,3),(3,90,1),(3,91,3),(3,92,5),(3,93,1),(3,95,2),(25,63,44),(25,64,1),(25,70,1),(25,75,1),(25,78,1),(25,79,1),(25,82,1),(25,83,1),(25,84,2),(25,85,83),(25,87,1),(25,89,1),(25,91,2),(25,92,5),(25,93,1),(28,63,44),(28,64,1),(28,67,2),(28,69,1),(28,70,1),(28,73,1),(28,74,3),(28,75,2),(28,76,1),(28,78,1),(28,82,1),(28,83,1),(28,86,1),(28,87,1),(28,88,2),(28,89,7),(28,90,1),(28,91,1),(28,92,6),(28,93,1),(29,70,1),(29,72,3),(29,73,3),(29,75,1),(29,76,2),(29,80,3),(29,82,1),(29,83,3),(29,84,1),(29,86,1),(29,87,1),(29,88,1),(29,91,2),(29,92,1),(30,63,44),(30,64,1),(30,70,1),(30,72,2),(30,73,1),(30,78,1),(30,79,1),(30,80,3),(30,81,3),(30,82,1),(30,83,1),(30,84,1),(30,85,83),(30,86,1),(30,87,2),(30,88,4),(30,89,1),(30,90,1),(30,91,2),(36,74,1),(36,78,1),(36,79,1),(36,80,1),(36,81,1),(36,82,1),(36,90,1),(36,93,1),(57,64,1),(57,70,1),(57,71,1),(57,75,1),(57,79,2),(57,80,1),(57,82,2),(57,83,1),(57,84,2),(57,85,1),(57,86,2),(57,87,1),(57,89,1),(57,91,1),(57,93,2),(57,94,1),(58,69,1),(58,70,1),(58,72,14),(58,73,2),(58,74,3),(58,75,83),(58,80,4),(58,81,4),(58,82,3),(58,83,3),(58,84,1),(58,86,1),(58,88,1),(58,91,1),(58,92,3),(65,63,44),(65,64,1),(65,69,2),(65,71,1),(65,72,14),(65,73,2),(65,74,1),(65,77,1),(65,80,1),(65,83,2),(65,85,1),(65,86,1),(65,88,1),(65,89,1),(65,92,2),(65,93,1),(67,64,2),(67,70,2),(67,75,14),(67,82,1),(67,92,2),(71,69,1),(71,70,1),(71,72,2),(71,74,1),(71,76,3),(71,77,2),(71,79,1),(71,80,1),(71,82,1),(71,83,5),(71,86,3),(71,87,1),(71,88,3),(71,89,4),(71,90,1),(71,93,3),(72,73,1),(72,79,1),(72,82,1),(72,83,1),(72,86,1),(78,80,1),(92,63,1),(92,74,1),(92,75,1),(92,76,3),(92,77,2),(92,78,1),(92,80,2),(92,83,1),(92,86,2),(92,87,1),(92,90,1),(92,94,1),(92,95,2),(101,63,44),(101,64,1),(148,70,1),(148,79,1),(148,91,1),(166,90,1),(191,79,1);
/*!40000 ALTER TABLE `cas_commune` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cas_region`
--

DROP TABLE IF EXISTS `cas_region`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cas_region` (
  `Region_idRegion` int NOT NULL,
  `communique_id_communique` int NOT NULL,
  `Nb_Cas_Communautaires_Reg` int DEFAULT NULL,
  PRIMARY KEY (`Region_idRegion`,`communique_id_communique`),
  KEY `fk_Region_has_communique_communique1_idx` (`communique_id_communique`),
  KEY `fk_Region_has_communique_Region1_idx` (`Region_idRegion`),
  CONSTRAINT `fk_Region_has_communique_communique1` FOREIGN KEY (`communique_id_communique`) REFERENCES `communique` (`id_communique`),
  CONSTRAINT `fk_Region_has_communique_Region1` FOREIGN KEY (`Region_idRegion`) REFERENCES `region` (`idRegion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cas_region`
--

LOCK TABLES `cas_region` WRITE;
/*!40000 ALTER TABLE `cas_region` DISABLE KEYS */;
INSERT INTO `cas_region` VALUES (1,63,34),(1,64,6),(1,66,14),(1,69,22),(1,70,30),(1,72,19),(1,73,7),(1,74,7),(1,78,15),(1,80,34),(1,82,30),(1,83,8),(1,84,2),(1,85,6),(1,87,40),(1,88,3),(1,91,58),(1,93,8),(1,94,11),(2,63,44),(2,64,1),(2,89,3),(3,63,44),(3,64,3),(3,72,1),(4,63,1),(5,63,94),(5,64,1),(5,89,1),(5,91,1),(5,92,1),(5,95,1),(7,70,2),(7,71,1),(7,72,2),(7,75,14),(7,76,1),(7,77,2),(7,78,1),(7,82,2),(7,83,2),(7,89,2),(7,92,2),(7,93,2),(7,94,5),(7,95,3),(8,63,44),(9,63,1),(9,69,2),(9,70,4),(9,71,1),(9,72,1),(9,75,14),(9,77,1),(9,79,3),(9,82,1),(9,83,1),(9,90,1),(9,91,3),(9,93,1),(9,94,3),(14,70,1),(14,75,14),(14,79,1),(14,84,1),(14,89,1),(14,90,1),(14,92,1),(14,93,3),(14,94,3),(14,95,2);
/*!40000 ALTER TABLE `cas_region` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `communes`
--

DROP TABLE IF EXISTS `communes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `communes` (
  `idCommunes` int NOT NULL AUTO_INCREMENT,
  `Nom_Commune` varchar(45) DEFAULT NULL,
  `Population` int DEFAULT NULL,
  `Departement_idDepartement` int NOT NULL,
  PRIMARY KEY (`idCommunes`),
  KEY `fk_Communes_Departement1_idx` (`Departement_idDepartement`),
  CONSTRAINT `fk_Communes_Departement1` FOREIGN KEY (`Departement_idDepartement`) REFERENCES `departement` (`idDepartement`)
) ENGINE=InnoDB AUTO_INCREMENT=251 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `communes`
--

LOCK TABLES `communes` WRITE;
/*!40000 ALTER TABLE `communes` DISABLE KEYS */;
INSERT INTO `communes` VALUES (1,'Goree',NULL,1),(2,'Dakar',NULL,1),(3,'Plateau',NULL,1),(4,'Gueule Tapee',NULL,1),(5,'Fass-Colobane',NULL,1),(6,'Fann',NULL,1),(7,'Point E',NULL,1),(8,'Amitie',NULL,1),(10,'Biscuiterie',NULL,1),(11,'Dieuppeul',NULL,1),(12,'Derkle',NULL,1),(13,'gibraltar',NULL,1),(14,'cite horizon',NULL,1),(15,'cite soprim',NULL,1),(16,'cite apecsy',NULL,1),(17,'nord foire',NULL,1),(18,'ouest foire',NULL,1),(19,'Hann',NULL,1),(20,'Bel Air',NULL,1),(21,'ouagou niaye',NULL,1),(22,'Maristes',NULL,1),(23,'Sicap',NULL,1),(24,'Liberte',NULL,1),(25,'HLM',NULL,1),(26,'Mermoz ',NULL,1),(27,'Sacre CÅ“ur',NULL,1),(28,'Ouakam',NULL,1),(29,'Ngor',NULL,1),(30,'Yoff',NULL,1),(31,'Grand Yoff',NULL,1),(32,'Patte DOie',NULL,1),(34,'Camberene',NULL,1),(35,'zone de captage',NULL,1),(36,'fass',NULL,1),(37,'fass-delorme',NULL,1),(38,'scat-urbam',NULL,1),(39,'bourguiba',NULL,1),(40,'mamelles',NULL,1),(41,'niary-taly',NULL,1),(42,'yarakh',NULL,1),(43,'cite-comico',NULL,1),(44,'cite aliou sow',NULL,1),(45,'cite fadia',NULL,1),(46,'cite las palmas',NULL,1),(47,'cite-keur-damel',NULL,1),(48,'cite-keur-gorgui',NULL,1),(49,'keur-mbaye-fall',NULL,1),(50,'bopp',NULL,1),(51,'cite isra',NULL,1),(52,'centenaire',NULL,1),(53,'cite capverdienne',NULL,1),(54,'kounoune',NULL,1),(55,'DAKAR-PLATEAU',NULL,1),(56,'GRAND DAKAR',NULL,1),(57,'ALMADIES',NULL,1),(58,'PARCELLES ASSAINIES',NULL,1),(59,'Golf Sud',NULL,2),(60,'Sam Notaire',NULL,2),(61,'Ndiareme Limamoulaye',NULL,2),(62,'Medina Gounass',NULL,2),(63,'Wakhinane Nimzath',NULL,2),(64,'Thiaroye Gare',NULL,2),(65,'Mbao',NULL,2),(66,'Thiaroye sur Mer',NULL,2),(67,'Tivaouane',NULL,2),(68,'Diack Sao',NULL,2),(69,'Diamagueune',NULL,2),(70,'Sicap Mbao',NULL,2),(71,'Keur Massar',NULL,2),(72,'Malika',NULL,2),(73,'Yeumbeul Nord',NULL,2),(74,'Yeumbeul Sud',NULL,2),(75,'Pikine Ouest',NULL,2),(76,'Pikine Est',NULL,2),(77,'Pikine Nord',NULL,2),(78,'Dalifort',NULL,2),(79,'Djidah Thiaroye Kao',NULL,2),(80,'Guinaw Rail Nord',NULL,2),(81,'Guinaw Rail Sud',NULL,2),(82,'ben taly',NULL,2),(83,'gnary taly',NULL,2),(84,'cite tacko',NULL,2),(85,'GUEDIAWAYE',NULL,2),(86,'THIAROYE',NULL,2),(87,'NIAYES',NULL,2),(88,'PIKINEÂ DAGOUDAN',NULL,2),(89,'Rufisque Est',NULL,3),(90,'Bargny',NULL,3),(91,'Rufisque Nord',NULL,3),(92,'Diamniadio',NULL,3),(93,'Rufisque Ouest',NULL,3),(94,'Sebikotane',NULL,3),(95,'zac mbao',NULL,3),(96,'grand mbao',NULL,3),(97,'bambilor',NULL,3),(98,'cap des biches',NULL,3),(99,'yene',NULL,3),(100,'RUFISQUE - EST',NULL,3),(101,'SANGALKAM',NULL,3),(102,'Dinguiraye',NULL,4),(104,'Keur Samba Kane',NULL,4),(105,'Thiakhar',NULL,4),(106,'Ndondol',NULL,4),(107,'Ndangalma',NULL,4),(109,'Refane',NULL,4),(110,'Gawane',NULL,4),(111,'Ngogom',NULL,4),(112,'BABA GARAGE',NULL,4),(113,'NGOYE Ngoye',NULL,4),(114,'LAMBAYE',NULL,4),(116,'Ngohe',NULL,5),(117,'Pattar',NULL,5),(118,'Tocky Gare',NULL,5),(119,'Toure Mbonde',NULL,5),(120,'Ndankh Sene',NULL,5),(121,'Gade Escale',NULL,5),(122,'Keur Ngalgou',NULL,5),(124,'Taiba Moutoupha',NULL,5),(125,'NDOULO',NULL,5),(126,'NDINDY',NULL,5),(127,'Touba Mosquee',NULL,6),(128,'Dalla Ngabou',NULL,6),(130,'Nghaye',NULL,6),(131,'Touba Fall',NULL,6),(132,'Madina',NULL,6),(133,'KAEL Touba Mboul',NULL,6),(134,'Dendeye Gouy Gui',NULL,6),(135,'Ndioumane Taiba Thiekene',NULL,6),(137,'Sadio',NULL,6),(138,'NDAME',NULL,6),(139,'Kael',NULL,6),(140,'TAIF',NULL,6),(141,'DIAKHAO',NULL,7),(142,'FIMELA',NULL,7),(143,'NIAKHAR',NULL,7),(144,'TATTAGUINE',NULL,7),(145,'TOUBACOUTA',NULL,7),(146,'DJILOR',NULL,8),(147,'NIODIOR',NULL,8),(148,'COLOBANE',NULL,8),(149,'OUADIOUR',NULL,9),(150,'birkelane',NULL,10),(152,'BIRKILANE',NULL,10),(153,'MABO',NULL,10),(154,'KEUR MBOUKI',NULL,10),(155,'KATAKEL',NULL,11),(156,'GNIBY',NULL,11),(157,'MISSIRAH WADENE',NULL,12),(158,'IDA MOURIDE',NULL,12),(159,'LOUR ESCALE',NULL,12),(160,'DAROU MINAME 2',NULL,13),(161,'SAGNA',NULL,13),(162,'Mbadakhoune',NULL,14),(163,'NGUELOU',NULL,14),(164,'KOUMBAL',NULL,15),(165,'NDIEDIENG',NULL,15),(166,'SIBASSOR',NULL,15),(167,'MEDINA SABAKH',NULL,16),(168,'PAOS KOTO',NULL,16),(169,'WACK NGOUNA',NULL,16),(170,'BANDAFASSI',NULL,17),(171,'FONGOLIMBI',NULL,17),(172,'DAKATELI',NULL,18),(173,'DAR SALAM',NULL,18),(174,'BEMBOU',NULL,19),(175,'SABODALA',NULL,19),(176,'MAMPATIM',NULL,20),(177,'SARE BIDJI',NULL,20),(178,'DIOULACOLON',NULL,20),(179,'FAFACOUROU Badion Fafacourou',NULL,21),(180,'NDORNA',NULL,21),(181,'NIAMING',NULL,21),(182,'SARE COLY SALLE',NULL,21),(183,'PAKOUR',NULL,22),(184,'BONCONTO',NULL,22),(185,'NDANDE',NULL,23),(186,'DAROU MOUSTY',NULL,23),(187,'SAGATTA',NULL,23),(188,'Barkedji Gassane Thiarny Thiel',NULL,23),(189,'DODJI',NULL,24),(190,'YANG YANG',NULL,24),(191,'COKI',NULL,25),(192,'KEUR MOMAR SARR',NULL,25),(193,'MBEDIENE',NULL,25),(194,'SAKAL',NULL,25),(195,'WOURO SIDY',NULL,26),(196,'ORKADIERE',NULL,27),(197,'AGNAM CIVOL',NULL,27),(198,'OGO',NULL,28),(199,'VELINGARA',NULL,28),(200,'NDIAYE',NULL,29),(201,'MBANE',NULL,29),(202,'CAS',NULL,30),(203,'GAMADJI SARE',NULL,30),(204,'THILE BOUBACAR',NULL,30),(205,'SALDE',NULL,30),(206,'RAO',NULL,31),(207,'BOGHAL',NULL,32),(208,'BONA',NULL,32),(210,'DIAROUME',NULL,33),(211,'DJIBANAR',NULL,33),(212,'SIMBANDI BRASSOU',NULL,33),(213,'KARANTABA',NULL,33),(214,'DJIREDJI',NULL,33),(215,'DJIBABOUYA',NULL,34),(216,'BELE',NULL,35),(217,'KENIEBA',NULL,35),(218,'MOUDERY',NULL,35),(219,'BOYNGUEL BAMBA',NULL,35),(220,'DIANKE MAKHA',NULL,36),(221,'KOULOR',NULL,36),(222,'BALA',NULL,36),(223,'BAMBA THIALENE',NULL,37),(224,'KOUTHIABA WOLOF',NULL,37),(225,'MAKACOLIBANTANG',NULL,37),(226,'MISSIRAH',NULL,38),(227,'KOUSSANAR ',NULL,38),(228,'malicounda',NULL,39),(229,'FISSEL',NULL,39),(230,'SESSENE',NULL,39),(231,'SINDIA',NULL,39),(232,'THIENABA',NULL,39),(233,'KEUR MOUSSA',NULL,40),(234,'NOTTO',NULL,40),(235,'MEOUANE',NULL,40),(236,'pire',NULL,41),(237,'pire goureye',NULL,41),(238,'MERINA DAKHAR',NULL,41),(239,'NIAKHENE',NULL,41),(240,'PAMBAL',NULL,41),(241,'NIAGUIS',NULL,42),(242,'NIASSIA',NULL,42),(243,'CABROUSSE',NULL,43),(244,'LOUDIA OUOLOF',NULL,43),(245,'KATABA 1',NULL,43),(246,'KATABA 2',NULL,43),(247,'KATABA 3',NULL,43),(248,'TENGHORI',NULL,44),(249,'TENDOUCK',NULL,44),(250,'SINDIAN',NULL,44);
/*!40000 ALTER TABLE `communes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `communique`
--

DROP TABLE IF EXISTS `communique`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `communique` (
  `id_communique` int NOT NULL AUTO_INCREMENT,
  `la_date` varchar(100) NOT NULL,
  `Nb_Test` int NOT NULL,
  `Nb_nouveaux_Cas` int NOT NULL,
  `Nb_Cas_Contacts` int NOT NULL,
  `Nb_Cas_Communautaires` int NOT NULL,
  `Nb_Gueris` int DEFAULT NULL,
  `Nb_Deces` int DEFAULT NULL,
  `NomFichierSource` varchar(50) NOT NULL,
  `DateHeureExtraction` varchar(50) NOT NULL,
  `mois` varchar(50) NOT NULL,
  PRIMARY KEY (`id_communique`)
) ENGINE=InnoDB AUTO_INCREMENT=269 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `communique`
--

LOCK TABLES `communique` WRITE;
/*!40000 ALTER TABLE `communique` DISABLE KEYS */;
INSERT INTO `communique` VALUES (63,'Ce Jeudi 31 dÃ©cembre 2020,',1402,195,81,114,53,8,'communique n118.pdf','2021-05-03','dÃ©cembre'),(64,'Ce Dimanche 13 dÃ©cembre 2020,',227,78,32,45,85,1,'communique n136.pdf','2021-05-03','dÃ©cembre'),(65,'Ce dimanche 05 juillet 2020,',756,128,92,34,157,4,'communique n298.pdf','2021-05-03','juillet'),(66,'Ce lundi 09 novembre 2020,',544,3,2,1,13,1,'communique n170.pdf','2021-05-03','novembre'),(67,'Ce mardi 27 octobre 2020,',453,6,3,2,121,1,'communique n184.pdf','2021-05-03','octobre'),(68,'Ce samedi 05 septembre 2020,',1313,67,27,40,128,1,'communique n236.pdf','2021-05-03','septembre'),(69,'Ce Jeudi 22 avril 2021,',1392,65,30,35,51,1,'communique n10.pdf','2021-05-03','avril'),(70,'Ce Mercredi 21 avril 2021,',1649,74,30,44,68,1,'communique n11.pdf','2021-05-03','avril'),(71,'Ce Mardi 20 avril 2021,',911,15,7,8,61,4,'communique n12.pdf','2021-05-03','avril'),(72,'Ce Lundi 19 avril 2021,',1221,39,7,32,28,4,'communique n13.pdf','2021-05-03','avril'),(73,'Ce Dimanche 18 avril 2021,',1536,51,11,40,46,2,'communique n14.pdf','2021-05-03','avril'),(74,'Ce Samedi 17 avril 2021,',1672,67,28,39,10,1,'communique n15.pdf','2021-05-03','avril'),(75,'Ce Vendredi 16 avril 2021,',1575,58,21,37,67,2,'communique n16.pdf','2021-05-03','avril'),(76,'Ce Jeudi 15 avril 2021,',1315,46,15,31,53,1,'communique n17.pdf','2021-05-03','avril'),(77,'Ce Mardi 13 avril 2021,',999,30,13,17,26,2,'communique n18.pdf','2021-05-03','avril'),(78,'Ce Lundi 12 avril 2021,',1287,34,11,23,41,1,'communique n19.pdf','2021-05-03','avril'),(79,'Ce Vendredi 30 avril 2021,',1280,49,14,35,62,1,'communique n2.pdf','2021-05-03','avril'),(80,'Ce Dimanche 11 avril 2021,',1810,67,23,44,62,1,'communique n20.pdf','2021-05-03','avril'),(81,'Ce Samedi 10 avril 2021,',1515,57,19,38,156,1,'communique n21.pdf','2021-05-03','avril'),(82,'Ce Vendredi 09 avril 2021,',1441,70,25,45,61,1,'communique n22.pdf','2021-05-03','avril'),(83,'Ce Jeudi 08 avril 2021,',1421,73,29,44,82,83,'communique n23.pdf','2021-05-03','avril'),(84,'Ce Mercredi 07 avril 2021,',867,377,13,24,66,5,'communique n24.pdf','2021-05-03','avril'),(85,'Ce Mardi 06 avril 2021,',793,34,13,21,49,2,'communique n25.pdf','2021-05-03','avril'),(86,'Ce Lundi 05 avril 2021,',1421,69,29,40,63,2,'communique n26.pdf','2021-05-03','avril'),(87,'Ce Dimanche 04 avril 2021,',1834,71,22,49,16,2,'communique n27.pdf','2021-05-03','avril'),(88,'Ce Samedi 03 avril 2021,',1635,64,21,43,121,4,'communique n28.pdf','2021-05-03','avril'),(89,'Ce Vendredi 02 avril 2021,',1823,107,32,75,98,2,'communique n29.pdf','2021-05-03','avril'),(90,'Ce Jeudi 29 avril 2021,',1309,46,17,29,30,4,'communique n3.pdf','2021-05-03','avril'),(91,'Ce Samedi 1Â° Mai 2021,',1552,44,9,35,NULL,NULL,'communique n1.pdf','2021-05-03','Mai'),(92,'Ce Jeudi 1Â° avril 2021,',1659,77,17,60,113,3,'communique n30.pdf','2021-05-03','avril'),(93,'Ce Mercredi 31 mars 2021,',1607,87,45,42,93,2,'communique n31.pdf','2021-05-03','mars'),(94,'Ce Mardi 30 mars 2021,',1073,52,19,33,188,5,'communique n32.pdf','2021-05-03','mars'),(95,'Ce Mercredi 03 Juin 2020,',1549,96,80,16,287,7,'communique n329.pdf','2021-05-03','Juin'),(232,'Ce Jeudi 31 dÃ©cembre 2020,',1402,195,81,114,53,8,'communique n118.pdf','2021-05-03','dÃ©cembre'),(233,'Ce Dimanche 13 dÃ©cembre 2020,',227,78,32,45,85,1,'communique n136.pdf','2021-05-03','dÃ©cembre'),(234,'Ce dimanche 05 juillet 2020,',756,128,92,34,157,4,'communique n298.pdf','2021-05-03','juillet'),(235,'Ce lundi 09 novembre 2020,',544,3,2,1,13,1,'communique n170.pdf','2021-05-03','novembre'),(236,'Ce mardi 27 octobre 2020,',453,6,3,2,121,1,'communique n184.pdf','2021-05-03','octobre'),(237,'Ce samedi 05 septembre 2020,',1313,67,27,40,128,1,'communique n236.pdf','2021-05-03','septembre'),(238,'Ce Jeudi 22 avril 2021,',1392,65,30,35,51,1,'communique n10.pdf','2021-05-03','avril'),(239,'Ce Mercredi 21 avril 2021,',1649,74,30,44,68,1,'communique n11.pdf','2021-05-03','avril'),(240,'Ce Mardi 20 avril 2021,',911,15,7,8,61,4,'communique n12.pdf','2021-05-03','avril'),(241,'Ce Lundi 19 avril 2021,',1221,39,7,32,28,4,'communique n13.pdf','2021-05-03','avril'),(242,'Ce Dimanche 18 avril 2021,',1536,51,11,40,46,2,'communique n14.pdf','2021-05-03','avril'),(243,'Ce Samedi 17 avril 2021,',1672,67,28,39,10,1,'communique n15.pdf','2021-05-03','avril'),(244,'Ce Vendredi 16 avril 2021,',1575,58,21,37,67,2,'communique n16.pdf','2021-05-03','avril'),(245,'Ce Jeudi 15 avril 2021,',1315,46,15,31,53,1,'communique n17.pdf','2021-05-03','avril'),(246,'Ce Mardi 13 avril 2021,',999,30,13,17,26,2,'communique n18.pdf','2021-05-03','avril'),(247,'Ce Lundi 12 avril 2021,',1287,34,11,23,41,1,'communique n19.pdf','2021-05-03','avril'),(248,'Ce Vendredi 30 avril 2021,',1280,49,14,35,62,1,'communique n2.pdf','2021-05-03','avril'),(249,'Ce Dimanche 11 avril 2021,',1810,67,23,44,62,1,'communique n20.pdf','2021-05-03','avril'),(250,'Ce Samedi 10 avril 2021,',1515,57,19,38,156,1,'communique n21.pdf','2021-05-03','avril'),(251,'Ce Vendredi 09 avril 2021,',1441,70,25,45,61,1,'communique n22.pdf','2021-05-03','avril'),(252,'Ce Jeudi 08 avril 2021,',1421,73,29,44,82,83,'communique n23.pdf','2021-05-03','avril'),(253,'Ce Mercredi 07 avril 2021,',867,377,13,24,66,5,'communique n24.pdf','2021-05-03','avril'),(254,'Ce Mardi 06 avril 2021,',793,34,13,21,49,2,'communique n25.pdf','2021-05-03','avril'),(255,'Ce Lundi 05 avril 2021,',1421,69,29,40,63,2,'communique n26.pdf','2021-05-03','avril'),(256,'Ce Dimanche 04 avril 2021,',1834,71,22,49,16,2,'communique n27.pdf','2021-05-03','avril'),(257,'Ce Samedi 03 avril 2021,',1635,64,21,43,121,4,'communique n28.pdf','2021-05-03','avril'),(258,'Ce Vendredi 02 avril 2021,',1823,107,32,75,98,2,'communique n29.pdf','2021-05-03','avril'),(259,'Ce Jeudi 29 avril 2021,',1309,46,17,29,30,4,'communique n3.pdf','2021-05-03','avril'),(260,'Ce Samedi 1Â° Mai 2021,',1552,44,9,35,NULL,NULL,'communique n1.pdf','2021-05-03','Mai'),(261,'Ce Jeudi 1Â° avril 2021,',1659,77,17,60,113,3,'communique n30.pdf','2021-05-03','avril'),(262,'Ce Mercredi 31 mars 2021,',1607,87,45,42,93,2,'communique n31.pdf','2021-05-03','mars'),(263,'Ce Mardi 30 mars 2021,',1073,52,19,33,188,5,'communique n32.pdf','2021-05-03','mars'),(264,'Ce Mercredi 03 Juin 2020,',1549,96,80,16,287,7,'communique n329.pdf','2021-05-03','Juin');
/*!40000 ALTER TABLE `communique` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `communiques_user`
--

DROP TABLE IF EXISTS `communiques_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `communiques_user` (
  `user_iduser` int NOT NULL,
  `communique_id_communique` int NOT NULL,
  PRIMARY KEY (`user_iduser`,`communique_id_communique`),
  KEY `fk_user_has_communique_communique1_idx` (`communique_id_communique`),
  KEY `fk_user_has_communique_user1_idx` (`user_iduser`),
  CONSTRAINT `fk_user_has_communique_communique1` FOREIGN KEY (`communique_id_communique`) REFERENCES `communique` (`id_communique`),
  CONSTRAINT `fk_user_has_communique_user1` FOREIGN KEY (`user_iduser`) REFERENCES `user` (`iduser`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `communiques_user`
--

LOCK TABLES `communiques_user` WRITE;
/*!40000 ALTER TABLE `communiques_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `communiques_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departement`
--

DROP TABLE IF EXISTS `departement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `departement` (
  `idDepartement` int NOT NULL AUTO_INCREMENT,
  `Nom_Departement` varchar(45) NOT NULL,
  `Population` int DEFAULT NULL,
  `Nb_Cas_Communautaires_Dpt` int DEFAULT NULL,
  `Region_idRegion` int NOT NULL,
  PRIMARY KEY (`idDepartement`),
  KEY `fk_Departement_Region1_idx` (`Region_idRegion`),
  CONSTRAINT `fk_Departement_Region1` FOREIGN KEY (`Region_idRegion`) REFERENCES `region` (`idRegion`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departement`
--

LOCK TABLES `departement` WRITE;
/*!40000 ALTER TABLE `departement` DISABLE KEYS */;
INSERT INTO `departement` VALUES (1,'Dakar',NULL,NULL,1),(2,'GUEDIAWAYE',NULL,NULL,1),(3,'RUFISQUE',NULL,NULL,1),(4,'BAMBEY',NULL,NULL,2),(5,'DIOURBEL',NULL,NULL,2),(6,'MBACKE',NULL,NULL,2),(7,'FATICK',NULL,NULL,3),(8,'FOUNDIOUGNE',NULL,NULL,3),(9,'GOSSAS',NULL,NULL,3),(10,'BIRKILANE',NULL,NULL,4),(11,'KAFFRINE',NULL,NULL,4),(12,'KOUNGHEUL',NULL,NULL,4),(13,'MALEM HODDAR',NULL,NULL,4),(14,'Guinguineo',NULL,NULL,5),(15,'KAOLACK',NULL,NULL,5),(16,'NIORO',NULL,NULL,5),(17,'KEDOUGOU',NULL,NULL,6),(18,'SALEMATA',NULL,NULL,6),(19,'SARAYA',NULL,NULL,6),(20,'KOLDA',NULL,NULL,7),(21,'MEDINA YORO FOULAH',NULL,NULL,7),(22,'VELINGARA',NULL,NULL,7),(23,'KEBEMER',NULL,NULL,8),(24,'LINGUERE',NULL,NULL,8),(25,'LOUGA',NULL,NULL,8),(26,'KANEL',NULL,NULL,9),(27,'MATAM',NULL,NULL,9),(28,'RANEROU FERLO',NULL,NULL,9),(29,'DAGANA',NULL,NULL,10),(30,'PODOR',NULL,NULL,10),(31,'SAINT LOUIS ',NULL,NULL,10),(32,'BOUNKILING',NULL,NULL,11),(33,'GOUDOMP',NULL,NULL,11),(34,'SEDHIOU',NULL,NULL,11),(35,'BAKEL',NULL,NULL,12),(36,'GOUDIRY',NULL,NULL,12),(37,'KOUPENTOUM',NULL,NULL,12),(38,'TAMBACOUNDA',NULL,NULL,12),(39,'MBOUR',NULL,NULL,13),(40,'THIES',NULL,NULL,13),(41,'TIVAOUANE',NULL,NULL,13),(42,'ZIGUINCHOR',NULL,NULL,14),(43,'OUSSOUYE',NULL,NULL,14),(44,'BIGNONA',NULL,NULL,14);
/*!40000 ALTER TABLE `departement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `region`
--

DROP TABLE IF EXISTS `region`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `region` (
  `idRegion` int NOT NULL AUTO_INCREMENT,
  `Nom_Region` varchar(45) NOT NULL,
  `Population` int DEFAULT NULL,
  PRIMARY KEY (`idRegion`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `region`
--

LOCK TABLES `region` WRITE;
/*!40000 ALTER TABLE `region` DISABLE KEYS */;
INSERT INTO `region` VALUES (1,'DAKAR',NULL),(2,'DIOURBEL',NULL),(3,'FATICK',NULL),(4,'KAFFRINE',NULL),(5,'KAOLACK',NULL),(6,'KEDOUGOU',NULL),(7,'KOLDA',NULL),(8,'LOUGA',NULL),(9,'MATAM',NULL),(10,'SAINT LOUIS',NULL),(11,'SEDHIOU',NULL),(12,'TAMBACOUNDA',NULL),(13,'THIES',NULL),(14,'ZIGUINCHOR',NULL);
/*!40000 ALTER TABLE `region` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `iduser` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(45) DEFAULT NULL,
  `prenom` varchar(45) DEFAULT NULL,
  `login` varchar(45) DEFAULT NULL,
  `mot_de_passe` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`iduser`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-05 10:09:56
