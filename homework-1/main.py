"""Скрипт для заполнения данными таблиц в БД Postgres."""

"""
Подключение к Postgres из командной строки. Создание БД с названием `north`(копия из терминала).

dyadyasawa@dyadyasawa-MS-7A70:~$ sudo -i -u postgres 
[sudo] пароль для dyadyasawa:            
postgres@dyadyasawa-MS-7A70:~$ psql
psql (14.10 (Ubuntu 14.10-0ubuntu0.22.04.1))
Type "help" for help.

postgres=# \q
postgres@dyadyasawa-MS-7A70:~$ createdb north
postgres@dyadyasawa-MS-7A70:~$ psql
psql (14.10 (Ubuntu 14.10-0ubuntu0.22.04.1))
Type "help" for help.

postgres=# \l
                                  List of databases
   Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-----------+----------+----------+-------------+-------------+-----------------------
 north     | postgres | UTF8     | ru_UA.UTF-8 | ru_UA.UTF-8 | 
 postgres  | postgres | UTF8     | ru_UA.UTF-8 | ru_UA.UTF-8 | 
 template0 | postgres | UTF8     | ru_UA.UTF-8 | ru_UA.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 template1 | postgres | UTF8     | ru_UA.UTF-8 | ru_UA.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
(4 rows)

"""

import os
import psycopg2
from csv import DictReader

password = os.getenv('PASSWORD_FOR_DB') # Пароль для базы данных. Находится в переменной окружения.

conn = psycopg2.connect(host='localhost', database='north', user='postgres', password=password)
try:
    with conn:

        with conn.cursor() as curs:

            with open('employees_data.csv', newline='', encoding='utf-8') as f:
                reader = DictReader(f)
                for row in reader:
                    result_tuple = (int(row['employee_id']), row['first_name'], row['last_name'], row['title'], string_to_date(row['birth_date']), row['notes'])
                    curs.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', result_tuple)

            with open('customers_data.csv', newline='', encoding='utf-8') as f:
                reader = DictReader(f)
                for row in reader:
                    result_tuple = (row['customer_id'], row['company_name'], row['contact_name'])
                    curs.execute('INSERT INTO customers VALUES (%s, %s, %s)', result_tuple)

            with open('orders_data.csv', newline='', encoding='utf-8') as f:
                reader = DictReader(f)
                for row in reader:
                    result_tuple = (int(row['order_id']), row['customer_id'], int(row['employee_id']), string_to_date(row['order_date']), row['ship_city'])
                    curs.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', result_tuple)

finally:
    conn.close()
