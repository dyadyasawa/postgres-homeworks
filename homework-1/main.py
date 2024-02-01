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
