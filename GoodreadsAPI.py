#-------------------------------------------------------------IMPORT OF MODULES-------------------------------------------------------------#
import requests
#--------------------------------------------------------------------------------------------------------------------------------------------#


#[Annija] and referenced from https://rapidapi.com/raygorodskij/api/Goodreads#
#The key: JnUP42tF3SjMYKotdkgrSA#
#The secret: yy1EpTPtnKAUZLljIkeSZ8BJ9cc0QB70K6GeGQNGB0#
url = "https://goodreadsraygorodskijv1.p.rapidapi.com/getAuthorBooks"

payload = ""
headers = {
    'x-rapidapi-host': "GoodreadsraygorodskijV1.p.rapidapi.com",
    'x-rapidapi-key': "81920e6a13msh6e78958b0ee4e66p1089ccjsn2155f80b3790",
    'content-type': "application/x-www-form-urlencoded"
    }

response = requests.request("POST", url, data=payload, headers=headers)


#you get an error but i'm sure you can work through it Kaz and Bohan
#Link to documentation: https://rapidapi.com/raygorodskij/api/Goodreads?endpoint=apiendpoint_22bb56e0-f967-11e7-8a9f-ddc04c05c7d2getAuthorBooks
print(response.text)