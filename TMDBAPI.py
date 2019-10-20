import requests as req

#api_key: used to get access to information on TMDB
api_key = "732f0435865bde3d7f9d58852db87043"

def movie_search():

    #this inputs the keyword(s) into the search
    #"shutte island" will only return one result; easy to read for now 
    query = input("please type in the movie title you wish to search for: ")

    #takes the input from query and replaces the spaces with "%20"
    #"%20" represents a space in a link
    sQuery = query.replace(" ", "%20")

    #this implements the api key and sQuery so we do not have to constantly type it out
    url = "https://api.themoviedb.org/3/search/movie/?api_key="+api_key+"&language=en-US&query="+sQuery+"&page=1&include_adult=false"

    #retreives information from the search and prints to the screen as somewhat readable text    
    response = req.get(url)
    movDict = response.json()
    print(list(movDict["results"]))
    #print(type(movDict))
    #print("page" in movDict)

movie_search()