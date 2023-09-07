# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 16:57:30 2022

@author: user
"""

class Transportation():
    def drive(self):
        print('drive method is called')

class Car(Transportation):
    def accelerate(self):
        print('Car is accelerating')

class Airplane(Transportation):
    def fly(self):
        print('Airplane is flying')
    

mycar = Car()
myplane = Airplane()
mycar.drive()
mycar.accelerate()
myplane.drive()
myplane.fly()























