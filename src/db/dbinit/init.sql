CREATE DATABASE multicontainer_todoapp;
USE multicontainer_todoapp;

CREATE TABLE todo (
  id INT NOT NULL AUTO_INCREMENT,
  todoItem VARCHAR(200) NOT NULL DEFAULT 'NA',
  PRIMARY KEY (`id`)
);