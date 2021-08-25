'''
Created on Aug 25, 2021

@author: mikes
'''
from _ast import Name
from telnetlib import STATUS

class Card(object):
    
    Type = ""
    Name = ""
    MoneyEarned = 0
    VPEarned = 0
    Status = 0
    SpecialCard = False
    SpecialAbility = 0
    

    def __init__(self, params):
        '''
        Constructor
        '''
        