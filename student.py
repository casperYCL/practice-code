# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 15:26:42 2022

@author: user
"""
class Student():
    def __init__(self,chinese,english,math,physics,chemistry,history,geography):
        self.name=['chinese','english','math','physics','chemistry','history','geography']
        self.scores=[chinese,english,math,physics,chemistry,history,geography]
        
    def calcAverage(self):
        avg=sum(self.scores)/len(self.scores)
        print(f"{len(self.scores)}科平均是{avg:.4}")
    def printScore(self):
        for i in range(len(self.scores)):
            print(f"{self.name[i]} {self.scores[i]}分")
    
class STEM_person(Student):
    def calcAverage(self):
        self.STEM_scores=[0,0,0,0,0,0,0]
        for i in range(7):
            self.STEM_scores[i]=self.scores[i]
        for i in range(2,5):
            self.STEM_scores[i]=self.STEM_scores[i]*1.2        
        avg=sum(self.STEM_scores)/7.6
        print(f"STEM學生{len(self.scores)}科平均是{avg:.4}")
    
class ART_person(Student):
    def calcAverage(self):
        self.ART_scores=[0,0,0,0,0,0,0]
        for i in range(7):
            self.ART_scores[i]=self.scores[i]       
        for i in range(5,7):
            self.ART_scores[i]=self.ART_scores[i]*1.2
        avg=sum(self.ART_scores)/7.4
        print(f"ART學生{len(self.scores)}科平均是{avg:.4}")
    
# joe=Student(78,85,82,90,66,80,75)
# STEM_person=STEM_person(78,85,82,90,66,80,75)
# ART_person=ART_person(78,85,82,90,66,80,75)
# joe.calcAverage()
# print('----------------------------------')
# STEM_person.calcAverage()
# STEM_person.printScore()
# print('----------------------------------')
# ART_person.calcAverage()
# ART_person.printScore()









