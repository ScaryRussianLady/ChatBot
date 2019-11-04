# Use this script to manage the User_Datastore.json file

import json

# [CALLUM] This code allows the program to update the jason file with users previous responses and allows for multiple users 
def SaveData(Data, UserID, Location):

    count = 0
    
    with open("User_Datastore.json") as uds:
        UserData = json.load(uds)
    
    if IsNewID(UserData, UserID):
        UserData = CreateNewID(UserData, UserID)
    
    for entry in UserData['data']:  # This code check through the entrys of User Data to find the correct User ID entry
        if entry['UserID'] == UserID:
            if Location == "Name" or Location == "LastMessage" or Location ==  "LastFilmReply" or Location ==  "LastNewsReply" or Location == "LastBookReply": #these catagories can only take a single argument
                UserData['data'][count][Location] = Data # This replaces the entry with the updated user data
            else:
                UserData['data'][count][Location].append(Data) # This adds to a list to add to user data
        count += 1
    
    with open("User_Datastore.json", 'w') as uds: #writes updated data to json file
        json.dump(UserData, uds , indent= 3)

   

# [CHRISTIAN] Checks if UserID already exists in the datastore and returns false if it does and true if it doesn't
# [CALLUM] changed the loop to incorporate new method of checking through the file, old loop commented out below if neeeded
def IsNewID(jsonfile, userID):
    for entry in jsonfile["data"]:
        if userID == (entry["UserID"]):
            return False
    return True
    

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
    "PreviousViewedFilms": ["Example Film", "Another Example"], 
    "PreviousViewedBooks": ["Example Book", "Another Example"],
    "PreviousViewedArticles": ["Example Article", "Another Example"],})
    
    with open("User_Datastore.json", 'w') as uds:
        json.dump(UserData, uds , indent= 3)
    return UserData

# [CALLUM] Allows Data to be removed from single dictionaries and Lists in the json File
def RemoveData(DelWhole, ListPos, UserID, Location): 
    count = 0
    
    with open("User_Datastore.json") as uds:
        UserData = json.load(uds)

        for entry in UserData['data']: 
            if entry['UserID'] == UserID:
                if Location == "Name" or Location == "LastMessage" or Location ==  "LastFilmReply" or Location ==  "LastNewsReply" or Location == "LastBookReply": 
                    UserData['data'][count][Location] = "" 
                else:
                    del UserData['data'][count][Location][int(ListPos)]
                    # UserData['data'][count][Location].remove(Item) For use if we want to remove items by name instead of position in the list
            count += 1

        with open("User_Datastore.json", 'w') as uds:
            json.dump(UserData, uds , indent= 3)


# [CALLUM] Allows other scripts to retrive data from the json file
def RetrieveData(UserID, Location):
    count = 0

    with open("User_Datastore.json") as uds:
        UserData = json.load(uds)
    
    for entry in UserData['data']:
        if UserID == entry['UserID']:
            Data = UserData['data'][count][Location]
        count += 1
    return Data

# This tests the function in the terminal
SaveData("Bowser", "001", "Name")

Data = RetrieveData("001" ,"FavBookGenre" )
print(Data)

RemoveData(False, "0" , "001", "FavBookGenre" )