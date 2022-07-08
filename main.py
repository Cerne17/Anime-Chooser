from random import randint
from time import sleep
from jikanpy import Jikan

print("\n\n~~~~Random Anime Picker~~~~\n\n")

jikan = Jikan()
animeCode = randint(0,4000)
tempDict = jikan.anime(animeCode)
title = tempDict["title"]
titleJap = tempDict["title_japanese"]

sleep(3)

print("You'll watch \"{}\" / {}\n\n".format(title, titleJap))
print("Have fun! 😁😁\n\n")