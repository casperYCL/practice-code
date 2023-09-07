# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 13:38:01 2022

@author: user
"""

from student import*

joe=Student(78,85,82,90,66,80,75)
STEM_person=STEM_person(78,85,82,90,66,80,75)
ART_person=ART_person(78,85,82,90,66,80,75)
joe.calcAverage()
print('----------------------------------')
STEM_person.calcAverage()
STEM_person.printScore()
print('----------------------------------')
ART_person.calcAverage()
ART_person.printScore()







