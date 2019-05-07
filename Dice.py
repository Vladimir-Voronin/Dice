import random
from collections import Counter


class Dice():
    def __init__(self):
        self.name = self
        self.fallout = random.randint(1,6)

    
    def dictin(self):
        dictpart = self.fallout
        return dictpart

    @staticmethod
    def main():            
        
        for i in [6,5,4,3,2,1]:
            iterat = coincidence.get(i)
            if not iterat or iterat == 1:
                pass
            else:
                if i == 1:
                    print('Dropped', coincidence[i], 'ones')
                if i == 2:
                    print('Dropped', coincidence[i], 'twos')
                if i == 3:
                    print('Dropped', coincidence[i], 'threes')
                if i == 4:
                    print('Dropped', coincidence[i], 'fours')
                if i == 5:
                    print('Dropped', coincidence[i], 'fives')
                if i == 6:
                    print('Dropped', coincidence[i], 'sixes')
                
                
        
dictdicev = []  #list of values

dice1 = Dice()
dice2 = Dice()
dice3 = Dice()
dice4 = Dice()
dice5 = Dice()
dice6 = Dice()
iterat = 1
for i in [dice1,dice2,dice3,dice4,dice5,dice6]:
    up = i.dictin()
    dictdicev.append(up)

dictdicekeys = ['dice1','dice2','dice3','dice4','dice5','dice6']

dictdice = dict(zip(dictdicekeys,dictdicev))
print(dictdice)

dictdicev = map(int, dictdicev)

coincidence = Counter(dictdicev)

Dice.main()
