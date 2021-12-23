import mysql.connector
import os, time

def create_database(db_connection,db_name,cursor):
	cursor.execute(f"CREATE DATABASE {db_name};")
	cursor.execute(f"COMMIT;")
	cursor.execute(f"USE {db_name};")
	
	# Tabla jokes
	cursor.execute('''CREATE TABLE jokes (
		id_joke INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
		joke VARCHAR(200)
		);''')

	cursor.execute("SET GLOBAL time_zone = 'UTC';")
	cursor.execute("SET SESSION time_zone = 'UTC';")

	cursor.execute("COMMIT;") 

def insert_data(cursor):
    print("insert")
    cursor.execute('''INSERT INTO jokes (joke) VALUES
    ('¿Cuál es el último animal que subió al arca de Noé?... El del-fin.'),
    ('¿Cómo se dice pañuelo en japonés?... Saka-moko.'),
    ('¿Cómo se dice disparo en árabe?... Ahí-va-la-bala.'),
    ('¿Qué le dice un gusano a otro gusano?... Voy a dar una vuelta a la manzana.'),
    ('¿Cuál es el colmo de Aladdín?... Tener mal genio.'),
    ('Si se muere una pulga, ¿a dónde va?... Al pulgatorio'),
    ('¿Por qué las focas miran siempre hacia arriba?... ¡Porque ahí están los focos!'),
    ('Camarero, ese filete tiene muchos nervios. Pues normal, es la primera vez que se lo comen.'),
    ('¿Cómo se llama el primo de Bruce Lee?... Broco Lee.');''')
    cursor.execute("COMMIT;") 

#######################

def main():
	print("start creating database...")

	DATABASE = "joke_manager2"

	DATABASE_IP = str(os.environ['DATABASE_IP1'])

	DATABASE_USER = "root"
	DATABASE_USER_PASSWORD = "root"
	DATABASE_PORT=3306

	not_connected = True

	while(not_connected):
		try:
			print(DATABASE_IP,"IP")
			db_connection = mysql.connector.connect(user=DATABASE_USER,host=DATABASE_IP,port=DATABASE_PORT, password=DATABASE_USER_PASSWORD)
			not_connected = False

		except Exception as e:
			time.sleep(3)
			print(e, "error!!!")
			print("can't connect to mysql server, might be intializing")
			
	cursor = db_connection.cursor()

	try:
		cursor.execute(f"USE {DATABASE}")
		print(f"Database: {DATABASE} already exists")
	except Exception as e:
		print("creating database...")
		create_database(db_connection,DATABASE,cursor)
		insert_data(cursor)
		print(f"Succesfully created: {DATABASE}")
