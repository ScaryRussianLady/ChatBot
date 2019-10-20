#This imports the requests package which allows for HTTP requests.
import requests	 

#Function for fetching the top ten headlines of today.#
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

	#Calls the function, only using this to ensure that everything is getting called correctly, these function names will
	#be used to import from chatbot_script.py later on.
	NewsFromBBC() 
