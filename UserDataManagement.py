# Use this script to manage the User_Datastore.json file

import json

# [CALLUM]
def SaveData(Data, UserID, Location):
    with open("User_Datastore.json") as uds:
        UserData = json.load(uds)
    
    if IsNewID(UserData, UserID):
        pass # Create a new object in the userdata array with this userID
    
    # For the rest of the code, write the data to the Location.
    # Location is the variable name that the data will be stored in.

    # Here will save the data to that specific ID

# [CHRISTIAN] Checks if UserID already exists in the datastore and returns false if it does and true if it doesn't
def IsNewID(jsonfile, userID):
    for i in range(len(jsonfile)):
        if str(userID) == jsonfile[i]["UserID"]:
            return False
    return True
