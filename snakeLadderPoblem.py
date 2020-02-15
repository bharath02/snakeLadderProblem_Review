"""This problem simulates a Snake and Ladder Game. The Player starts from 0 rolls the die to get a number between 1 to 6, finds a safe place, ladder or a snake keeps doing till the winning spot 100 is achieved."""
#UC1 Snake and Ladder game played with single player at start position 0
#UC2 Player rolls the die to get a number 1 to 6
#UC3  The Player then Check for a Option. they are No Play, Ladder or Snake.
#UC4 Repeat till the Player reaches the winning position 100.
#UC5position go above 100, the player stays in the same previous position till the player gets the exact number that adds to 100

import random
def snakeLader(player1):
    die=throw()
    # Random Used for Noplay, Ladder and Snake bite
    while(int(player1)<=100):
        option=random.randint(0,2)

        if(option==0):
            print("NO Play stay same Number")
            return player1
        elif(option==1):
            print("You get a ladder to play increase")
            player1+=die
            return player1
        else:
            print("Snake Bite you")
            player1 -= die
            return player1

def throw():
    n = random.randint(1, 6)
    return n
player1=0
while(snakeLader(player1)<101):
    player1=snakeLader(player1)
    if(player1<=100):
        print("Postion of a player1",player1)
