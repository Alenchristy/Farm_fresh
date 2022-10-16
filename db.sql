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
  PRIMARY KEY (`b_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `booking` */

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(15) NOT NULL,
  `image` varchar(50) NOT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `category` */

insert  into `category`(`category_id`,`category_name`,`image`) values 
(3,'frt','20221005120537.jpg'),
(4,'fruits','20220926143442.jpg'),
(5,'others','20221005143714.jpg');

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
  `details` varchar(100) NOT NULL,
  `rate` int(11) NOT NULL,
  `image` varchar(30) NOT NULL,
  `status` varchar(15) NOT NULL,
  PRIMARY KEY (`h_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `homestay` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(15) NOT NULL,
  `password` varchar(15) NOT NULL,
  `type` varchar(10) NOT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(2,'user','user','user'),
(3,'123','123','user'),
(4,'alen','123','user'),
(5,'ergern','admi','user'),
(6,'ergern','4534534234','user'),
(7,'alen','123','user'),
(8,'alen','5675768787','user'),
(9,'alen','','user'),
(10,'user','user','user'),
(11,'admin','admin','user'),
(12,'al','al','user'),
(13,'ygygy','123','user'),
(14,'ram','12','user');

/*Table structure for table `order` */

DROP TABLE IF EXISTS `order`;

CREATE TABLE `order` (
  `order_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `price` int(11) NOT NULL,
  `status` varchar(15) NOT NULL,
  `del_date` date NOT NULL,
  `del_address` varchar(40) NOT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `order` */

/*Table structure for table `order_item` */

DROP TABLE IF EXISTS `order_item`;

CREATE TABLE `order_item` (
  `oi_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  PRIMARY KEY (`oi_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `order_item` */

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `mode` varchar(20) NOT NULL,
  `status` varchar(15) NOT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

/*Table structure for table `products` */

DROP TABLE IF EXISTS `products`;

CREATE TABLE `products` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_id` int(11) DEFAULT NULL,
  `p_name` varchar(20) NOT NULL,
  `details` varchar(100) NOT NULL,
  `price` int(11) NOT NULL,
  `stock` varchar(15) NOT NULL,
  `image` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `products` */

insert  into `products`(`product_id`,`category_id`,`p_name`,`details`,`price`,`stock`,`image`) values 
(1,0,'khk','gsrg',6544,'646','20221001122903.jpg'),
(2,1,'sfa','sgsrge',345,'23kg','20221001123301.jpg'),
(3,1,'mango','ahdhqowi',200,'50kg','20221001145821.jpg'),
(6,3,'Dragon','wdqwdq',300,'40','20221005122639.jpg'),
(7,4,'plant','etwqe',245,'34','20221005143637.jpg');

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
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `register` */

insert  into `register`(`user_id`,`login_id`,`first_name`,`last_name`,`gender`,`place`,`post`,`pin`,`phone`,`email_id`) values 
(8,10,'al','dsanj','radiobutto','adnqnd','qwedni',32389,'3298','abdbi'),
(9,11,'hiuhiu','sdf','radiobutto','fweiojio','ewfjj',283,'24','wef'),
(10,12,'alen','cs','radiobutto','qwdqw','qwdqw',45325,'2147483647','sdvsdgs'),
(11,13,'alen','ghy8','radiobutto','sfdas','9u98h',789898,'75678','jbuguyu'),
(12,14,'Ram','ss','FEMALE','safasfuy','fdwe',2352,'2147483647','dwqdqwf');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
