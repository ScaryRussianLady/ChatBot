import requests as req
import ast


#api_key: used to get access to information on TMDB
api_key = "732f0435865bde3d7f9d58852db87043"

#--------------------------------------------------------USER GREETING FUNCTION--------------------------------------------------------#

#welcomes the user to the movie data base and 
#(Jamie)
def firstUserInt():
    print("Hello there... and welcome to the movie directory")
    print("well... Umm there's plenty to choose from.\nlet's see. Ahh yes we can sort through genres, search for movies, display upcoming, you could also view top rated or even see what is popular/trending at the moment")
    FnctnFinder = input("please tell me what you would like to see so i can give it to you. ")
    FnctnFinderWords = FnctnFinder.split(" ")

    #stores lists of words for possible user input
    #code adapted from NewsAPI.py(created by Annija Balode)
    genList = ["genre", "genres"]
    searchList = ["search", "movie", "movies", "title"]
    upCList = ["upcoming", "future", "releases"]
    popList = ["trending", "popular"]
    topList = ["top", "rated"]

    #cycles through the user input and if statement makes decision on what function should be called based on the words input by the user
    for x in range(len(FnctnFinderWords)):
        
        if FnctnFinderWords[x].lower() in genList:
            genre_list()
            break
        elif FnctnFinderWords[x].lower() in searchList:
            movie_search()
            break
        elif FnctnFinderWords[x].lower() in upCList:
            upcoming()
            break
        elif FnctnFinderWords[x].lower() in popList:
            search_popular()
            break
        elif FnctnFinderWords[x].lower() in topList:
            top_rated()
            break
#end of block(Jamie)


#--------------------------------------------------------MOVIE SEARCH FUNCTION--------------------------------------------------------#
#(Jamie)
#refernce https://developers.themoviedb.org/3/search/search-movies
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

    #adapted code from stack overflow https://stackoverflow.com/questions/988228/convert-a-string-representation-of-a-dictionary-to-a-dictionary
    for title in movDict['results']:
        titleDict = ast.literal_eval(str(title))
        print('Title: '+ titleDict['title'])
        print('Released on: '+ titleDict['release_date'])
        print('Rated '+ str(titleDict['vote_average'])+'/10')
        print('Overview: '+titleDict['overview'])
        print('====================================')
    #end of adapted code from stack overflow

        #second attempt at getting code to work. introduced for loop(still only worked for one result)
        #strppdResults = str(movDict['results'])
        #resultsDict = ast.literal_eval(strppdResults.strip('[]'))
        #for key in resultsDict:
            #print(key+': '+ str(resultsDict[key]))
        #print(title)

    #before i introduced a for loop i used this (didn't work for multiple results)
    #print('Title: '+ resultsDict['title'])
    #print(resultsDict['overview'])
    #print('With a release date of '+str(resultsDict['release_date'])+', this movie has mustered up a rating of '+ str(resultsDict['vote_average'])+'/10')

#--------------------------------------------------------GENRE LIST SEARCH FUNCTION--------------------------------------------------------#

#(Jamie)
#reference https://developers.themoviedb.org/3/genres/get-movie-list
def genre_list():
    print("=================================================================================================================================")
    #used a dict to store possible search queries. more efficient than using an if statement
    genreDict = {"Action": "28", "Adventure": "12", "Animation": "16", "Comedy": "35", "Crime": "80", "Documentary": "99", "Drama": "18", "Family": "10751", "Fantasy": "14", "History": "36", "Horror": "27", "Music": "10402", "Mystery": "9648", "Romance": "10749", "Science Fiction": "878", "TV Movie": "10770", "Thriller": "53", "war": "10752", "western": "37"}
    UserChoice = input("here is a list of genres available: 'Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Mystery', 'Romance', 'Science Fiction', 'TV Movie', 'Thriller', 'War', and 'Western'. Please select one by typing it in: ")

    url = "https://api.themoviedb.org/3/discover/movie?language=en-US&api_key="+api_key+"&with_genres="+str(genreDict[UserChoice])


    #retreives the genre data from server
    #makes it readable for user
    #the "type" shows that it prtints a <dict>
    response = req.get(url)
    genDict = response.json()

    #adapted code from stack overflow https://stackoverflow.com/questions/988228/convert-a-string-representation-of-a-dictionary-to-a-dictionary
    for title in genDict['results']:
        titleDict = ast.literal_eval(str(title))
        print('Title: '+ titleDict['title'])
        print('Released on: '+ titleDict['release_date'])
        print('Rated '+ str(titleDict['vote_average'])+'/10')
        print('Overview: '+titleDict['overview'])
        print('====================================')
    #end of adapted code

    


#--------------------------------------------------------SEE POPULAR FUNCTION--------------------------------------------------------#
#(kesh)
#reference https://developers.themoviedb.org/3/trending/get-trending
def search_popular():
    print("=================================================================================================================================")
    #input allows user to choose between what they would like to see
    choice = ""
    selection = input("Now, you can either see actors(and actresses) or movies. your choice. ")
    selectionWord = selection.split()
    
    selectionOne = ["actors", "actor", "actress", "actresses", "people"]
    selectionTwo = ["films", "movies"]

    for i in range(len(selectionWord)):

        if selectionWord[i].lower() in selectionOne:
            choice = "person"
            break
        elif selectionWord[i].lower() in selectionTwo:
            choice = "movie"
            break

  
    #url with the choice variable and api key placed in
    url = ("http://api.themoviedb.org/3/trending/"+choice+"/week?api_key="+api_key)

    #extracts data from the url and makes it presentable
    response = req.get(url)
    popDict = response.json()
    #prints data to screen
    print(popDict)
    #print(type(popDict))


#--------------------------------------------------------VIEW TOP RATED FUNCTION--------------------------------------------------------#

#(kesh)
#reference https://developers.themoviedb.org/3/movies/get-top-rated-movies
def top_rated():
    print("=================================================================================================================================")
    #allows user to input a page number
    pageNum = input("what page would you like to go to? ")

    #used to request the informaion from the servers
    url = "http://api.themoviedb.org/3/movie/top_rated?page="+pageNum+"&language=en-US&api_key="+api_key
    #retreives the ratings data from server
    #makes it readable for user
    response = req.get(url)
    topDict = response.json()
    # prints readable information to screen
    print(topDict)
    #print(type(topDict))


#--------------------------------------------------------UPCOMING TITLES FUNCTION--------------------------------------------------------#


#(Kesh)
#reference https://developers.themoviedb.org/3/movies/get-upcoming
def upcoming():
    
    #used to request the informaion from the servers
    url = "http://api.themoviedb.org/3/movie/upcoming?page=1&language=en-US&api_key="+api_key
    #retreives information of the upcoming movie titles
    #makes it readable for user
    response = req.get(url)
    upcDict = response.json()
    # prints somewhat readable information to screen
    print(upcDict)
    #print(type(upcDict))


firstUserInt()