import requests 
from bs4 import BeautifulSoup
import os
import twilio
from twilio.rest import Client

#diff_signs = ('libra', 'scorpio', 'capricon', 'aries', 'saggitarius', 'aquarius', 'pisces', 'gemini', 'cancer', 'taurus', 'virgo', 'leo') 			# All the different sign variables

user_sign = str(input("What's their sign?: ")).lower()  																								#user input asking sign and making it lower case
															
#print(response.text)

source = requests.get(f"https://www.astrology.com/horoscope/daily/{user_sign}.html").text 															# f string with link that pulls data depending on which sign the user picks

soup = BeautifulSoup(source, 'lxml')

header = soup.find('div', class_='grid-md-c-s2').p.text
love = soup.find('div', class_='daily-love topic mb-2 mb-md-3').p.text
work = soup.find('div', class_='daily-work topic mb-2 mb-md-3').p.text

#print(header + "\n" + "\n" + love + "\n" + "\n" + work)

which_friend = str(input("What's the ten-digit phone number?: "))
friendship = "1" + which_friend 

# Your Account SID from twilio.com/console
account_sid = "ACa2c90771a9cb235a7dd6eaf356640837"
# Your Auth Token from twilio.com/console
auth_token  = "2630b9b75f9a392eb84ec857191b1584"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to= friendship, 
    from_="++13012501683",
    body= header + "\n" + "\n" + love )

print(message.sid)
