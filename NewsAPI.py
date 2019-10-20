#This imports the requests package which allows for HTTP requests.
import requests	 
from newsapi import NewsApiClient

#IMPORTANT: this is our API key 72742ae51f514418a9a6da52faf58be6'

#Function for fetchin all of the top headline news from around UK. (can adjust this for different countries, which may be something to look at later)#
#[Annija] and referenced from https://newsapi.org/docs/endpoints/top-headlines#
def EveryTopHeadline():
	#Gets the top headlines from the UK, 'country=gb' can be changed depending on what country you want to look at.
	url = ('https://newsapi.org/v2/top-headlines?'
       'country=gb&'
	   #Can adjust the category depending on what you want specifically, there are only certain categories available: 
	   #general, health, science, technology, business, sports, management, entertainment.
	   'category=general&'
	   #Returns a set amount of news articles, default will be 20 if you do not specify and the maximum is 100, but we should not go
	   #above 10 realistically, or however many the user will request for.
		'pageSize=1&'
       'apiKey=72742ae51f514418a9a6da52faf58be6')
	response = requests.get(url)
	
	#Fetches the data in JSON format.
	theURL = response.json()
	print(theURL)

#A function for finding news around the world depending on specific words/key terms.
#However, this search does not allow for country-specific searches.#
#[Annija] and referenced from https://newsapi.org/docs/endpoints/everything#
def SpecificNews():
	url = ('https://newsapi.org/v2/everything?'
	#This is the key word that should appear in the title of the article.
       'q=Murder&'
	   'pageSize=1&'
	   #From what date it should get searched (depending how old you want the article to be)
       'from=2019-10-20&'
	   #How to sort the articles (the most popular will show first, therefore, the most relevant and most likely to be in English)
       'sortBy=popularity&'
       'apiKey=72742ae51f514418a9a6da52faf58be6')

	response = requests.get(url)

	#Fetches the data in JSON format.
	theURL = response.json()

	print(theURL)

#Function for fetching the top ten headlines of today from BBC News.#
#[Annija] and referenced from https://www.geeksforgeeks.org/fetching-top-news-using-news-api/#
def NewsFromBBC(): 
	#This is the BBC News API with our own personal API key. 
	main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=72742ae51f514418a9a6da52faf58be6"

	#Fetches the data in JSON format. 
	open_bbc_page = requests.get(main_url).json() 

	# getting all articles in a string article 
	article = open_bbc_page["articles"] 

	#This is an empty list which will contain all of the results (the articles).
	results = [] 
	
	#Adds the title of the article to the results list.
	for ar in article: 
		results.append(ar["title"]) 
	
	for i in range(len(results)): 
		#Simply prints all the trending news right now (top ten).
		print(i + 1, results[i])

if __name__ == '__main__':
	#Calls the function, only using this to ensure that everything is getting called correctly, these function names will
	#be used to import from chatbot_script.py later on.
		NewsFromBBC()
		EveryTopHeadline() 
		SpecificNews()
