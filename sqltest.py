import sqlite3
from sqlite3.dbapi2 import connect

conn=sqlite3.connect('test.db')
cursor=conn.cursor()
#cursor.execute('create table user (id varchar(20) primary key,name varchar(20))')
#cursor.execute('insert into user(id,name) values (\'1\',\'Jim\')')
#cursor.rowcount
#cursor.close()
#conn.commit()
#conn.close


#conn=sqlite3.connect('test.db')
cursor.execute('select * from user where id=?',('1',))
value=cursor.fetchall()
print(value)
cursor.close()
conn.close()