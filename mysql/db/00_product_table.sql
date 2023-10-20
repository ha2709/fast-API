CREATE TABLE `product` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  `description` varchar(256) NOT NULL,
 
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
);
