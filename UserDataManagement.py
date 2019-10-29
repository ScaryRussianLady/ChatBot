# Use this script to manage the User_Datastore.json file

import json

# [CALLUM] 
def SaveData(Data, UserID, Location):
    with open("User_Datastore.json") as uds:
        UserData = json.load(uds)
    #print(UserData)
    
    if IsNewID(UserData, UserID):
        UserData = CreateNewID(UserData, UserID)
    

    for entry in UserData['data']['UserID']:
        if entry['Location'] == Location:
            entry['Location'].remove()
            entry['Location'].insert(Data)
            
    

    # Here will save the data to that specific ID

# [CHRISTIAN] Checks if UserID already exists in the datastore and returns false if it does and true if it doesn't
# [CALLUM] changed the loop to incorporate new method of checking through the file, old loop commented out below if neeeded
def IsNewID(jsonfile, userID):
    for entry in jsonfile["data"]:
        if userID == (entry["UserID"]):
            return False
    return True
    
     #for i in range(len(jsonfile)):
        #if str(userID) == jsonfile[i]["UserID"]:
            #return False
    #return True

# [CALLUM] creates a new entry in the json file with that user id and then returns the updated user data to have the data saved
def CreateNewID(UserData, UserID):
    UserData['data'].append({ 'UserID' : UserID , "Name": "Placeholder" , "LastMessage": "Placeholder", "LastFilmReply": "Example reply", "LastNewsReply": "Example reply", "LastBookReply": "Example reply","FavFilmGenre": ["Example Genre", "Another Example"],"FavBookGenre": ["Example Genre", "Another Example"],"FavNewsTopic": ["Example Topic", "Another Example"]})
    with open("User_Datastore.json", 'w') as uds:
        json.dump(UserData, uds , indent= 3)
    return UserData


# This tests the function in the terminal
SaveData("pop", "003", "LastMessage")