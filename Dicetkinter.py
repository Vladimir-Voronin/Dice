import random
from collections import Counter
from tkinter import *

class Dice():
    def __init__(self):
        self.name = self
        self.fallout = random.randint(1,6)

    
    def dictin(self):
        dictpart = (self.fallout)
        return dictpart

    @staticmethod
    def game(event):
        dice1 = Dice()
        dice2 = Dice()
        dice3 = Dice()
        dice4 = Dice()
        dice5 = Dice()
        dice6 = Dice()

        dictdicev = []

        iterat = 1
        for i in [dice1,dice2,dice3,dice4,dice5,dice6]:
            up = i.dictin()
            dictdicev.append(up)

        dictdicevsave = map(str,dictdicev)

        dictdicekeys = ['dice1','dice2','dice3','dice4','dice5','dice6']

        dictdice = dict(zip(dictdicekeys,dictdicev))


        dictdicev = map(int, dictdicev)
        coincidence = Counter(dictdicev)
        labellist = []
        iteratlist = []
        for i in [6,5,4,3,2,1]:
            iterat = coincidence.get(i)
        
            if not iterat or iterat == 1:
                iteratlist.append(1)
            elif iterat >= 2:
                if i == 1:
                    labellist.append(str(str(coincidence[i]) + ' ones'))
                if i == 2:
                    labellist.append(str(str(coincidence[i]) + ' twos'))
                if i == 3:
                    labellist.append(str(str(coincidence[i]) + ' threes'))
                if i == 4:
                    labellist.append(str(str(coincidence[i]) + ' fours'))
                if i == 5:
                    labellist.append(str(str(coincidence[i]) + ' fives'))
                if i == 6:
                    labellist.append(str(str(coincidence[i]) + ' sixes'))

                    
        if iteratlist == [1,1,1,1,1,1]:
            labellist.append('Nothing fell out')

        l['text'] = '  '.join(labellist)     
        dicelab['text'] = '    '.join(dictdicevsave)

root = Tk()

b = Button (root,                  
            text = 'Click to roll the dice',       
            width=50,height=5,     
            bg="white",fg="black")

l = Label(root, bg='black', fg='white', width=50, height=2)

dicelab = Label(root,bg='yellow', fg='black', width=50, height=2)

b.bind('<Button-1>', Dice.game)

l.pack()
b.pack()
dicelab.pack()
root.mainloop()                
        


