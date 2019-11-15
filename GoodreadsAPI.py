#-------------------------------------------------------------IMPORT OF MODULES-------------------------------------------------------------#
import requests
from bs4 import BeautifulSoup
import urllib.request
import time
from UserDataManagement import SaveData
#--------------------------------------------------------------------------------------------------------------------------------------------#

######################################################################################################################################
#This code was removed due to the fact that the other team members assigned to this API went through a different method. This was placed as a template and guidance for these team members.

#Beginning of code by [Annija Balode, ID No: 9102828] and referenced from https://rapidapi.com/raygorodskij/api/Goodreads.

#The key for this API: JnUP42tF3SjMYKotdkgrSA
#The secret necessary for this API to work: yy1EpTPtnKAUZLljIkeSZ8BJ9cc0QB70K6GeGQNGB0#
#url = "https://goodreadsraygorodskijv1.p.rapidapi.com/getAuthorBooks"

#payload = ""
#headers = {
  #  'x-rapidapi-host': "GoodreadsraygorodskijV1.p.rapidapi.com",
  #  'x-rapidapi-key': "81920e6a13msh6e78958b0ee4e66p1089ccjsn2155f80b3790",
  #  'content-type': "application/x-www-form-urlencoded"
  #  }
  
#response = requests.request("POST", url, data=payload, headers=headers)
#Link to documentation: https://rapidapi.com/raygorodskij/api/Goodreads?endpoint=apiendpoint_22bb56e0-f967-11e7-8a9f-ddc04c05c7d2getAuthorBooks

#End of code by [Annija Balode, ID No: 9102828] and referenced from https://rapidapi.com/raygorodskij/api/Goodreads.
######################################################################################################################################

#[Gerald Owusu-Manu]
#The Key:NxRD7Y051igsxA6xbjQRpQ
#The secret: u65168BEZcYv39AJsYrc8hSjkLzA4boifPdsSEYbIw

# Next ONE line by Christian Shaw | Saves a STATIC global variable for the script's global reply ID
BookScriptGlobal_ID = "2151"


#Start of block by [Gerald Owusu-Manu]

#API can retrieve specific titles of books that the user requests.
#reference https://www.goodreads.com/api/index#search.books
def booksearch(MsgObj):

    # Next ONE line by Christian Shaw | Saves the ReplyID to the JSON database so that dialogue can be done on discord. Very important for user input.
    SaveData(BookScriptGlobal_ID+"_BookSearch2", MsgObj.userID, "ReplyID")

    #booktitle=input("Please type in the name of the book you would like to search")
    #requests user to input a book name
    return "Please type in the name of the book you would like to search"

def booksearch2(MsgObj):
    booktitle = MsgObj.msg
    #The key is added to url to allow access to use the api and the name of the book inputted by the user is added
    url = ('https://www.goodreads.com/search.xml?key=NxRD7Y051igsxA6xbjQRpQ&q=' +booktitle)
    #adapted code from https://www.youtube.com/watch?v=pKz1faPVNMA
    # retreives the data from the url as text
    response = requests.get(url).text
    xml = BeautifulSoup(response, 'xml')

    # previous adapted code no longer needed as modified by [Christian Shaw at the end of the script]
   #print ("Displaying results for  " +str(booktitle) + "... \n")
    #prints only the title tag from the xml after 2 seconds
    #time.sleep(2)
    #end of previous code


    #xml function used to find the relevant tags that would output the information to the user
    Work = (xml.find("work"))

    # Next ONE line by Christian Shaw | Returns a natural reply using the dictionary data to the discord main script
    return NaturalReply(Work, "search", MsgObj)

    #for item in xml.findAll('title'):
    #end of adapted code   
    #    print (item.text)
# End of block [Gerald Owusu-Manu]



# Start of block [Gerald Owusu-Manu]
# Gets reviews of a specific book from the given isbn
# reference https://www.goodreads.com/book/isbn/ISBN?format=FORMAT     
# How to pass info into url "https://www.goodreads.com/book/isbn/"+isbn+"?key=NxRD7Y051igsxA6xbjQRpQ"  

def bookreview(MsgObj):
   
    # Next ONE line by Christian Shaw | Saves the ReplyID to the JSON database so that dialogue can be done on discord. Very important for user input.
    SaveData(BookScriptGlobal_ID+"_BookReview2", MsgObj.userID, "ReplyID")

    #isbn =input("Please type in the isbn of a book you would like to see the ratings of")
    #askes the user to input isbn of the book they want ratings for
    return "Please type in the isbn of a book you would like to see the ratings of"

def bookreview2(MsgObj):

    isbn = MsgObj.msg
    # key is added to url along with isbn inputted by user
    url = ("https://www.goodreads.com/book/isbn/" +isbn+ "?key=NxRD7Y051igsxA6xbjQRpQ")
    #adapted code from https://www.youtube.com/watch?v=pKz1faPVNMA
    #result from the url is returned as text
    response = requests.get(url).text
    xml = BeautifulSoup(response, 'xml')
    #xml function used to find the relevant tags that would output the information to the user
    Work = (xml.find("work"))
    #end of adapted code
    # Next ONE line by Christian Shaw | Returns a natural reply using the dictionary data to the discord main script
    return NaturalReply(Work, "ratings", MsgObj)

    #previous adapted code no longer in use as modified by [Christian Shaw] at the end of the script

    #organised with headings where the first result from each xml tag are displayed under
    
    #print ("Book reviews for isbn:" +str(isbn))
    # print ("Book title:")
    #for item in xml.findAll('title')[0:1]:
    #    print (item.text)
    #print ("Author name:")
    #for item in xml.findAll('name')[0:1]:
    #    print (item.text)
    #print ("Star rating:")
    #for item in xml.findAll('rating_dist'):
    #    print (item.text)
    #print ("Average Rating:")    
    #for item in xml.findAll('average_rating')[0:1]:
    #    print (item.text)
    
    #end of previous code
    
# End of block [Gerald Owusu-Manu]

# Start of block [Gerald Owusu-Manu]

#reference https://www.goodreads.com/api/index#search.books

def releasedate(MsgObj):

    # Next ONE line by Christian Shaw | Saves the ReplyID to the JSON database so that dialogue can be done on discord. Very important for user input.
    SaveData(BookScriptGlobal_ID+"_ReleaseDate2", MsgObj.userID, "ReplyID")

    #booktitle=input("Please type in the name of the book you want the release date of")
    #asks the user to input book name they want release date of
    return "Please type in the name of the book you want the release date of"

def releasedate2(MsgObj):
    #saves user input into booktitle variable
    booktitle = MsgObj.msg
    #variable is passed into url
    url = ('https://www.goodreads.com/search.xml?key=NxRD7Y051igsxA6xbjQRpQ&q=' +booktitle)
    #adapted code from https://www.youtube.com/watch?v=pKz1faPVNMA
    #result from the url is returned as text
    response = requests.get(url).text
    xml = BeautifulSoup(response, 'xml')
    #xml function used to find the relevant tags that would output the information to the user
    Work = (xml.find("work"))
    #end of adapted code

    # Next ONE line by Christian Shaw | Returns a natural reply using the dictionary data to the discord main script
    return NaturalReply(Work, "date", MsgObj)
    #previous adapted code no longer needed as [modified by christian shaw at the end of the script]
    #print ("Year:")
    
    #for item in xml.findAll('original_publication_year')[0:1]:
    #    print (item.text)
    #print ("Month:")
    #       
    #for item in xml.findAll('original_publication_month')[0:1]:
    #    print (item.text)
    # end of previous code
# end of block [Gerald Owusu-Manu]

#Start of block [Gerald Owusu-Manu]
def authorMostpopular(MsgObj):

    # Next ONE line by Christian Shaw | Saves the ReplyID to the JSON database so that dialogue can be done on discord. Very important for user input.
    SaveData(BookScriptGlobal_ID+"_AuthorMostPopular2", MsgObj.userID, "ReplyID")
    # asks user to input the name of the author
    #author=input("Please type in the name of the author you would like to search to see their most popular books")
    return "Please type in the name of the author you would like to search to see their most popular books"

def authorMostpopular2(MsgObj):
    #user input is saved into author variable
    author = MsgObj.msg
    #author variable is passed into url to be searched
    url = ('https://www.goodreads.com/search.xml?key=NxRD7Y051igsxA6xbjQRpQ&q=' +author)
    #adapted code from https://www.youtube.com/watch?v=pKz1faPVNMA
    #result from the url is returned as text
    response = requests.get(url).text
    
    # previous adapted code no longer needed as modified by [Christian Shaw at the end of the script]
    #print ("Displaying " +str(author) + " most popular books... \n")
    #results are outputted after a 2 second delay
    #time.sleep(2)
    #end of previous code


    #xml function used to find the relevant tags that would output the information to the user
    xml = BeautifulSoup(response, 'xml')

    Work = (xml.find("work"))
    #end of adapted code
    # Next ONE line by Christian Shaw | Returns a natural reply using the dictionary data to the discord main script
    return NaturalReply(Work, "search", MsgObj)

    # previous adapted code no longer needed as modified by [Christian Shaw at the end of the script]
    #headlines are created and displays the first name found in the author xml tag and outputs the most popular books found in the title tag
    #print ("Author name:")
    
    #for item in xml.findAll('name')[0:1]:
    #    print (item.text)
    #print ("Book titles:")
    
    #for item in xml.findAll('title'):
    #    print (item.text)
    #end of previous code
  #End of block [Gerald Owusu-Manu]

# Start of Block [Gerald Owusu-Manu]

def UserIntro(MsgObj):
    
    # Next ONE line by Christian Shaw | Saves the ReplyID to the JSON database so that dialogue can be done on discord. Very important for user input.
    SaveData(BookScriptGlobal_ID+"_UserIntro2", MsgObj.userID, "ReplyID")

    #print ("Hello, Welcome to the Book directory. \n I have the ability to provide you with book searches, book reviews/ratings and the release dates of any current or upcoming books and most popular books that an author has.")
    #UserOption  = input("What would you like to see?")

    # displays the features the chatbot provides to the user and asks them what they want to see
    return "I have the ability to provide you with book searches, book reviews/ratings and the release dates of any current or upcoming books and most popular books that an author has.\nWhat would you like to see?"

def UserIntro2(MsgObj):
    UserOptionWords = MsgObj.list
    #code adapted from NewsAPI.py [created by Annija Balode]
    # stores a list of keywords that the user may enter 
    searchList = ["book","books","title",]
    releasedList = ["release", "releases", "date", "upcoming"]
    reviewList = ["rating", "rated","reviews","review"]
    PopList = ["popular", "most popular",]
    #based on the keywords in the list if what the user enters corrosponds with a certain list a particular function is called
    for x in range(len(UserOptionWords)):
        if UserOptionWords[x].lower() in searchList:
            return booksearch(MsgObj)
            #break
        elif UserOptionWords[x].lower() in releasedList:
            return releasedate(MsgObj)
            #break
        elif UserOptionWords[x].lower() in reviewList:
            return bookreview(MsgObj)
            #break
        elif UserOptionWords[x].lower() in PopList:
            return authorMostpopular(MsgObj)
            #break
#end of adapted code
    #end of block [ Gerald Owusu-Manu]
# Start of block [Gerald Owusu-Manu]
#Tried to implement a while loop in previous version of code which would allow the user to keep trying each time their input could not be found in the lists of keywords i made
#def UserIntro():
    #print ("Hello, Welcome to the Book directory. \n I have the ability to provide you with book searches, book reviews/ratings and the release dates of any current or upcoming books and most popular books that an author has.")
    #UserOption  = input("What would you like to see?")
    #UserOptionWords = UserOption.split(" ")
    
    #searchList = ["book","books","title",]
    #releasedList = ["release", "releases", "date", "upcoming"]
    #reviewList = ["rating", "rated","reviews","review"]
    #PopList = ["popular", "most popular",]

   #while UserOption not in (searchList,releasedList,reviewList,PopList):
        #print ("option could not be found, please try again")
        #UserOption  = input("What would you like to see?")

    #if UserOption in (searchList,releasedList,reviewList,PopList):
        #for x in range(len(UserOptionWords)):
            #if UserOptionWords[x].lower() in searchList:
                #booksearch()
               #break
            #elif UserOptionWords[x].lower() in releasedList:
                #releasedate()
                #break
            #elif UserOptionWords[x].lower() in reviewList:
                #bookreview()
                #break
            #elif UserOptionWords[x].lower() in PopList:
                #authorMostpopular()
                #break

#UserIntro()
#could not get it to function as even when the correct keywords were entered the loop would still iterate
# End of block









#--------------------------------------------------------REPLY SELECTION FUNCTION--------------------------------------------------------#

# [Start of Code by Christian Shaw] 

# Essentially, this function talks to the main chatbot script to identify which reply is next in line in the conversation
# Whatever the replyID is set to will determine the function used in this script.

def FindID(obj, ID):
    if ID == "UserIntro2":
        return UserIntro2(obj)
    if ID == "BookSearch2":
        return booksearch2(obj)
    if ID == "BookReview2":
        return bookreview2(obj)
    if ID == "ReleaseDate2":
        return releasedate2(obj)
    if ID == "AuthorMostPopular2":
        return authorMostpopular2(obj)

# [End of Code by Christian Shaw] 

#------------------------------------------------------RETURN RELEVANT DATA TO USER-----------------------------------------------------#

# [Start of Code by Christian Shaw]

# Essentially, this function creates and returns a string which will be the bot's reply.
# It takes arguments which determine how the reply will be structured.
def NaturalReply(WorkXml, Context, MsgObj):
    from random import randrange

    # The ISBN opens a different HTML file
    if Context != "ratings":
        BookTitle = WorkXml.find("best_book").find("title").text
        BookID = WorkXml.find("best_book").find("id").text

        # Saves the recommended film to the json database for later use
        SaveData(BookTitle, MsgObj.userID, "PreviousViewedBooks")
        time.sleep(1)
        SaveData(BookTitle, MsgObj.userID, "PreviousViewedEntertainment")

    # Creates a list of months so that there is a coherent date instead of numbers
    Months = [
        "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    ReleaseDay = WorkXml.find("original_publication_day").text
    ReleaseMonth = WorkXml.find("original_publication_month").text
    ReleaseYear = WorkXml.find("original_publication_year").text

    # This creates the release month from a number to text if the month exists
    if ReleaseMonth != "":
        ReleaseMonth = Months[int(ReleaseMonth)-1]

    RatingNo = WorkXml.find("ratings_count").text

    # Depending on the context, different things are printed.
    if Context == "search":
        Phrase = ["The book you're looking for probably is ", "I found a book called ", "The book you speak of is called "]
        MainString = (Phrase[randrange(len(Phrase))]+BookTitle+"\nHere's a link to it: "+"https://www.goodreads.com/book/show/"+BookID)
    elif Context == "date":
        Phrase = [" released on ", " was published on ", " came out on "]

        MainString = BookTitle+(Phrase[randrange(len(Phrase))])+ReleaseDay+" "+ReleaseMonth+" "+ReleaseYear
    elif Context == "ratings":
        Phrase = [" was rated ", " has been rated ", " got rated "]
        MainString = ("This book has been rated "+RatingNo+" times.")
    
    # Returns the string that was created to that the relevant scripts can return it to the main discord bot to be sent to the user on discord.
    return MainString

# [End of Code by Christian Shaw] 