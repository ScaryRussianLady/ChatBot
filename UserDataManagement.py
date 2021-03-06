# Use this script to manage the User_Datastore.json file

import json

# [Callum Jones , ID No. 9406128 ] This code allows the program to update the jason file with users previous responses and allows for multiple users 
def SaveData(Data, UserID, Location):

    count = 0
    
    with open("User_Datastore.json") as uds: #opens json file for reading only and saves all data into a dictionary
        UserData = json.load(uds)
    
    if IsNewID(UserData, UserID):
        UserData = CreateNewID(UserData, UserID)
    
    count = FidnEntry(UserData , UserID) #Find Entry is used to find the data specific to specified user
    
    if Location == "UserID" or Location == "Name" or Location == "ReplyID" or Location == "LastMessage" or Location ==  "LastFilmReply" or Location ==  "LastNewsReply" or Location == "LastBookReply": #these catagories can only take a single argument
        UserData['data'][count][Location] = Data # This replaces the entry with the updated user data
    else:
        UserData['data'][count][Location].append(Data) # This adds to a list to add to user data
        
    
    with open("User_Datastore.json", 'w') as uds: #opens json file to be written too with updated data
        json.dump(UserData, uds , indent= 3) # saves the updated data with an indent of 3 so file is organised and can be read by a user if needed

   

# [Callum Jones , ID No. 9406128 ] checks through the file to check if new id is needed
def IsNewID(jsonfile, userID):
    for entry in jsonfile["data"]:
        if userID == (entry["UserID"]):
            return False
    return True
    

# [Callum Jones , ID No. 9406128 ] creates a new entry in the json file with that user id and then returns the updated user data to have the data saved
def CreateNewID(UserData, UserID):
    UserData['data'].append({ 'UserID' : int(UserID) , 
    "Name": "Placeholder" , 
    "LastMessage": "Placeholder", 
    "ReplyID" : "XXXX_XXXX", # Addition [Christian Shaw | ID No. 9262834]
    #[Annija Balode ID No: 9102828] removed the example data as this was getting brought up when the bot was running, made them empty so data can be stored into them.
    "LastFilmReply":"", 
    "LastNewsReply":"", 
    "LastBookReply":"",
    "FavFilmGenre": [],
    "FavBookGenre": [],
    "FavNewsTopic": [],
    "PreviousViewedEntertainment": [],
    "PreviousViewedFilms": [], 
    "PreviousViewedBooks": [],
    "PreviousViewedArticles": []}) 
    #[Annija Balode ID No: 9102828] end of wiping example data on this function.
    
    
    with open("User_Datastore.json", 'w') as uds:
        json.dump(UserData, uds , indent= 3)
    return UserData

# [Callum Jones , ID No. 9406128 ] Allows Data to be removed from single dictionaries and Lists in the json File
def RemoveData(DelWhole, ListPos, UserID, Location): 
    count = 0
    
    with open("User_Datastore.json") as uds:
        UserData = json.load(uds)

        count = FidnEntry(UserData , UserID)

        if Location == "Name" or Location == "LastMessage" or Location ==  "LastFilmReply" or Location ==  "LastNewsReply" or Location == "LastBookReply": 
            UserData['data'][count][Location] = "" 
        else:
            try:
                del UserData['data'][count][Location][int(ListPos)]
            except:
                return
            # UserData['data'][count][Location].remove(Item) For use if we want to remove items by name instead of position in the list
            

        with open("User_Datastore.json", 'w') as uds:
            json.dump(UserData, uds , indent= 3)
#End of [Callum Jones, ID No. 9406128]

# [Callum Jones , ID No. 9406128 ] Allows other scripts to retrive data from the json file
def RetrieveData(UserID, Location):
    count = 0
    DataStr = ""
    DataLst = []

    #[Annija Balode, ID No: 9102828] Addition below, slightly adjusted the reading of the JSON file, more efficient and less likely to throw an error.
    with open("User_Datastore.json") as uds:
        content = uds.read()
        UserData = json.loads(content)
       # UserData = json.load(uds)
    #[Annija Balode, ID No: 9102828] End of addition.
    count = FidnEntry(UserData , UserID)

    if Location == "Name" or Location == "LastMessage" or Location ==  "LastFilmReply" or Location ==  "LastNewsReply" or Location == "LastBookReply":
        DataStr = UserData['data'][count][Location]
        return DataStr
    else:
        DataLst = UserData['data'][count][Location]
        return DataLst
       
    
# [Callum Jones , ID No. 9406128 ] searches through UserData to find the entry the user or program has requested
def FidnEntry(UserData , UserID): 
    count = 0
    for entry in UserData['data']:  #spilts the individual entrys in the dictionary up
        if entry['UserID'] == int(UserID): # if the userID mathces the cuurent users ID then it returns the position of their data in list of entrys in the dictionary
            return count 
        count += 1

# This tests the function in the terminal


SaveData("Fred", 1, "Name")

Data = RetrieveData(1 ,"FavBookGenre" )
print(Data)

RemoveData(False, "0" , 1, "FavBookGenre" )