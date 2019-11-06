#-------------------------------------------------------------IMPORT OF MODULES-------------------------------------------------------------#
import requests
from bs4 import BeautifulSoup
import urllib.request
import time
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



#API can retrieve specific titles of books that the user requests.
#[kofi]
def booksearch():
    booktitle=input("Please type in the name of the book you would like to search")
    url = ('https://www.goodreads.com/search.xml?key=NxRD7Y051igsxA6xbjQRpQ&q=' +booktitle)
    response = requests.get(url).text
    xml = BeautifulSoup(response, 'xml')
    print ("Displaying results for  " +str(booktitle) + "... \n")
    time.sleep(2)
    for item in xml.findAll('title'):
        print (item.text)


#API can reviews of books that the user request by isbn.
#"https://www.goodreads.com/book/isbn/"+isbn+"?key=NxRD7Y051igsxA6xbjQRpQ"

#[kofi]        
def bookreview():
    isbn =input("Please type in the isbn of a book you would like to see the ratings of")
    url = ("https://www.goodreads.com/book/isbn/" +isbn+ "?key=NxRD7Y051igsxA6xbjQRpQ")
    response = requests.get(url).text
    xml = BeautifulSoup(response, 'xml')

    print ("Book reviews for isbn:" +str(isbn))

    print ("Book title:")
    for item in xml.findAll('title')[0:1]:
        print (item.text)
    print ("Author name:")
    for item in xml.findAll('name')[0:1]:
        print (item.text)
    print ("Star rating:")
    for item in xml.findAll('rating_dist'):
        print (item.text)
    print ("Average Rating:")    
    for item in xml.findAll('average_rating')[0:1]:
        print (item.text)
#[kofi]
def releasedate():
    booktitle=input("Please type in the name of the book you want the release date of")
    url = ('https://www.goodreads.com/search.xml?key=NxRD7Y051igsxA6xbjQRpQ&q=' +booktitle)
    response = requests.get(url).text
    xml = BeautifulSoup(response, 'xml')

    
    print ("Year:")
    
    for item in xml.findAll('original_publication_year')[0:1]:
        print (item.text)
    print ("Month:")
           
    for item in xml.findAll('original_publication_month')[0:1]:
        print (item.text)
#[kofi]
def authorMostpopular():
    author=input("Please type in the name of the author you would like to search to see their most popular books")
    url = ('https://www.goodreads.com/search.xml?key=NxRD7Y051igsxA6xbjQRpQ&q=' +author)
    response = requests.get(url).text
    
    print ("Displaying " +str(author) + " most popular books... \n")
    time.sleep(2)

    xml = BeautifulSoup(response, 'xml')

    print ("Author name:")
    
    for item in xml.findAll('name')[0:1]:
        print (item.text)
    print ("Book titles:")
    
    for item in xml.findAll('title'):
        print (item.text)

#[kofi]
def UserIntro():
    print ("Hello, Welcome to the Book directory. \n I have the ability to provide you with book searches, book reviews/ratings and the release dates of any current or upcoming books and most popular books that an author has.")
    UserOption  = input("What would you like to see?")
    UserOptionWords = UserOption.split(" ")
    
    searchList = ["book","books","title",]
    releasedList = ["release", "releases", "date", "upcoming"]
    reviewList = ["rating", "rated","reviews","review"]
    PopList = ["popular", "most popular",]
    for x in range(len(UserOptionWords)):
        if UserOptionWords[x].lower() in searchList:
            booksearch()
            break
        elif UserOptionWords[x].lower() in releasedList:
            releasedate()
            break
        elif UserOptionWords[x].lower() in reviewList:
            bookreview()
            break
        elif UserOptionWords[x].lower() in PopList:
            authorMostpopular()
            break
UserIntro()


