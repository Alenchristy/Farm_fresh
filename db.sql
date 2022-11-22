/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - farmfresh
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`farmfresh` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `farmfresh`;

/*Table structure for table `booking` */

DROP TABLE IF EXISTS `booking`;

CREATE TABLE `booking` (
  `b_id` int(11) NOT NULL AUTO_INCREMENT,
  `h_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `b_date` date NOT NULL,
  `status` varchar(15) NOT NULL,
  `book_dat` date NOT NULL,
  PRIMARY KEY (`b_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `booking` */

insert  into `booking`(`b_id`,`h_id`,`user_id`,`b_date`,`status`,`book_dat`) values 
(1,2,23,'2022-10-30','canceled','2022-10-30'),
(2,2,23,'2022-10-30','canceled','2022-11-03'),
(3,2,23,'2022-10-30','canceled','2022-11-02'),
(4,3,23,'2022-10-30','canceled','2022-11-02'),
(5,3,23,'2022-10-30','rejected','2022-10-30'),
(6,2,23,'2022-10-31','accepted','2022-11-05');

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(15) NOT NULL,
  `image` varchar(50) NOT NULL,
  `status` varchar(13) NOT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `category` */

insert  into `category`(`category_id`,`category_name`,`image`,`status`) values 
(5,'Others','20221017072127.jpg','Enabled'),
(11,'Plants','20221017050004.jpg','Enabled'),
(12,'saplings','20221030124530.jpg','Disabled'),
(13,'Fruits','20221019064225.jpg','Enabled'),
(14,'rger','20221018210912.jpg','Disabled');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `f_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `feedback` varchar(100) NOT NULL,
  PRIMARY KEY (`f_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

/*Table structure for table `homestay` */

DROP TABLE IF EXISTS `homestay`;

CREATE TABLE `homestay` (
  `h_id` int(11) NOT NULL AUTO_INCREMENT,
  `h_name` varchar(20) NOT NULL,
  `details` varchar(100) NOT NULL,
  `rate` int(11) NOT NULL,
  `image` varchar(30) NOT NULL,
  `status` varchar(15) NOT NULL,
  PRIMARY KEY (`h_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `homestay` */

insert  into `homestay`(`h_id`,`h_name`,`details`,`rate`,`image`,`status`) values 
(2,'mist villa','dqwdq',3500,'20221006140622.jpg','Not Available'),
(3,'Woods','superb',4000,'20221007221759.jpg','Available'),
(4,'SUNSHINE','rfre',3000,'20221013112353.jpg','Available');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(15) NOT NULL,
  `password` varchar(15) NOT NULL,
  `type` varchar(10) NOT NULL,
  PRIMARY KEY (`login_id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(2,'dd','user','user'),
(13,'ygygy','123','user'),
(19,'zxc','1234','user'),
(20,'we','1234','user'),
(21,'sh','12ab','user'),
(22,'user','admi','user'),
(23,'alen','9876','user'),
(24,'asdfg','7777','user');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `n_id` int(11) NOT NULL AUTO_INCREMENT,
  `a_id` int(11) NOT NULL,
  `n_date` date NOT NULL,
  `notifi` varchar(500) NOT NULL,
  `names` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`n_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`n_id`,`a_id`,`n_date`,`notifi`,`names`) values 
(1,101,'2022-11-07','your order for Mangosteen,Rambuttan  will be deliverd on 2022-11-10','14:01:15'),
(2,101,'2022-11-07','Your order of products is rejected due to payment error','15:02:14'),
(3,104,'2022-11-12','Your order of products is rejected due to payment error','14:11:31'),
(4,104,'2022-11-12','Your order of products is rejected due to payment error','14:12:50'),
(5,103,'2022-11-12','Your order of products is rejected due to payment error','14:18:06'),
(6,119,'2022-11-12','Your order of products is rejected due to payment error','14:27:49');

/*Table structure for table `order` */

DROP TABLE IF EXISTS `order`;

CREATE TABLE `order` (
  `order_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `price` int(11) NOT NULL,
  `status` varchar(15) NOT NULL,
  `del_date` varchar(20) NOT NULL,
  `del_address` varchar(40) NOT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=124 DEFAULT CHARSET=latin1;

/*Data for the table `order` */

insert  into `order`(`order_id`,`user_id`,`date`,`price`,`status`,`del_date`,`del_address`) values 
(1,23,'2022-11-02',1500,'canceled','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(2,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(3,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(4,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(5,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(6,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(7,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(8,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(9,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(10,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(11,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(12,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(13,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(14,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(15,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(16,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(17,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(18,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(19,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(20,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(21,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(22,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(23,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(24,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(25,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(26,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(27,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(28,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(29,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(30,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(31,23,'2022-11-02',150,'canceled','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(32,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(33,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(34,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(35,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(36,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(37,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(38,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(39,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(40,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(41,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(42,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(43,23,'2022-11-02',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(44,23,'2022-11-03',200,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(45,23,'2022-11-03',200,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(46,23,'2022-11-03',200,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(47,23,'2022-11-03',200,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(48,23,'2022-11-03',200,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(49,23,'2022-11-03',200,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(50,23,'2022-11-03',200,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(51,23,'2022-11-03',200,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(52,23,'2022-11-03',200,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(53,23,'2022-11-03',200,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(54,23,'2022-11-03',200,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(55,23,'2022-11-03',200,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(56,23,'2022-11-03',200,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(57,23,'2022-11-03',200,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(58,23,'2022-11-03',200,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(59,23,'2022-11-03',200,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(60,23,'2022-11-03',200,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(61,23,'2022-11-03',200,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(62,23,'2022-11-03',200,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(63,23,'2022-11-03',200,'deliverd','2022-11-10',' gui, hgfhg, 456734, 1234567890'),
(64,23,'2022-11-03',1500,'canceled','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(65,23,'2022-11-03',300,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(66,23,'2022-11-03',300,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(67,23,'2022-11-03',450,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(68,23,'2022-11-03',450,'deliverd','2022-11-10',' gui, hgfhg, 456734, 1234567890'),
(69,23,'2022-11-03',1200,'canceled','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(70,23,'2022-11-03',1200,'deliverd','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(71,23,'2022-11-03',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(72,23,'2022-11-03',200,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(73,23,'2022-11-03',300,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(74,23,'2022-11-03',2250,'deliverd','2022-11-09',' gui, hgfhg, 456734, 1234567890'),
(75,23,'2022-11-03',450,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(76,23,'2022-11-03',500,'canceled','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(77,23,'2022-11-03',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(78,23,'2022-11-03',5100,'canceled','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(79,23,'2022-11-03',3230,'deliverd','2022-11-09',' gui, hgfhg, 456734, 1234567890'),
(80,23,'2022-11-03',980,'canceled','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(81,23,'2022-11-03',1100,'canceled','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(82,23,'2022-11-03',980,'canceled','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(83,23,'2022-11-03',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(84,23,'2022-11-03',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(85,23,'2022-11-03',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(86,23,'2022-11-03',150,'pending','2022-11-08',' gui, hgfhg, 456734, 1234567890'),
(87,23,'2022-11-04',1700,'deliverd','2022-11-09',' gui, hgfhg, 456734, 1234567890'),
(88,23,'2022-11-05',6000,'deliverd','2022-11-10',' gui, hgfhg, 456734, 1234567890'),
(89,23,'2022-11-05',680,'canceled','2022-11-12',' gui, hgfhg, 456734, 1234567890'),
(90,23,'2022-11-06',245,'deliverd','2022-11-11',' gui, hgfhg, 456734, 1234567890'),
(91,23,'2022-11-06',300,'canceled','2022-11-10',' gui, hgfhg, 456734, 1234567890'),
(92,23,'2022-11-06',300,'pending','pending',' gui, hgfhg, 456734, 1234567890'),
(93,23,'2022-11-06',580,'canceled','2022-11-06',' gui, hgfhg, 456734, 1234567890'),
(94,23,'2022-11-06',1445,'canceled','pending',' gui, hgfhg, 456734, 1234567890'),
(95,23,'2022-11-06',2900,'canceled','2022-11-06',' gui, hgfhg, 456734, 1234567890'),
(96,23,'2022-11-06',2900,'canceled','2022-11-10',' gui, hgfhg, 456734, 1234567890'),
(97,23,'2022-11-06',5100,'canceled','pending',' gui, hgfhg, 456734, 1234567890'),
(98,23,'2022-11-06',655,'canceled','2022-11-06',' gui, hgfhg, 456734, 1234567890'),
(99,23,'2022-11-06',3300,'canceled','2022-11-07',' gui, hgfhg, 456734, 1234567890'),
(100,23,'2022-11-06',1200,'canceled','2022-11-06',' gui, hgfhg, 456734, 1234567890'),
(101,23,'2022-11-06',1200,'canceled','2022-11-10',' gui, hgfhg, 456734, 1234567890'),
(102,23,'2022-11-12',3600,'canceled','pending',' gui, hgfhg, 456734, 1234567890'),
(103,23,'2022-11-06',245,'canceled','pending',' gui, hgfhg, 456734, 1234567890'),
(104,23,'2022-11-06',300,'canceled','pending',' gui, hgfhg, 456734, 1234567890'),
(105,23,'2022-11-12',750,'pending','pending',' gui, hgfhg, 456734, 1234567890'),
(106,23,'2022-11-12',750,'pending','pending',' gui, hgfhg, 456734, 1234567890'),
(107,23,'2022-11-12',750,'pending','pending',' gui, hgfhg, 456734, 1234567890'),
(108,23,'2022-11-12',750,'pending','pending',' gui, hgfhg, 456734, 1234567890'),
(109,23,'2022-11-12',750,'pending','pending',' gui, hgfhg, 456734, 1234567890'),
(110,23,'2022-11-12',750,'pending','pending',' gui, hgfhg, 456734, 1234567890'),
(111,23,'2022-11-12',750,'pending','pending',' gui, hgfhg, 456734, 1234567890'),
(112,23,'2022-11-12',750,'pending','pending',' gui, hgfhg, 456734, 1234567890'),
(113,23,'2022-11-12',750,'pending','pending',' gui, hgfhg, 456734, 1234567890'),
(114,23,'2022-11-12',750,'pending','pending',' gui, hgfhg, 456734, 1234567890'),
(115,23,'2022-11-12',750,'pending','pending',' gui, hgfhg, 456734, 1234567890'),
(116,23,'2022-11-12',750,'pending','pending',' gui, hgfhg, 456734, 1234567890'),
(117,23,'2022-11-12',150,'pending','pending',' gui, hgfhg, 456734, 1234567890'),
(118,23,'2022-11-12',300,'pending','pending',' gui, hgfhg, 456734, 1234567890'),
(119,23,'2022-11-12',820,'canceled','pending',' gui, hgfhg, 456734, 1234567890'),
(120,23,'2022-11-12',245,'cod','pending',' gui, hgfhg, 456734, 1234567890'),
(121,23,'2022-11-12',1040,'cod','pending',' gui, hgfhg, 456734, 1234567890'),
(122,23,'2022-11-12',8990,'canceled','pending',' gui, hgfhg, 456734, 1234567890'),
(123,23,'2022-11-12',545,'canceled','pending',' gui, hgfhg, 456734, 1234567890');

/*Table structure for table `order_item` */

DROP TABLE IF EXISTS `order_item`;

CREATE TABLE `order_item` (
  `oi_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `status` varchar(20) NOT NULL,
  PRIMARY KEY (`oi_id`)
) ENGINE=InnoDB AUTO_INCREMENT=161 DEFAULT CHARSET=latin1;

/*Data for the table `order_item` */

insert  into `order_item`(`oi_id`,`order_id`,`product_id`,`quantity`,`status`) values 
(1,40,14,5,'canceled'),
(2,21,26,5,'canceled'),
(3,21,11,3,'canceled'),
(4,1,11,4,'canceled'),
(5,1,14,4,'canceled'),
(6,2,13,1,'pending'),
(7,3,13,1,'pending'),
(8,4,13,1,'pending'),
(9,5,13,1,'pending'),
(10,6,13,1,'pending'),
(11,7,13,1,'pending'),
(12,8,13,1,'pending'),
(13,9,13,1,'pending'),
(14,10,13,1,'pending'),
(15,11,13,1,'pending'),
(16,12,13,1,'pending'),
(17,13,13,1,'pending'),
(18,14,13,1,'pending'),
(19,15,13,1,'pending'),
(20,16,13,1,'pending'),
(21,17,13,1,'pending'),
(22,18,13,1,'pending'),
(23,19,13,1,'pending'),
(24,20,13,1,'pending'),
(25,21,13,1,'pending'),
(26,22,13,1,'pending'),
(27,23,13,1,'pending'),
(28,24,13,1,'pending'),
(29,25,13,1,'pending'),
(30,26,13,1,'pending'),
(31,27,13,1,'pending'),
(32,28,13,1,'pending'),
(33,29,13,1,'pending'),
(34,30,13,1,'pending'),
(35,31,13,1,'canceled'),
(36,32,13,1,'pending'),
(37,33,13,1,'pending'),
(38,34,13,1,'pending'),
(39,35,13,1,'pending'),
(40,36,13,1,'pending'),
(41,37,13,1,'pending'),
(42,38,13,1,'pending'),
(43,39,13,1,'pending'),
(44,40,13,1,'pending'),
(45,41,13,1,'pending'),
(46,42,13,1,'pending'),
(47,43,13,1,'pending'),
(48,44,15,1,'pending'),
(49,45,15,1,'pending'),
(50,46,15,1,'pending'),
(51,47,15,1,'pending'),
(52,48,15,1,'pending'),
(53,49,15,1,'pending'),
(54,50,15,1,'pending'),
(55,51,15,1,'pending'),
(56,52,15,1,'pending'),
(57,53,15,1,'pending'),
(58,54,15,1,'pending'),
(59,55,15,1,'pending'),
(60,56,15,1,'pending'),
(61,57,15,1,'pending'),
(62,58,15,1,'pending'),
(63,59,15,1,'pending'),
(64,60,15,1,'pending'),
(65,61,15,1,'pending'),
(66,62,15,1,'pending'),
(67,63,15,1,'cod'),
(69,64,14,5,'canceled'),
(70,65,14,1,'pending'),
(71,66,14,1,'pending'),
(72,67,26,1,'pending'),
(73,68,26,5,'cod'),
(74,69,14,4,'canceled'),
(75,70,14,4,'cod'),
(76,71,13,1,'pending'),
(77,72,15,1,'pending'),
(78,73,14,1,'pending'),
(79,74,22,5,'cod'),
(80,75,22,1,'pending'),
(81,76,23,1,'canceled'),
(82,76,11,1,'canceled'),
(83,77,13,1,'pending'),
(85,78,25,1,'canceled'),
(86,79,25,3,'cod'),
(88,79,20,4,'cod'),
(89,80,20,4,'canceled'),
(90,81,21,4,'canceled'),
(91,82,7,4,'canceled'),
(92,83,13,1,'pending'),
(93,84,13,1,'pending'),
(94,85,13,1,'pending'),
(95,86,13,1,'pending'),
(96,87,14,5,'cod'),
(97,87,15,1,'cod'),
(98,88,26,4,'cod'),
(99,88,25,4,'cod'),
(100,88,14,4,'cod'),
(101,89,23,1,'canceled'),
(102,89,11,1,'canceled'),
(103,89,24,1,'canceled'),
(104,90,7,1,'cod'),
(105,91,14,1,'canceled'),
(106,92,14,1,'pending'),
(107,93,14,1,'canceled'),
(108,93,19,1,'canceled'),
(109,94,22,1,'canceled'),
(110,94,20,21,'canceled'),
(111,94,25,1,'canceled'),
(112,95,22,4,'canceled'),
(113,95,21,4,'canceled'),
(114,96,21,4,'canceled'),
(115,96,26,4,'canceled'),
(116,97,22,3,'canceled'),
(117,97,25,5,'canceled'),
(120,98,15,1,'canceled'),
(121,98,21,1,'canceled'),
(122,98,24,1,'canceled'),
(123,99,25,2,'canceled'),
(124,99,26,4,'canceled'),
(125,100,25,1,'canceled'),
(126,100,26,1,'canceled'),
(127,101,25,1,'canceled'),
(128,101,26,1,'canceled'),
(129,102,22,3,'canceled'),
(130,102,25,3,'canceled'),
(131,103,7,1,'canceled'),
(132,104,14,1,'canceled'),
(133,105,25,1,'pending'),
(134,106,25,1,'pending'),
(135,107,25,1,'pending'),
(136,108,25,1,'pending'),
(137,109,25,1,'pending'),
(138,110,25,1,'pending'),
(139,111,25,1,'pending'),
(140,112,25,1,'pending'),
(141,113,25,1,'pending'),
(142,114,25,1,'pending'),
(143,115,25,1,'pending'),
(144,116,25,1,'pending'),
(145,117,13,1,'pending'),
(146,118,14,1,'pending'),
(147,119,14,1,'canceled'),
(148,119,21,1,'canceled'),
(149,119,20,1,'canceled'),
(150,120,20,1,'cod'),
(151,121,20,1,'cod'),
(152,121,7,1,'cod'),
(153,121,13,1,'cod'),
(154,121,23,1,'cod'),
(155,122,7,12,'canceled'),
(156,122,13,17,'canceled'),
(157,122,11,35,'canceled'),
(158,123,15,10,'canceled'),
(159,123,27,13,'canceled');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `mode` varchar(20) NOT NULL,
  `status` varchar(15) NOT NULL,
  `scrshot` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=126 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`order_id`,`price`,`mode`,`status`,`scrshot`) values 
(1,59,200,'online','pending',NULL),
(2,60,200,'online','pending',NULL),
(3,61,200,'online','pending',NULL),
(4,62,200,'online','pending',NULL),
(5,63,200,'online','paid','20221103061445.jpg'),
(6,65,300,'online','pending',NULL),
(7,66,300,'online','pending',NULL),
(8,67,450,'online','pending',NULL),
(9,0,0,'online','paid',NULL),
(10,0,0,'online','paid',NULL),
(11,69,1200,'online','paid',NULL),
(12,70,1200,'online','paid',NULL),
(13,71,150,'online','pending',NULL),
(14,72,200,'online','pending',NULL),
(15,73,300,'online','pending',NULL),
(16,74,2250,'online','paid',NULL),
(17,75,450,'online','pending',NULL),
(18,76,500,'online','paid','20221103142723.jpg'),
(19,76,500,'online','paid',NULL),
(20,77,150,'online','pending',NULL),
(21,78,4950,'online','paid','20221103213457.jpg'),
(22,78,4950,'online','paid','20221103213457.jpg'),
(23,78,5100,'online','paid','20221103213457.jpg'),
(24,79,750,'online','paid','20221103214047.jpg'),
(25,79,995,'online','paid','20221103214047.jpg'),
(26,79,3230,'online','paid','20221103214047.jpg'),
(27,79,3230,'online','paid','20221103214047.jpg'),
(28,80,245,'online','paid','20221103214346.jpg'),
(29,80,980,'online','paid','20221103214346.jpg'),
(30,81,275,'online','paid','20221103214807.jpg'),
(31,81,1100,'online','paid','20221103214807.jpg'),
(32,81,1100,'online','paid','20221103214807.jpg'),
(33,0,0,'online','paid',NULL),
(34,0,0,'online','paid',NULL),
(35,82,245,'online','paid','20221103215056.jpg'),
(36,82,980,'online','paid','20221103215056.jpg'),
(37,82,980,'online','paid','20221103215056.jpg'),
(38,83,150,'online','pending',NULL),
(39,84,150,'online','pending',NULL),
(40,85,150,'online','pending',NULL),
(41,86,150,'online','pending',NULL),
(42,87,1700,'online','paid','20221104222257.jpg'),
(43,88,6000,'online','paid','20221105121542.jpg'),
(44,88,6000,'online','paid','20221105121542.jpg'),
(45,88,6000,'online','paid','20221105121542.jpg'),
(46,89,680,'online','paid','20221105122745.jpg'),
(47,90,245,'online','paid','20221106084928.jpg'),
(48,91,300,'online','paid','20221106085914.jpg'),
(49,92,300,'online','pending',NULL),
(50,93,580,'online','paid','20221106090857.jpg'),
(51,94,1445,'online','paid','20221106092349.jpg'),
(52,95,725,'online','paid','20221106092857.jpg'),
(53,95,2900,'online','paid','20221106092857.jpg'),
(54,96,2900,'online','paid','20221106093037.jpg'),
(55,97,5100,'online','paid','20221106093501.jpg'),
(56,98,1200,'online','paid','20221106094152.jpg'),
(57,98,655,'online','paid','20221106094152.jpg'),
(58,99,3300,'online','paid','20221106094502.jpg'),
(59,100,1200,'online','paid','20221106094717.jpg'),
(60,101,1200,'online','paid','20221106095024.jpg'),
(61,102,1200,'online','paid','20221112104956.jpg'),
(62,102,3600,'online','paid','20221112104956.jpg'),
(63,102,3600,'online','paid','20221112104956.jpg'),
(64,102,6000,'online','paid','20221112104956.jpg'),
(65,102,6000,'online','paid','20221112104956.jpg'),
(66,102,9600,'online','paid','20221112104956.jpg'),
(67,102,9600,'online','paid','20221112104956.jpg'),
(68,102,10950,'online','paid','20221112104956.jpg'),
(69,102,13200,'online','paid','20221112104956.jpg'),
(70,102,17100,'online','paid','20221112104956.jpg'),
(71,102,17100,'online','paid','20221112104956.jpg'),
(72,102,17100,'online','paid','20221112104956.jpg'),
(73,102,17100,'online','paid','20221112104956.jpg'),
(74,102,15450,'online','paid','20221112104956.jpg'),
(75,102,15450,'online','paid','20221112104956.jpg'),
(76,102,19200,'online','paid','20221112104956.jpg'),
(77,102,19200,'online','paid','20221112104956.jpg'),
(78,102,0,'online','paid','20221112104956.jpg'),
(79,102,15000,'online','paid','20221112104956.jpg'),
(80,102,2700,'online','paid','20221112104956.jpg'),
(81,102,0,'online','paid','20221112104956.jpg'),
(82,102,21000,'online','paid','20221112104956.jpg'),
(83,102,21450,'online','paid','20221112104956.jpg'),
(84,103,245,'online','paid','20221106124933.jpg'),
(85,104,300,'online','paid','20221106125003.jpg'),
(86,105,750,'online','pending',NULL),
(87,106,750,'online','pending',NULL),
(88,107,750,'online','pending',NULL),
(89,108,750,'online','pending',NULL),
(90,109,750,'online','pending',NULL),
(91,110,750,'online','pending',NULL),
(92,111,750,'online','pending',NULL),
(93,112,750,'online','pending',NULL),
(94,113,750,'online','pending',NULL),
(95,114,750,'online','pending',NULL),
(96,115,750,'online','pending',NULL),
(97,116,750,'online','pending',NULL),
(98,117,150,'online','pending',NULL),
(99,118,300,'online','pending',NULL),
(100,102,21000,'online','paid','20221112104956.jpg'),
(101,102,3600,'online','paid','20221112104956.jpg'),
(102,119,820,'online','paid','20221112141954.jpg'),
(103,120,245,'online','paid','20221112142941.jpg'),
(104,121,1040,'online','paid','20221112143416.jpg'),
(105,122,8990,'online','paid','20221112144754.jpg'),
(106,122,8990,'online','paid','20221112144754.jpg'),
(107,122,8990,'online','paid','20221112144754.jpg'),
(109,122,8990,'online','paid','20221112144754.jpg'),
(110,123,545,'online','paid','20221112154614.jpg'),
(111,123,0,'online','paid','20221112154614.jpg'),
(112,123,0,'online','paid','20221112154614.jpg'),
(113,123,13335,'online','paid','20221112154614.jpg'),
(114,123,13335,'online','paid','20221112154614.jpg'),
(115,123,13335,'online','paid','20221112154614.jpg'),
(116,123,0,'online','paid','20221112154614.jpg'),
(117,123,0,'online','paid','20221112154614.jpg'),
(118,123,0,'online','paid','20221112154614.jpg'),
(119,123,345,'online','paid','20221112154614.jpg'),
(120,123,345,'online','paid','20221112154614.jpg'),
(121,123,0,'online','paid','20221112154614.jpg'),
(122,123,445,'online','paid','20221112154614.jpg'),
(123,123,935,'online','paid','20221112154614.jpg'),
(124,123,1280,'online','paid','20221112154614.jpg'),
(125,123,545,'online','paid','20221112154614.jpg');

/*Table structure for table `products` */

DROP TABLE IF EXISTS `products`;

CREATE TABLE `products` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_id` int(11) DEFAULT NULL,
  `p_name` varchar(20) NOT NULL,
  `details` varchar(100) NOT NULL,
  `price` int(11) NOT NULL,
  `stock` int(15) NOT NULL,
  `qty` varchar(10) DEFAULT NULL,
  `image` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

/*Data for the table `products` */

insert  into `products`(`product_id`,`category_id`,`p_name`,`details`,`price`,`stock`,`qty`,`image`) values 
(7,13,'Sapota','Sapota is a great fruit for enhancing skin health and beauty. The abundance of vitamins A, C, E and ',245,12,'Kg','20221017063351.jpg'),
(11,5,'Plastic Orchid Plant','Multicolour, 18cm x 15cm x 12 cm',100,35,'Nos','20221017064023.jpg'),
(13,13,'Avocado','What are the benefits of eating avocado?\r\nImage result for avocado\r\nAvocados are a source of vitamin',150,17,'Kg','20221017063643.jpg'),
(14,13,'Mangosteen','Mangosteen has been used to treat skin infections and diarrhea.',300,39,'Kg','20221015054835.jpg'),
(15,13,'Rambuttan','Rambutans are also full of potassium, a mineral that helps your heart beat, kidneys function, and mu',200,37,'Kg','20221015054856.jpg'),
(19,13,'Dragon Fruit','Dragon fruit is high in vitamin C and other antioxidants, which are good for your immune system. It ',280,9,'Kg','20221015055142.jpg'),
(20,11,'Champagne Palm','Ornamental plant. Indoor/Outdoor Usage	Outdoor',245,33,'Nos','20221017062412.jpg'),
(21,11,'Areca palm','Palm\r\nIndoor Usage	\r\nMoisture Needs	Moderate Watering\r\nHealthy Plants Potted in Organic Medium\r\nPlan',275,19,'Nos','20221017062754.jpg'),
(22,11,'Pegasus Flora Cactus','size 1.5 inches [small]\r\ncontents: 4 inch color pot-1, soil mix, live plant-1.',450,15,'Nos','20221017064238.jpg'),
(23,5,'Plastic Pot','60 x 60 x 60 Centimeters\r\nPlant pots for your home light weight and easy to handle sturdy quality vi',400,19,'Kg','20221017064432.jpg'),
(24,5,'Yellow Planter POTS','Plant planters for all your gardening indoor or outdoor uses',180,19,'Nos','20221017064557.jpg'),
(25,11,'Mangosteen','Plant Age	6 Months\r\nMaturity Duration	4.5 to 6 years',750,20,'Nos','20221017092413.jpg'),
(26,11,'Rambuttan ','In one acre of land, up to 35 saplings could be planted. The pits (1m sq.) should be filled with top',450,31,'Nos','20221017092957.jpg'),
(27,13,'orange','wefw',345,23,'Kg','20221112103316.jpg');

/*Table structure for table `register` */

DROP TABLE IF EXISTS `register`;

CREATE TABLE `register` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) NOT NULL,
  `first_name` varchar(15) NOT NULL,
  `last_name` varchar(15) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `place` varchar(20) NOT NULL,
  `post` varchar(20) NOT NULL,
  `pin` int(11) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `email_id` varchar(25) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;

/*Data for the table `register` */

insert  into `register`(`user_id`,`login_id`,`first_name`,`last_name`,`gender`,`place`,`post`,`pin`,`phone`,`email_id`) values 
(12,14,'Ram','crucial','MALE','safasfuy','fdweerc',235245,'2147483647','dwqdqwf'),
(17,19,'hl','hk','MALE','hrt','thtr',454534,'5423333333','alen@gmail.com'),
(18,20,'kk','jk','MALE','cv','md',123456,'1234567891','skdf@gmail.com'),
(19,21,'ef','fr','MALE','rf','eer',12,'1234567891','alen@gmail.com'),
(20,22,'divya','p','MALE','calicut','frt',4555565,'8089999911','alen1@gmail.com'),
(21,23,'Alen','christy','MALE','gui','hgfhg',456734,'1234567890','alenchristy0201@gmail.com'),
(22,24,'re','fwerf','MALE','ertyer','sgrs',36576,'1234567890','alen@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
