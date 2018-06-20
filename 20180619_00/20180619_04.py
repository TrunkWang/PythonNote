#!/usr/bin/env python
# -*- coding:utf-8 -*-




import sqlite3


create = False
insert = False
select = True
update = False


if create:
	conn = sqlite3.connect('abc.db')
	c = conn.cursor()
	c.execute('''CREATE TABLE category (id int primary key,sort int ,name text)''')
	c.execute('''CREATE TABLE book (id int primary key,sort int,name tet,price real,category int,FOREIGN KEY (category) REFERENCES category(id))''')
	conn.commit()
	conn.close()




if insert:
	conn = sqlite3.connect('abc.db')
	c  = conn.cursor()

	books = [(1,1,'Cook Recipe',3.12,1),(2,3,'Python Intro',17.5,2),(3,2,'OS Intro',13.6,2),]

	c.execute("INSERT INTO category VALUES (1,1,'kitchen')")
	c.execute("INSERT INTO category VALUES (?,?,?)",(2,2,'computer'))
	c.executemany("INSERT INTO book VALUES (?,?,?,?,?)",books)

	conn.commit()
	conn.close()



if select:
	conn = sqlite3.connect('abc.db')
	c = conn.cursor()

	c.execute("SELECT name FROM category ORDER BY sort")
	print c.fetchone()
	print c.fetchone()

	c.execute("SELECT * FROM book WHERE book.category=1")
	print c.fetchall()

	for row in c.execute("SELECT name ,price FROM book ORDER BY sort"):
		print row


if update:
	conn = sqlite3.connect('abc.db')
	c = conn.cursor()

	c.execute("SELECT * FROM book")
	print c.fetchall()

	c.execute("UPDATE book SET price = ? WHERE id = ?",(1000,1))
	c.execute("DELETE FROM book WHERE id = 2")

	c.execute("SELECT * FROM book")
	print c.fetchall()

	conn.commit()
	conn.close()





