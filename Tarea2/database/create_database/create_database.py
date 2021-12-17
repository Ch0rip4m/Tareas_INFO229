import mysql.connector
import os, time

def create_database(db_connection,db_name,cursor):
	cursor.execute(f"CREATE DATABASE {db_name};")
	cursor.execute(f"COMMIT;")
	cursor.execute(f"USE {db_name};")
	
	# Tabla news
	cursor.execute('''CREATE TABLE news (
		id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
		title VARCHAR(50),
		date DATE, 
		url VARCHAR(50),
		media_outlet VARCHAR(50),
		category VARCHAR(50)
        );''')

	cursor.execute("SET GLOBAL time_zone = 'UTC';")
	cursor.execute("SET SESSION time_zone = 'UTC';")

	cursor.execute("COMMIT;") 

def insert_data(cursor):
    print("insert")
    cursor.execute('''INSERT INTO news (title,date,url,media_outlet,category) VALUES
    ('Gol Cr7','2021-01-01 ','www.deportes.com','Internet','sport'),
    ('Robo de banco','2021-01-15','www.crimenes.com','TV','delincuencia'),
    ('Gano Seleccion Chilena','2021-01-29','www.deportes.com','Diario','sport');''')
    cursor.execute("COMMIT;") 

#######################
DATABASE = "sun"

DATABASE_IP = str(os.environ['DATABASE_IP'])

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
    create_database(db_connection,DATABASE,cursor)
    insert_data(cursor)
    print(f"Succesfully created: {DATABASE}")
