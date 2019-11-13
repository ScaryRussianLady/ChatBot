#---------------------------------------------------------- ADAPTATION INFORMATION------------------------------------------------------#


# This code has been adapted by Christian Shaw in order to make it work with the main chatbot script
#
# These adaptations include:
#
# Splitting functions into two when it requested for user input (This is so that replies can be done through discord instead of terminal)
# Altering what was returned to the main script and commenting out prints since it's in discord (Less information printed, more natural)


#----------------------------------------IMPORTING MODULES AND SETTING STATIC GLOBAL VARIABLES------------------------------------------#

import requests as req
import ast
from UserDataManagement import SaveData


#api_key: used to get access to information on TMDB
api_key = "732f0435865bde3d7f9d58852db87043"

#Reply Global ID
FilmScriptGlobal_ID = "6912"

#--------------------------------------------------------USER GREETING FUNCTION--------------------------------------------------------#

#welcomes the user to the movie data base and 
#start of block (Jamie Warnock- ID no: 9328082)
def firstUserInt(MsgObj):

    # Saves the ReplyID to the JSON database so that dialogue can be done on discord. Very important for user input.
    SaveData(FilmScriptGlobal_ID+"_FirstUserInt2", MsgObj.userID, "ReplyID")

    string = ("I can sort through genres, search for movies, display upcoming, you could also view top rated or even see what is popular/trending at the moment") + (
                "\n Please tell me what you would like to see so i can give it to you.")
    
    return string

def firstUserInt2(MsgObj):
    #stores lists of words for possible user input
    #code adapted from NewsAPI.py(created by Annija Balode)
    FnctnFinderWords = MsgObj.list

    genList = ["genre", "genres"]
    searchList = ["search", "movie", "movies", "title"]
    upCList = ["upcoming", "future", "releases"]
    popList = ["trending", "popular"]
    topList = ["top", "rated"]
    showList = ["show", "shows", "tv"]

    #cycles through the user input and if statement makes decision on what function should be called based on the words input by the user
    for x in range(len(FnctnFinderWords)):
        
        if FnctnFinderWords[x].lower() in genList:
            return genre_list(MsgObj)
            
        elif FnctnFinderWords[x].lower() in searchList:
            return movie_search(MsgObj)
           
        elif FnctnFinderWords[x].lower() in upCList:
            return upcoming()
          
        elif FnctnFinderWords[x].lower() in popList:
            return search_popular(MsgObj)
           
        elif FnctnFinderWords[x].lower() in topList:
            return top_rated(MsgObj)

        elif FnctnFinderWords[x].lower() in showList:
            return show_search(MsgObj)

#end of block (Jamie Warnock- ID no: 9328082)


#--------------------------------------------------------MOVIE SEARCH FUNCTION--------------------------------------------------------#
#start of block(Jamie Warnock- ID no: 9328082)
#refernce https://developers.themoviedb.org/3/search/search-movies
def movie_search(MsgObj):

    # Saves the ReplyID to the JSON database so that dialogue can be done on discord. Very important for user input.
    SaveData(FilmScriptGlobal_ID+"_MovieSearch2", MsgObj.userID, "ReplyID")

    #this inputs the keyword(s) into the search
    return("please type in the movie title you wish to search for: ")

def movies_search2(MsgObj):
    #SaveData(FilmScriptGlobal_ID+"_MovieSearch3", MsgObj.userID, "ReplyID")
    #takes the input from query and replaces the spaces with "%20"
    #"%20" represents a space in a link
    query = MsgObj.msg
    sQuery = query.replace(" ", "%20")

    pageNum = 1 # NO INPUT FOR TEST

    if type(pageNum) == int:
        page = pageNum
    else:
        page = 1

    #this implements the api key and sQuery so we do not have to constantly type it out
    url = "https://api.themoviedb.org/3/search/movie?sort_by=vote_average.lte=8&api_key="+api_key+"&language=en-US&query="+sQuery+"&page=1&include_adult=false"+str(page)

    #retreives information in json as a    
    response = req.get(url)
    movDict = response.json()

    # Returns a natural reply using the dictionary data to the discord main script
    return NaturalReply(movDict, False, True, None)
 
    #adapted code from stack overflow https://stackoverflow.com/questions/988228/convert-a-string-representation-of-a-dictionary-to-a-dictionary
    #for title in movDict['results']:
        #titleDict = ast.literal_eval(str(title)) - i used to use this, however i found it is not necessary
        #print('====================================')
        #print("RKAEVKE", title)

        #print('Released on: '+ title['release_date'])
        #print('Rated '+ str(title['vote_average'])+'/10 with a total of '+str(title['vote_count'])+' votes')
        # print('Overview: '+title['overview'])
        #print('BackDrop: https://image.tmdb.org/t/p/original'+str(title['poster_path']))
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
def genre_list(MsgObj):

    # Saves the ReplyID to the JSON database so that dialogue can be done on discord. Very important for user input.
    SaveData(FilmScriptGlobal_ID+"_GenreList2", MsgObj.userID, "ReplyID")

    #print("=================================================================================================================================")
    #used a dict to store possible search queries. more efficient than using an if statement
    return ("here is a list of genres available: 'Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Mystery', 'Romance', 'Science Fiction', 'TV Movie', 'Thriller', 'War', and 'Western'.\n Please select one by typing it in: ")

def genre_list2(MsgObj):
    genreDict = {"action": "28", "adventure": "12", "animation": "16", "comedy": "35", "crime": "80", "documentary": "99", "drama": "18", "family": "10751", "fantasy": "14", "history": "36", "horror": "27", "music": "10402", "mystery": "9648", "romance": "10749", "science fiction": "878", "tv movie": "10770", "thriller": "53", "war": "10752", "western": "37"}

    UserChoice = MsgObj.msg
    pageNum = 1

    if type(pageNum) == int:
        page = pageNum
    else:
        page = 1

    url = "https://api.themoviedb.org/3/discover/movie?language=en-US&api_key="+api_key+"&with_genres="+str(genreDict[UserChoice.lower()])+"&page="+str(page)


    #retreives the genre data from server to be used later
    response = req.get(url)
    genDict = response.json()

    # Returns a natural reply using the dictionary data to the discord main script
    return NaturalReply(genDict, True, False, (MsgObj.msg).lower())
   
    #adapted code from stack overflow https://stackoverflow.com/questions/988228/convert-a-string-representation-of-a-dictionary-to-a-dictionary
    #for title in genDict['results']:
        #print('====================================')
        #titleDict = ast.literal_eval(str(title))
        #print('Title: '+ title['title'])
        #print('Released on: '+ title['release_date'])
        #print('Rated '+ str(title['vote_average'])+'/10 with a total of '+str(title['vote_count'])+' votes')
        #print('Overview: '+title['overview'])
        #print('BackDrop: https://image.tmdb.org/t/p/original'+title['poster_path'])
    #end of adapted code
#end of block (Jamie Warnock- ID no: 9328082) 
#--------------------------------------------------------SEARCH TV SHOWS--------------------------------------------------------#
#start of block (Jamie Warnock - ID no: 9328082) 
def show_search(MsgObj):

    # Saves the ReplyID to the JSON database so that dialogue can be done on discord. Very important for user input.
    SaveData(FilmScriptGlobal_ID+"_MovieSearch2", MsgObj.userID, "ReplyID")

    #this inputs the keyword(s) into the search
    return ("please type in the show title you wish to search for: ")

    #takes the input from query and replaces the spaces with "%20"
    #"%20" represents a space in a link
def show_search2(MsgObj):
    query = MsgObj.msg
    sQuery = query.replace(" ", "%20")

    pageNum = 1

    if type(pageNum) == int:
        page = pageNum
    else:
        page = 1

    url = "https://api.themoviedb.org/3/search/tv?api_key=732f0435865bde3d7f9d58852db87043&language=en-US&query="+str(sQuery)+"&page="+str(page)

    response = req.get(url)
    showDict = response.json()

    # Returns a natural reply using the dictionary data to the discord main script
    return NaturalReply(showDict, False, True, None)

    #for show in showDict['results']:
    #    print('====================================')
    #    print('Title: '+ show['name'])
    #    print('First aired: '+ show['first_air_date'])
    #    print('Rated '+ str(show['vote_average'])+'/10 with a total of '+str(show['vote_count'])+' votes')
    #    print('Overview: '+show['overview'])
    #    print('BackDrop: https://image.tmdb.org/t/p/original'+str(show['backdrop_path']))
    
#end of block (Jamie Warnock- ID no: 9328082) 
#--------------------------------------------------------SEE POPULAR FUNCTION--------------------------------------------------------#
# [Start of code by Rishikesh | ID No. ?]

#reference https://developers.themoviedb.org/3/trending/get-trending
def search_popular(MsgObj):

    # Saves the ReplyID to the JSON database so that dialogue can be done on discord. Very important for user input.
    SaveData(FilmScriptGlobal_ID+"_SearchPop2", MsgObj.userID, "ReplyID")

    #input allows user to choose between what they would like to see
    return ("Now, you can either see actors(and actresses) or movies. your choice. ")

def search_popular2(MsgObj):
    choice = ""
    selection = MsgObj.msg
    selectionWord = selection.split()
    
    selectionOne = ["actors", "actor", "actress", "actresses", "people"]
    selectionTwo = ["films", "movies"]

    for i in range(len(selectionWord)):

        url = ""

        if selectionWord[i].lower() in selectionOne:
            choice = "person"
            url = ("http://api.themoviedb.org/3/trending/"+choice+"/day?api_key="+api_key)
        elif selectionWord[i].lower() in selectionTwo:
            choice = "movie"
            url = ("http://api.themoviedb.org/3/trending/"+choice+"/day?api_key="+api_key)
            break

  
    #url with the choice variable and api key placed in
    #url = ("http://api.themoviedb.org/3/trending/"+choice+"/week?api_key="+api_key)

    #extracts data from the url and makes it presentable
    response = req.get(url)
    popDict = response.json()

    # Returns a natural reply using the dictionary data to the discord main script
    return NaturalReply(popDict, True, False, "popular")

    #prints data to screen
    #print(popDict)
    #print('====================================')
     #           print('Title: '+ show['name'])
                #print('First aired: '+ show['release_date'])
                #print('Rated '+ str(show['vote_average'])+'/10 with a total of '+str(show['vote_count'])+' votes')
                #print('Overview: '+show['overview'])
      #          print('BackDrop: https://image.tmdb.org/t/p/original'+str(show['backdrop_path'])) 

# [Start of code by Rishikesh | ID No. ?]

#--------------------------------------------------------VIEW TOP RATED FUNCTION--------------------------------------------------------#

# [Start of code by Rishikesh | ID No. ?]

#reference https://developers.themoviedb.org/3/movies/get-top-rated-movies
def top_rated(MsgObj):

    # Saves the ReplyID to the JSON database so that dialogue can be done on discord. Very important for user input.
    SaveData(FilmScriptGlobal_ID+"_TopRated2", MsgObj.userID, "ReplyID")

    #allows user to input a page number
    return ("what page would you like to go to? ")

def top_rated2(MsgObj):
    pageNum = MsgObj.msg

    #used to request the informaion from the servers
    url = "http://api.themoviedb.org/3/movie/top_rated?page="+pageNum+"&language=en-US&api_key="+api_key
    #retreives the ratings data from server
    #makes it readable for user
    response = req.get(url)
    topDict = response.json()

    # Returns a natural reply using the dictionary data to the discord main script
    return NaturalReply(topDict, True, False, "top rated")


    # prints readable information to screen
    #    for show in topDict'results']:
    #    print('====================================')
    #    print('Title: '+ show['title'])
    #    print('First aired: '+ show['release_date'])
    #    print('Rated '+ str(show['vote_average'])+'/10 with a total of '+str(show['vote_count'])+' votes')
    #    print('Overview: '+show['overview'])
    #    print('BackDrop: https://image.tmdb.org/t/p/original'+str(show['poster_path']))
    #print(topDict)

# [End of code by Rishikesh | ID No. ?]


#--------------------------------------------------------UPCOMING TITLES FUNCTION--------------------------------------------------------#
# [Start of code by Rishikesh | ID No. ?]

#reference https://developers.themoviedb.org/3/movies/get-upcoming
def upcoming():
    
    #used to request the informaion from the servers
    url = "http://api.themoviedb.org/3/movie/upcoming?page=1&language=en-US&api_key="+api_key
    #retreives information of the upcoming movie titles
    #makes it readable for user
    response = req.get(url)
    upcDict = response.json()

    # Returns a natural reply using the dictionary data to the discord main script
    return NaturalReply(upcDict, True, False, "upcoming")

    # prints somewhat readable information to terminal
        #print(upcDict)
    #for show in upcDict['results']:
    #    print('====================================')
    #    print('Title: '+ show['name'])
    #    print('First aired: '+ show['release_date'])
    #    print('Rated '+ str(show['vote_average'])+'/10 with a total of '+str(show['vote_count'])+' votes')
    #    print('Overview: '+show['overview'])
    #    print('BackDrop: https://image.tmdb.org/t/p/original'+str(show['poster_path']))


# [End of code by Rishikesh | ID No. ?]

#--------------------------------------------------------REPLY SELECTION FUNCTION--------------------------------------------------------#

# [Start of Code by Christian Shaw] 

# Essentially, this function talks to the main chatbot script to identify which reply is next in line in the conversation
# Whatever the replyID is set to will determine the function used in this script.

def FindID(obj, ID):
    if ID == "FirstUserInt2":
        return firstUserInt2(obj)
    if ID == "MovieSearch2":
        return movies_search2(obj)
    if ID == "GenreList2":
        return genre_list2(obj)
    if ID == "ShowSearch2":
        return show_search2(obj)
    if ID == "SearchPop2":
        return search_popular2(obj)
    if ID == "TopRated2":
        return top_rated2(obj)

# [End of Code by Christian Shaw] 

#------------------------------------------------------RETURN RELEVANT DATA TO USER-----------------------------------------------------#

# [Start of Code by Christian Shaw]

# Essentially, this function creates and returns a string which will be the bot's reply.
# It takes arguments which determine how the reply will be structured.
def NaturalReply(Dictionary, RandBool, SearchBool, Context):
    from random import randrange

    # If the argument given to RandBool was True, then a random film will be taken from the dictionary and assigned to DictData
    if RandBool == True:
        RandNo = randrange(len(Dictionary["results"]))
        DictData = Dictionary["results"][RandNo]
    
    # Else, it will be false and will assign the first film from the dictionary to DictData
    else:
        DictData = Dictionary["results"][0]

    # If the SearchBool is True, this shows that the user searched for a film instead of wanted to be recommended one
    # the phrase list and sentence structure in the mainstring will change accordingly to this.

    # The context parameter will put in the context where needed to the sentence structure. To provide fluid, natural responses.

    # Phrases are also randomised, giving a more natural and fluid sounding reply. Less robotic.
    if SearchBool == True:
        Phrase = ["Aah, you're looking for is ", "We've found the movie that you're looking for. It's ", "Hmm, I think this is the film you're thinking about is "]
        MainString = (Phrase[randrange(len(Phrase))]+ DictData['title']+"\n You can find more info here: "+'https://www.themoviedb.org/movie/'+str(DictData['id']))
    else:
        Phrase = ["Well, here's my recommendation of a", "Hmmm, this is a good ", "I think you might like this "]
        MainString = (Phrase[randrange(len(Phrase))]+Context+" movie. It's called "+DictData["title"]+"\n You can find more info here: "+'https://www.themoviedb.org/movie/'+str(DictData['id']))

    # Returns the string that was created to that the relevant scripts can return it to the main discord bot to be sent to the user on discord.
    return MainString

# [End of Code by Christian Shaw] 

#firstUserInt()