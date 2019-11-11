# This file is just for testing and for example purposes

from UserDataManagement import SaveData

def mainDialogue(obj):
    SaveData("0001_0002", obj.userID, "ReplyID")
    return "This is the main dialogue"

def Reply1(obj):
    SaveData("0001_0003", obj.userID, "ReplyID")
    return ("This is the first reply")

def Reply2(obj):
    return ("This is the second reply")

def Reply3(obj):
    return ("This is the third reply")

def FindID(obj, ID):
    if ID == "0002":
        return Reply1(obj)
    if ID == "0003":
        return Reply2(obj)