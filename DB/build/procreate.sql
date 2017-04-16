/* Javier Sorribes, 04/04/2017
	Populates DB one initial time
	SHOULD ONLY BE RUN ONCE
*/
USE library;

INSERT INTO user  (username,userpass,role,id) VALUES ('jsorribes','javier',1,1);
INSERT INTO user  (username,userpass,role,id) VALUES ('enakagawa','eldon',1,2);
INSERT INTO user  (username,userpass,role,id) VALUES ('rnguyen','ricky',1,3);
INSERT INTO user  (username,userpass,role,id) VALUES ('aparakh','aditya',1,4);
INSERT INTO user  (username,userpass,role,id) VALUES ('pgarcia','pepe',2,1);
INSERT INTO user  (username,userpass,role,id) VALUES ('oaldawud','omar',2,2);
INSERT INTO user  (username,userpass,role,id) VALUES ('xyi','xue',2,3);
INSERT INTO user  (username,userpass,role,id) VALUES ('kvladilkov','kristoff',2,4);
INSERT INTO user  (username,userpass,role,id) VALUES ('mmichelson','mike',3,1);
INSERT INTO user  (username,userpass,role,id) VALUES ('sstevenson','steve',3,2);
INSERT INTO user  (username,userpass,role,id) VALUES ('ppeterson','peter',3,3);
INSERT INTO user  (username,userpass,role,id) VALUES ('ssue','suzanne',3,4);
INSERT INTO user  (username,userpass,role,id) VALUES ('jcorrales','jarvin',3,5);
INSERT INTO user  (username,userpass,role,id) VALUES ('apatel','ashkosh',3,6);


INSERT INTO admin (firstname,lastname) VALUES ('Javier','Sorribes');
INSERT INTO admin (firstname,lastname) VALUES ('Eldon','Nakagawa');
INSERT INTO admin (firstname,lastname) VALUES ('Ricky','Nguyen');
INSERT INTO admin (firstname,lastname) VALUES ('Aditya','Parakh');

INSERT INTO teacher (firstname,lastname) VALUES ('Pepe','Garcia');
INSERT INTO teacher (firstname,lastname) VALUES ('Omar','Aldawud');
INSERT INTO teacher (firstname,lastname) VALUES ('Xue','Yi');
INSERT INTO teacher (firstname,lastname) VALUES ('Kristoff','Vladilkov');

INSERT INTO student (firstname,lastname,advisorid) VALUES ('Mike','Michelson',1);
INSERT INTO student (firstname,lastname,advisorid) VALUES ('Steve','Stevenson',1);
INSERT INTO student (firstname,lastname,advisorid) VALUES ('Peter','Peterson',2);
INSERT INTO student (firstname,lastname,advisorid) VALUES ('Suzanne','Sue',2);
INSERT INTO student (firstname,lastname,advisorid) VALUES ('Jarvin','Corrales',2);
INSERT INTO student (firstname,lastname,advisorid) VALUES ('Ashkosh','Patel',4);

INSERT INTO parent (firstname,lastname) VALUES ('Onur','Tankre');
INSERT INTO parent (firstname,lastname) VALUES ('Suzanne','Peters');
INSERT INTO parent (firstname,lastname) VALUES ('Monica','Fork');
INSERT INTO parent (firstname,lastname) VALUES ('Shaquille','Spoon');
INSERT INTO parent (firstname,lastname) VALUES ('Samuel','Sue');
INSERT INTO parent (firstname,lastname) VALUES ('Miguel','Corrales');
INSERT INTO parent (firstname,lastname) VALUES ('Latiffa','Sparks');
INSERT INTO parent (firstname,lastname) VALUES ('Vaishnati','Singh');

INSERT INTO has (parentid,studentid) VALUES (1,1);
INSERT INTO has (parentid,studentid) VALUES (2,1);
INSERT INTO has (parentid,studentid) VALUES (3,2);
INSERT INTO has (parentid,studentid) VALUES (4,2);
INSERT INTO has (parentid,studentid) VALUES (5,4);
INSERT INTO has (parentid,studentid) VALUES (6,5);
INSERT INTO has (parentid,studentid) VALUES (7,5);
INSERT INTO has (parentid,studentid) VALUES (1,6);
INSERT INTO has (parentid,studentid) VALUES (8,6);

INSERT INTO parent_contact (contact,parentid) VALUES ('otankre@gmail.com',1);
INSERT INTO parent_contact (contact,parentid) VALUES ('312-687-9525',2);
INSERT INTO parent_contact (contact,parentid) VALUES ('suzypeters@suzyinc.com',2);
INSERT INTO parent_contact (contact,parentid) VALUES ('forkss@silverware.com',3);
INSERT INTO parent_contact (contact,parentid) VALUES ('shaqspoon@silverware.com',4);
INSERT INTO parent_contact (contact,parentid) VALUES ('872-858-8963',4);
INSERT INTO parent_contact (contact,parentid) VALUES ('312-555-5555',5);
INSERT INTO parent_contact (contact,parentid) VALUES ('ssue@yahoo.com',5);
INSERT INTO parent_contact (contact,parentid) VALUES ('3124 S Wacker Dr, Chicago, IL 61623',5);
INSERT INTO parent_contact (contact,parentid) VALUES ('mcorrales@gmail.com',6);
INSERT INTO parent_contact (contact,parentid) VALUES ('v96singh2sing@gmail.co.uk',7);

INSERT INTO course (name,year,semester,teacherid) VALUES ('CS425',2016,'fall',3);
INSERT INTO course (name,year,semester,teacherid) VALUES ('CS425',2016,'summer',2);
INSERT INTO course (name,year,semester,teacherid) VALUES ('CS425',2017,'spring',2);
INSERT INTO course (name,year,semester,teacherid) VALUES ('LIT202',2017,'fall',4);
INSERT INTO course (name,year,semester,teacherid) VALUES ('LIT202',2017,'summer',4);
INSERT INTO course (name,year,semester,teacherid) VALUES ('LIT202',2016,'spring',4);
INSERT INTO course (name,year,semester,teacherid) VALUES ('MATH333',2017,'spring',4);
INSERT INTO course (name,year,semester,teacherid) VALUES ('MATH333',2016,'summer',3);
INSERT INTO course (name,year,semester,teacherid) VALUES ('MATH374',2017,'spring',2);
INSERT INTO course (name,year,semester,teacherid) VALUES ('CS487',2017,'spring',2);

INSERT INTO takes (name,year,semester,studentid) VALUES ('CS425',2016,'fall',1);
INSERT INTO takes (name,year,semester,studentid) VALUES ('CS425',2016,'summer',3);
INSERT INTO takes (name,year,semester,studentid) VALUES ('CS425',2017,'spring',6);
INSERT INTO takes (name,year,semester,studentid) VALUES ('LIT202',2017,'summer',6);
INSERT INTO takes (name,year,semester,studentid) VALUES ('LIT202',2016,'spring',1);
INSERT INTO takes (name,year,semester,studentid) VALUES ('MATH333',2017,'spring',2);
INSERT INTO takes (name,year,semester,studentid) VALUES ('MATH333',2016,'summer',2);
INSERT INTO takes (name,year,semester,studentid) VALUES ('MATH374',2017,'spring',1);
INSERT INTO takes (name,year,semester,studentid) VALUES ('CS487',2017,'spring',1);
INSERT INTO takes (name,year,semester,studentid) VALUES ('CS425',2016,'fall',3);
INSERT INTO takes (name,year,semester,studentid) VALUES ('CS425',2016,'summer',2);
INSERT INTO takes (name,year,semester,studentid) VALUES ('CS425',2017,'spring',2);
INSERT INTO takes (name,year,semester,studentid) VALUES ('LIT202',2017,'summer',4);
INSERT INTO takes (name,year,semester,studentid) VALUES ('LIT202',2016,'spring',4);
INSERT INTO takes (name,year,semester,studentid) VALUES ('MATH333',2017,'spring',4);
INSERT INTO takes (name,year,semester,studentid) VALUES ('MATH374',2017,'spring',2);
INSERT INTO takes (name,year,semester,studentid) VALUES ('CS487',2017,'spring',2);

/*could omit the studentids here*/
INSERT INTO book (isbn,cost,duedate,datecheckedout,title,coursename,courseyear,coursesemester,studentid) VALUES ('0321369572',36.50,NULL,NULL,'Database Systems','CS425',2016,'fall',NULL);
INSERT INTO book (isbn,cost,duedate,datecheckedout,title,coursename,courseyear,coursesemester,studentid) VALUES ('0321369572',36.50,'2016-08-03','2016-07-04','Database Systems','CS425',2016,'summer',3);
INSERT INTO book (isbn,cost,duedate,datecheckedout,title,coursename,courseyear,coursesemester,studentid) VALUES ('0321369572',36.50,'2017-02-22','2017-01-23','Database Systems','CS425',2017,'spring',6);
INSERT INTO book (isbn,cost,duedate,datecheckedout,title,coursename,courseyear,coursesemester,studentid) VALUES ('0060935464',20.10,NULL,NULL,'English Literature','LIT202',2017,'summer',NULL);
INSERT INTO book (isbn,cost,duedate,datecheckedout,title,coursename,courseyear,coursesemester,studentid) VALUES ('0060935464',9.53,'2017-03-28','2017-02-26','English Literature','LIT202',2016,'spring',1);
INSERT INTO book (isbn,cost,duedate,datecheckedout,title,coursename,courseyear,coursesemester,studentid) VALUES ('0139491570',56.00,'2017-04-29','2017-03-30','Complex Analysis, Determinants and Matrices','MATH333',2017,'spring',2);
INSERT INTO book (isbn,cost,duedate,datecheckedout,title,coursename,courseyear,coursesemester,studentid) VALUES ('0321210263',15.20,'2017-05-12','2017-04-12','Software Engineering for Engineers','CS487',2017,'spring',1);
INSERT INTO book (isbn,cost,duedate,datecheckedout,title,coursename,courseyear,coursesemester,studentid) VALUES ('0321369572',36.50,'2016-11-24','2016-10-25','Database Systems','CS425',2016,'fall',3);
INSERT INTO book (isbn,cost,duedate,datecheckedout,title,coursename,courseyear,coursesemester,studentid) VALUES ('0321369572',36.50,NULL,NULL,'Database Systems','CS425',2016,'summer',NULL);
INSERT INTO book (isbn,cost,duedate,datecheckedout,title,coursename,courseyear,coursesemester,studentid) VALUES ('0321369572',36.50,NULL,NULL,'Database Systems','CS425',2017,'spring',NULL);
INSERT INTO book (isbn,cost,duedate,datecheckedout,title,coursename,courseyear,coursesemester,studentid) VALUES ('0060935464',20.10,NULL,NULL,'English Literature','LIT202',2017,'summer',NULL);
INSERT INTO book (isbn,cost,duedate,datecheckedout,title,coursename,courseyear,coursesemester,studentid) VALUES ('0060935464',9.53,NULL,NULL,'English Literature','LIT202',2016,'spring',NULL);
INSERT INTO book (isbn,cost,duedate,datecheckedout,title,coursename,courseyear,coursesemester,studentid) VALUES ('0321210263',15.20,NULL,NULL,'Software Engineering for Engineers','CS487',2017,'spring',NULL);
INSERT INTO book (isbn,cost,duedate,datecheckedout,title,coursename,courseyear,coursesemester,studentid) VALUES ('0321369572',36.50,NULL,NULL,'Database Systems','CS425',2017,'spring',NULL);

INSERT INTO book_request (isbn,cost,title,coursename,courseyear,coursesemester,requestedby,quantity) VALUES ('0139491570',56.00,'Complex Analysis, Determinants and Matrices','MATH333',2017,'spring','student',1);
INSERT INTO book_request (isbn,cost,title,coursename,courseyear,coursesemester,requestedby,quantity) VALUES ('0060935464',9.53,'English Literature','LIT202',2017,'spring','teacher',5);
INSERT INTO book_request (isbn,cost,title,coursename,courseyear,coursesemester,requestedby,quantity) VALUES ('0321210263',15.20,'Software Engineering for Engineers','CS487',2017,'spring','teacher',3);

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
