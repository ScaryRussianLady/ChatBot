
#Finish of all comments.

#-------------------------------------------------------------BEGINNING OF IMPORT OF MODULES-------------------------------------------------------------#
# Beginning of code by [Annija Balode ID No: 9102828]

# This imports the requests package which allows for HTTP requests.
import requests

# The following imports the News API client specifically rather than everything from the News API that is being used in this script.
#from newsapi import NewsApiClient

# This will be used to ensure that no matter when the user accesses the API, the articles that are being pulled down are from the current date.
# Obviously, the date will be changed but only if the user wishes to do so.
from datetime import datetime

#
import discord
from discord.ext import commands

#
# from chatbot_script import *
# import chatbot_script

#
import json

# Imports the translator element from the Google Translate module which will allow for the user's text to be translated between their language
# and English if it is non-English.
from googletrans import Translator

# Installed pillow in terminal and then imported the module required for loading the URL of images.
# First had an issue with importing PIL so I referenced from https://stackoverflow.com/questions/8863917/importerror-no-module-named-pil to find the solution.
from PIL import Image


from io import BytesIO

from UserDataManagement import SaveData

# IMPORTANT: this is our API key 72742ae51f514418a9a6da52faf58be6

NewsScriptGlobal_ID = "1423"

# End of code by [Annija Balode ID No: 9102828]
#---------------------------------------------------------------END OF IMPORT OF MODULES-------------------------------------------------------------------#


#-------------------------------------------------------------BEGINNING OF INTRODUCTION FUNCTION-------------------------------------------------------------#
#Function for introducing the possibilities to the user, it allows for the file to know which function to bring up.#
# Beginning of code by [Annija Balode ID No: 9102828]

def IntroductionToUser(MsgObj):
	SaveData(NewsScriptGlobal_ID + "_KeywordsForBranching", MsgObj.userID, "ReplyID")
	
	beginningResponse = ("So you want to look at some news? Good choice! Unfortunately, I can't read your mind so you might have to help me out here.") + ("\n I can tell you about an article that includes a word of your choice, I can output the top headlines of today, or you can even look into specific categories.") + ("\n So, what would you like to do?")
	
	return beginningResponse

def KeywordsForBranching(MsgObj):
	FindWords = MsgObj.list

	specificNewsKeywords = ["specific", "definite", "exact", "individual"]
	#olderNewsKeywords = ["older", "earlier", "past", "before", "ago"]
	#topHeadlineKeywords = ["themes", "theme", "headlines", "top", "categories", "category", "different"]
	#noKeywords = ["no", "nah", "nope"]

	# await self.bot.say("News woo!")
	#print("So you want to look at some news? Good choice! Unfortunately, I can't read your mind so you might have to help me out here.")
	#specificFunction = input("Is there anything specific you want to look at, for example, specific topics? ")
	# specificFunctionList = specificFunction.split(" ")
	#specificFunctionKeywords = ["yes", "ye", "yeah", "yep", "sure", "yeh"]


	# for i in range(len(specificFunctionList)):
		# Will later change this to accessing a list of different ways of saying 'yes' so that it can run it and check it against that (more efficient).
	#if any(element in specificFunction for element in specificFunctionKeywords):
		# if specificFunctionList[i] == "yes":
	#	userChoice = input("Okay, what would you like to look into? There's stuff like, specific topics, older news, or even different categories (stuff like sports). ")
	#else:
	#	print("Cool, I will just look up the top news of today from BBC! If you want to look into films or books instead, just say 'let me go back' ")
	#	userChoice = "no"


	# userChoiceList = userChoice.split(" ")
	#specificNewsKeywords = ["specific", "definite", "exact", "individual"]
	#olderNewsKeywords = ["older", "earlier", "past", "before", "ago"]
	#topHeadlineKeywords = ["themes", "theme", "headlines", "top", "categories", "category", "different"]
	#noKeywords = ["no", "nah", "nope"]


	for word in range(len(FindWords)):
		if FindWords[word].lower() in specificNewsKeywords:
			specificResponse = ("Okay, give me a word or words and I will find you an article that includes it!")
			return specificResponse + SpecificNews(MsgObj)
	#if any(element in userChoice for element in specificNewsKeywords):
			#SpecificNews()

	#elif any(element in userChoice for element in olderNewsKeywords):
	#		OlderNews()

	#elif any(element in userChoice for element in topHeadlineKeywords):
	#		EveryTopHeadline()

	#elif any(element in userChoice for element in noKeywords):
	#		NewsFromBBC()

	#else:
	#		print("Sorry, I don't understand what you mean. Try rephrasing! I promise I am doing my best to understand you. :)")
	#		IntroductionToUser(MsgObj)

# End of code by [Annija Balode ID No: 9102828]		
#-----------------------------------------------------------------------------------------------------------------------------------------------#


#-------------------------------------------------------------TOP HEADLINES FUNCTION-------------------------------------------------------------#
# Beginning of code by [Annija Balode ID No: 9102828] and referenced from https://newsapi.org/docs/endpoints/top-headlines
def EveryTopHeadline():

	specificCategoryQuestion = input("Would you like to choose a specific category you would like to look at? ")
	specificCategoryQuestionList = specificCategoryQuestion.split(" ")

	# Allows the user to choose a specific category from the top headlines, if they can't think of one, then the choice is set to general as default.
	for i in range(len(specificCategoryQuestionList)):
		if specificCategoryQuestionList[i] == 'yes':
			categoryChoices = input("Your options are as follows: general; health; science; technology; business; sports; management; and entertaintment." + '\n' + "Which category would you like? ")
			amountOfArticles = input("Alright! But, before I show you the articles, how many would you like to see? ")
		else:
			print("That's okay. I will just output the general top headline from today! :)")
			categoryChoices = "general"
			amountOfArticles = "1"

	# Gets the top headlines from the UK, 'country=gb' can be changed depending on what country you want to look at.
	url = ('https://newsapi.org/v2/top-headlines?'
       'country=gb&'
	   # Can adjust the category depending on what you want specifically, there are only certain categories available: 
	   # general, health, science, technology, business, sports, management, entertainment.
	   'category='+categoryChoices+'&'
	   # Returns a set amount of news articles, default will be 20 if you do not specify and the maximum is 100, but we should not go
	   # above 10 realistically, or however many the user will request for.
		'pageSize='+amountOfArticles+'&'
       'apiKey=72742ae51f514418a9a6da52faf58be6')

	response = requests.get(url).json()

	specificArticle = response["articles"]

	theAcceptedResponseTitle = []
	theAcceptedResponseAuthor = []
	theAcceptedResponseURL = []

	for title in specificArticle:
		theAcceptedResponseTitle.append(title["title"])
	
	for author in specificArticle:
		theAcceptedResponseAuthor.append(author["author"])

	for url in specificArticle:
		theAcceptedResponseURL.append(url["url"])

	
	for i in range(len(theAcceptedResponseTitle)):
		print(i+1, str(theAcceptedResponseTitle[i]) + " by " + str(theAcceptedResponseAuthor[i]) + ": " + str(theAcceptedResponseURL[i]))

	
	
	# Fetches the data in JSON format.
	# theURL = response.json()
	# print(theURL)

# End of code by [Annija Balode ID No: 9102828] and referenced from https://newsapi.org/docs/endpoints/top-headlines
#-----------------------------------------------------------------------------------------------------------------------------------------------#


#-------------------------------------------------------------SPECIFIC NEWS FUNCTION-------------------------------------------------------------#
# A function for finding news around the world depending on specific words/key terms.
#However, this search does not allow for country-specific searches.#

# Beginning of code by [Annija Balode ID No: 9102828] and referenced from https://newsapi.org/docs/endpoints/everything
def SpecificNews(MsgObj):
#IMPORTANT NOTICE: This is only a rough 'sketch' of how the API will be laid out, as there will be no input statements like this, the bot will handle this differently.#

	chosenTopic = MsgObj.msg
	# Stores the specific word(s) that the user enters and then will use this variable to search up the relevant articles.
	#chosenTopic = input("What topic would you like to look at?" + '\n' + "Give me one word or several words and I will fetch you the most popular article right now based on that topic! ")
	
	# Stores the amount of articles that the user wants to see from the topic they chose.
	#amountOfArticles = input("Nice topic! But, before I tell you the relevant articles, how many would you like to see? ")

	# currentDate = str(datetime.now())

	url = ('https://newsapi.org/v2/everything?'
	# This is the key word that should bring up the relevant article.
       'qInTitle='+str(chosenTopic.lower())+'&'
	   'pageSize=1&'
	   # From what date it should get searched (depending how old you want the article to be)
	   'from=2019-11-01&'
	   # How to sort the articles (the most popular will show first, therefore, the most relevant and most likely to be in English)
       'sortBy=popularity&'
       'apiKey=72742ae51f514418a9a6da52faf58be6')

	# Fetches the data in JSON format.
	response = requests.get(url).json()
	specificArticle = response["articles"]

	#theAcceptedResponseTitle = []
	#theAcceptedResponseAuthor = []
	#theAcceptedResponseURL = []

	#for title in specificArticle:
	#	theAcceptedResponseTitle.append(title["title"])
	
	#for author in specificArticle:
	#	theAcceptedResponseAuthor.append(author["author"])

	#for url in specificArticle:
	#	theAcceptedResponseURL.append(url["url"])

#	for i in range(len(theAcceptedResponseTitle)):
#		print(i+1, theAcceptedResponseTitle[i] + " by " + theAcceptedResponseAuthor[i] + ": " + theAcceptedResponseURL[i])
	return str("Here's an article I found based on the word(s) you gave me: " + specificArticle)

	# Loops back to the beginning of the function if they wish to search another topic. Further improvements will be made.
	#findAnotherTopic = input("Here is what I found. Hope these are okay for you!" + '\n' + "Are there any other topics you would like to look at? ")
	#findAnotherTopicList = findAnotherTopic.split(" ")
	#for i in range(len(findAnotherTopicList)):
		#if findAnotherTopicList[i] == "yes":
			#SpecificNews()
	#	else:
	#		print("Cool. See you soon!")

# End of code by [Annija Balode ID No: 9102828] and referenced from https://newsapi.org/docs/endpoints/everything
#------------------------------------------------------------------------------------------------------------------------------------------------#


#-------------------------------------------------------------OLDER ARTICLES FUNCTION-------------------------------------------------------------#
# Function which allows the user to look at certain articles from within the past month, does not allow for a wider space of time as need to upgrade
#to a paid plan for that.#

# Beginning of code by [Annija Balode ID No: 9102828] and referenced from https://newsapi.org/docs/endpoints/everything
def OlderNews():

	howOldQuestion = input("Please make sure to write in the format YYYY-MM-DD including the dashes (I know, it's a strange format!)" + '\n' + "From what date within the last month would you like to view news? ")
	howOldQuestionStr = str(howOldQuestion)
	url = ('https://newsapi.org/v2/everything?'
       'q=apples&'
	   'pageSize=1&'
	   'from='+howOldQuestionStr+'&'
       'sortBy=popularity&'
       'apiKey=72742ae51f514418a9a6da52faf58be6')
	
	response = requests.get(url).json()

	specificArticle = response["articles"]

	theAcceptedResponseTitle = []
	theAcceptedResponseAuthor = []
	theAcceptedResponseURL = []

	for title in specificArticle:
		theAcceptedResponseTitle.append(title["title"])
	
	for author in specificArticle:
		theAcceptedResponseAuthor.append(author["author"])

	for url in specificArticle:
		theAcceptedResponseURL.append(url["url"])

	
	for i in range(len(theAcceptedResponseTitle)):
		print(i+1, theAcceptedResponseTitle[i] + " by " + theAcceptedResponseAuthor[i] + ": " + theAcceptedResponseURL[i])

# End of code by [Annija Balode ID No: 9102828] and referenced from https://newsapi.org/docs/endpoints/everything
#-------------------------------------------------------------------------------------------------------------------------------------------------#


#-------------------------------------------------------------NEWS FROM BBC SPECIFICALLY FUNCTION-------------------------------------------------------------#
#Function for fetching the top ten headlines of today from BBC News.#

# Beginning of code by [Annija Balode ID No: 9102828] and reference  from https://www.geeksforgeeks.org/fetching-top-news-using-news-api/
def NewsFromBBC(): 
	# This is the BBC News API with our own personal API key. 
	url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=72742ae51f514418a9a6da52faf58be6"

	# Fetches the data in JSON format. 
	response = requests.get(url).json()

	specificArticle = response["articles"]

	theAcceptedResponseTitle = []
	theAcceptedResponseAuthor = []
	theAcceptedResponseURL = []

	for title in specificArticle:
		theAcceptedResponseTitle.append(title["title"])
	
	for author in specificArticle:
		theAcceptedResponseAuthor.append(author["author"])

	for url in specificArticle:
		theAcceptedResponseURL.append(url["url"])

	
	for i in range(len(theAcceptedResponseTitle)):
		print(i+1, theAcceptedResponseTitle[i] + " by " + theAcceptedResponseAuthor[i] + ": " + theAcceptedResponseURL[i])

# End of code by [Annija Balode ID No: 9102828] reference from https://www.geeksforgeeks.org/fetching-top-news-using-news-api/
#-------------------------------------------------------------------------------------------------------------------------------------------------------------#


#-------------------------------------------------------------TESTING FUNCTION----------------------------------------------------------------#
#if __name__ == '__main__':
	# Calls the function, only using this to ensure that everything is getting called correctly, these function names will
	# be used to import from chatbot_script.py later on.
		# NewsFromBBC()
		# EveryTopHeadline() 
		# SpecificNews()
		# OlderNews()
		#IntroductionToUser()
#----------------------------------------------------------------------------------------------------------------------------------------------#

def FindID(obj, ID):
	if ID == "KeywordsForBranching":
		return KeywordsForBranching(obj)
	if ID == "SpecificNews":
		return SpecificNews(obj)
	#if ID == "EveryTopHeadline":
		#return EveryTopHeadline(obj)
	#if ID == "OlderNews":
	#	return OlderNews(obj)
	#if ID == "NewsFromBBC":
	#	return NewsFromBBC(obj)

