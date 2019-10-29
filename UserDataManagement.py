# Use this script to manage the User_Datastore.json file

import json

# [CALLUM] This code allows the program to update the jason file with users previous responses and allows for multiple users 
def SaveData(Data, UserID, Location):
    with open("User_Datastore.json") as uds:
        UserData = json.load(uds)
    catagories = ["LastMessage", "LastFilmReply" , "LastNewsReply","LastBookReply"] #List of items taht can only take a single argument
    count = 0
    if IsNewID(UserData, UserID):
        UserData = CreateNewID(UserData, UserID)
    

    for entry in UserData['data']:  # This code check through the entrys of User Data to find the correct User ID entry
        if entry['UserID'] == UserID:
            for Cat in catagories:
                if Location == Cat:
                    UserData['data'][count][Location] = Data # This replaces the entry with the updated user data
                else:
                    UserData['data'][count][Location].append(Data) # This adds to a list for the gneres to be saved
        count += 1
    with open("User_Datastore.json", 'w') as uds: #writes updated data to json file
        json.dump(UserData, uds , indent= 3)

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
    UserData['data'].append({ 'UserID' : UserID , 
    "Name": "Placeholder" , 
    "LastMessage": "Placeholder", 
    "LastFilmReply": "Example reply", 
    "LastNewsReply": "Example reply", 
    "LastBookReply": "Example reply",
    "FavFilmGenre": ["Example Genre", "Another Example"],
    "FavBookGenre": ["Example Genre", "Another Example"],
    "FavNewsTopic": ["Example Topic", "Another Example"],
    "Previous Viewed Films": ["Example Film", "Another Example"], 
    "Previous Viewed Books": ["Example Book", "Another Example"],
    "Previous Viewed Articles": ["Example Article", "Another Example"],})
    
    with open("User_Datastore.json", 'w') as uds:
        json.dump(UserData, uds , indent= 3)
    return UserData


# This tests the function in the terminal
SaveData("romance", "006", "FavBookGenre")