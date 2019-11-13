import requests as req
import ast


#api_key: used to get access to information on TMDB
api_key = "732f0435865bde3d7f9d58852db87043"

#--------------------------------------------------------USER GREETING FUNCTION--------------------------------------------------------#

#welcomes the user to the movie data base and 
#start of block (Jamie Warnock- ID no: 9328082)
def firstUserInt():
    print("Hello there... and welcome to the movie directory")
    print("well... Umm there's plenty to choose from.\nlet's see. Ahh yes we can sort through genres, search for movies, display upcoming, you could also view top rated or even see what is popular/trending at the moment")
    FnctnFinder = input("please tell me what you would like to see so i can give it to you. ")


    #stores lists of words for possible user input
    #code adapted from NewsAPI.py(created by Annija Balode)
    FnctnFinderWords = FnctnFinder.split(" ")
    genList = ["genre", "genres"]
    searchList = ["search", "movie", "movies", "title"]
    upCList = ["upcoming", "future", "releases"]
    popList = ["trending", "popular"]
    topList = ["top", "rated"]
    showList = ["show", "shows", "tv"]

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
        elif FnctnFinderWords[x].lower() in showList:
            show_search()
            break
#end of block (Jamie Warnock- ID no: 9328082)


#--------------------------------------------------------MOVIE SEARCH FUNCTION--------------------------------------------------------#
#start of block(Jamie Warnock- ID no: 9328082)
#refernce https://developers.themoviedb.org/3/search/search-movies
def movie_search():

    #this inputs the keyword(s) into the search
    query = input("please type in the movie title you wish to search for: ")

    #takes the input from query and replaces the spaces with "%20"
    #"%20" represents a space in a link
    sQuery = query.replace(" ", "%20")

    pageNum = input("would you like to see a specific page number or stick to the first page? ")

    if type(pageNum) == int:
        page = pageNum
    else:
        page = 1

    #this implements the api key and sQuery so we do not have to constantly type it out
    url = "https://api.themoviedb.org/3/search/movie?sort_by=vote_average.lte=8&api_key="+api_key+"&language=en-US&query="+sQuery+"&page=1&include_adult=false"+str(page)

    #retreives information in json as a    
    response = req.get(url)
    movDict = response.json()

    #adapted code from stack overflow https://stackoverflow.com/questions/988228/convert-a-string-representation-of-a-dictionary-to-a-dictionary
    for title in movDict['results']:
        #titleDict = ast.literal_eval(str(title)) - i used to use this, however i found it is not necessary
        print('====================================')
        print('Title: '+ title['title'])
        print('Released on: '+ title['release_date'])
        print('Rated '+ str(title['vote_average'])+'/10 with a total of '+str(title['vote_count'])+' votes')
        print('Overview: '+title['overview'])
        print('BackDrop: https://image.tmdb.org/t/p/original'+str(title['poster_path']))
    #end of adapted code from stack overflow

        #--------------------Second attempt at formal printing-------------------------
        #second attempt at getting code to work. introduced for loop(still only worked for one result)
        #strppdResults = str(movDict['results'])
        #resultsDict = ast.literal_eval(strppdResults.strip('[]'))
        #for key in resultsDict:
            #print(key+': '+ str(resultsDict[key]))
        #------------------------------------------------------------------------------
    #-----------------------First iteration of formal printing-------------------------
    #before i introduced a for loop i used this (didn't work for multiple results)
    #print('Title: '+ resultsDict['title'])
    #print(resultsDict['overview'])
    #print('With a release date of '+str(resultsDict['release_date'])+', this movie has mustered up a rating of '+ str(resultsDict['vote_average'])+'/10')
    #----------------------------------------------------------------------------------

#end of block (Jamie Warnock- ID no: 9328082) 
#--------------------------------------------------------GENRE LIST SEARCH FUNCTION--------------------------------------------------------#

#start of block (Jamie Warnock - ID no: 9328082) 
#reference https://developers.themoviedb.org/3/genres/get-movie-list
def genre_list():
    print("=================================================================================================================================")
    #used a dict to store possible search queries. more efficient than using an if statement
    genreDict = {"action": "28", "adventure": "12", "animation": "16", "comedy": "35", "crime": "80", "documentary": "99", "drama": "18", "family": "10751", "fantasy": "14", "history": "36", "horror": "27", "music": "10402", "mystery": "9648", "romance": "10749", "science fiction": "878", "tv movie": "10770", "thriller": "53", "war": "10752", "western": "37"}
    UserChoice = input("here is a list of genres available: 'Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Mystery', 'Romance', 'Science Fiction', 'TV Movie', 'Thriller', 'War', and 'Western'.\n Please select one by typing it in: ")

    pageNum = input("would you like to see a specific page number or stick to the first page? ")

    if type(pageNum) == int:
        page = pageNum
    else:
        page = 1

    url = "https://api.themoviedb.org/3/discover/movie?language=en-US&api_key="+api_key+"&with_genres="+str(genreDict[UserChoice.lower()])+"&page="+str(page)


    #retreives the genre data from server to be used later
    response = req.get(url)
    genDict = response.json()

    #adapted code from stack overflow https://stackoverflow.com/questions/988228/convert-a-string-representation-of-a-dictionary-to-a-dictionary
    for title in genDict['results']:
        print('====================================')
        #titleDict = ast.literal_eval(str(title))
        print('Title: '+ title['title'])
        print('Released on: '+ title['release_date'])
        print('Rated '+ str(title['vote_average'])+'/10 with a total of '+str(title['vote_count'])+' votes')
        print('Overview: '+title['overview'])
        print('BackDrop: https://image.tmdb.org/t/p/original'+title['poster_path'])
    #end of adapted code
#end of block (Jamie Warnock- ID no: 9328082) 
#--------------------------------------------------------SEARCH TV SHOWS--------------------------------------------------------#
#start of block (Jamie Warnock - ID no: 9328082) 
def show_search():

    #this inputs the keyword(s) into the search
    query = input("please type in the movie title you wish to search for: ")

    #takes the input from query and replaces the spaces with "%20"
    #"%20" represents a space in a link
    sQuery = query.replace(" ", "%20")

    pageNum = input("would you like to see a specific page number or stick to the first page? ")

    if type(pageNum) == int:
        page = pageNum
    else:
        page = 1

    url = "https://api.themoviedb.org/3/search/tv?api_key=732f0435865bde3d7f9d58852db87043&language=en-US&query="+str(sQuery)+"&page="+str(page)

    response = req.get(url)
    showDict = response.json()

    for show in showDict['results']:
        print('====================================')
        print('Title: '+ show['name'])
        print('First aired: '+ show['first_air_date'])
        print('Rated '+ str(show['vote_average'])+'/10 with a total of '+str(show['vote_count'])+' votes')
        print('Overview: '+show['overview'])
        print('BackDrop: https://image.tmdb.org/t/p/original'+str(show['backdrop_path']))
    
#end of block (Jamie Warnock- ID no: 9328082) 
#--------------------------------------------------------SEE POPULAR FUNCTION--------------------------------------------------------#
#start of block (Rishikesh Saujani - ID no: 9798610) 
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
    #adapted code from stack overflow https://stackoverflow.com/questions/988228/convert-a-string-representation-of-a-dictionary-to-a-dictionary
        if selectionWord[i].lower() in selectionOne:
            choice = "person"
            url = ("http://api.themoviedb.org/3/trending/"+choice+"/day?api_key="+api_key)
            for show in popDict['results']:
                print('====================================')
                print('Title: '+ show['name'])
                #print('First aired: '+ show['release_date'])
                #print('Rated '+ str(show['vote_average'])+'/10 with a total of '+str(show['vote_count'])+' votes')
                #print('Overview: '+show['overview'])
                #print('BackDrop: https://image.tmdb.org/t/p/original'+str(show['backdrop_path'])) 
        elif selectionWord[i].lower() in selectionTwo:
            choice = "movie"
            url = ("http://api.themoviedb.org/3/trending/"+choice+"/day?api_key="+api_key)
            for show in popDict['results']:
                print('====================================')
                print('Title: '+ show['title'])
                print('First aired: '+ show['release_date'])
                print('Rated '+ str(show['vote_average'])+'/10 with a total of '+str(show['vote_count'])+' votes')
                print('Overview: '+show['overview'])
                print('BackDrop: https://image.tmdb.org/t/p/original'+str(show['poster_path'])) 

  
    #url with the choice variable and api key placed in
    
    #extracts data from the url and makes it presentable
    response = req.get(url)
    popDict = response.json()
    #prints data to screen
    #print(popDict)
    #print(type(popDict))

#end of block (Rishikesh Saujani - ID no: 9798610) 
#--------------------------------------------------------VIEW TOP RATED FUNCTION--------------------------------------------------------#

#start of block (Rishikesh Saujani - ID no: 9798610) 
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
    #adapted code from stack overflow https://stackoverflow.com/questions/988228/convert-a-string-representation-of-a-dictionary-to-a-dictionary
    for show in topDict['results']:
        print('====================================')
        print('Title: '+ show['title'])
        print('First aired: '+ show['release_date'])
        print('Rated '+ str(show['vote_average'])+'/10 with a total of '+str(show['vote_count'])+' votes')
        print('Overview: '+show['overview'])
        print('BackDrop: https://image.tmdb.org/t/p/original'+str(show['poster_path']))
    #print(topDict)
    #print(type(topDict))

#end of block (Rishikesh Saujani - ID no: 9798610) 
#--------------------------------------------------------UPCOMING TITLES FUNCTION--------------------------------------------------------#


#start of block (Rishikesh Saujani - ID no: 9798610) 
#reference https://developers.themoviedb.org/3/movies/get-upcoming
def upcoming():
    
    #used to request the informaion from the servers
    url = "http://api.themoviedb.org/3/movie/upcoming?page=1&language=en-US&api_key="+api_key
    #retreives information of the upcoming movie titles
    #makes it readable for user
    response = req.get(url)
    upcDict = response.json()
    # prints somewhat readable information to screen
    #print(upcDict)
    #adapted code from stack overflow https://stackoverflow.com/questions/988228/convert-a-string-representation-of-a-dictionary-to-a-dictionary
    for show in upcDict['results']:
        print('====================================')
        print('Title: '+ show['title'])
        print('First aired: '+ show['release_date'])
        print('Rated '+ str(show['vote_average'])+'/10 with a total of '+str(show['vote_count'])+' votes')
        print('Overview: '+show['overview'])
        print('BackDrop: https://image.tmdb.org/t/p/original'+str(show['poster_path']))

    #print(type(upcDict))


firstUserInt()
#end of block (Rishikesh Saujani - ID no: 9798610) 