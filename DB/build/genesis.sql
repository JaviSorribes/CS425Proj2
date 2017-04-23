/* Javier Sorribes, 04/04/2017
	Schema for DB
	Based on HW 1, CS 425
*/

CREATE DATABASE IF NOT EXISTS library;
USE library;

CREATE TABLE user
(
  username VARCHAR(20) NOT NULL,
  userpass VARCHAR(20) NOT NULL,
  role INT NOT NULL,
  id INT NOT NULL,
  PRIMARY KEY (username)
);

CREATE TABLE admin
(
  adminid INT NOT NULL AUTO_INCREMENT,
  lastname VARCHAR(20) NOT NULL, -- Added name for Admin and Teacher
  firstname VARCHAR(20) NOT NULL,
  PRIMARY KEY (adminid)
);

CREATE TABLE teacher
(
  teacherid INT NOT NULL AUTO_INCREMENT,
  lastname VARCHAR(20) NOT NULL,
  firstname VARCHAR(20) NOT NULL,
  PRIMARY KEY (teacherid)
);

CREATE TABLE student
(
  studentid INT NOT NULL AUTO_INCREMENT,
  firstname VARCHAR(20) NOT NULL,
  lastname VARCHAR(20) NOT NULL,
  amountdue NUMERIC(5,2) NOT NULL DEFAULT 0 CHECK (amountdue >= 0),
  advisorid INT,
  PRIMARY KEY (studentid),
  FOREIGN KEY (advisorid) REFERENCES teacher(teacherid) ON DELETE SET NULL
);

CREATE TABLE parent
(
  parentid INT NOT NULL AUTO_INCREMENT,
  lastname VARCHAR(20) NOT NULL,
  firstname VARCHAR(20) NOT NULL,
  PRIMARY KEY (parentid)
  /*FOREIGN KEY (studentid) REFERENCES student(studentid)*/
);

CREATE TABLE parent_contact
(
  parentid INT NOT NULL,
  contact VARCHAR(50) NOT NULL,
  PRIMARY KEY (contact, parentid),
  FOREIGN KEY (parentid) REFERENCES parent(parentid) ON DELETE CASCADE
);

CREATE TABLE course
(
  name VARCHAR(20) NOT NULL,
  year INT(4) NOT NULL,
  semester ENUM('fall','spring','summer') NOT NULL,
  teacherid INT,
  PRIMARY KEY (name, year, semester),
  FOREIGN KEY (teacherid) REFERENCES teacher(teacherid) ON DELETE SET NULL
);

CREATE TABLE book
(
  bookid INT NOT NULL AUTO_INCREMENT,
  isbn VARCHAR(10) NOT NULL CHECK (LEN(isbn) = 10),
  cost NUMERIC(6,2) NOT NULL CHECK (cost >= 0000.00),
  duedate DATE,
  datecheckedout DATE,
  title VARCHAR(50) NOT NULL,
  coursename VARCHAR(20),
  courseyear INT(4),
  coursesemester ENUM('fall','spring','summer'),
  studentid INT,
  PRIMARY KEY (bookid),
  FOREIGN KEY (coursename, courseyear, coursesemester) REFERENCES course(name, year, semester) ON DELETE SET NULL,
  FOREIGN KEY (studentid) REFERENCES student(studentid) ON DELETE SET NULL
);

CREATE TABLE book_request
(
  requestid INT NOT NULL AUTO_INCREMENT,
  isbn VARCHAR(10) NOT NULL CHECK (LEN(isbn) = 10),
  cost NUMERIC(6,2) NOT NULL CHECK (cost >= 0000.00),
  title VARCHAR(50) NOT NULL,
  coursename VARCHAR(20) NOT NULL,
  courseyear INT(4) NOT NULL,
  coursesemester ENUM('fall','spring','summer') NOT NULL,
  requestedby ENUM('student','teacher') NOT NULL,
  quantity INT(4) NOT NULL CHECK (quantity > 0),
  PRIMARY KEY (requestid)
);

-- M:N relationships
CREATE TABLE has
(
  studentid INT NOT NULL,
  parentid INT NOT NULL,
  PRIMARY KEY (studentid, parentid),
  FOREIGN KEY (studentid) REFERENCES student(studentid) ON DELETE CASCADE,
  FOREIGN KEY (parentid) REFERENCES parent(parentid) ON DELETE CASCADE
);

CREATE TABLE takes
(
  studentid INT NOT NULL,
  name VARCHAR(20) NOT NULL,
  year INT NOT NULL,
  semester ENUM('fall','spring','summer') NOT NULL,
  PRIMARY KEY (studentid, name, year, semester),
  FOREIGN KEY (studentid) REFERENCES student(studentid) ON DELETE CASCADE,
  FOREIGN KEY (name, year, semester) REFERENCES course(name, year, semester) ON DELETE CASCADE
);

/* Not being used because all admins control all books
CREATE TABLE controls
(
  adminid INT NOT NULL,
  bookid INT NOT NULL,
  /*name VARCHAR(20) NOT NULL,
  year INT NOT NULL,
  semester CHAR NOT NULL,
  PRIMARY KEY (adminid, bookid),/*, name, year, semester),
  FOREIGN KEY (adminid) REFERENCES admin(adminid),
  FOREIGN KEY (bookid) REFERENCES book(bookid)
);
*/