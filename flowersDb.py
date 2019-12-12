from flask import Flask
app = Flask(__name__)

import sqlite3

#
###################### EVERYTHING WORKS EXCEPT UPDATE GENUS AND SPECIES #############################
#
#
#


username1 = jimmy1996
password1 = mySecretPasscode

username1 = susie1334
password1 = mySecretPasscode2


def updateGenus(crs2,ogName):
	print("what is the new genus?")
	newName = input()

	#update name
	sql_command = """update flowers set genus=:newName where comname=:ogName"""

	#execute the statement
	crs2.execute(sql_command, {"newName":newName, "ogName":ogName})

	crs2.close()

def updateSpecies(crs2,ogName):
	print("what is the new species?")
	newName = input()

	#update name
	sql_command = """update flowers set species=:newName where comname=:ogName"""

	#execute the statement
	crs2.execute(sql_command, {"newName":newName, "ogName":ogName})

	crs2.close()

def updateComname(crs2,ogName):
	print("what is the new name?")
	newName = input()

	#update name
	sql_command = """update flowers set comname=:newName where comname=:ogName"""

	#execute the statement
	crs2.execute(sql_command, {"newName":newName, "ogName":ogName})

	crs2.close()

def flowerQuery(crs):
	#################################### QUERY  ####################################

	#user selects flower
	flowerChoice = input()

	#SQL command to perform a query
	sql_command = """SELECT person,location,sighted 
	FROM SIGHTINGS 
	WHERE name =:flowerChoice 
	GROUP BY sighted 
	LIMIT 10;
	"""

	#execute the statement
	crs.execute(sql_command, {"flowerChoice":flowerChoice})

	# store query results
	ans= crs.fetchall()  
	  
	# print 10 most recent sightings of selected flower 
	for i in ans: 
	    print(i) 

	crs.close()

def flowerInsert(crs):
	#################################### INSERT ####################################
	
	#asks user for flower name
	insertName = input()

	#asks user for flower person
	insertPerson = input()

	#asks user for flower location
	insertLocation = input()

	#asks user for flower sighted
	insertSighted = input()

	#execute the statement
	crs.execute("INSERT INTO SIGHTINGS VALUES (?, ?, ?, ?)", (insertName, insertPerson, insertLocation, insertSighted))

	crs.close()

def flowerUpdate(crs):
	#################################### UPDATE  ####################################

	print("which flower do you want to update? provide comname")
	ogName = input()

	print("do you want to modify genus, species, or comname?")
	updateChoice = input()

	#perform query on flowers
	if updateChoice == 'genus':
		updateGenus(crs,ogName)

	#perform insert on flowers
	if updateChoice == 'species':
		updateSpecies(crs,ogName)

	#perform update on flowers
	if updateChoice == 'comname':
		updateComname(crs,ogName)	

	crs.close()


def printFlowers(crs):
	#SQL command to query all flowers
	sql_command = """SELECT comname FROM FLOWERS"""

	#execute the statement
	crs.execute(sql_command)

	# store list of all flowers
	ans= crs.fetchall()  

	# print all flowers 
	for i in ans: 
	    print(i)

@app.route('/')
def main():

	print(Hello! Welcome to the Database. Enter username to begin login process")

	#connect to database
	connection = sqlite3.connect("flowers2019.db")

	#cursor
	crsr = connection.cursor()

	#print flowers
	printFlowers(crsr)

	print("Would you like to query, update, or insert?")

	userChoice = input()

	#perform query on flowers
	if userChoice == 'query':
		flowerQuery(crsr)

	#perform insert on flowers
	if userChoice == 'insert':
		flowerInsert(crsr)

	#perform update on flowers
	if userChoice == 'update':
		flowerUpdate(crsr)	
	
	print("hello")
	#commit and close
	crsr.close()
	connection.commit()
	connection.close()


if __name__ == '__main__':
	main()