import requests as req
import http.client


#api_key: used to get access to information on TMDB
api_key = "732f0435865bde3d7f9d58852db87043"


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
    print(list(movDict["results"]))
    print(type(movDict))
    print(movDict)




#(Jamie)
#reference https://developers.themoviedb.org/3/genres/get-movie-list
def genre_list():
    #used a dict to store possible search queries. more efficient than using an if statement
    genreDict = {"Action": "28", "Adventure": "12", "Animation": "16", "Comedy": "35", "Crime": "80", "Documentary": "99", "Drama": "18", "Family": "10751", "Fantasy": "14", "History": "36", "Horror": "27", "Music": "10402", "Mystery": "9648", "Romance": "10749", "Science Fiction": "878", "TV Movie": "10770", "Thriller": "53", "war": "10752", "western": "37"}
    UserChoice = input("here is a list of genres available: 'Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Mystery', 'Romance', 'Science Fiction', 'TV Movie', 'Thriller', 'War', and 'Western'. Please select one by typing it in: ")
    #used to request the informaion from the servers
    url = "https://api.themoviedb.org/3/discover/movie?language=en-US&api_key="+api_key+"&with_genres="+str(genreDict[UserChoice])

    #retreives the genre data from server
    #makes it readable for user
    #the "type" shows that it prtints a <dict>
    response = req.get(url)
    genDict = response.json()
    print(genDict)
    print(type(genDict))
    print(list(genDict))
    





#(kesh)
#reference https://developers.themoviedb.org/3/trending/get-trending
def search_popular():

    #input allows user to choose between what they would like to see
    choice = ""
    selection = int(input("would you like popular actors[1], or films[2]. please use corresponding number: "))
    if selection == 1:
        choice = "person"
    elif selection == 2:
        choice = "movie"
    else:
        print("please use a corresponding number")
    
    #url with the choice variable and api key placed in
    url = ("http://api.themoviedb.org/3/trending/"+choice+"/week?api_key="+api_key)
    #extracts data from the url and makes it presentable
    response = req.get(url)
    popDict = response.json()
    #prints data to screen
    print(popDict)
    print(type(popDict))




#(kesh)
#reference https://developers.themoviedb.org/3/movies/get-top-rated-movies
def top_rated():

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
    print(type(topDict))





#(Jamie)
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
    print(type(upcDict))


#(rish)
#prompts a user to input what they would like to do.
print("1) Movie search")
print("2) Genre search")
print("3) See popular")
print("4) Popular actors/movies")
print("5) Upcoming")
UserSelection = int(input("Please enter a corresponding number to what you would like to do: "))
#iterates through until it finds a match for the user input
if UserSelection == 1:
    movie_search()
elif UserSelection == 2:
    genre_list()
elif UserSelection == 3:
    search_popular()
elif UserSelection == 4:
    top_rated()
elif UserSelection == 5:
    upcoming()
else:
    print("please select a number")