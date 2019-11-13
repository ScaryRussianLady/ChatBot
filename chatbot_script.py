#-------------------------------------------------------------IMPORTING MODULES-------------------------------------------------------------#
import discord
import random
from discord.ext import commands
from googletrans import Translator
import json
import asyncio

#-----------------------------------------------------------------------------------------------------------------------------------------------#

#-------------------------------------------------------------ESTABLISHING THE BOT-------------------------------------------------------------#

#[Start of Code by Christian Shaw]

#[Code in this block is adapted from the discord.py documentation: 
# https://discordpy.readthedocs.io/en/latest/quickstart.html#a-minimal-bot]

# Assigns the variable client to the bot and sets the command's prefix to "-"
client = commands.Bot(command_prefix = "-")

# When the bot has connected to discord a message will be printed to the terminal
@client.event
async def on_ready():
    print("\nThe E-Bot is online!")
    # For terminal use only. Creates space between information on the terminal to make it easier to read.
    print("\n--------------------------------------------------------------------------")

#[End of Code by Christian Shaw]

#-----------------------------------------------------------------------------------------------------------------------------------------------#

#-------------------------------------------------------------BOT COMMAND ASYNC FUNCTION--------------------------------------------------------#
#[Start of Code by Christian Shaw]

# This is the MAIN function for the chatbot | com = the command (bot), msg = the user input after the command is called
# E.G The user typing "-bot My name is Bill" will make msg = "My name is Bill"
@client.command()
async def bot(com, *, msg):

    # [Start of Code by Christian Shaw] Calls the function that creates the message object
    msgObj = createMsgObj(msg, com.author.id, str(com.author), com.channel)
    print("User's message            >>", msgObj.msg)
    print("User's message as list    >>", msgObj.list)
    print("User's message's language >>", msgObj.lang)
    print("User's ID                 >>", msgObj.userID)
    print("User's name               >>", msgObj.username)
    print("User's channel            >>", msgObj.channel)

    # Saves the userID and message data to the user_datastore.json file
    from UserDataManagement import SaveData
    SaveData(msgObj.userID, msgObj.userID, "UserID")
    SaveData(str(msgObj.username), msgObj.userID, "Name")
    SaveData(msgObj.msg, msgObj.userID, "LastMessage")
    
    # Calls the function which calls for other scripts to generate replies and returns it as a list
    botReply = generateReplies(msgObj) 
   
    # Send's the replies on discord in the order of the botReply list.
    if len(botReply) != 0:
        for i in botReply:
            # Uses the translateText function I created to translate the bot's reply back into the user's language
            Reply = translateText(i, msgObj.lang)
            await com.send(Reply)
    else:
        # If there weren't any replies found to send, it will reply with this:
        Reply = "Could you try rephrasing what you said? I promise I am doing my best to understand you!"
        # Uses the translateText function I created to translate the bot's reply back into the user's language
        Reply = translateText(Reply, msgObj.lang)
        await com.send(Reply)
    
    #For terminal use only. Creates space between information on the terminal to make it easier to read.
    print("\n--------------------------------------------------------------------------")

#[End of Code by Christian Shaw]

#-----------------------------------------------------------------------------------------------------------------------------------------------#

#-------------------------------------------------------------BOT REPLY COMMAND ASYNC FUNCTION--------------------------------------------------#

# [Start of Code by Christian Shaw] 

# This async function will handle all of the replies
# Instead of the command -bot, for replies the user most type -r
@client.command()
async def r(com, *, reply):

    msgObj = createMsgObj(reply, com.author.id, str(com.author), com.channel)
    print("User's reply            >>", msgObj.msg)
    print("User's reply as list    >>", msgObj.list)
    print("User's reply's language >>", msgObj.lang)
    print("User's ID               >>", msgObj.userID)
    print("User's name             >>", msgObj.username)
    print("User's channel          >>", msgObj.channel)

    # Saves the userID and message data to the user_datastore.json file
    from UserDataManagement import SaveData
    SaveData(msgObj.userID, msgObj.userID, "UserID")
    SaveData(str(msgObj.username), msgObj.userID, "Name")
    SaveData(msgObj.msg, msgObj.userID, "LastMessage")

    from UserDataManagement import RetrieveData
    ReplyID = RetrieveData(msgObj.userID, "ReplyID")

    Global_ID = ""
    for char in range(len(ReplyID)):
        if ReplyID[char] == "_":
            #ReplyID = Global_ID
            break
        Global_ID = Global_ID+ReplyID[char]

    Local_ID = ""
    check = False
    for char in range(len(ReplyID)):
        if check == True:
            Local_ID = Local_ID+ReplyID[char]

        if ReplyID[char] == "_":
            #ReplyID = Local_ID
            check = True
        
    # This will be the variable that the reply is stored into (must remain empty)
    BotReply = ""
    
    # This part of the code will use the ReplyID to find the correct scripts to use
    TestScriptGlobal_ID = "0001"
    NewsScriptGlobal_ID = "1423"
    FilmScriptGlobal_ID = "6912"
    BookScriptGlobal_ID = "2151"

    # This is for the test script
    if Global_ID == TestScriptGlobal_ID:
        from Temp_testReply import FindID
        BotReply = FindID(msgObj, Local_ID)

    # This is for the news script
    if Global_ID == NewsScriptGlobal_ID:
        from NewsAPI import FindID
        BotReply = FindID(msgObj, Local_ID)

    # This is for the film script
    if Global_ID == FilmScriptGlobal_ID:
        from TMDBAPI_DiscordPrototype import FindID
        BotReply = FindID(msgObj, Local_ID)

    # This is for the book script
    if Global_ID == BookScriptGlobal_ID:
        pass

    # Next part is going to retrieve and check the "replyID" and go to the required script & function
    if BotReply == None or BotReply == "":
        BotReply = translateText("Sorry, I didn't quite understand that reply", msgObj.lang)
        await com.send(BotReply)
    else:
        BotReply = translateText(BotReply, msgObj.lang)
        await com.send(BotReply)

    #For terminal use only. Creates space between information on the terminal to make it easier to read.
    print("\n--------------------------------------------------------------------------")

# [End of Code by Christian Shaw] 

#-----------------------------------------------------------------------------------------------------------------------------------------------#

#-------------------------------------------------------------BOT TRANSLATION FUNCTIONS---------------------------------------------------------#

# [Start of Code by Christian Shaw] 

# This will translate the languages of strings using the googletrans API and returns it
# The parameters: text = the string to be translated, lang = the language the string will be translated to
def translateText(text, lang):
    translator = Translator()
    translatedMessage = translator.translate(text, dest=lang)
    return translatedMessage.text

# This will find (detect) the language a string is in usings the googletrans API and returns the language
# The parameter: text = the string that we want to detect the language of
def detectLanguage(text):
    translator = Translator()
    language = translator.detect(text)
    return language.lang

# [End of Code by Christian Shaw] 

#-----------------------------------------------------------------------------------------------------------------------------------------------#

#-------------------------------------------------------------MESSAGE OBJECTS AND FUNCTIONS-----------------------------------------------------#

# [Start of Code by Christian Shaw] 

# This creates an object to store the message properties AND a function to create the object and give it the properties it needs
class messageObj():
    msgCount = 0
    def __init__(self, msg, msgList, msgLang, msgUserID, msgUsr, msgChannel):
        self.msg = msg
        self.list = msgList
        self.lang = msgLang
        self.userID = msgUserID
        self.username = msgUsr
        self.channel = msgChannel
        messageObj.msgCount += 1

# This is a function that will convert the raw data input into something we want the object to take
def createMsgObj(msg, authorID, usr, channel):
    
    # This part of the script translates the raw user input into English so that the bot can interpret it better
    # Also, languages such as Korean, Japanese and Chinese don't have spaces between their characters, so finding individual words wouldn't work
    msgLanguage = detectLanguage(msg)
    if msgLanguage != 'en':
        msg = translateText(msg, "en")
    msgList = msg.split()

    # This part of the code is going to remove the hashtags and ID from the username that discord uses to identify users
    # Monster#1334 will become Monster. The hashtags makes the bot seem more robotic and we don't want that
    NewUsr = ""
    for char in range(len(usr)):
        if usr[char] == "#":
            usr = NewUsr
            break
        
        NewUsr = NewUsr+usr[char]

    msg_obj = messageObj(msg, msgList, msgLanguage, authorID, usr, channel)
    return msg_obj

# [End of Code by Christian Shaw] 

#-----------------------------------------------------------------------------------------------------------------------------------------------#

#-------------------------------------------------------------REPLY GENERATION ALGORITHM--------------------------------------------------------#

# [Start of Code by Christian Shaw] 
# Please note: The scripts imported in the algorithm when a keyword is identified may not be ones that I have written

# This algorthim will search for specific keywords from a list to determine what scripts will be used for replies
def generateReplies(msgObj):

    # Takes the list of words from the user input and assigns it to msgList
    msgList = msgObj.list

    # A list of keywords that will trigger a response for the bot
    greetingKeywords = ["hi", "hello", "good", "greetings", "hey"]
    appreciationKeywords = ["thank", "thanks"]
    filmKeywords = ["movie", "film", "series"]
    newsKeywords = ["news", "article", "weather", "articles", "headlines", "headline"]
    bookKeywords = ["book", "story"]
    farewellKeywords = ["bye", "goodbye", "farewell"]

    # An empty list which will have the bot's replies be appended into it as the relevant scripts as executed
    # This is so that when the bot sends these messages back, it's in order and appears more fluid
    Replies = []

    #from Temp_testReply import mainDialogue
    #Replies.append(mainDialogue(msgObj))

    # This for loop will scan the entire list of words and identify any keywords
    for i in range(len(msgList)):

        # This will identify greeting words in the list
        for j in range(len(greetingKeywords)):
            if msgList[i].lower() == greetingKeywords[j]:
                
                if greetingKeywords[j] != "good":
                    from BasicResponses import greetingReply
                    Replies.append(greetingReply(msgObj))
                    break
                else:

                    # In this special case of good morning, evening and afternoon, this will only identify is as a keyword is followed
                    # by morning, evening or afternoon
                    if len(msgList) != 1:
                        try:
                            if msgList[i+1].lower() == "morning" or msgList[i+1].lower() == "evening" or msgList[i+1].lower() == "afternoon":
                                from BasicResponses import greetingReply
                                Replies.append(greetingReply(msgObj))
                                break
                        except:
                            pass
        
        # This will identify appreciation words in the list
        for j in range(len(appreciationKeywords)):
            if msgList[i].lower() == appreciationKeywords[j]:
                from BasicResponses import appreciationReply
                Replies.append(appreciationReply(msgObj))
                break
        
        # This will identify film related words in the list
        for j in range(len(filmKeywords)):
            if msgList[i].lower() == filmKeywords[j] or msgList[i].lower() == (filmKeywords[j]+"s"):
                # Call for film function inside of the placeholder
                from TMDBAPI_DiscordPrototype import firstUserInt
                Replies.append(firstUserInt(msgObj))
                #Replies.append("Placeholder Film Info")
                break
        
        # This will identify news related words in the list
        #Annija
        for j in range(len(newsKeywords)):
            if msgList[i].lower() == newsKeywords[j] or msgList[i].lower() == (newsKeywords[j]+"s"):
                from NewsAPI import IntroductionToUser
                Replies.append(IntroductionToUser(msgObj))
                break

        # This will identify book related words in the list
        for j in range(len(bookKeywords)):
            if msgList[i].lower() == bookKeywords[j] or msgList[i].lower() == (bookKeywords[j]+"s"):
                # Call for book function inside of the placeholder
                from GoodreadsAPI import UserIntro
                #Replies.append("Placeholder Book Info")
                break
        
        # This will identify farewell words in the list
        for j in range(len(farewellKeywords)):
            if msgList[i].lower() == farewellKeywords[j]:
                from BasicResponses import farewellReply
                Replies.append(farewellReply(msgObj))
                break
    
    return Replies

# [End of Code by Christian Shaw] 

#-----------------------------------------------------------------------------------------------------------------------------------------------#

#-----------------------------------------------------BOT RUN-----------------------------------------------------------------------------------#

# This runs the bot. Note: The token is specific to the bot
client.run("NjMzMzQ0NTM5NDk0NzExMzM2.XbHZtw.CLPjwoYCqMaQDYQ0jLElxYNfIGg")

#-----------------------------------------------------------------------------------------------------------------------------------------------#