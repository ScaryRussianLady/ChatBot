# List of modules
import discord
import random
from discord.ext import commands
from googletrans import Translator
import json
import asyncio


#[Annija] simply importing everything from my API script.
#import NewsAPI

#This specifies what extensions will be added, add the name of the script you want to access.
startup_extensions = ['cogs.NewsAPI']

#[CHRISTIAN] Sets the command's prefix to "-"
client = commands.Bot(command_prefix = "-")

@client.event
#[CHRISTIAN] This will print the text to the python terminal when the bot is ready on discord
async def on_ready():
    print("\nThe E-Bot is online!")
    # For terminal use only. Creates space between information on the terminal to make it easier to read.
    print("\n--------------------------------------------------------------------------")

@client.command()
# [CHRISTIAN] This is the MAIN function for the chatbot | com = the command (bot), msg = the user input after the command is called
# E.G The user typing "-bot My name is Bill" will make msg = "My name is Bill"
async def bot(com, *, msg):

    # [CHRISTIAN] Calls the function that creates the message object
    msgObj = createMsgObj(msg, com.author.id, str(com.author), com.channel)
    print("User's message            >>", msgObj.msg)
    print("User's message as list    >>", msgObj.list)
    print("User's message's language >>", msgObj.lang)
    print("User's ID                 >>", msgObj.userID)
    print("User's name               >>", msgObj.username)
    print("User's channel            >>", msgObj.channel)

    # Saves the userID and message data to the user_datastore.json file
    from UserDataManagement import SaveData
    #SaveData(msgObj.userID, msgObj.userID, "UserID")
    #SaveData(str(msgObj.username), msgObj.userID, "Name")
    #SaveData(msgObj.msg, msgObj.userID, "LastMessage")
    
    # [CHRISTIAN] Calls the function which generates replies (Scroll to see the function for more information | Returns as a list
    botReply = generateReplies(msgObj) 
   
    # [CHRISTIAN] Send's the replies on discord in the order of the botReply list. If there are no replies, sends a different message
    # it will also translate the message if the message sent by the user wasn't in English
    if len(botReply) != 0:
        for i in botReply:
            Reply = translateText(i, msgObj.lang)
            await com.send(Reply)
    else:
        Reply = "A keyword was not mentioned" # This is a placeholder reply.
        Reply = translateText(Reply, msgObj.lang)
        await com.send(Reply)
    
    #For terminal use only. Creates space between information on the terminal to make it easier to read.
    print("\n--------------------------------------------------------------------------")

# [CHRISTIAN] This async function will handle all of the replies (fingers crossed). I want to make it as convienant as possible.
# In layman terms, replies are going to be done without the -bot prefix. and instead with the -r
@client.command()
async def r(com, *, reply):

    msgObj = createMsgObj(reply, com.author.id, str(com.author), com.channel)
    print("User's reply            >>", msgObj.msg)
    print("User's reply as list    >>", msgObj.list)
    print("User's reply's language >>", msgObj.lang)
    print("User's ID               >>", msgObj.userID)
    print("User's name             >>", msgObj.username)
    print("User's channel          >>", msgObj.channel)

    # Next part is going to retrieve and check the "replyID" and go to the required script & function

    await com.send("Reply function us under construction (replyID)")

    #For terminal use only. Creates space between information on the terminal to make it easier to read.
    print("\n--------------------------------------------------------------------------")

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
    def __init__(self, msg, msgList, msgLang, msgUserID, msgUsr, msgChannel):
        self.msg = msg
        self.list = msgList
        self.lang = msgLang
        self.userID = msgUserID
        self.username = msgUsr
        self.channel = msgChannel
        messageObj.msgCount += 1

def createMsgObj(msg, authorID, usr, channel):
    msgLanguage = detectLanguage(msg)
    #if msgLanguage != 'en':
    #    msg = translateText(msg, "en")
    msgList = msg.split()

    # This part of the code is going to remove the hashtag from the username that discord uses
    NewUsr = ""
    for char in range(len(usr)):
        if usr[char] == "#":
            usr = NewUsr
            break
        
        NewUsr = NewUsr+usr[char]

    msg_obj = messageObj(msg, msgList, msgLanguage, authorID, usr, channel)
    return msg_obj

# [CHRISTIAN] This algorthim will search for specific keywords from a list to determine what scripts will be used for replies
def generateReplies(MessageObject):
    
    Replies = commonReplies(MessageObject)
    return Replies

def commonReplies(msgObj):

    msgList = msgObj.list

    greetingKeywords = ["hi", "hello", "good", "greetings", "hey"]
    appreciationKeywords = ["thank", "thanks"]
    filmKeywords = ["movie", "film", "series"]
    newsKeywords = ["news", "article", "weather", "articles", "headlines", "headline"]
    bookKeywords = ["book", "story"]
    farewellKeywords = ["bye", "goodbye", "farewell"]

    Replies = []

    for i in range(len(msgList)):
        for j in range(len(greetingKeywords)):
            if msgList[i].lower() == greetingKeywords[j]:
                if greetingKeywords[j] != "good":
                    from BasicResponses import greetingReply
                    Replies.append(greetingReply(msgObj))
                    break
                else:
                    if len(msgList) != 1:
                        try:
                            if msgList[i+1].lower() == "morning" or msgList[i+1].lower() == "evening" or msgList[i+1].lower() == "afternoon":
                                from BasicResponses import greetingReply
                                Replies.append(greetingReply(msgObj))
                                break
                        except:
                            pass

        for j in range(len(appreciationKeywords)):
            if msgList[i].lower() == appreciationKeywords[j]:
                from BasicResponses import appreciationReply
                Replies.append(appreciationReply(msgObj))
                break
        
        for j in range(len(filmKeywords)):
            if msgList[i].lower() == filmKeywords[j] or msgList[i].lower() == (filmKeywords[j]+"s"):
                # Call for film function inside of the placeholder
                from TMDBAPI import firstUserInt
                #Replies.append("Placeholder Film Info")
                break
        
        for j in range(len(newsKeywords)):
            if msgList[i].lower() == newsKeywords[j] or msgList[i].lower() == (newsKeywords[j]+"s"):
                # Call for news function inside of the placeholder
                #Replies.append("Cool! Let's go look at some news!")
                #NewsAPI.IntroductionToUser()
                #load() 
                #[Annija Balode ID No: 9102828]
                for extension in startup_extensions:
                    bot.load_extension(extension)
                break

        for j in range(len(bookKeywords)):
            if msgList[i].lower() == bookKeywords[j] or msgList[i].lower() == (bookKeywords[j]+"s"):
                # Call for book function inside of the placeholder
                from GoodreadsAPI import UserIntro
                #Replies.append("Placeholder Book Info")
                break
        
        for j in range(len(farewellKeywords)):
            if msgList[i].lower() == farewellKeywords[j]:
                from BasicResponses import farewellReply
                Replies.append(farewellReply(msgObj))
                break
    
    return Replies

# [CHRISTIAN] I don't even know what to call this yet
def PathReplies(msg):
    with open("User_Datastore.json") as uds:
        UserData = json.load(uds)

    yes = ["yes", "yea", "yeah"]
    no = ["no", "nah"]

    print(UserData)
    print(no)
    print(yes)

# [CHRISTIAN] Does like an input thing that sends a message and takes the input and returns it.
# These are some test function and... the test failed. So, replies are gonna have to be done a different way.
async def SendMessage(Message, Channel):
    await client.wait_until_ready()
    asyncio.sleep(5)
    #print("It's alive?")
    await Channel.send(Message)
    return

def DiscordInput(Message, Channel):
    client.loop.create_task(SendMessage(Message, Channel))

# [CHRISTIAN] This runs the bot. Note: The token is specific to the bot
client.run("NjMzMzQ0NTM5NDk0NzExMzM2.XbHZtw.CLPjwoYCqMaQDYQ0jLElxYNfIGg")