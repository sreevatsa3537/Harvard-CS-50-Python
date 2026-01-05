# # import random

# # coin=random.choice(['Heads', 'Tails'])
# # print(coin)

# #### ORRRRRRRR more sprcific way ##########

# from random import choice
# coin = choice(['Heads', 'Tails'])
# print(coin)

# import random
# num=random.randint(1, 10)
# print(num)

import random
cards=["King", "Queen", "Jack", "Ace"]
random.shuffle(cards)
print(cards)
for card in cards:
    print(card)
    
import statistics
print("the mean is ", statistics.mean([1, 2, 3, 4, 5]))

import cowsay
cowsay.cow("Hello" + " there!")
import cowsay
cowsay.trex("Hello" + " there!")