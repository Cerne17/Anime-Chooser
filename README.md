This Program idea is to help people to choose an anime to watch when they aren't sure about which one to choose.

Main Objectives: 
    choose an anime from a list of options.
Side Quests:
    Implement a mood based choice;
    Implement a category based algorithm;
    Show the summary from the result obtained;
    Create a visual interface.

First Commit:
    The user inputs some animes to the programm and it chooses randomly one of those.

Second Commit:
    The user no longer has to input any anime, the programm "talks" to the Jikanpy API and gets one randomly from the MyAnimeList DB.

    Version 2 bugs:
        In this version we're finding some problems with the API behaviour. Sometimes, the API fails to send the data and the app crashes - Maybe, in the version 3 it'd be a great idea to implement a try method to avoid those errors.

Third Commit:
    The objectives for this commit is to implement some filters for the user to preset their "profile" and find something that they may like.