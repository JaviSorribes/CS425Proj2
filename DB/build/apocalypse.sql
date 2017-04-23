/* Javier Sorribes, 04/04/2017
	Clears the whole DB, dropping all tables
	BE CAREFUL!!!
*/
USE library;
DROP TABLE IF EXISTS  book_request;
/*DROP TABLE IF EXISTS  controls;*/
DROP TABLE IF EXISTS  takes;
DROP TABLE IF EXISTS  has;
DROP TABLE IF EXISTS  book;
DROP TABLE IF EXISTS  course;
DROP TABLE IF EXISTS  parent_contact;
DROP TABLE IF EXISTS  parent;
DROP TABLE IF EXISTS  student;
DROP TABLE IF EXISTS  teacher;
DROP TABLE IF EXISTS  admin;
DROP DATABASE library;