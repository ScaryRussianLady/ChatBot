#-------------------------------------------------------------IMPORTING MODULES-------------------------------------------------------------#
from random import randrange
from UserDataManagement import RetrieveData
#-------------------------------------------------------------------------------------------------------------------------------------------#

#-------------------------------------------------------------INTRODUCTION FUNCTION---------------------------------------------------------#

#[Beginning of Code by Callum Jones | ID No. 9406128 ]

def introduction(msgList, welcome):
    for i in range(len(msgList)):
        if msgList[i] == 'hey' or msgList[i] == 'hi' or msgList[i] == 'hello':
            print("Message received.")
            #botReply = "Hey there! I'm E-Bot, I am here to provide you with certain services. Would you like to know what I can do?"
            welcome = True

    if welcome == True:        
        for i in range(len(msgList)):
            if msgList[i] == 'yes':
                print("Message received.")
                #botReply = "Okay, cool! So, I can search films, books and news for you and give information on them, recommendations, ratings and anything else you want to know about them. Would you like to give it a go?"
            elif msgList[i] == 'no':
                print("Message received.")
                #botReply = "Well, that's a shame! If you change your mind just come and say hello to me again. Hope to see you soon! :)"

#[End of Code by Callum Jones | ID No. 9406128]

#-------------------------------------------------------------------------------------------------------------------------------------------#

#-------------------------------------------------------------GENERIC RESPONSE FUNCTIONS----------------------------------------------------#

#[Start of Code by Christian Shaw]

# Function searches keywords and provides a farewell message if the user says an farewell keyword
def farewellReply(msgObj):
    ReplyList = [
    "See you soon, ",
    "Bye, ",
    "Until next time, "
    ]

    BasicFarewell = str((ReplyList[randrange(len(ReplyList))])+msgObj.username+"!")

    # This part is going to add additional text to the greetings to make the bot more personalised.

    #EntList = ["the news article", "the film", "the book"]
    #DataList = []

    #EntRNG = EntList[randrange(len(EntList))]

    #if EntRNG == "the news article":
     #   DataList = RetrieveData(msgObj.userID, "PreviousViewedArticles")
    #elif EntRNG == "the film":
    #    DataList = RetrieveData(msgObj.userID, "PreviousViewedFilms")
    #elif EntRNG == "the book":
     #   DataList = RetrieveData(msgObj.userID, "PreviousViewedBooks")

    #Topic = DataList[(len(DataList)-1)]

    PhraseList_1 = [" Please do enjoy ", " I hope you enjoy ", " Have fun with "]

    #SuggestiveFarewell = (PhraseList_1[randrange(len(PhraseList_1))])+EntRNG+" "+Topic

    NewDataList = RetrieveData(msgObj.userID, "PreviousViewedEntertainment")

    SuggestiveFarewell = (PhraseList_1[randrange(len(PhraseList_1))]+NewDataList[len(NewDataList)-1]+"!")

    return BasicFarewell+SuggestiveFarewell

# Function searches keywords and provides a greeting message if the user says an greeting keyword
def greetingReply(msgObj):
    ReplyList = [
    "Hello there, ",
    "Hi, ",
    "Hey, ",
    "Greetings, "
    ]

    BasicGreeting = str((ReplyList[randrange(len(ReplyList))])+msgObj.username+"!")

    #This part is going to add additional text to the greetings to make the bot more personalised.
    SuggestionRNG = randrange(2)

    if SuggestionRNG == 0:
        # Will suggest topics
        EntList = ["news", "films", "books"]
        DataList = []

        EntRNG = EntList[randrange(len(EntList))]

        if EntRNG == "news":
            DataList = RetrieveData(msgObj.userID, "FavNewsTopic")
        elif EntRNG == "films":
            DataList = RetrieveData(msgObj.userID, "FavFilmGenre")
        elif EntRNG == "books":
            DataList = RetrieveData(msgObj.userID, "FavBookGenre")

        Topic = DataList[randrange(len(DataList))]

        PhraseList_1 = [" Could I interest you with any ", " Are you here to find any ", " Would you like to see any "]
        PhraseList_2 = ["? You seem to like it very much.", "? You appear to be enjoying them", "? I sense that you might."]

        SuggestiveGreeting = (PhraseList_1[randrange(len(PhraseList_1))])+Topic+" "+EntRNG+(PhraseList_2[randrange(len(PhraseList_2))])

    elif SuggestionRNG == 1:
        # Will suggest content
        EntList = ["the news article", "the film", "the book"]
        DataList = []

        EntRNG = EntList[randrange(len(EntList))]

        if EntRNG == "the news article about": #[Annija Balode, ID No: 9102828] just changed the string to make more sense when communicating with the user.
            DataList = RetrieveData(msgObj.userID, "PreviousViewedArticles")
        elif EntRNG == "the film":
            DataList = RetrieveData(msgObj.userID, "PreviousViewedFilms")
        elif EntRNG == "the book":
            DataList = RetrieveData(msgObj.userID, "PreviousViewedBooks")

        Topic = DataList[(len(DataList)-1)]

        PhraseList_1 = [" I really hope you enjoyed ", " By the way, I hope you enjoyed ", " Back for more? You must have enjoyed "]

        SuggestiveGreeting = (PhraseList_1[randrange(len(PhraseList_1))])+EntRNG+" "+Topic


    return BasicGreeting+SuggestiveGreeting

#Function searches keywords and provides a appreciation message if the user says an appeciation keyword
def appreciationReply(msgObj):
    ReplyList = [
    "No problem, ",
    "That's what I'm here for, ",
    "My pleasure, ",
    "You're very welcome, "
    ]

    return str((ReplyList[randrange(len(ReplyList))])+msgObj.username+"!")

#[End of Code by Christian Shaw]

#-------------------------------------------------------------------------------------------------------------------------------------------#