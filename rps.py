# Write your code here :-)
import random
print('welcome to rock,paper and scissor game')
win = 0
lose = 0
tie = 0
n = int(input('enter your target : '))
for i in range (0,n):
    print('please select your choice: ' )
    ui = input()
    if (ui != 'rock') and (ui != 'paper') and (ui != 'scissor') :
        print('invalid input')

    complist = ['rock','paper','scissor']
    ri = random.choice(complist)
    print('computer choice :' , ri)
    if ri == ui :
        print('it is a tie')
        tie = tie + 1
    elif ui == 'rock' and ri == 'paper' :
        print ('player lost')
        lose = lose + 1
    elif ui == 'rock' and ri == 'scissor':
        print ('player wins')
        win = win + 1
    elif ui == 'scissor' and ri == 'rock' :
        print ('player lost')
        lose = lose + 1
    elif ui == 'scissor' and ri == 'paper' :
        print ('player wins')
        win = win + 1
    elif ui == 'paper' and ri == 'rock' :
        print ('player wins')
        win = win + 1
    elif ui == 'paper' and ri == 'scissor' :
        print ('player lose')
        lose = lose + 1

print('player won the chance :',win)
print('player loose the chance :',lose)
print('player got tie with computer : ',tie)
if win > lose :
        print('player is in lead by ', win ,' points from the computer')
elif lose > win :
        print('computer wins and the player lost by', lose ,'points')
else:
        print('player has same points with computer')
