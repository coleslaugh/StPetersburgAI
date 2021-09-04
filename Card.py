'''
Created on Aug 25, 2021

@author: mikes
'''
from random import random


class Card(object):
    

    def __init__(self, param):
        self.CardID = param['ID']
        self.CardType = param['Card Type']
        self.CardName = param['Name']
        self.CardCost = param['Cost']
        self.MoneyEarned = param['Money']
        self.VPEarned = param['VP']
        self.CardStatus = param['Status']
        self.isUpgradable = param['IsUpgradable']
        self.UpgrageValue = param['Upgrade Value']
        self.isSpecialCard = param['IsSpecialCard']
        self.SpecialAbility = param['SpecialAbility']
        self.CardClass = param['Class']
        self.Row = 0
        self.CardDiscount = 0
        self.CardOrder = random ()