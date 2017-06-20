import random
#import pynder

#generates a random number and pulls that number of line from a text file
#text files first line must contain an integer that is the number of lines in the file
def choose_phrase():
    with open("phrases_generated.txt", "r") as f:
        count = int(f.readline().strip())
        for line in f:
            if not random.randrange(0, count):
                return line.strip()
            count-=1
			
#test print statement of the line. to be shifted into bot output later
#print choose_phrase()

#retrieves authentication info from text file
#line 1: facebook_id
#line 2: facebook_auth_token
#line 3: Latitude
#line 4: Longitutde
open ("account_info.txt", "r") as account_info_stream

account_info_stream

#session = pynder.Session(facebook_id, facebook_auth_token)
#session.matches() # get users you have already been matched with
#session.update_location(LAT, LON) # updates latitude and longitude for your profile
#session.profile  # your profile. If you update its attributes they will be updated on Tinder.
#users = session.nearby_users() # returns a iterable of users nearby
