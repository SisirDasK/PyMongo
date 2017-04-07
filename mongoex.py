import pprint, sys
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

def displayAllUsers():
    usersCollection = db.users
    users = usersCollection.find()
    for user in users:
        print
        pprint.pprint( user )
        print

def displayUser( id ):
    usersCollection = db.users
    user = usersCollection.find_one({"_id": ObjectId(id)})
    print
    pprint.pprint( user )
    print

def addUser():
    name = raw_input( "Enter the user's name: " )
    age = raw_input( "Enter the user's age: " )
    height = raw_input( "Enter the user's height in meters: " )
    weight = raw_input( "Enter the user's weight in KGs: " )

    user = {    "Name": name,
                "Age": age,
                "Height": height,
                "Weight": weight
                }

    userId = db.users.insert_one(user).inserted_id

    print "\nUser successfully added with ID: " + str(userId) + "\n"

def updateUser( id ):

    while True:
        try:
            updateVal = int( raw_input( "Choose a field to update:\n1. Name\n2. Age\n3. Height\n4. Weight\n" ) )

            if updateVal == 1:
                name = raw_input ( "Enter the new value for name: " )
                result = db.users.update_one( {"_id": ObjectId(id)}, {"$set": {"Name": name}} )
                print "\n" + str( result.raw_result ) + "\n"
                break
            elif updateVal == 2:
                age = raw_input ( "Enter the new value for age: " )
                result = db.users.update_one( {"_id": ObjectId(id)}, {"$set": {"Age": age}} )
                print "\n" + str( result.raw_result ) + "\n"
                break
            elif updateVal == 3:
                height = raw_input ( "Enter the new value for height: " )
                result = db.users.update_one( {"_id": ObjectId(id)}, {"$set": {"Height": height}} )
                print "\n" + str( result.raw_result ) + "\n"
                break
            elif updateVal == 4:
                weight = raw_input ( "Enter the new value for weight: " )
                result = db.users.update_one( {"_id": ObjectId(id)}, {"$set": {"Weight": weight}} )
                print "\n" + str( result.raw_result ) + "\n"
                break
            else:
                print "\nInvalid choice. Please try again.\n"
        except ValueError:
            print "\nInvalid choice. Please try again.\n"
            
def deleteUser( id ):
    result = db.users.delete_one( {"_id": ObjectId(id)} )
    print "\n" + str( result.raw_result ) + "\n"



client = MongoClient()
db = client['sisDB']

while True:

    try:
        choice = int( raw_input( "Choose an operation (Eg - 3):\n1. Display all users\n2. Display a specific user by ID\n3. Add an user\n4. Update an user by ID\n5. Delete an user by ID\n6. Exit\n" ) )

        if choice == 1:
            displayAllUsers()

        elif choice == 2:
            displayUser( raw_input( "Enter the user's ID: " ) )

        elif choice == 3:
            addUser()

        elif choice == 4:
            updateUser( raw_input( "Enter the user's ID: " ) )

        elif choice == 5:
            deleteUser( raw_input( "Enter the user's ID: " ) )

        elif choice == 6:
            sys.exit()

        else:
            print "\nInvalid choice. Please try again.\n"

    except ValueError:
        print "\nInvalid choice. Please try again.\n"
