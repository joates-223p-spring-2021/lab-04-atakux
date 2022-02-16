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
    print("What is your {0}? My {0} is {1}".format(questions, answers))



#grabs all the new york teams
NY = [ny for nyTeams in sports_teams for ny in nyTeams if "New York" in ny]
print(NY)


#grabs all the los angeles teams
LA = [la for laTeams in sports_teams for la in laTeams if "Los Angeles" in la]
print(LA)