'''
Created on Aug 25, 2021

@author: mikes
'''
from random import random


class Card(object):

    #CardID = 0
    #CardType = 0
    #CardName = ""
    #CardCost = 0
    #MoneyEarned = 0
    #VPEarned = 0
    #CardStatus = 0
    #isUpgradable = 0
    #UpgrageValue = 0
    #isSpecialCard = 0
    #SpecialAbility = 0
    #CardClass = 0
    #CardOrder = 0


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
        self.CardDiscount = 0
        self.CardOrder = random ()