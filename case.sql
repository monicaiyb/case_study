CREATE DATABASE IF NOT EXISTS `case` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `case`;

CREATE TABLE IF NOT EXISTS `farmers` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
  	`name` varchar(50) NOT NULL,
	`phone`varchar(20) NOT NULL,
  	`password` varchar(255) NOT NULL,
  	`email` varchar(100) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS `deliveries` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
  	`name` varchar(50) NOT NULL,
	`phone`varchar(20) NOT NULL,
  	`password` varchar(255) NOT NULL,
  	`email` varchar(100) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;