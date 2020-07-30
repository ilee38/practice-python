#!/usr/bin/env python3

""" Using p022_names.txt, a 46K text file containing over five-thousand first names,
    begin by sorting it into alphabetical order. Then working out the
    alphabetical value for each name, multiply this value by its alphabetical position in the list
    to obtain a name score.

    For example, when the list is sorted into alphabetical order, COLIN, which is worth
    3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of
    938 × 53 = 49714.

    What is the total of all the name scores in the file?
"""

import csv

alphabet = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open('p022_names.txt', newline='') as f:
    reader = csv.reader(f)
    name_list = next(reader)
    name_list.sort()

    total = 0
    for name in name_list:
        name_score = 0
        for letter in name:
            name_score += alphabet.index(letter)
        name_score *= (name_list.index(name) + 1)
        total += name_score

    print(f'Total score {total}')
