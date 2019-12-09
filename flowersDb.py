#import module
import sqlite3

#INSERT TASK
#define task
def create_task(conn, task):
	"""
    Create a new task
    :param conn:
    :param task:
    :return:
    """

	# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!SQL BINDINGS PLS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	sql_command='''INSERT INTO SIGHTINGS (SIGHTINGS.name. SIGHTINGS.person, 
				 SIGHTINGS.location, SIGHTINGS.sighted)
				 VALUES (?, ?, ?, ?); '''	
	cur = conn.crsr
	cur.execute(sql,task)
	return cur.lastrowid

	


def main():

	#connect to database
	connection = sqlite3.connect("flowers2019.db")

	#cursor
	crsr = connection.cursor()


	#################################### QUERY  #################################### 
	#SQL command to perform a query
	sql_command = """SELECT * 
	FROM SIGHTINGS 
	WHERE name = "Woodland star" 
	GROUP BY sighted 
	LIMIT 10;
	"""

	#execute the statement
	crsr.execute(sql_command)

	# store all the fetched data in the ans variable 
	ans= crsr.fetchall()  
	  
	# loop to print all the data 
	for i in ans: 
	    print(i) 

	#################################### INSERT ####################################




	#asks user for flower name
	insertName = input()

	#asks user for flower person
	insertPerson = input()

	#asks user for flower location
	insertLocation = input()

	#asks user for flower sighted
	insertSighted = input()

	#SQL command to perform an insert


	task = (insertName, insertPerson, insertLocation, insertSighted)

	# store all the fetched data in the ans variable 
	ans= task 
	  
	# loop to print all the data 
	for i in task:
	    print(i) 
	#execute the statement
	crsr.execute(sql_command,task)


	#################################### UPDATE  ####################################
	#SQL command to perform an update


	#execute the statement
	#crsr.execute(sql_command)


	connection.commit()

	connection.close()


if __name__ == '__main__':
	main()