"""This problem simulates a Snake and Ladder Game. The Player starts from 0 rolls the die to get a number between 1 to 6, finds a safe place, ladder or a snake keeps doing till the winning spot 100 is achieved."""
#UC1 Snake and Ladder game played with single player at start position 0
#UC2 Player rolls the die to get a number 1 to 6
import random
def snakeLader():
    player1=0
    die=throw()
    player1+=die
    return player1

def throw():
    n = random.randint(1, 6)
    return n
print("Postion of a player1",snakeLader())
