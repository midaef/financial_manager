
from ezprint import p
import os
import sqlite3


db_host = 'localhost'
db_username = 'root'
db_password = ''
db_db = 'hash'
db_charset = 'utf8'
db_table = 'users'
db_filename = '1.db'
base_dir = 'base'


def connect_db():
	global c
	try:
		connection = sqlite3.connect(db_filename)
		c = connection.cursor()
	except:
		print('Connect ERROR!\nCheck internet connection')
		exit()

	
def create_table():
	connect_db()
	c.execute('CREATE TABLE IF NOT EXISTS users ( login TEXT NOT NULL , password VARCHAR(32) NOT NULL )')
	c.execute('CREATE TABLE IF NOT EXISTS data ( id INT(11) NOT NULL AUTO_INCREMENT , login VARCHAR(64) NOT NULL , type INT(1) NOT NULL , date DATE NOT NULL , money INT(11) NOT NULL , PRIMARY KEY (id))')
	c.close()


def main():
	p('1. Login')
	p('2. Register')
	v = input('Input value: ')
	if v == '1':
		l1 = input('Input login: ')
		p1 = input('Input password: ')
	if v == '2':
		l = input('Input new login: ')
		p = input('Input new password: ')
		try:
			query = "INSERT INTO users (login, password) VALUES ('" + l + "', '" + p + "')"
			args = (password, hash)
			cursor.execute(query)
			cursor.close()
		except:
			cursor.close()


if __name__ == '__main__':
	create_table()
	main()