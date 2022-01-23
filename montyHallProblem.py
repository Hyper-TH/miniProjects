from numpy.random import randint

print('''
    Welcome to The Monty Hall Gameshow!
    There's a car behind one of the 3 doors.
    The rest of them have a goat.
    The Computer will play two hundred times and will see how many times it won or lost the game. 

''')

NumberOfPlays = 0
win = 0
lose = 0

while NumberOfPlays != 200:

    guess = randint(1,3)    # Computer guesses a random door
    answer = randint(1,3)   # Answer randomly generated

    # If computer gets the answer right
    if guess == answer:

        win += 1
    
    # If computer does not get answer right
    else:
    
        lose += 1
        
    NumberOfPlays += 1

print("Game is over \n\
    Computer played: {} times \n\
    Computer won: {} times \n\
    Computer lost: {} times \n"
    .format(NumberOfPlays, win, lose))

