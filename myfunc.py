def main_menu():
    print('Welcome to Nighttime Parents\n'
          'You must collect all 4 items to defeat the cranky baby\n'
          'Move Commands: North, East, South, West\n'
          'To collect item in inventory: get "item name"\n'
          'Have fun and good luck parent')

def main():
    rooms = [
        {
        'parents bedroom': {'east': 'hallway',
                            'south': 'bathroom',
                            'item1': 'tub'}
        },
        {
        'kitchen': {'west': 'hallway',
                    'south': 'living room',
                    'item2': 'bunny'}
        },
        {
        'hallway': {'east': 'kitchen',
                    'item3': 'food',
                    'west': 'parents bedroom',
                    'south': 'emilia bedroom'}
        },
        {
        'living room': {'north': 'kitchen',
                        'item3': 'food',
                        'west': 'playroom',
                        'item4': 'music box'}
        },
        {
        'playroom': {'east': 'living room',
                     'item2': 'bunny',
                     'north': 'emilia bedroom',
                     'west': 'bathroom',
                     'item1': 'tub'}
        },
        {
        'bathroom': {'north': 'parents bedroom',
                     'east': 'playroom',
                     'item4': 'music box'}
        },
        {'emilia bedroom': 'check'}
    ]
    return rooms

def moveRoom(currentRoom, choice):
    room = currentRoom
    if currentRoom == 0:
        if choice == 'east':
            room += 2
        elif choice == 'south':
            room += 5
    elif currentRoom == 1:
        if choice == 'south':
            room += 2
        elif choice == 'west':
            room += 1
    elif currentRoom == 2:
        if choice == 'east':
            room -= 1
        elif choice == 'west':
            room -= 2
        elif choice == 'south':
            room += 4
    elif currentRoom == 3:
        if choice == 'north':
            room -= 2
        elif choice == 'west':
            room += 1
    elif currentRoom == 4:
        if choice == 'east':
            room -= 1
        elif choice == 'north':
            room += 2
        elif choice == 'west':
            room += 1
    elif currentRoom == 5:
        if choice == 'north':
            room -= 5
        elif choice == 'east':
            room -= 1
    elif currentRoom == 6:
        room += 0

    return room