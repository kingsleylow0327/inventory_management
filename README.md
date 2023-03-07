# inventory_management


# Creating DB schema and table
CREATE SCHEMA `inventory` ;
CREATE TABLE `inventory`.`inventory` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `category` VARCHAR(45) NULL,
  `price` VARCHAR(45) NULL,
  `last_updated_dt` DATETIME NULL,
  PRIMARY KEY (`id`));
  SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));

