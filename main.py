from random import randint
from jikanpy import Jikan
from timeit import timeit

print("\n\n~~~~Random Anime Picker~~~~\n\n")

def AnimeSearcher():
        
    jikan = Jikan()
    animeCode = randint(0,4000)
    tempDict = jikan.anime(animeCode)
    title = tempDict["title"]
    titleJap = tempDict["title_japanese"]

    return title, titleJap

title1, title2 = AnimeSearcher()

print("You'll watch \"{}\" / {}\n\n".format(title1, title2))
print("Have fun! 😁😁\n\n")