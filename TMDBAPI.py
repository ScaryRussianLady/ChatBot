import requests as req



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
    #cycles through the user input and if statement makes decision on what function should be called based on the words input by the user
    for x in range(len(FnctnFinderWords)):
        
        if FnctnFinderWords[x].lower() == "genre" or FnctnFinderWords[x].lower() == "genres":
            genre_list()
            break
        elif FnctnFinderWords[x].lower() == "search" or FnctnFinderWords[x].lower() == "movie" or FnctnFinderWords[x].lower() == "movies":
            movie_search()
            break
        elif FnctnFinderWords[x].lower() == "upcoming":
            upcoming()
            break
        elif FnctnFinderWords[x].lower() == "trending" or FnctnFinderWords[x].lower() == "popular":
            search_popular()
            break
        elif FnctnFinderWords[x].lower() == "top" or FnctnFinderWords[x].lower() == "rated":
            top_rated()
            break



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
    #print(list(movDict["results"]))
    #print(type(movDict))
    print(movDict)


#--------------------------------------------------------GENRE LIST SEARCH FUNCTION--------------------------------------------------------#

#(Jamie)
#reference https://developers.themoviedb.org/3/genres/get-movie-list
def genre_list():
    print("=================================================================================================================================")
    #used a dict to store possible search queries. more efficient than using a for and an if statement
    #i know this is messy... I'm sorry
    genreDict = {"action": "28", "adventure": "12", "animation": "16", "comedy": "35", "crime": "80", "documentary": "99", "drama": "18", "family": "10751", "fantasy": "14", "history": "36", "horror": "27", "music": "10402", "mystery": "9648", "romance": "10749", "science fiction": "878", "tv movie": "10770", "thriller": "53", "war": "10752", "western": "37"}
    UserChoice = input("here is a list of genres available: 'Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 'Drama',\n'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Mystery', 'Romance', 'Science Fiction', 'TV Movie', 'Thriller', 'War', and 'Western'.\n Please let me know which genre you would like to explore: ")
    UserChoiceList = UserChoice.split(" ")
    genreChoice = ""
    #used to request the informaion from the servers
    for c in range(len(UserChoiceList)):
        for key in genreDict:
            if str(c) in key:
                genreChoice = genreDict[key]
    url = "https://api.themoviedb.org/3/discover/movie?language=en-US&api_key="+api_key+"&with_genres="+str(genreChoice)


    #retreives the genre data from server
    #makes it readable for user
    #the "type" shows that it prtints a <dict>
    response = req.get(url)
    genDict = response.json()
    print(genDict)
    #print(type(genDict))
    #print(list(genDict))
    


#--------------------------------------------------------SEE POPULAR FUNCTION--------------------------------------------------------#
#(kesh)
#reference https://developers.themoviedb.org/3/trending/get-trending
def search_popular():
    print("=================================================================================================================================")
    #input allows user to choose between what they would like to see
    choice = ""
    selection = input("Now, you can either see actors(and actresses) or movies. your choice. ")
    selectionWord = selection.split()

    for i in range(len(selectionWord)):

        if selectionWord[i].lower() == "actors" or selectionWord[i].lower() == "actor" or selectionWord[i].lower() == "actress" or selectionWord[i].lower() == "actresses" or selectionWord[i].lower() == "people":
            choice = "person"
            break
        elif selectionWord[i].lower() == "films" or selectionWord[i].lower() == "movies":
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