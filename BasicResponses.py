from random import randrange
from UserDataManagement import RetrieveData

# [CALLUM] Function searches for keywords and provides a message
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

# [CHRISTIAN] Function searches keywords and provides a goodbye message if the user says a farewell keyword
def farewellReply(msgObj):
    ReplyList = [
    "See you soon, ",
    "Bye, ",
    "Until next time, "
    ]

    BasicFarewell = str((ReplyList[randrange(len(ReplyList))])+msgObj.username+"!")

    # This part is going to add additional text to the greetings to make the bot more personalised.

    EntList = ["the news article", "the film", "the book"]
    DataList = []

    EntRNG = EntList[randrange(len(EntList))]

    if EntRNG == "the news article":
        DataList = RetrieveData(msgObj.userID, "PreviousViewedArticles")
    elif EntRNG == "the film":
        DataList = RetrieveData(msgObj.userID, "PreviousViewedFilms")
    elif EntRNG == "the book":
        DataList = RetrieveData(msgObj.userID, "PreviousViewedBooks")

    Topic = DataList[randrange(len(DataList))]

    PhraseList_1 = [" Please do enjoy ", " I hope you enjoy ", " Have fun with "]

    SuggestiveFarewell = (PhraseList_1[randrange(len(PhraseList_1))])+EntRNG+" "+Topic

    return BasicFarewell+SuggestiveFarewell

# [CHRISTIAN] Function searches keywords and provides a greeting message if the user says a farewell keyword
def greetingReply(msgObj):
    ReplyList = [
    "Hello there, ",
    "Hi, ",
    "Hey, ",
    "Greetings, "
    ]

    BasicGreeting = str((ReplyList[randrange(len(ReplyList))])+msgObj.username+"!")

    # This part is going to add additional text to the greetings to make the bot more personalised.
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

        PhraseList_1 = [" Could I interesting you with any ", " Are you here to find any ", " Would you like to see any "]
        PhraseList_2 = ["? You seem to like it very much.", "? You appear to be enjoying them", "? I sense that you might."]

        SuggestiveGreeting = (PhraseList_1[randrange(len(PhraseList_1))])+Topic+" "+EntRNG+(PhraseList_2[randrange(len(PhraseList_2))])

        #print(SuggestiveGreeting)
    elif SuggestionRNG == 1:
        # Will suggest content
        EntList = ["the news article", "the film", "the book"]
        DataList = []

        EntRNG = EntList[randrange(len(EntList))]

        if EntRNG == "the news article":
            DataList = RetrieveData(msgObj.userID, "PreviousViewedArticles")
        elif EntRNG == "the film":
            DataList = RetrieveData(msgObj.userID, "PreviousViewedFilms")
        elif EntRNG == "the book":
            DataList = RetrieveData(msgObj.userID, "PreviousViewedBooks")

        Topic = DataList[randrange(len(DataList))]

        PhraseList_1 = [" I really hope you enjoyed ", " By the why, I hope you enjoyed ", " Back for more? You must have enjoyed "]

        SuggestiveGreeting = (PhraseList_1[randrange(len(PhraseList_1))])+EntRNG+" "+Topic


    return BasicGreeting+SuggestiveGreeting

# [CHRISTIAN] Function searches keywords and provides a appreciation message if the user says a farewell keyword
def appreciationReply(msgObj):
    ReplyList = [
    "No problem, ",
    "That's what I'm here for, ",
    "My pleasure, ",
    "You're very welcome, "
    ]

    return str((ReplyList[randrange(len(ReplyList))])+msgObj.username+"!")

