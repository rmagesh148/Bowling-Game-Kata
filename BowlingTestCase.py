# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 15:35:20 2016

@author: MaGesh
"""
#from unittest import TestCase as tc
from Game import Game
#import operator
nameObj=[]
nameList=[]
scoreList=[]
totalNoOfFrame = 2
n=int(raw_input("Please input How many members?"))
for i in range(0,n):
    names=raw_input("Enter Players name")
    nameObj.append(names)
    nameList.append(names)
    nameObj[i]=Game()
print "Let's Play!!"
for frame in range(0,totalNoOfFrame):
    print "For Frame :" + str(frame+1)
    for i in range(0,n):
        roll1=raw_input("Enter the first roll score of "+ nameList[i] + " player\t")
        roll1=int(roll1)
        if roll1 == 10:
            roll2=0
        else:
            roll2=int(raw_input("Enter the second roll for"+ nameList[i] +" player\t"))
        nameObj[i].roll(roll1)
        nameObj[i].roll(roll2)
        if frame == totalNoOfFrame -1:
            totalScore = nameObj[i].displayScore()
            print "Total Score for this Game: ",totalScore
            scoreList.append(totalScore)
        else:
            print "Cumulative Score for each rounds: ", nameObj[i].displayScore()
winnerIndices=[i for i,j in enumerate(scoreList) if j == max(scoreList)]
if len(winnerIndices) > 1:
    print "There is a tie for the players\n"
    for i in range(0,len(winnerIndices)):
        print "Winners are as follows: \n"
        print "Players Name \t" + nameList[winnerIndices[i]]
else:
    print "The winner is: \t" + nameList[winnerIndices]
