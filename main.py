from random import choice

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

def main():
    listOfAnimes = []

    print("~~~~Anime Picker~~~~\n\n")
    numberOfInputs = int(input("Declare the number of animes to be sorted: \n"))
    print("\n-----------------------")
    for i in range(numberOfInputs):
        listOfAnimes.append(str(input("Enter the name of the disired animes to be choosen: \n")))
    print("You'll watch {}!! Have fun 😁😁".format(choice(listOfAnimes)))

if __name__ == '__main__':
    main()