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

-- create delivery table
CREATE TABLE IF NOT EXISTS `deliveries` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
  	`farmer_name` varchar(50) NOT NULL,
	`address`varchar(20) NOT NULL,
  	`location` varchar(255) NOT NULL,
  	`quantity` varchar(100) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- Query to select only to 10 milk producer

SELECT deliveries.farmer_name, deliveries.quantity FROM deliveries, farmers WHERE farmers.name=deliveries.farmer_name;