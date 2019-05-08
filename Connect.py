import psycopg2
import DatabaseCommands`

from configparser import ConfigParser

def config(filename = 'database.ini', section='postgresql') :
	parser = ConfigParser()
	parser.read(filename)

	db = {}
	if parser.has_section(section) :
		params = parser.items(section)
		for param in params :
			db[param[0]] = param[1]
	else :
		raise Exception('Section {0} not found in the {1} file'.format(section, filename))

	return db

def connect() :
	conn = None
	try :
		params = config()

		print('Connecting to the PostgreSQL database...')
		conn = psycopg2.connect(**params)

		curr = conn.cursor()
		
		start.getData(curr)

		curr.close()
		conn.commit()

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally :
		if conn is not None :
			conn.close()
			print('Database connection closed')



if __name__ == '__main__' :
	connect()