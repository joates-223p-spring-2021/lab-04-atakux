# -*- coding: utf-8 -*-
"""

Angela DeLeo
CPSC 223P-01
Mon Jan 14, 2022
atakux707@csu.fullerton.edu

"""

#import lists file
import lists


sports_teams = [lists.football_teams, lists.baseball_teams, lists.basketball_teams]


#swaps out hot dogs for bratwurst in menu using listcomp
menu = [food if food != "hot dogs" else "bratwurst" for food in lists.school_lunches]
print(menu)


#prints the questions and answers formatted into a sentence
for questions, answers in zip(lists.questions, lists.answers):
    print("What is your {0}? My {0} is {1}.".format(questions, answers))


#grab all the LA teams
losAngeles = "Los Angeles"
LA = []
for i in sports_teams[0]:
    if losAngeles in i:
        LA.append(i)
for i in sports_teams[1]:
    if losAngeles in i:
        LA.append(i)
for i in sports_teams[2]:
    if losAngeles in i:
        LA.append(i)
print(LA)


#grab all the NY teams
newYork = "New York"
NY = []
for i in sports_teams[0]:
    if newYork in i:
        NY.append(i)
for i in sports_teams[1]:
    if newYork in i:
        NY.append(i)
for i in sports_teams[2]:
    if newYork in i:
        NY.append(i)
print(NY)