from random import randint
from time import sleep
from jikanpy import Jikan

'''
This Program idea is to help people to choose an anime to watch when they aren't sure about which one to choose.

Main Objectives: 
    choose an anime from a list of options.
Side Quests:
    Implement a mood based choice;
    Implement a category based algorithm;
    Show the summary from the result obtained;
    Create a visual interface.
'''

print("\n\n~~~~Random Anime Picker~~~~\n\n")

jikan = Jikan()
animeCode = randint(0,4000)
tempDict = jikan.anime(animeCode)
title = tempDict["title"]
titleJap = tempDict["title_japanese"]

sleep(3)

print("You'll watch \"{}\" / {}\n\n".format(title, titleJap))
print("Have fun! 😁😁\n\n")