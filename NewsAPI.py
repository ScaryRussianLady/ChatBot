#-------------------------------------------------------------BEGINNING OF IMPORT OF MODULES-------------------------------------------------------------#
"""A section for importing all modules necessary for this script."""
#Beginning of code by [Annija Balode, ID No: 9102828]

#This imports the requests package which allows for HTTP requests.
import requests

######################################################################################################################################
#The code below was commented out as it was unnecessary when attempting to use Cogs in order to allow this file to be loaded within the main chatbot file.

#The following imports the News API client specifically rather than everything from the News API that is being used in this script.
#from newsapi import NewsApiClient
######################################################################################################################################


#This will be used to ensure that no matter when the user accesses the API, the articles that are being pulled down are from the current date. Obviously, the date will be amendable but only if the user wishes to do so.
from datetime import datetime

#This allows for discord.py to be imported in order to have full access to the Discord API and the commands that can be found within the official documentation.
import discord
from discord.ext import commands

######################################################################################################################################
#The following code is from previous versions when attempting to import the same commands from the main file to this API file so communication could continue between the bot on Discord and the user rather than everything going through terminal.

# from chatbot_script import *
# import chatbot_script
######################################################################################################################################

#This imports the JSON module so things further down this file can be converted into JSON format.
import json

#Imports the translator element from the Google Translate module which will allow for the user's text to be translated between their language and English if it is non-English.
from googletrans import Translator

######################################################################################################################################
#The following code was not necessary anymore once the everything was being pulled through to the Discord bot itself.

#Installed pillow in terminal and then imported the module required for loading the URL of images.
#First had an issue with importing PIL so I referenced from https://stackoverflow.com/questions/8863917/importerror-no-module-named-pil to find the solution.
#from PIL import Image
######################################################################################################################################

#Importing the SaveData function from the user data management script in order to be able to save the users preferences and previous messages.
from UserDataManagement import SaveData

#IMPORTANT: this is the API key needed for accessing the News API 72742ae51f514418a9a6da52faf58be6

#The appropriate ReplyID for this script so that the main file knows to run this specific file only. Line 47 taken from chatbot_script.py.
NewsScriptGlobal_ID = "1423"

#End of code by [Annija Balode, ID No: 9102828]
#---------------------------------------------------------------END OF IMPORT OF MODULES-------------------------------------------------------------------#

######################################################################################################################################
#This was an attempt to add the News API file as an extension to the main file in order to be able to load it from the main script from previous versions.

#Beginning of code by [Annija Balode, ID No: 9102828] and referenced from official Discord API documentation.

#class MembersCog(commands.Cog):
    #def __init__(self, client):
    	#self.client = client


#def setup(client):
	#client.add_cog(MembersCog(client))

#End of code by [Annija Balode, ID No: 9102828] and referenced from official Discord API documentation.
######################################################################################################################################

#-------------------------------------------------------------BEGINNING OF INTRODUCTION FUNCTION-------------------------------------------------------------#
#Beginning of code by [Annija Balode, ID No: 9102828] and referenced from TMDBAPI_DiscordPrototype.py with adaptations.

"""Function for introducing the possibilities available to the user."""

def IntroductionToUser(MsgObj):
	#Saves the ReplyID to the JSON database so that dialogue can be done on discord and referenced from TMDBAPI_DiscordPrototype.py to ensure everything is being consistently called from all files.
	SaveData(NewsScriptGlobal_ID + "_KeywordsForBranching", MsgObj.userID, "ReplyID")
	
	#The beginning response that the bot says to the user so they are aware that they are searching in the News API. Also allows for the user to be aware of what they can search for.
	beginningResponse = ("So you want to look at some news? Good choice! Unfortunately, I can't read your mind so you might have to help me out here.") + ("\n I can tell you about an article that includes a word of your choice, I can output the top headlines of today, or you can even look into specific categories.") + ("\n So, what would you like to do? (Please use the prefix -r to communicate with me now).")
	
	return beginningResponse

"""A function which allows the Discord bot to know which function to branch off into depending on what the user says."""
def KeywordsForBranching(MsgObj):

	#Turns the user's message into a list which can be searched through to find certain keywords that will branch off into different functions. It allows for the bot to know what the user wants to look into.
	FindWords = MsgObj.list

	#The different keywords in a list associated to each function. There is also a list for no keywords in case the user does not have anything specific in mind.
	specificNewsKeywords = ["specific", "definite", "exact", "individual"]
	olderNewsKeywords = ["older", "earlier", "past", "before", "ago"]
	topHeadlineKeywords = ["themes", "theme", "headlines", "top", "categories", "category", "different", "headline"]
	noKeywords = ["no", "nah", "nope", "not sure", "idk", "dunno", "i don't know", "whatever"]

	#The following searches through the list of words that have been created from the users message and if any key words are located certain functions are ran.
	for word in range(len(FindWords)):
		if FindWords[word].lower() in specificNewsKeywords:
			#Runs the function for finding specific articles from the user giving keywords.
			return SpecificNewsPrimary(MsgObj)

		elif FindWords[word].lower() in olderNewsKeywords:
			#Runs the function for finding news that are older (from current date).
			return OlderNewsPrimary(MsgObj)

		elif FindWords[word].lower() in topHeadlineKeywords:
			#Runs the function for outputting the top headline of today to the user.
			return EveryTopHeadlinePrimary(MsgObj)

		elif FindWords[word].lower() in noKeywords:
			#Runs the function for outputting the top headline of today from BBC news specifically if the user is unsure of what they want.
			return NewsFromBBC(MsgObj)

#End of code by [Annija Balode, ID No: 9102828] and referenced from TMDBAPI_DiscordPrototype.py	with adaptations.

######################################################################################################################################
#Code from previous versions where the users message was split into a list and then ran through to locate certain keywords. One of the issues was that it would not be able to pick up capital letters or anything like that.
#The older code also was printing out to the terminal rather than being able to run through Discord itself.

#Beginning of code by [Annija Balode, ID No: 9102828]

	#Prints to the user to introduce them to the capabilities of the News API and what they can look into. Begins a conversation with the user.
	#print("So you want to look at some news? Good choice! Unfortunately, I can't read your mind so you might have to help me out here.")
	
	#Takes input from the user and splits it into a list to locate a keyword for progressing on further with the function.
	#specificFunction = input("Is there anything specific you want to look at, for example, specific topics? ")
	#specificFunctionList = specificFunction.split(" ")
	#specificFunctionKeywords = ["yes", "ye", "yeah", "yep", "sure", "yeh"]


	#Goes through the list from the users message to be able to ask a further question on what they would like to look into specifically.
	#for i in range(len(specificFunctionList)):
		#Will later change this to accessing a list of different ways of saying 'yes' so that it can run it and check it against that (more efficient).
	#if any(element in specificFunction for element in specificFunctionKeywords):
		#if specificFunctionList[i] == "yes":
		#userChoice = input("Okay, what would you like to look into? There's stuff like, specific topics, older news, or even different categories (stuff like sports). ")
	#else:
		#print("Cool, I will just look up the top news of today from BBC! If you want to look into films or books instead, just say 'let me go back' ")
		#userChoice = "no"

	#Splits the next users message to be able to locate a keyword for different functions of the News API.
	#userChoiceList = userChoice.split(" ")
	#specificNewsKeywords = ["specific", "definite", "exact", "individual"]
	#olderNewsKeywords = ["older", "earlier", "past", "before", "ago"]
	#topHeadlineKeywords = ["themes", "theme", "headlines", "top", "categories", "category", "different"]
	#noKeywords = ["no", "nah", "nope"]

	#Allows the function to be able to choose which function should be ran next depending on what the user has chosen.
	#if any(element in userChoice for element in specificNewsKeywords):
		#SpecificNews()

	#elif any(element in userChoice for element in olderNewsKeywords):
		#OlderNews()

	#elif any(element in userChoice for element in topHeadlineKeywords):
		#EveryTopHeadline()

	#elif any(element in userChoice for element in noKeywords):
		#NewsFromBBC()

	#else:
		#print("Sorry, I don't understand what you mean. Try rephrasing! I promise I am doing my best to understand you.")
		#IntroductionToUser()

#End of code by [Annija Balode, ID No: 9102828]
######################################################################################################################################	
#-----------------------------------------------------------------------------------------------------------------------------------------------#


#-------------------------------------------------------------TOP HEADLINES FUNCTION-------------------------------------------------------------#
# Beginning of code by [Annija Balode ID No: 9102828] and referenced from documentation https://newsapi.org/docs/endpoints/top-headlines
def EveryTopHeadlinePrimary(MsgObj):
	#Saves the ReplyID to the JSON database so that dialogue can be done on discord.
	SaveData(NewsScriptGlobal_ID + "_EveryTopHeadline", MsgObj.userID, "ReplyID")
	return ("What category would you like to look at for a top headline? The following choices are: general; health; science; technology; business; sports; management; and entertaintment.")

def EveryTopHeadline(MsgObj):
	#Sets the category choice to the users so the function can print out the top headline from the current date for that specific category..
	categoryChoices = MsgObj.msg
	#Sets the amount of articles to be printed to 1 so that the user is not bombarded with multiple articles in one go.
	amountOfArticles = "1"

	#Gets the top headlines from the UK, 'country=gb' can be changed depending on what country you want to look at. It has been set to UK as it is most likely that the user is an English speaker using this bot in England.
	url = ('https://newsapi.org/v2/top-headlines?'
       'country=gb&'
	   #Can adjust the category depending on what you want specifically, there are only certain categories available: 
	   #general, health, science, technology, business, sports, management, entertainment.
	   'category='+categoryChoices+'&'
	   #Returns a set amount of news articles, default is 20 if a number is not specified and the maximum is 100.
		'pageSize='+amountOfArticles+'&'
       'apiKey=72742ae51f514418a9a6da52faf58be6')

	#Gets the URL in JSON format so that specific items can be retrieved later on in the function and allows for simple outputting to the user through the Discord bot.
	response = requests.get(url).json()

	specificArticle = response["articles"]

	#Goes through the JSON in order to retrive the title, author and url of the specific article.
	for title in specificArticle:
		theAcceptedResponseTitle = title["title"]

	for author in specificArticle:
		theAcceptedResponseAuthor = author["author"]
	
	for url in specificArticle:
		theAcceptedResponseURL = url["url"]

######################################################################################################################################
#The following code was not implemented as there were some issues in being able to retrieve just the name of the article provider.

	#for source in specificArticle:
		#theAcceptedResponseSource = source["source"]

	#for nameOfSource in theAcceptedResponseSource:
		#theAcceptedResponseName = nameOfSource[0]
######################################################################################################################################
	
	#Adds the title of the article and the author together so it makes grammatical sense when the Discord bot outputs to the user. 
	finalResponse = str(theAcceptedResponseTitle) + " by " + str(theAcceptedResponseAuthor)
	linkToReponse = ("\n You can access the article here: " + str(theAcceptedResponseURL))
	savedResponse = ("your article!")

	#Saves the article that the user just looked at into the JSON file so that next time they visit the bot is able to retrieve this - allows for a more personalised experience between the user and the bot.
	SaveData(savedResponse, MsgObj.userID, "PreviousViewedArticles")
	SaveData(savedResponse, MsgObj.userID, "PreviousViewedEntertainment")
	
	return finalResponse + linkToReponse

######################################################################################################################################
#The following code was removed as it was not running through terminal anymore and would not work with outputting to the Discord bot.

	#Takes in input from the user so that a specific category can be chosen.
	#specificCategoryQuestion = input("Would you like to choose a specific category you would like to look at? ")
	#specificCategoryQuestionList = specificCategoryQuestion.split(" ")

	#Allows the user to choose a specific category from the top headlines, if they can't think of one, then the choice is set to general as default.
	#for i in range(len(specificCategoryQuestionList)):
		#if specificCategoryQuestionList[i] == 'yes':
			#categoryChoices = input("Your options are as follows: general; health; science; technology; business; sports; management; and entertaintment." + '\n' + "Which category would you like? ")
			#amountOfArticles = input("Alright! But, before I show you the articles, how many would you like to see? ")
		#else:
			#print("That's okay. I will just output the general top headline from today! :)")
	
	#Empty lists for sorting out the title, author and url of the article.
	#theAcceptedResponseTitle = []
	#theAcceptedResponseAuthor = []
	#theAcceptedResponseURL = []

	#Goes through the JSON in order to retrive the title, author and url of the specific article and put it into different lists above.
	#for title in specificArticle:
		#theAcceptedResponseTitle.append(title["title"])
	
	#for author in specificArticle:
		#theAcceptedResponseAuthor.append(author["author"])

	#for url in specificArticle:
		#theAcceptedResponseURL.append(url["url"])

	#Prints out the articles in order from 1 to n depending on how many the user has chosen with the title, author and url of the article.
	#for i in range(len(theAcceptedResponseTitle)):
		#print(i+1, str(theAcceptedResponseTitle[i]) + " by " + str(theAcceptedResponseAuthor[i]) + ": " + str(theAcceptedResponseURL[i]))

	#Fetches the data in JSON format and prints it out in terminal.
	#theURL = response.json()
	#print(theURL)
######################################################################################################################################

#End of code by [Annija Balode ID No: 9102828] and referenced from documentation https://newsapi.org/docs/endpoints/top-headlines
#-----------------------------------------------------------------------------------------------------------------------------------------------#


#-------------------------------------------------------------SPECIFIC NEWS FUNCTION-------------------------------------------------------------#
#Beginning of code by [Annija Balode, ID No: 9102828] and referenced from the official News API documentation https://newsapi.org/docs/endpoints/everything
def SpecificNewsPrimary(MsgObj):
	#Saves the ReplyID to the JSON database so that dialogue can be done on discord.
	SaveData(NewsScriptGlobal_ID + "_SpecificNews", MsgObj.userID, "ReplyID")
	return ("Okay, give me a word or words and I will find you an article that includes it!")

"""A function for finding news around the world depending on specific words/key terms. However, this search does not allow for country-specific searches."""
def SpecificNews(MsgObj):
	chosenTopic = MsgObj.msg

	SaveData(chosenTopic, MsgObj.userID, "FavNewsTopic")

	url = ('https://newsapi.org/v2/everything?'
	# This is the key word that should bring up the relevant article.
       'qInTitle='+str(chosenTopic.lower())+'&'
	   'pageSize=1&'
	   # From what date it should get searched (depending how old you want the article to be)
	   'from=2019-11-01&'
	   # How to sort the articles (the most popular will show first, therefore, the most relevant and most likely to be in English)
       'sortBy=popularity&'
       'apiKey=72742ae51f514418a9a6da52faf58be6')

	#Fetches the data in JSON format.
	response = requests.get(url).json()
	specificArticle = response["articles"]

	#Searches through the JSON of the article that has been requested to find the title, author and url of it.
	for title in specificArticle:
		theAcceptedResponseTitle = title["title"]

	for author in specificArticle:
		theAcceptedResponseAuthor = author["author"]
	
	for url in specificArticle:
		theAcceptedResponseURL = url["url"]

	#Adds the title of the article and the author together so it makes grammatical sense when the Discord bot outputs to the user. 
	finalResponse = str(theAcceptedResponseTitle) + " by " + str(theAcceptedResponseAuthor)
	linkToReponse = ("\nYou can access the article here: " + str(theAcceptedResponseURL))
	savedResponse = ("your article on ") + str(chosenTopic)

	#Saves the article that the user just looked at into the JSON file so that next time they visit the bot is able to retrieve this - allows for a more personalised experience between the user and the bot.
	SaveData(chosenTopic, MsgObj.userID, "PreviousViewedArticles")
	SaveData(savedResponse, MsgObj.userID, "PreviousViewedEntertainment")
	
	return finalResponse + linkToReponse

######################################################################################################################################
#Code removed due to the fact that the function was not outputting to the terminal anymore and this code would not work when pushing through the Discord bot.

	#Stores the specific word(s) that the user enters and then will use this variable to search up the relevant articles.
	#chosenTopic = input("What topic would you like to look at?" + '\n' + "Give me one word or several words and I will fetch you the most popular article right now based on that topic! ")
	
	#Stores the amount of articles that the user wants to see from the topic they chose.
	#amountOfArticles = input("Nice topic! But, before I tell you the relevant articles, how many would you like to see? ")

	#Assigns the current date and time on the users laptop to the variable currentDate.
	#currentDate = str(datetime.now())

	#Empty lists for sorting out the title, author and url of the article.
	#theAcceptedResponseTitle = []
	#theAcceptedResponseAuthor = []
	#theAcceptedResponseURL = []

	#Goes through the JSON in order to retrive the title, author and url of the specific article and put it into different lists above.
	#for title in specificArticle:
		#theAcceptedResponseTitle.append(title["title"])
	
	#for author in specificArticle:
		#theAcceptedResponseAuthor.append(author["author"])

	#for url in specificArticle:
		#theAcceptedResponseURL.append(url["url"])

	#Prints out the articles in order from 1 to n depending on how many the user has chosen with the title, author and url of the article.
	#for i in range(len(theAcceptedResponseTitle)):
		#print(i+1, theAcceptedResponseTitle[i] + " by " + theAcceptedResponseAuthor[i] + ": " + theAcceptedResponseURL[i])
	

	#Loops back to the beginning of the function if they wish to search another topic. Further improvements will be made.
	#findAnotherTopic = input("Here is what I found. Hope these are okay for you!" + '\n' + "Are there any other topics you would like to look at? ")
	#findAnotherTopicList = findAnotherTopic.split(" ")
	#for i in range(len(findAnotherTopicList)):
		#if findAnotherTopicList[i] == "yes":
			#SpecificNews()
		#else:
			#print("Cool. See you soon!")
######################################################################################################################################

#End of code by [Annija Balode ID No: 9102828] and referenced from the official News API documentation https://newsapi.org/docs/endpoints/everything
#------------------------------------------------------------------------------------------------------------------------------------------------#


#-------------------------------------------------------------OLDER ARTICLES FUNCTION-------------------------------------------------------------#
"""Functions which allows the user to look at certain articles from within the past month, does not allow for a wider space of time as need to upgrade to a paid plan if want to do so."""

#Beginning of code by [Annija Balode ID No: 9102828] and referenced from the official News API documentation https://newsapi.org/docs/endpoints/everything

def OlderNewsPrimary(MsgObj):
	#Saves the ReplyID to the JSON database so that dialogue can be done on discord.
	SaveData(NewsScriptGlobal_ID + "_OlderNews", MsgObj.userID, "ReplyID")
	return ("Okay, from what date would you like to look at? Please make sure it's from within the past month and in the form YYYY-MM-DD so I can understand you!")

def OlderNews(MsgObj):
	#Assigns the users message to a variable so that the appropriate date can be implemented into the URL for searching and returning.
	chosenDate = MsgObj.msg

	url = ('https://newsapi.org/v2/everything?'
       'q=apples&'
	   'pageSize=1&'
	   'from='+chosenDate+'&'
       'sortBy=popularity&'
       'apiKey=72742ae51f514418a9a6da52faf58be6')

	#Fetches the data in JSON format.
	response = requests.get(url).json()
	specificArticle = response["articles"]

	#Searches through the JSON of the article that has been requested to find the title, author and url of it.
	for title in specificArticle:
		theAcceptedResponseTitle = title["title"]

	for author in specificArticle:
		theAcceptedResponseAuthor = author["author"]
	
	for url in specificArticle:
		theAcceptedResponseURL = url["url"]
		
	#Adds the title of the article and the author together so it makes grammatical sense when the Discord bot outputs to the user. 
	finalResponse = str(theAcceptedResponseTitle) + " by " + str(theAcceptedResponseAuthor)
	linkToReponse = ("\nYou can access the article here: " + str(theAcceptedResponseURL))
	savedResponse = ("your article from ") + str(chosenDate)

	#Saves the article that the user just looked at into the JSON file so that next time they visit the bot is able to retrieve this - allows for a more personalised experience between the user and the bot.
	SaveData(chosenDate, MsgObj.userID, "PreviousViewedArticles")
	SaveData(savedResponse, MsgObj.userID, "PreviousViewedEntertainment")
	
	return finalResponse + linkToReponse

######################################################################################################################################
#The following code was commented out as it was unnecessary due to the fact that the output was not being returned through the terminal. This code would not work for outputting through the Discord bot.

	#Asks the user for input on what date they would like to see articles from, it also lets them know that it has to be within the last month from the current date to avoid getting an error thrown at them.
	#howOldQuestion = input("Please make sure to write in the format YYYY-MM-DD including the dashes (I know, it's a strange format!)" + '\n' + "From what date within the last month would you like to view news? ")
	#howOldQuestionStr = str(howOldQuestion)

	#These are empty lists for the title, author and url of the article to appended into for returning to the user at the end of the function.
	#theAcceptedResponseTitle = []
	#theAcceptedResponseAuthor = []
	#theAcceptedResponseURL = []

	#Searches through the JSON of the article that has been requested to find the title, author and url of it.
	#for title in specificArticle:
		#Adds the title of the article to the list for title of the article.
		#theAcceptedResponseTitle.append(title["title"])
	
	#for author in specificArticle:
		#Adds the author of the article to the list for author of the article.
		#theAcceptedResponseAuthor.append(author["author"])

	#for url in specificArticle:
		#Adds the URL of the article to the list of the url of the article.
		#theAcceptedResponseURL.append(url["url"])

	#Prints out the articles in order from 1 to n depending on how many the user has chosen with the title, author and url of the article.
	#for i in range(len(theAcceptedResponseTitle)):
		#print(i+1, theAcceptedResponseTitle[i] + " by " + theAcceptedResponseAuthor[i] + ": " + theAcceptedResponseURL[i])
######################################################################################################################################

#End of code by [Annija Balode ID No: 9102828] and referenced from the official News API documentation https://newsapi.org/docs/endpoints/everything
#-------------------------------------------------------------------------------------------------------------------------------------------------#


#-------------------------------------------------------------NEWS FROM BBC SPECIFICALLY FUNCTION-------------------------------------------------------------#
"""A function for fetching the top ten headlines of today from BBC News."""

# Beginning of code by [Annija Balode ID No: 9102828] and reference from https://www.geeksforgeeks.org/fetching-top-news-using-news-api/ with adaptation.
def NewsFromBBC(MsgObj): 
	#Saves the ReplyID to the JSON database so that dialogue can be done on discord.
	SaveData(NewsScriptGlobal_ID + "_NewsFromBBC", MsgObj.userID, "ReplyID")

	# This is the BBC News API with our own personal API key. 
	url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=72742ae51f514418a9a6da52faf58be6"

	#Fetches the data in JSON format. 
	response = requests.get(url).json()

	specificArticle = response["articles"]

	#Searches through the JSON of the article that has been requested to find the title, author and url of it.
	for title in specificArticle:
		theAcceptedResponseTitle = title["title"]

	for author in specificArticle:
		theAcceptedResponseAuthor = author["author"]
	
	for url in specificArticle:
		theAcceptedResponseURL = url["url"]
		
	#Adds the title of the article and the author together so it makes grammatical sense when the Discord bot outputs to the user. 
	finalResponse = str(theAcceptedResponseTitle) + " by " + str(theAcceptedResponseAuthor)
	linkToReponse = ("\nYou can access the article here: " + str(theAcceptedResponseURL))
	savedResponse = ("your article!")

	#Saves the article that the user just looked at into the JSON file so that next time they visit the bot is able to retrieve this - allows for a more personalised experience between the user and the bot.
	SaveData(savedResponse, MsgObj.userID, "PreviousViewedArticles")
	SaveData(savedResponse, MsgObj.userID, "PreviousViewedEntertainment")
	
	return ("It's okay that you are not sure! Here, have the top article from BBC News") + "\n" + finalResponse + linkToReponse

######################################################################################################################################
#The following code was commented out as it was unnecessary due to the fact that the output was not being returned through the terminal. This code would not work for outputting through the Discord bot.

	#These are empty lists for the title, author and url of the article to appended into for returning to the user at the end of the function.
	#theAcceptedResponseTitle = []
	#theAcceptedResponseAuthor = []
	#theAcceptedResponseURL = []

	#Goes through the JSON in order to retrive the title, author and url of the specific article and put it into different lists above.
	#for title in specificArticle:
		#theAcceptedResponseTitle.append(title["title"])
	
	#for author in specificArticle:
		#theAcceptedResponseAuthor.append(author["author"])

	#for url in specificArticle:
		#theAcceptedResponseURL.append(url["url"])

	
	#Prints out the articles in order from 1 to n depending on how many the user has chosen with the title, author and url of the article.
	#for i in range(len(theAcceptedResponseTitle)):
		#print(i+1, theAcceptedResponseTitle[i] + " by " + theAcceptedResponseAuthor[i] + ": " + theAcceptedResponseURL[i])
######################################################################################################################################

#End of code by [Annija Balode, ID No: 9102828] and reference from https://www.geeksforgeeks.org/fetching-top-news-using-news-api/ with adaptation.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------#


######################################################################################################################################
#-------------------------------------------------------------TESTING FUNCTION----------------------------------------------------------------#
#A testing function which allowed for acceptance testing for specific functions through the terminal. This got removed as it was unnecessary once the News API was getting pulled through the Discord bot itself.

#Beginning of code by [Annija Balode, ID No: 9102828]

#if __name__ == '__main__':
	#Calls the function, only using this to ensure that everything is getting called correctly, these function names will be used to import from chatbot_script.py later on.
		#NewsFromBBC()
		#EveryTopHeadline() 
		#SpecificNews()
		#OlderNews()
		#IntroductionToUser()

#End of code by [Annija Balode, ID No: 9102828]
#----------------------------------------------------------------------------------------------------------------------------------------------#
######################################################################################################################################

#Beginning of code by [Annija Balode, ID No: 9102828] and referenced from TMDBAPI_DiscordPrototype.py with adaptations.

#Depending on what the reply ID is set to it will determine the function that needs to be used in this script.
def FindID(obj, ID):
	if ID == "KeywordsForBranching":
		return KeywordsForBranching(obj)
	if ID == "SpecificNews":
		return SpecificNews(obj)
	if ID == "EveryTopHeadline":
		return EveryTopHeadline(obj)
	if ID == "OlderNews":
		return OlderNews(obj)
	if ID == "NewsFromBBC":
		return NewsFromBBC(obj)

#End of code by [Annija Balode, ID No: 9102828] and referenced from TMDBAPI_DiscordPrototype.py with adaptations.

