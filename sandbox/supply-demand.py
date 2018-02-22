#!/usr/local/bin/python3

# A simple script to demonstrate fun things you can do with Python

import calendar
from decimal import Decimal

""" Open a file & read it """
file = open('title.txt', 'r')
title = file.read()

""" Print stuff """
print(title)
print("You have 1 year.")
print("Your goal is to either:")
print("(a) be more profitable than the competition")
print("(b) bankrupt the competition, thus creating a monopoly")
print("")
print("Each widget costs $0.50 to make. Your machinery has a capacity of")
print("making 1,000 widgets per month.")
print("You have $1,000 in capital. Good luck!")
print()

"""Ask for, and store user input"""
c1supply = float(input("How many widgets to make (max 1000)?"))
c1price = float(input("Set the price per widget for the 1st month:"))
c1capital = 1000
c2capital = 1000
c2supply = 200
c2price = 0.70

"""Here's an example of try-except syntax"""


def is_number(var):
    try:
        float(var)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(var)
        return True
    except (TypeError, ValueError):
        pass
    return False


rounds = 12
for x in range(1, rounds):
    if c1supply > 999:
        c1supply = 1000
    totalprices = c1price + c2price
    c1demand = (totalprices - c1price) / totalprices - c1price + 1.05
    c2demand = (totalprices - c2price) / totalprices - c2price + 1.05
    c1sold = c1supply * c1demand * c1demand
    c2sold = c2supply * c2demand * c2demand
    if c1sold + c2sold > 1999:
        if c1sold == c2sold:
            c1sold = 1000
            c2sold = 1000
        elif c1sold > c2sold:
            c2sold = 2000 - c1sold
        else:
            c1sold = 2000 - c2sold
    if c1sold > c1supply:
        c1sold = c1supply
    if c2sold > c2supply:
        c2sold = c2supply
    if c1demand >= 1:
        c1sold = c1supply
    if c2demand >= 1:
        c2sold = c2supply
    c1revenue = c1sold * c1price
    c2revenue = c2sold * c2price
    c1profit = c1revenue - c1supply * 0.50
    c2profit = c2revenue - c2supply * 0.50
    c1capital = c1capital + c1profit
    c2capital = c2capital + c2profit

    name = ['You ', 'They']
    supply = [str(c1supply) + " ", str(c2supply) + " "]
    price = [c1price, c2price]
    demand = [c1demand, c2demand]
    sold = [c1sold, c2sold]
    revenue = [c1revenue, c2revenue]
    profit = [c1profit, c2profit]
    capital = [c1capital, c2capital]
    rows = zip(name, supply, price, demand, sold, revenue, profit, capital)
    summary = list(rows)
    summary.sort()

    print("*** " + calendar.month_name[x].upper() + " REPORT ***")
    print("Name\t\tWidgets\tPrice\tDemand\tSold\tRevenue\tProfit\tCapital")
    for item in summary:
        print("")
        for data in item:
            if is_number(data):
                print(Decimal(data).quantize(Decimal('.01')), "\t", end='')
            else:
                print(data, "\t", end='')
    print()
    if c1capital < 0:
        print("You ran out of money!")
        break

    # This is the "AI"; Company 2 tries to beat your price
    if c1price < c2price:
        c2price = c1price - 0.01
    else:
        c2price = c1price
    if c2profit < c1profit:
        c2supply = c1supply + 25
        c2price = c1price - 0.01
    else:
        c2supply = c2supply - 100

    if c2supply < 0:
        c2supply = 100

    if x < 12:
        c1supply = float(input("How many widgets do you want to create?"))
        c1price = float(input('What price do you want to charge next month?'))

print("******** FISCAL REPORT **********")
if c1capital < 0:
    print("You lost by squandering all your money!")
elif c2capital < 0:
    print("You won by bankrupting your competition!")
elif c1capital > c2capital and c1capital > 1000:
    print("You won by being the most profitable widget creator!")
else:
    print("You lost! Your competition still has funds, and you aren't yet")
    print("turning a sufficient profit to keep your operations running.")