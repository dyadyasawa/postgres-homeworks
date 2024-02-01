-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	employee_id int PRIMARY KEY
	first_name varchar(100) NOTNULL
	last_name varchar(100) NOTNULL
	title varchar(100) NOTNULL
	birth_data date
	notes text
);

CREATE TABLE customers
(
	customer_id varchar(5) PRIMARY KEY
	company_name varchar(100) NOTNULL
	contact_name varchar(100) NOTNULL
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY
	customer_id varchar(5) NOTNULL
	employee_id int NOTNULL
	order_date date NOTNULL
	ship_city varchar(100) NOTNULL
);
