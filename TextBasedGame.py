# Tyler Barnes
# Game Setup
from myfunc import *
from art import logo
import os


game = True
while game == True:
    #setup
    print(logo)
    print('Welcome to Nightime Parents\nYou must collect all 4 items to defeat the cranky baby\nMove Commands: north, south, east or west\nHvae fun and good luck parent\n')


    rooms = main()
    currentRoom = rooms[0]
    newRoom = 0

    print("You start in parents bedroom.\n\nHint: From here you can go 'east' or 'south'.")

    # Movement through rooms until Emilia's room
    gameMove = True
    inventory = []
    while gameMove == True:
        print(f"You currently have {inventory} in your inventory.")
        choice = input("Where would you like to go?\n").lower()
        move = moveRoom(newRoom, choice)
        currentRoom = rooms[move]
        print(f"You are in {list(currentRoom.keys())[0]}.")
        newRoom = move
        if newRoom == 6:
            gameMove = False

    # loop will check which room the user is in and gives prompt to take item

        pickUp = True
        while pickUp == True:
            if newRoom == 5:
                pick = input("You see a 'tub'. Would you like to pick it up?\n'y' or 'n'\n")
                if pick == 'y':
                    inventory.append('tub')
                    pickUp = False
                else:
                    pickUp = False
            elif newRoom == 3:
                pick = input("You see a 'bunny'. Would you like to pick it up?\n'y' or 'n'\n")
                if pick == 'y':
                    inventory.append('bunny')
                    pickUp = False
                else:
                    pickUp = False

            elif newRoom == 1:
                pick = input("You see a 'food'. Would you like to pick it up?\n'y' or 'n'\n")
                if pick == 'y':
                    inventory.append('food')
                    pickUp = False
                else:
                    pickUp = False
            elif newRoom == 4:
                pick = input("You see a 'music box'. Would you like to pick it up?\n'y' or 'n'\n")
                if pick == 'y':
                    inventory.append('music box')
                    pickUp = False
                else:
                    pickUp = False
            elif newRoom == 6:
                print("You reached the final room.")
                pickUp = False
            else:
                print('There are no items to pick up in this room.')
                pickUp = False

# final stage: items and emilia's room. True is WIN, False is Lose

    inventory = set(inventory)
    score = 0
    checkList = ['tub', 'bunny', 'music box', 'food']
    check = True
    while check == True:

        for items in inventory:
            if items in checkList:
                score += 1
        if score == 4:
            print("You collected all the items and put Emilia to bed.\nYou Win!")
            check = False
        elif score < 4:
            missing = 4 - score
            print(f"You missed {missing} items.")
            print("Emilia will not go to bed.\nNow you will deal with Emilia all night, you lose!")
            check = False

    replay = input("\nWould you like to play again?\n'y' or 'n'\n").lower()
    if replay == 'y':
        game = True
        # os.system('clear')
# clear command doesn't work on pycharm
    else:
        # os.system('clear')
        print("Goodbye")
        game = False








