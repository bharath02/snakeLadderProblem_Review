"""This problem simulates a Snake and Ladder Game. The Player starts from 0 rolls the die to get a number between 1 to 6, finds a safe place, ladder or a snake keeps doing till the winning spot 100 is achieved."""
#UC1 Snake and Ladder game played with single player at start position 0
#UC2 Player rolls the die to get a number 1 to 6
#UC3 The Player then Check for a Option. they are No Play, Ladder or Snake.
#UC4 Repeat till the Player reaches the winning position 100.
#UC5 position go above 100, the player stays in the same previous position till the player gets the exact number that adds to 100
#UC6 Report the number of times the dice was played to win the game and also the position after every die role
#UC7 Play the game with 2 Player and report which Player won the game
import random
def snakeLader(player):
    die=throw()
    # Random Used for Noplay, Ladder and Snake bite
    option=random.randint(0,2)

    if(option==0):
        print("NO Play stay same Number")
        return player
    elif(option==1):
        print("You get a ladder to play increase")
        player+=die

        return player
    else:
        print("Snake Bite you")
        player -= die
        return player

def throw():
    n = random.randint(1, 6)
    return n
count1=0
count2=0
player=True
while(player):
    while(player):
        count1 += 1
        player1=snakeLader(player)
        player=False
    while(player==False):
        count2+=1
        player2= snakeLader(player)
        player=True
    if(player1==100):
        print("Number of time Dies roll to win : ",count)
        print("{}Position of a player1",player1)
        break
    elif(player2==100):
        print("Number of time Dies roll to win : ", count)
        print("{}Position of a player1", player2)
