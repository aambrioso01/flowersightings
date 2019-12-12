#from flask import Flask
#app = Flask(__name__)

import sqlite3

#
###################### EVERYTHING WORKS EXCEPT UPDATE GENUS AND SPECIES #############################
#
#
#

################################################ EXTRA CREDIT REQUIREMENTS ################################################


def updateSightingName(crs2,flowerName,personName,location,date):
	print("what is the new name?")
	newName = input()

	#update name
	sql_command = """update sightings set name=:newName where name=:flowerName"""

	#execute the statement
	crs2.execute(sql_command, {"newName":newName, "flowerName":flowerName})

	crs2.close()


username1 = "jimmy1996"
password1 = "mySecretPassword"

username2 = "susie1334"
password2 = "mySecretPassword"

def anywhereDelete(crs):
	print("What table would you like to modify?")
	tableName = input()

	if(tableName == "SIGHTINGS" or tableName == "sightings"):
		
		#asks user
		print("What is the name of sighting to delete?")
		oldName = input()

		#asks user
		print("the person?")
		oldPerson = input()

		#asks user
		print("the location?")
		oldLocation = input()

		#asks user
		print("the sighting? (YYYY-DD-MM)")
		oldDate = input()

		crs.execute("""delete from sightings where name=:oldName and person=:oldPerson and location=:oldLocation and sighted=:oldDate""", {"oldName":oldName, "oldPerson":oldPerson,"oldLocation":oldLocation, "oldDate":oldDate})
		return

	if(tableName == "FEATURES" or tableName == "features"):
		#asks user
		print("Input latitude of feature you want to delete")
		oldLatitude = input()

		#asks user
		print("Input longitude")
		oldLongitude = input()

		crs.execute("""delete from features where latitude=:oldLatitude and longitude=:oldLongitude""", {"oldLatitude":oldLatitude, "oldLongitude":oldLongitude})

		return

	if(tableName == "FLOWERS" or tableName == "flowers"):

		print("which flower do you want to delete? provide comname")
		ogName = input()

		crs.execute("""delete from flowers where comname=:ogName""", {"ogName":ogName})
		return

def anywhereUpdate(crs):
	print("What table would you like to modify?")
	tableName = input()

	if(tableName == "SIGHTINGS" or tableName == "sightings"):
		print("What is the name to update?")
		oldName = input()

		print("Who is the person?")
		oldPerson = input()

		print("What is the location?")
		oldLocation = input()

		print("When was the sighting? (YYYY-DD-MM)")
		oldDate = input()

		print("What do you want to modify?")
		updateChoice = input()

		print("what is the new value?")
		new = input()

		#sort users choice to modify
		if (updateChoice == 'name'):
			#execute the statement
			crs.execute("""update sightings set name=:new where name=:oldName""", {"new":new, "oldName":oldName})

		if (updateChoice == 'person'):
			crs.execute("""update sightings set person=:new where person=:oldPerson""", {"new":new, "oldPerson":oldPerson})

		if (updateChoice == 'location'):
			crs.execute("""update sightings set location=:new where location=:oldLocation""", {"new":new, "oldLocation":oldLocation})

###########################FIXXXXX
		if (updateChoice == 'sighted'):
			crs.execute("""update sightings set sighted=:new where date=:oldDate""", {"new":new, "oldDate":oldDate})

		return
		
	if(tableName == "FEATURES" or tableName == "features"):
		
		print("Input latitude of feature you want to modify")
		#asks user
		oldLatitude = input()
		print("Input longitude of feature you want to modify")
		#asks user
		oldLongitude = input()

		#asks user
		print("What do you want to modify?")
		updateChoice = input()

		print("what is the new value?")
		new = input()

		#sort users choice to modify
		if (updateChoice == 'location'):
			#execute the statement
			crs.execute("""update features set location=:new where latitude=:oldLatitude and longitude=:oldLongitude""", {"new":new, "oldLatitude":oldLatitude, "oldLongitude":oldLongitude})

		if (updateChoice == 'class'):
			crs.execute("""update features set class=:new where latitude=:oldLatitude and longitude=:oldLongitude""", {"new":new, "oldLatitude":oldLatitude, "oldLongitude":oldLongitude})

		if (updateChoice == 'latitude'):
			crs.execute("""update features set latitude=:new where latitude=:oldLatitude and longitude=:oldLongitude""", {"new":new, "oldLatitude":oldLatitude, "oldLongitude":oldLongitude})

		if (updateChoice == 'longitude'):
			crs.execute("""update features set longitude=:new where latitude=:oldLatitude and longitude=:oldLongitude""", {"new":new, "oldLatitude":oldLatitude, "oldLongitude":oldLongitude})

		if (updateChoice == 'map'):
			crs.execute("""update features set map=:new where latitude=:oldLatitude and longitude=:oldLongitude""", {"new":new, "oldLatitude":oldLatitude, "oldLongitude":oldLongitude})

		if (updateChoice == 'elev'):
			crs.execute("""update features set elev=:new where latitude=:oldLatitude and longitude=:oldLongitude""", {"new":new, "oldLatitude":oldLatitude, "oldLongitude":oldLongitude})
		return

	if(tableName == "FLOWERS" or tableName == "flowers"):
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
		return

def anywhereCreate(crs):
	print("What table would you like to modify?")
	tableName = input()

	if(tableName == "SIGHTINGS" or tableName == "sightings"):
		#asks user for flower name
		sightingsName = input()
		#asks user for flower person
		sightingsPerson = input()
		#asks user for flower location
		sigthingsLocation = input()
		#asks user for flower sighted
		sightingsSighted = input()
		#execute the statement
		crs.execute("INSERT INTO {SIGHTINGS VALUES (?, ?, ?, ?)", (sightingsName, sightingsPerson, sightingsLocation, sightingsSighted))
	if(tableName == "FEATURES" or tableName == "features"):
		#asks user for location
		featuresLocation = input()
		#asks user for class
		featuresClass = input()
		#asks user
		featuresLatitude = input()
		#asks user
		featuresLongitude = input()
		#asks user
		featuresMap = input()
		#asks user
		featuresElev = input()
		#execute the statement
		crs.execute("INSERT INTO FEATURES VALUES (?, ?, ?, ?, ?, ?)", (featuresLocation, featuresClass, featuresLatitude, featuresLongitude, featuresMap, featuresElev))
	if(tableName == "FLOWERS" or tableName == "flowers"):
		#asks user
		flowersGenus = input()
		#asks user
		flowersSpecies = input()
		#asks user
		flowersComname = input()
		#execute the statement
		crs.execute("INSERT INTO FLOWERS VALUES (?, ?, ?)", (flowersGenus, flowersSpecies, flowersComname))


################################################ MAIN PROJECT REQUIREMENTS ################################################
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

#################################### QUERY  ####################################
def flowerQuery(crs):
	
	#asks user
	print("What flower would you like to query?")

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

#################################### INSERT ####################################
def flowerInsert(crs):
	
	
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

#################################### UPDATE  ####################################
def flowerUpdate(crs):
	
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

# 	crs.close()


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

#@app.route('/')
def main():

	

	#################################  LOGIN CODE COMMENTED OUT FOR EASE OF TESTING #################################
	#user not logged in yet
	#loggedIn = 0

	# #take username and password
	# print("Hello! Welcome to the Database. Enter username to begin login process")
	# usernameInput = input()

	# print("Enter password")
	# passwordInput = input()

	# #check for first user
	# if usernameInput == username1 and passwordInput == password1:
	# 	loggedIn = 1
	# 	print("Welcome jimmy1996!\n")

	# #check for second user
	# if usernameInput == username1 and passwordInput == password2:
	# 	loggedIn = 1
	# 	print("Welcome jimmy1996!\n")

	# if loggedIn == 0:
	# 	print("User credentials not found. Exiting program...")
	# 	return 

	############################# LOGGED IN #############################

	#connect to database
	connection = sqlite3.connect("flowers2019.db")

	#cursor
	crsr = connection.cursor()

	#prints user options
	print("Which option would you like?\n\nMAIN FUNCTIONS:\n\n1. query 10 most recent sightings of a flower\n2. update flower information\n3. insert new sighting of a flower\n\nEXTRA CREDIT FUNCTIONS:\n\n4. create entry in a table\n5. update entry in a table\n6. delete entry in a table")
	
	userFunction = input()

	if(userFunction == '1'):
		flowerQuery(crsr)

	if(userFunction == '2'):
		flowerUpdate(crsr)	

	if(userFunction == '3'):
		flowerInsert(crsr)

	if(userFunction == '4'):
		anywhereCreate(crsr)

	if(userFunction == '5'):
		anywhereUpdate(crsr)

	if(userFunction == '6'):
		anywhereDelete(crsr)
	
	print("\nend of program...\n")
	#commit and close
	crsr.close()
	connection.commit()
	connection.close()


if __name__ == '__main__':
	main()