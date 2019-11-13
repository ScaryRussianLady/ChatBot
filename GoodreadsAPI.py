#-------------------------------------------------------------IMPORT OF MODULES-------------------------------------------------------------#
import requests
from bs4 import BeautifulSoup
import urllib.request
import time
from UserDataManagement import SaveData
#--------------------------------------------------------------------------------------------------------------------------------------------#


#[Annija] and referenced from https://rapidapi.com/raygorodskij/api/Goodreads#
#The key: JnUP42tF3SjMYKotdkgrSA#
#The secret: yy1EpTPtnKAUZLljIkeSZ8BJ9cc0QB70K6GeGQNGB0#
#url = "https://goodreadsraygorodskijv1.p.rapidapi.com/getAuthorBooks"

#payload = ""
#headers = {
  #  'x-rapidapi-host': "GoodreadsraygorodskijV1.p.rapidapi.com",
  #  'x-rapidapi-key': "81920e6a13msh6e78958b0ee4e66p1089ccjsn2155f80b3790",
  #  'content-type': "application/x-www-form-urlencoded"
  #  }
#response = requests.request("POST", url, data=payload, headers=headers)
#Link to documentation: https://rapidapi.com/raygorodskij/api/Goodreads?endpoint=apiendpoint_22bb56e0-f967-11e7-8a9f-ddc04c05c7d2getAuthorBooks

#[kofi]
#The Key:NxRD7Y051igsxA6xbjQRpQ
#The secret: u65168BEZcYv39AJsYrc8hSjkLzA4boifPdsSEYbIw

# Next ONE line by Christian Shaw | Saves a STATIC global variable for the script's global reply ID
BookScriptGlobal_ID = "2151"


#API can retrieve specific titles of books that the user requests.
#[kofi]
def booksearch(MsgObj):

    # Next ONE line by Christian Shaw | Saves the ReplyID to the JSON database so that dialogue can be done on discord. Very important for user input.
    SaveData(BookScriptGlobal_ID+"_BookSearch2", MsgObj.userID, "ReplyID")

    #booktitle=input("Please type in the name of the book you would like to search")
    return "Please type in the name of the book you would like to search"

def booksearch2(MsgObj):
    booktitle = MsgObj.msg
    url = ('https://www.goodreads.com/search.xml?key=NxRD7Y051igsxA6xbjQRpQ&q=' +booktitle)
    response = requests.get(url).text
    xml = BeautifulSoup(response, 'xml')
   #print ("Displaying results for  " +str(booktitle) + "... \n")
    #time.sleep(2)
    Work = (xml.find("work"))

    # Next ONE line by Christian Shaw | Returns a natural reply using the dictionary data to the discord main script
    return NaturalReply(Work, "search", MsgObj)

    #for item in xml.findAll('title'):
    #    print (item.text)


#API can reviews of books that the user request by isbn.
#"https://www.goodreads.com/book/isbn/"+isbn+"?key=NxRD7Y051igsxA6xbjQRpQ"

#[kofi]        
def bookreview(MsgObj):
   
    # Next ONE line by Christian Shaw | Saves the ReplyID to the JSON database so that dialogue can be done on discord. Very important for user input.
    SaveData(BookScriptGlobal_ID+"_BookReview2", MsgObj.userID, "ReplyID")

    #isbn =input("Please type in the isbn of a book you would like to see the ratings of")
    return "Please type in the isbn of a book you would like to see the ratings of"

def bookreview2(MsgObj):

    isbn = MsgObj.msg

    url = ("https://www.goodreads.com/book/isbn/" +isbn+ "?key=NxRD7Y051igsxA6xbjQRpQ")
    response = requests.get(url).text
    xml = BeautifulSoup(response, 'xml')

    Work = (xml.find("work"))

    # Next ONE line by Christian Shaw | Returns a natural reply using the dictionary data to the discord main script
    return NaturalReply(Work, "ratings", MsgObj)

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

#[kofi]
def releasedate(MsgObj):

    # Next ONE line by Christian Shaw | Saves the ReplyID to the JSON database so that dialogue can be done on discord. Very important for user input.
    SaveData(BookScriptGlobal_ID+"_ReleaseDate2", MsgObj.userID, "ReplyID")

    #booktitle=input("Please type in the name of the book you want the release date of")
    return "Please type in the name of the book you want the release date of"

def releasedate2(MsgObj):

    booktitle = MsgObj.msg

    url = ('https://www.goodreads.com/search.xml?key=NxRD7Y051igsxA6xbjQRpQ&q=' +booktitle)
    response = requests.get(url).text
    xml = BeautifulSoup(response, 'xml')

    Work = (xml.find("work"))

    # Next ONE line by Christian Shaw | Returns a natural reply using the dictionary data to the discord main script
    return NaturalReply(Work, "date", MsgObj)
    
    #print ("Year:")
    
    #for item in xml.findAll('original_publication_year')[0:1]:
    #    print (item.text)
    #print ("Month:")
    #       
    #for item in xml.findAll('original_publication_month')[0:1]:
    #    print (item.text)
#[kofi]

def authorMostpopular(MsgObj):

    # Next ONE line by Christian Shaw | Saves the ReplyID to the JSON database so that dialogue can be done on discord. Very important for user input.
    SaveData(BookScriptGlobal_ID+"_AuthorMostPopular2", MsgObj.userID, "ReplyID")

    #author=input("Please type in the name of the author you would like to search to see their most popular books")
    return "Please type in the name of the author you would like to search to see their most popular books"

def authorMostpopular2(MsgObj):
    author = MsgObj.msg
    url = ('https://www.goodreads.com/search.xml?key=NxRD7Y051igsxA6xbjQRpQ&q=' +author)
    response = requests.get(url).text
    
    #print ("Displaying " +str(author) + " most popular books... \n")
    #time.sleep(2)

    xml = BeautifulSoup(response, 'xml')

    Work = (xml.find("work"))

    # Next ONE line by Christian Shaw | Returns a natural reply using the dictionary data to the discord main script
    return NaturalReply(Work, "search", MsgObj)

    #print ("Author name:")
    
    #for item in xml.findAll('name')[0:1]:
    #    print (item.text)
    #print ("Book titles:")
    
    #for item in xml.findAll('title'):
    #    print (item.text)

#[kofi]
def UserIntro(MsgObj):
    
    # Next ONE line by Christian Shaw | Saves the ReplyID to the JSON database so that dialogue can be done on discord. Very important for user input.
    SaveData(BookScriptGlobal_ID+"_UserIntro2", MsgObj.userID, "ReplyID")

    #print ("Hello, Welcome to the Book directory. \n I have the ability to provide you with book searches, book reviews/ratings and the release dates of any current or upcoming books and most popular books that an author has.")
    #UserOption  = input("What would you like to see?")

    return "I have the ability to provide you with book searches, book reviews/ratings and the release dates of any current or upcoming books and most popular books that an author has.\nWhat would you like to see?"

def UserIntro2(MsgObj):
    UserOptionWords = MsgObj.list
    
    searchList = ["book","books","title",]
    releasedList = ["release", "releases", "date", "upcoming"]
    reviewList = ["rating", "rated","reviews","review"]
    PopList = ["popular", "most popular",]
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
#UserIntro()

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

    if Context != "ratings":
        BookTitle = WorkXml.find("best_book").find("title").text
        BookID = WorkXml.find("best_book").find("id").text

    Months = [
        "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    ReleaseDay = WorkXml.find("original_publication_day").text
    ReleaseMonth = WorkXml.find("original_publication_month").text
    ReleaseYear = WorkXml.find("original_publication_year").text

    if ReleaseMonth != "":
        ReleaseMonth = Months[int(ReleaseMonth)-1]

    RatingNo = WorkXml.find("ratings_count").text


    if Context == "search":
        Phrase = ["The book you're looking for probably is ", "I found a book called ", "The book you speak of is called "]
        MainString = (Phrase[randrange(len(Phrase))]+BookTitle+"\nHere's a link to it: "+"https://www.goodreads.com/book/show/"+BookID)
    elif Context == "date":
        Phrase = [" released on ", " was published on ", " came out on "]

        MainString = BookTitle+(Phrase[randrange(len(Phrase))])+ReleaseDay+" "+ReleaseMonth+" "+ReleaseYear
    elif Context == "ratings":
        Phrase = [" was rated ", " has been rated ", " got rated "]
        MainString = ("This book has been rated "+RatingNo+" times.")

    return MainString

    
    # Returns the string that was created to that the relevant scripts can return it to the main discord bot to be sent to the user on discord.
    #return MainString

# [End of Code by Christian Shaw] 
