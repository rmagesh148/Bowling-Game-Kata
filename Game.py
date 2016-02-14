# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 15:38:08 2016

@author: MaGesh

"""

class Game(object):
    def __init__(self):
        self.rollValue=[]
        self.score = []
        self.bonusForStrike = False
        self.bonusForSpare = False
        self.frameNo = 0
    def roll(self,pins):
        self.rollValue.append(pins)
    def calculateScore(self):
        self.bonusForStrike = False
        self.bonusForSpare = False
        self.frameNo += 1
        self.scoreOfFrame = 0
        if self.rollValue[0] == 10:
            self.score.append(self.rollValue[0])
            self.bonusForStrike = True
        else:            
            for rolls in range(0,2):
                self.scoreOfFrame += self.rollValue[rolls]
                if self.scoreOfFrame == 10:
                    self.bonusForSpare = True
            self.score.append(self.scoreOfFrame)
        return self.score[self.frameNo-1]
        
    def displayScore(self):
        self.checkForBonus()
        self.calculateScore()
        self.rollValue=[]
        return sum(self.score)  
        
        
    def checkForBonus(self):
        if self.bonusForStrike == True:
            #print "Strike, play next round"
            self.score[self.frameNo-1] +=  self.rollValue[0] + self.rollValue[1]
        elif self.bonusForSpare == True:
            self.score[self.frameNo-1] += self.rollValue[0]
        return self.score