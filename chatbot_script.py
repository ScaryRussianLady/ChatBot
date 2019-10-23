# List of modules
import discord
import random
from discord.ext import commands
from googletrans import Translator

# Keywords list - Add keywords here
keywordsList = {
    "This",
    "is",
    "an",
    "example"
}

#[CHRISTIAN] Sets the command's prefix to "-"
client = commands.Bot(command_prefix = "-")

@client.event
#[CHRISTIAN] This will print the text to the python terminal when the bot is ready on discord
async def on_ready():
    print("The E-Bot is online!")


@client.command()
# [CHRISTIAN] This is the MAIN function for the chatbot | com = the command (bot), msg = the user input after the command is called
# E.G The user typing "-bot My name is Bill" will make msg = "My name is Bill"
async def bot(com, *, msg):

    # [CHRISTIAN] Calls the function that creates the message object | Establishes the variable which will contain the bot's reply
    msgObj = createMsgObj(msg, com.author.id)
    print(msgObj.msg)
    print(msgObj.list)
    print(msgObj.lang)
    print(msgObj.userID)

    botReply = None # Currently set as None because a reply hasn't been generated yet
    welcome = False # to determine if bot has introduced
    
    #[callum] begining of the basic responses code, working on a way to make previous responses determine the next allowed inputs ard responses, can currently give a brief summary of the bots functions
    for i in range(len(msgObj.list)):
        if msgObj.list[i] == 'hey' or msgObj.list[i] == 'hi' or msgObj.list[i] == 'hello':
            print("Message received.")
            botReply = "Hey there! I'm E-Bot, I am here to provide you with certain services. Would you like to know what I can do?"
            welcome = True

    if welcome == True:        
        for i in range(len(msgObj.list)):
            if msgObj.list[i] == 'yes':
                print("Message received.")
                botReply = "Okay, cool! So, I can search films, books and news for you and give information on them, recommendations, ratings and anything else you want to know about them. Would you like to give it a go?"
            elif msgObj.list[i] == 'no':
                print("Message received.")
                botReply = "Well, that's a shame! If you change your mind just come and say hello to me again. Hope to see you soon! :)"
                
    botReply = translateText(botReply, msgObj.lang) #small issue with translate, truns bot into not       
    await com.send(botReply)
    msgObj.list.clear()


    #------------------------------------------- INSIDE THESE LINES DETERMINES THE BOT'S RESPONSE -------------------------------------------#
    
    # List of .py collaborative files (import the functions from the files that you work on)
    # from [your file name] import [function/class name]

    # Call your script's functions here
    #botReply = "Placeholder reply" # Placeholder

    #------------------------------------------- INSIDE THESE LINES DETERMINES THE BOT'S RESPONSE -------------------------------------------#    
    

    # [CHRISTIAN] If the user input was not in English then this will translate botReply from English to the language the user used | then the bot will send the botReply string on discord.
    #botReply = translateText(botReply, msgObj.lang)
    #await com.send(botReply)


# [CHRISTIAN] This function detects of certain word have been said
# Deprecated
def findKeywords(msgList, keywords):
    saidWord = False
    for i in msgList:
        if i.lower() == keywords:
            saidWord = True
    return saidWord

# [CHRISTIAN] This will translate the languages of messages
def translateText(text, lang):
    translator = Translator()
    translatedMessage = translator.translate(text, dest=lang)
    #print("Message Translated >> ", translatedMessage.text)
    return translatedMessage.text

# [CHRISTIAN] This will find the language a string is in
def detectLanguage(text):
    translator = Translator()
    language = translator.detect(text)
    return language.lang

# [CHRISTIAN] This creates an object to store the message properties AND a function to create the object and give it the properties it needs
class messageObj():
    msgCount = 0
    def __init__(self, msg, msgList, msgLang, msgUserID):
        self.msg = msg
        self.list = msgList
        self.lang = msgLang
        self.userID = msgUserID
        messageObj.msgCount += 1

def createMsgObj(msg, authorID):
    msgLanguage = detectLanguage(msg)
    #if msgLanguage != 'en':
    #    msg = translateText(msg, "en")
    msgList = msg.split()

    msg_obj = messageObj(msg, msgList, msgLanguage, authorID)
    return msg_obj

    
# [CHRISTIAN] This runs the bot. Note: The token is specific to the bot
client.run("NjMzMzQ0NTM5NDk0NzExMzM2.XaTNgA.WhYbdsxRBsY5fVqu4n3pi5lCnVg")
