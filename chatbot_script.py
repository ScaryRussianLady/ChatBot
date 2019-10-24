# List of modules
import discord
import random
from discord.ext import commands
from googletrans import Translator

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
    print("User's message            >>", msgObj.msg)
    print("User's message as list    >>", msgObj.list)
    print("User's message's language >>", msgObj.lang)
    print("User's ID                 >>", msgObj.userID)

    # [CHRISTIAN] This algorthim will search for specific keywords from a list to determine what scripts will be used for replies
    botReply = generateReplies(msgObj.list) 
   
    # [CHRISTIAN] If the user input was not in English then this will translate botReply from English to the language the user used | then the bot will send the botReply string on discord.
    if len(botReply) != 0:
        for i in botReply:
            Reply = translateText(i, msgObj.lang)
            await com.send(Reply)
    else:
        Reply = "A keyword was not mentioned" # This is a placeholder reply.
        Reply = translateText(Reply, msgObj.lang)
        await com.send(Reply)

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

# [CHRISTIAN] This algorthim will search for specific keywords from a list to determine what scripts will be used for replies
def generateReplies(msgList):
    greetingKeywords = ["hi", "hello", "good", "greetings", "hey"]
    appreciationKeywords = ["thank", "thanks"]
    filmKeywords = ["movie", "film", "series"]
    newsKeywords = ["news", "article", "weather"]
    bookKeywords = ["book", "story"]
    farewellKeywords = ["bye", "goodbye", "farewell"]

    Replies = []

    for i in range(len(msgList)):
        for j in range(len(greetingKeywords)):
            if msgList[i].lower() == greetingKeywords[j] or msgList[i].lower() == greetingKeywords[j]+" morning":
                # Call for greeting function inside of the placeholder
                #Replies.append("Placeholder Greeting")
                from BasicResponses import greetingReply
                Replies.append(greetingReply(msgList))
                break

        for j in range(len(appreciationKeywords)):
            if msgList[i].lower() == appreciationKeywords[j]:
                # Call for appreciation function inside of the placeholder
                #Replies.append("Placeholder Appreciation")
                from BasicResponses import appreciationReply
                Replies.append(appreciationReply(msgList))
                break
        
        for j in range(len(filmKeywords)):
            if msgList[i].lower() == filmKeywords[j]:
                # Call for film function inside of the placeholder
                Replies.append("Placeholder Film Info")
                break
        
        for j in range(len(newsKeywords)):
            if msgList[i].lower() == newsKeywords[j]:
                # Call for news function inside of the placeholder
                Replies.append("Placeholder News Info")
                break

        for j in range(len(bookKeywords)):
            if msgList[i].lower() == bookKeywords[j]:
                # Call for book function inside of the placeholder
                Replies.append("Placeholder Book Info")
                break
        
        for j in range(len(farewellKeywords)):
            if msgList[i].lower() == farewellKeywords[j]:
                # Call for farewell function inside of the placeholder
                # Replies.append("Placeholder Farewell")
                from BasicResponses import farewellReply
                Replies.append(farewellReply(msgList))
                break
    
    print(Replies)
    return Replies

# [CHRISTIAN] This runs the bot. Note: The token is specific to the bot
client.run("NjMzMzQ0NTM5NDk0NzExMzM2.XbHZtw.CLPjwoYCqMaQDYQ0jLElxYNfIGg")