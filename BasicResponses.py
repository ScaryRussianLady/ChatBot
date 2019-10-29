from random import randrange

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
    "See you soon!",
    "Bye, user!",
    "Until next time!"
    ]

    return ReplyList[randrange(len(ReplyList))]

# [CHRISTIAN] Function searches keywords and provides a greeting message if the user says a farewell keyword
def greetingReply(msgObj):
    ReplyList = [
    "Hello there!",
    "Hi!",
    "Hey!",
    "Greetings!"
    ]

    return ReplyList[randrange(len(ReplyList))]


# [CHRISTIAN] Function searches keywords and provides a appreciation message if the user says a farewell keyword
def appreciationReply(msgObj):
    ReplyList = [
    "No problem!",
    "That's what I'm here for!",
    "No... Thank you...",
    "You're very welcome!"
    ]

    return ReplyList[randrange(len(ReplyList))]

