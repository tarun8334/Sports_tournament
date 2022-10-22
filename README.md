##### for creating the database sql commands:-

DROP DATABASE IF EXISTS `phase4_2`;
CREATE SCHEMA `phase4_2`;
USE `phase4_2`;

DROP TABLE IF EXISTS `registrants`;
CREATE TABLE `registrants` (
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL UNIQUE,
  `password` varchar(9) NOT NULL,
  `age` int(11)  NOT NULL,
  `date_of_birth` char(10) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `address` varchar(50) NOT NULL,
  `type_of_marathon` varchar(50) NOT NULL, 
  `phonenumber1` BIGINT(8) NOT NULL UNIQUE,
  `phonenumber2` BIGINT(8) DEFAULT NULL,
  `registration_id` int(11) NOT NULL,
  CONSTRAINT PK_Person0 PRIMARY KEY (registration_id)
);

INSERT INTO registrants (name,email,password,age,date_of_birth,gender,address,type_of_marathon,phonenumber1,registration_id)
VALUES ("aaaa",'a@gmail.com','a',10,'10/10/1010','male','aa','relay',1111111111,1);
INSERT INTO registrants (name,email,password,age,date_of_birth,gender,address,type_of_marathon,phonenumber1,phonenumber2,registration_id)
VALUES ("bbbb",'b@gmail.com','b',10,'10/10/1010','female','bb','relay',222222222,22222222,2);
INSERT INTO registrants (name,email,password,age,date_of_birth,gender,address,type_of_marathon,phonenumber1,registration_id)
VALUES ("cccc",'c@gmail.com','c',10,'10/10/1010','male','cc','relay',1111111112,3);



DROP TABLE IF EXISTS `donation`;
CREATE TABLE `donation` (
  `Name` varchar(50) NOT NULL,
  `amount` int(11) NOT NULL,
  `email` varchar(50) NOT NULL UNIQUE,
  `tribute_information` varchar(50) NOT NULL,
  `company_name` varchar(50) NOT NULL,
  `billing_address` varchar(50) NOT NULL,
  `phonenumber1` BIGINT(8) NOT NULL,
  `phonenumber2` BIGINT(8) DEFAULT NULL,
  `card_detail` varchar(50) NOT NULL,
  -- CONSTRAINT PK_Person1 PRIMARY KEY (email)
  CONSTRAINT `donation_ibfk_1` FOREIGN KEY (`email`) REFERENCES `registrants` (`email`)
);

INSERT INTO donation 
VALUES ('aaaa',1000,'a@gmail.com','xyz','xyz','xyz',6876686878,98798798,'xyz');
INSERT INTO donation 
VALUES ('bbbb',1000,'b@gmail.com','xyz','xyz','xyz',6876686878,98798798,'xyz');
INSERT INTO donation 
VALUES ('cccc',1000,'c@gmail.com','xyz','xyz','xyz',6876686878,98798798,'xyz');


DROP TABLE IF EXISTS `shop`;
CREATE TABLE `shop` (
  `Name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL UNIQUE,
  `phonenumber1` BIGINT(8) NOT NULL,
  `phonenumber2` BIGINT(8) DEFAULT NULL,
  `colour` varchar(20) NOT NULL,
  `item_id` int(11) NOT NULL,
  `size` int(11) NOT NULL,
  `shipping_address` varchar(50) NOT NULL,
  `payment_detail` varchar(50) NOT NULL,
  `quality` varchar(50) NOT NULL,
  -- CONSTRAINT PK_Person2 PRIMARY KEY (email)
  CONSTRAINT `shops_ibfk_1` FOREIGN KEY (`email`) REFERENCES `registrants` (`email`)
);


INSERT INTO shop 
VALUES ('aaaa','a@gmail.com',6876686878,98798798,'xyz',11,12,'xyz','xyz','12');
INSERT INTO shop
VALUES ('aaaa','b@gmail.com',6876686878,98798798,'aaa',12,11,'aaz','aaz','13');



DROP TABLE IF EXISTS `hotels`;
CREATE TABLE `hotels` (
  `hotel_id` int(11) NOT NULL,
  `hotel_name` varchar(50) NOT NULL,
  `location` varchar(50) NOT NULL,
  `room_type` varchar(15) NOT NULL,
  `destination_id` int(11) NOT NULL UNIQUE,
  `destination_name` varchar(30) NOT NULL,
  `vacancy` varchar(10) NOT NULL,
  `bank_detail` varchar(50) NOT NULL, 
  CONSTRAINT PK_Person3 PRIMARY KEY (hotel_id)
);

INSERT INTO hotels 
VALUES (1,'aa','xyz','cheap',1,'xyz','e','xyz');
INSERT INTO hotels 
VALUES (2,'aa','xyz','cheap',2,'xyz','f','xyz');




DROP TABLE IF EXISTS `lodges`;
CREATE TABLE `lodges` (
  `hotel_id` int(11) NOT NULL ,
  `registrantid` int(11) NOT NULL UNIQUE ,
  -- CONSTRAINT PK_Person3 PRIMARY KEY (hotel_id,registrantid)
  CONSTRAINT `hotels_ibfk_1` FOREIGN KEY (`hotel_id`) REFERENCES `hotels` (`hotel_id`)
);
INSERT INTO lodges
VALUES (2,1);
INSERT INTO lodges 
VALUES (1,2);



DROP TABLE IF EXISTS `results`;
CREATE TABLE `results` (
  `competitor` varchar(50) NOT NULL,
  `results` varchar(50) NOT NULL,
  `year_of_event` int(11) NOT NULL,
  `type_of_marathon` varchar(50) NOT NULL,
  CONSTRAINT PK_Person4 PRIMARY KEY (competitor)
);
INSERT INTO results
VALUES ("aaaa","w",1,"relay");
INSERT INTO results 
VALUES ("bbbb","l",1,"relay");


DROP TABLE IF EXISTS `recreational_facilites`;
CREATE TABLE `recreational_facilities` (
  `hotel_id` int(11) NOT NULL,
  `supervisor_id` int(11) NOT NULL UNIQUE,
  `discription` varchar(100) NOT NULL,
  `provider` varchar(100) NOT NULL,
  CONSTRAINT `recreational_facilities_ibfk_1` FOREIGN KEY (`hotel_id`) REFERENCES `hotels` (`hotel_id`)
);
INSERT INTO recreational_facilities
VALUES (1,1,'xyz','xyz');
INSERT INTO recreational_facilities
VALUES (2,2,'xyz','xyz');


DROP TABLE IF EXISTS `destination`;
CREATE TABLE `destination` (
  `destination_id` int(11) NOT NULL UNIQUE,
  `transport_detail` varchar(100) NOT NULL,
  `destination_name` varchar(100) NOT NULL,
  `location` varchar(100) NOT NULL,
  CONSTRAINT `destination_ibfk_1` FOREIGN KEY (`destination_id`) REFERENCES `hotels` (`destination_id`)
);

INSERT INTO destination
VALUES (1,'xyz','xyz','xyz');
INSERT INTO destination
VALUES (2,'xyz','xyz','xyz');


DROP TABLE IF EXISTS `volunteer_registration`;
CREATE TABLE `volunteer_registration` (
  `registration_id` int(11) NOT NULL,
  `volunteer_opportunities` varchar(100) NOT NULL,
  CONSTRAINT `volunteer_registration_ibfk_1` FOREIGN KEY (`registration_id`) REFERENCES `registrants` (`registration_id`) 
) ;

INSERT INTO volunteer_registration
VALUES (1,'ground');
INSERT INTO volunteer_registration
VALUES (2,'sky');

DROP TABLE IF EXISTS `contacts`;
CREATE TABLE `contacts` (
  `phonenumber` bigint(8) NOT NULL UNIQUE,
  `email` varchar(100) NOT NULL UNIQUE,
  `question` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  CONSTRAINT `contacts_ibfk_1` FOREIGN KEY (`phonenumber`) REFERENCES `registrants` (`phonenumber1`)
);
INSERT INTO contacts
VALUES (1111111111,'a@gmail.com','xyz','aaaa');
INSERT INTO contacts
VALUES 1111111112,'b@gmail.com','xyz','bbbb');


##### for python file:-

# option-1:-
 Insert a new participant;  
# option-2:-
 Delete the details of people who have cancelled their booking for a hotel. 
# option-3:-
 Update the phone number of Rregistrant.
# option-4:-
 Prints details of registrants living in hotel_id = 1")
# option-5:-
 Results of all winning participants")
# option-6:-
 Details of minimmum age participants")
# option-7:-
 Details of all the participants in a particular hotel")
# option-8:-
 Results.
# option-2:-
 Delete the details of people who have cancelled their booking for a hotel. 
# option-9:-
 Logout.














