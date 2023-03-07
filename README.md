# inventory_management

# Pip Package
Install following package before run the programe  \
pip3 install flask  \
pip3 install Flask-SQLAlchemy  \
pip3 install pytz  \
pip3 install python-dotenv  \
pip3 install PyMySQL

# Data Base Environment Setup
Create a .env file under same dir as app.py with following format(Don't Change SCHEMA):  \
HOST=  \
PASSWORD=  \
IP=  \
PORT=  \
SCHEMA=inventory

# Creating DB schema and table
CREATE SCHEMA `inventory` ;  \
CREATE TABLE `inventory`.`inventory` (  \
  `id` INT NOT NULL AUTO_INCREMENT,  \
  `name` VARCHAR(45) NULL,  \
  `category` VARCHAR(45) NULL,  \
  `price` VARCHAR(45) NULL,  \
  `last_updated_dt` DATETIME NULL,  \
  PRIMARY KEY (`id`));  \
SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));

# Running the program
python3 app.py  \

Request example:  \
url = http://127.0.0.1:5001/category  \
Body = {"category":"all"}  \
Content Type ='application/json'  \
Request Method = POST

# Unit Test
Simply cd into unit_test folder and run each py script accordingly

