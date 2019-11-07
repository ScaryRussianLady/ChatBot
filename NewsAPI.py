#-------------------------------------------------------------BEGINNING OF IMPORT OF MODULES-------------------------------------------------------------#
# Beginning of code by [Annija Balode ID No: 9102828]

# This imports the requests package which allows for HTTP requests.
import requests

# The following imports the News API client specifically rather than everything from the News API that is being used in this script.
from newsapi import NewsApiClient

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

# IMPORTANT: this is our API key 72742ae51f514418a9a6da52faf58be6

# End of code by [Annija Balode ID No: 9102828]
#---------------------------------------------------------------END OF IMPORT OF MODULES-------------------------------------------------------------------#


############################################################################
class MembersCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def joined(self, ctx, *, member: discord.Member):
        """Says when a member joined."""
        await ctx.send(f'{member.display_name} joined on {member.joined_at}')

    @commands.command(name='coolbot')
    async def cool_bot(self, ctx):
        """Is the bot cool?"""
        await ctx.send('This bot is cool. :)')

    @commands.command(name='top_role', aliases=['toprole'])
    @commands.guild_only()
    async def show_toprole(self, ctx, *, member: discord.Member=None):
        """Simple command which shows the members Top Role."""

        if member is None:
            member = ctx.author

        await ctx.send(f'The top role for {member.display_name} is {member.top_role.name}')
    
    @commands.command(name='perms', aliases=['perms_for', 'permissions'])
    @commands.guild_only()
    async def check_permissions(self, ctx, *, member: discord.Member=None):
        """A simple command which checks a members Guild Permissions.
        If member is not provided, the author will be checked."""

        if not member:
            member = ctx.author

        # Here we check if the value of each permission is True.
        perms = '\n'.join(perm for perm, value in member.guild_permissions if value)

        # And to make it look nice, we wrap it in an Embed.
        embed = discord.Embed(title='Permissions for:', description=ctx.guild.name, colour=member.colour)
        embed.set_author(icon_url=member.avatar_url, name=str(member))

        # \uFEFF is a Zero-Width Space, which basically allows us to have an empty field name.
        embed.add_field(name='\uFEFF', value=perms)

        await ctx.send(content=None, embed=embed)
        # Thanks to Gio for the Command.

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(MembersCog(bot))

##############################################################################

#-------------------------------------------------------------BEGINNING OF INTRODUCTION FUNCTION-------------------------------------------------------------#
#Function for introducing the possibilities to the user, it allows for the file to know which function to bring up.#
# Beginning of code by [Annija Balode ID No: 9102828]

def IntroductionToUser():
	# await self.bot.say("News woo!")
	print("So you want to look at some news? Good choice! Unfortunately, I can't read your mind so you might have to help me out here.")
	specificFunction = input("Is there anything specific you want to look at, for example, specific topics? ")
	# specificFunctionList = specificFunction.split(" ")
	specificFunctionKeywords = ["yes", "ye", "yeah", "yep", "sure", "yeh"]


	# for i in range(len(specificFunctionList)):
		# Will later change this to accessing a list of different ways of saying 'yes' so that it can run it and check it against that (more efficient).
	if any(element in specificFunction for element in specificFunctionKeywords):
		# if specificFunctionList[i] == "yes":
		userChoice = input("Okay, what would you like to look into? There's stuff like, specific topics, older news, or even different categories (stuff like sports). ")
	else:
		print("Cool, I will just look up the top news of today from BBC! If you want to look into films or books instead, just say 'let me go back' ")
		userChoice = "no"


	# userChoiceList = userChoice.split(" ")
	specificNewsKeywords = ["specific", "definite", "exact", "individual"]
	olderNewsKeywords = ["older", "earlier", "past", "before", "ago"]
	topHeadlineKeywords = ["themes", "theme", "headlines", "top", "categories", "category", "different"]
	noKeywords = ["no", "nah", "nope"]


	if any(element in userChoice for element in specificNewsKeywords):
			SpecificNews()

	elif any(element in userChoice for element in olderNewsKeywords):
			OlderNews()

	elif any(element in userChoice for element in topHeadlineKeywords):
			EveryTopHeadline()

	elif any(element in userChoice for element in noKeywords):
			NewsFromBBC()

	else:
			print("Sorry, I don't understand what you mean. Try rephrasing! I promise I am doing my best to understand you. :)")
			IntroductionToUser()

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
def SpecificNews():
#IMPORTANT NOTICE: This is only a rough 'sketch' of how the API will be laid out, as there will be no input statements like this, the bot will handle this differently.#

	# Stores the specific word(s) that the user enters and then will use this variable to search up the relevant articles.
	chosenTopic = input("What topic would you like to look at?" + '\n' + "Give me one word or several words and I will fetch you the most popular article right now based on that topic! ")
	
	# Stores the amount of articles that the user wants to see from the topic they chose.
	amountOfArticles = input("Nice topic! But, before I tell you the relevant articles, how many would you like to see? ")

	# currentDate = str(datetime.now())

	url = ('https://newsapi.org/v2/everything?'
	# This is the key word that should bring up the relevant article.
       'qInTitle='+chosenTopic+'&'
	   'pageSize='+amountOfArticles+'&'
	   # From what date it should get searched (depending how old you want the article to be)
	   'from=2019-10-20&'
	   # How to sort the articles (the most popular will show first, therefore, the most relevant and most likely to be in English)
       'sortBy=popularity&'
       'apiKey=72742ae51f514418a9a6da52faf58be6')

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

	# Loops back to the beginning of the function if they wish to search another topic. Further improvements will be made.
	findAnotherTopic = input("Here is what I found. Hope these are okay for you!" + '\n' + "Are there any other topics you would like to look at? ")
	findAnotherTopicList = findAnotherTopic.split(" ")
	for i in range(len(findAnotherTopicList)):
		if findAnotherTopicList[i] == "yes":
			SpecificNews()
		else:
			print("Cool. See you soon!")

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
if __name__ == '__main__':
	# Calls the function, only using this to ensure that everything is getting called correctly, these function names will
	# be used to import from chatbot_script.py later on.
		# NewsFromBBC()
		# EveryTopHeadline() 
		# SpecificNews()
		# OlderNews()
		IntroductionToUser()
#----------------------------------------------------------------------------------------------------------------------------------------------#


