
from ezprint import p
import os
import sqlite3


db_filename = '1.db'

session = []
connection = ''
cursor = ''

def connect_db():
	global connection
	global cursor
	connection = sqlite3.connect('database.db')

	
def create_table():
	connect_db()
	cursor = connection.cursor()
	cursor.execute('CREATE TABLE IF NOT EXISTS users ( login TEXT NOT NULL , password VARCHAR(32) NOT NULL )')
	cursor.execute('CREATE TABLE IF NOT EXISTS data ( id INTEGER(11) PRIMARY KEY NOT NULL , login VARCHAR(64) NOT NULL , type INT(1) NOT NULL , date DATE NOT NULL , money INT(11) NOT NULL )')
	cursor.close()


def main():
	global session

	while True:
		if session == []:
			p('1. Login')
			p('2. Register')
			choose = input('Input value: ')
			if choose == '1':
				login = input('Input login: ')
				passwd = input('Input password: ')

				cursor = connection.cursor()

				query = "SELECT password FROM users WHERE login = " + '"' + login + '"'
				cursor.execute(query)
				data = cursor.fetchall()
				if data == []:
					p('Wrong login or password')
					return
				
				password = data[0][0]

				if passwd == password:
					session = [login, password]
					p('Login successful')
				else:
					p('Wrong login or password')

			if choose == '2':
				login = input('Input new login: ')
				passwd = input('Input new password: ')

				cursor = connection.cursor()

				query = "SELECT * FROM users WHERE login = " + '"' + login + '"'
				cursor.execute(query)
				data = cursor.fetchall()
				if data == []:
					query = "INSERT INTO users (login, password) VALUES ('" + login + "', '" + passwd + "')"
					cursor.execute(query)
					cursor.close()
					connection.commit()
				else:
					p('Login is busy')
					cursor.close()
			else:
				break
				# тут будут комадны


if __name__ == '__main__':
	create_table()
	main()




# перед действием с бд надо создать курсор      cursor = connection.cursor()
# если были изменения в бд надо сделать коммит  connection.commit()
# после действия закрыть                        cursor.close()