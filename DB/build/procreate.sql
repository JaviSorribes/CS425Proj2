/* Javier Sorribes, 04/04/2017
	Populates DB one initial time
	SHOULD ONLY BE RUN ONCE
*/
USE library;

INSERT INTO users (username,userpass,role) VALUES ('jsorribes','javier',1);
INSERT INTO users (username,userpass,role) VALUES ('enakagawa','eldon',1);
INSERT INTO users (username,userpass,role) VALUES ('rnguyen','ricky',1);
INSERT INTO users (username,userpass,role) VALUES ('aparakh','aditya',1);
INSERT INTO users (username,userpass,role) VALUES ('pgarcia','pepe',2);
INSERT INTO users (username,userpass,role) VALUES ('oaldawud','omar',2);
INSERT INTO users (username,userpass,role) VALUES ('xyi','xue',2);
INSERT INTO users (username,userpass,role) VALUES ('kvladilkov','kristoff',2);
INSERT INTO users (username,userpass,role) VALUES ('mmichelson','mike',3);
INSERT INTO users (username,userpass,role) VALUES ('sstevenson','steve',3);
INSERT INTO users (username,userpass,role) VALUES ('ppeterson','peter',3);
INSERT INTO users (username,userpass,role) VALUES ('ssue','suzanne',3);
INSERT INTO users (username,userpass,role) VALUES ('jcorrales','jarvin',3);
INSERT INTO users (username,userpass,role) VALUES ('apatel','ashkosh',3);


INSERT INTO admin (username,firstname,lastname) VALUES ('jsorribes','Javier','Sorribes');
INSERT INTO admin (username,firstname,lastname) VALUES ('enakagawa','Eldon','Nakagawa');
INSERT INTO admin (username,firstname,lastname) VALUES ('rnguyen','Ricky','Nguyen');
INSERT INTO admin (username,firstname,lastname) VALUES ('aparakh','Aditya','Parakh');

INSERT INTO teacher (username,firstname,lastname) VALUES ('pgarcia','Pepe','Garcia');
INSERT INTO teacher (username,firstname,lastname) VALUES ('oaldawud','Omar','Aldawud');
INSERT INTO teacher (username,firstname,lastname) VALUES ('xyi','Xue','Yi');
INSERT INTO teacher (username,firstname,lastname) VALUES ('kvladilkov','Kristoff','Vladilkov');

INSERT INTO student (username,firstname,lastname,advisorid) VALUES ('mmichelson','Mike','Michelson',1);
INSERT INTO student (username,firstname,lastname,advisorid) VALUES ('sstevenson','Steve','Stevenson',1);
INSERT INTO student (username,firstname,lastname,advisorid) VALUES ('ppeterson','Peter','Peterson',2);
INSERT INTO student (username,firstname,lastname,advisorid) VALUES ('ssue','Suzanne','Sue',2);
INSERT INTO student (username,firstname,lastname,advisorid) VALUES ('jcorrales','Jarvin','Corrales',2);
INSERT INTO student (username,firstname,lastname,advisorid) VALUES ('apatel','Ashkosh','Patel',4);

INSERT INTO parent (firstname,lastname) VALUES ('Onur','Tankre');
INSERT INTO parent (firstname,lastname) VALUES ('Suzanne','Peters');
INSERT INTO parent (firstname,lastname) VALUES ('Monica','Fork');
INSERT INTO parent (firstname,lastname) VALUES ('Shaquille','Spoon');
INSERT INTO parent (firstname,lastname) VALUES ('Samuel','Sue');
INSERT INTO parent (firstname,lastname) VALUES ('Miguel','Corrales');
INSERT INTO parent (firstname,lastname) VALUES ('Latiffa','Sparks');
INSERT INTO parent (firstname,lastname) VALUES ('Vaishnati','Singh');

INSERT INTO has (firstname,lastname,studentid) VALUES ('Onur','Tankre',1);
INSERT INTO has (firstname,lastname,studentid) VALUES ('Suzanne','Peters',1);
INSERT INTO has (firstname,lastname,studentid) VALUES ('Monica','Fork',2);
INSERT INTO has (firstname,lastname,studentid) VALUES ('Shaquille','Spoon',2);
INSERT INTO has (firstname,lastname,studentid) VALUES ('Samuel','Sue',4);
INSERT INTO has (firstname,lastname,studentid) VALUES ('Miguel','Corrales',5);
INSERT INTO has (firstname,lastname,studentid) VALUES ('Latiffa','Sparks',5);
INSERT INTO has (firstname,lastname,studentid) VALUES ('Onur','Tankre',6);
INSERT INTO has (firstname,lastname,studentid) VALUES ('Vaishnati','Singh',6);

INSERT INTO parent_contact (contact,firstname,lastname) VALUES ('otankre@gmail.com','Onur','Tankre');
INSERT INTO parent_contact (contact,firstname,lastname) VALUES ('312-687-9525','Suzanne','Peters');
INSERT INTO parent_contact (contact,firstname,lastname) VALUES ('suzypeters@suzyinc.com','Suzanne','Peters');
INSERT INTO parent_contact (contact,firstname,lastname) VALUES ('forkss@silverware.com','Monica','Fork');
INSERT INTO parent_contact (contact,firstname,lastname) VALUES ('shaqspoon@silverware.com','Shaquille','Spoon');
INSERT INTO parent_contact (contact,firstname,lastname) VALUES ('872-858-8963','Shaquille','Spoon');
INSERT INTO parent_contact (contact,firstname,lastname) VALUES ('312-555-5555','Samuel','Sue');
INSERT INTO parent_contact (contact,firstname,lastname) VALUES ('ssue@yahoo.com','Samuel','Sue');
INSERT INTO parent_contact (contact,firstname,lastname) VALUES ('3124 S Wacker Dr, Chicago, IL 61623','Samuel','Sue');
INSERT INTO parent_contact (contact,firstname,lastname) VALUES ('mcorrales@gmail.com','Miguel','Corrales');
INSERT INTO parent_contact (contact,firstname,lastname) VALUES ('v96singh2sing@gmail.co.uk','Vaishnati','Singh');

INSERT INTO course (name,year,semester,teacherid) VALUES ('CS425',2016,'fall',3);
INSERT INTO course (name,year,semester,teacherid) VALUES ('CS425',2016,'summer',2);
INSERT INTO course (name,year,semester,teacherid) VALUES ('CS425',2017,'spring',2);
INSERT INTO course (name,year,semester,teacherid) VALUES ('LIT202',2017,'fall',4);
INSERT INTO course (name,year,semester,teacherid) VALUES ('LIT202',2017,'summer',4);
INSERT INTO course (name,year,semester,teacherid) VALUES ('LIT202',2016,'spring',4);
INSERT INTO course (name,year,semester,teacherid) VALUES ('MATH333',2017,'fall',4);
INSERT INTO course (name,year,semester,teacherid) VALUES ('MATH333',2016,'summer',3);
INSERT INTO course (name,year,semester,teacherid) VALUES ('MATH374',2017,'spring',2);
INSERT INTO course (name,year,semester,teacherid) VALUES ('CS487',2017,'spring',2);

INSERT INTO takes (name,year,semester,studentid) VALUES ('CS425',2016,'fall',1);
INSERT INTO takes (name,year,semester,studentid) VALUES ('CS425',2016,'summer',3);
INSERT INTO takes (name,year,semester,studentid) VALUES ('CS425',2017,'spring',6);
INSERT INTO takes (name,year,semester,studentid) VALUES ('LIT202',2017,'summer',6);
INSERT INTO takes (name,year,semester,studentid) VALUES ('LIT202',2016,'spring',1);
INSERT INTO takes (name,year,semester,studentid) VALUES ('MATH333',2017,'fall',2);
INSERT INTO takes (name,year,semester,studentid) VALUES ('MATH333',2016,'summer',2);
INSERT INTO takes (name,year,semester,studentid) VALUES ('MATH374',2017,'spring',1);
INSERT INTO takes (name,year,semester,studentid) VALUES ('CS487',2017,'spring',1);
INSERT INTO takes (name,year,semester,studentid) VALUES ('CS425',2016,'fall',3);
INSERT INTO takes (name,year,semester,studentid) VALUES ('CS425',2016,'summer',2);
INSERT INTO takes (name,year,semester,studentid) VALUES ('CS425',2017,'spring',2);
INSERT INTO takes (name,year,semester,studentid) VALUES ('LIT202',2017,'summer',4);
INSERT INTO takes (name,year,semester,studentid) VALUES ('LIT202',2016,'spring',4);
INSERT INTO takes (name,year,semester,studentid) VALUES ('MATH333',2017,'fall',4);
INSERT INTO takes (name,year,semester,studentid) VALUES ('MATH374',2017,'spring',2);
INSERT INTO takes (name,year,semester,studentid) VALUES ('CS487',2017,'spring',2);

/*could omit the studentids here*/
INSERT INTO book (isbn,cost,title,coursename,courseyear,coursesemester,studentid) VALUES (962344588,36.50,'Database Systems','CS425',2016,'fall',1);
INSERT INTO book (isbn,cost,title,coursename,courseyear,coursesemester,studentid) VALUES (962344588,36.50,'Database Systems','CS425',2016,'summer',3);
INSERT INTO book (isbn,cost,title,coursename,courseyear,coursesemester,studentid) VALUES (962344588,36.50,'Database Systems','CS425',2017,'spring',6);
INSERT INTO book (isbn,cost,title,coursename,courseyear,coursesemester,studentid) VALUES (785685352,20.10,'English Literature','LIT202',2017,'summer',6);
INSERT INTO book (isbn,cost,title,coursename,courseyear,coursesemester,studentid) VALUES (785685348,9.53,'English Literature','LIT202',2016,'spring',1);
INSERT INTO book (isbn,cost,title,coursename,courseyear,coursesemester,studentid) VALUES (444555856,56.00,'Complex Analysis, Determinants and Matrices','MATH333',2017,'fall',2);
INSERT INTO book (isbn,cost,title,coursename,courseyear,coursesemester,studentid) VALUES (785654255,15.20,'Software Engineering for Engineers','CS487',2017,'spring',1);
INSERT INTO book (isbn,cost,title,coursename,courseyear,coursesemester,studentid) VALUES (962344588,36.50,'Database Systems','CS425',2016,'fall',3);
INSERT INTO book (isbn,cost,title,coursename,courseyear,coursesemester,studentid) VALUES (962344588,36.50,'Database Systems','CS425',2016,'summer',2);
INSERT INTO book (isbn,cost,title,coursename,courseyear,coursesemester,studentid) VALUES (962344588,36.50,'Database Systems','CS425',2017,'spring',2);
INSERT INTO book (isbn,cost,title,coursename,courseyear,coursesemester,studentid) VALUES (785685352,20.10,'English Literature','LIT202',2017,'summer',4);
INSERT INTO book (isbn,cost,title,coursename,courseyear,coursesemester,studentid) VALUES (785685348,9.53,'English Literature','LIT202',2016,'spring',4);
INSERT INTO book (isbn,cost,title,coursename,courseyear,coursesemester,studentid) VALUES (785654255,15.20,'Software Engineering for Engineers','CS487',2017,'spring',2);
INSERT INTO book (isbn,cost,title,coursename,courseyear,coursesemester,studentid) VALUES (962344588,36.50,'Database Systems','CS425',2017,'spring',NULL);

INSERT INTO controls (adminid,bookid) VALUES (1,1);
INSERT INTO controls (adminid,bookid) VALUES (1,2);
INSERT INTO controls (adminid,bookid) VALUES (1,3);
INSERT INTO controls (adminid,bookid) VALUES (1,4);
INSERT INTO controls (adminid,bookid) VALUES (2,5);
INSERT INTO controls (adminid,bookid) VALUES (2,6);
INSERT INTO controls (adminid,bookid) VALUES (2,7);
INSERT INTO controls (adminid,bookid) VALUES (2,8);
INSERT INTO controls (adminid,bookid) VALUES (2,9);
INSERT INTO controls (adminid,bookid) VALUES (2,10);
INSERT INTO controls (adminid,bookid) VALUES (2,11);
INSERT INTO controls (adminid,bookid) VALUES (3,12);
INSERT INTO controls (adminid,bookid) VALUES (3,13);
INSERT INTO controls (adminid,bookid) VALUES (3,14);
