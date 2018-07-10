#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import random

strategies = ["Tit For Tat", "Random", "Greedy", "Generous"]
choices = ["compete", "collaborate"]


def titForTat(last="unknown"):
    # Strategy: Do unto others as they hath done to you.
    if last == "compete" or last == "collaborate":
        return last
    else:
        return "collaborate"


def playRandom():
    # Strategy: be unpredictable
    return random.choice(choices)


def greedy():
    # Strategy: always compete
    return "compete"


def generous():
    # Strategy: always collaborate
    return "collaborate"


def chooseStrategy():
    # Helper function for the computer to choose a strategy.
    return random.choice(strategies)


print('Welcome to Game Theory!')
print('Your goal: score more than 5,000 points. You have 1,000 rounds.')
print('Rules: each round, choose whether to "compete" or "collaborate"')
print('A) If you compete & your opponent competes, neither of you win')
print('B) If you compete & your opponent collaborates, you get 10, your opponent 0')
print('C) If you collaborate & your opponent collaborates, you both get 5')
print('D) If you collaborate & your opponent competes, you get 0 and your opponent gets 10')
print('Your available strategies are: Random, Greedy, Generous, & Tit For Tat')
print('At the end, you will learn what strategy your opponent chose.')
player = input('What is your name? ')
strategy = input('What is your strategy? ')
rounds = 1000
p1score = 0
p2score = 0
p1competes = 0
p1collaborates = 0
p1last = "unknown"
p2last = "unknown"
p2strategy = chooseStrategy()

for x in range(0, rounds):
    if strategy == "Tit For Tat":
        p1choice = titForTat(p2last)
    elif strategy == "Generous":
        p1choice = generous()
    elif strategy == "Greedy":
        p1choice = greedy()
    else:
        p1choice = playRandom()

    if p2strategy == "Tit For Tat":
        p2choice = titForTat(p1last)
    elif p2strategy == "Generous":
        p2choice = generous()
    elif p2strategy == "Greedy":
        p2choice = greedy()
    else:
        p2choice = playRandom()
    p2last = p2choice
    p1last = p1choice
    print('Round', x+1, ": Player 1 ->", p1choice, " Player 2 ->", p2choice)
    if p1choice == "compete" and p2choice == "compete":
        # print('Player 1 wins 0')
        p1competes = p1competes + 1
    elif p1choice == "compete" and p2choice == "collaborate":
        # print('Player 1 wins 10')
        p1score = p1score + 10
        p1competes = p1competes + 1
    elif p1choice == "collaborate" and p2choice == "collaborate":
        # print('Player 1 wins 5')
        p1score = p1score + 5
        p2score = p2score + 5
        p1collaborates = p1collaborates + 1
    elif p1choice == "collaborate" and p2choice == "compete":
        # print ('Player 2 wins 10')
        p2score = p2score + 10
        p1collaborates = p1collaborates + 1

print(player, "final score:", p1score)
print("Oppnent final score:", p2score)
print("Combined score:", p1score + p2score)
print(player, "competition/collaboration ratio:", int(p1competes / rounds * 100), ":", int(p1collaborates / rounds * 100))
print("Your opponent's strategy was:", p2strategy)
if p1score >= 5000:
    print(player, "wins!")
else:
    print(player, "did not meet the goal.")
