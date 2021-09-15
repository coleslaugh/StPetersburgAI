#----------------------------------------------------------------------------------------------------------------------------------------------------------
# St. Petersburg Machine Learning Simulation
# Card Class - Contains Card Attributes
# Author: Mike Slaugh
#----------------------------------------------------------------------------------------------------------------------------------------------------------

from random import random


class Card(object):
    

    def __init__(self, param):
        self.CardID = param['ID']
        self.CardType = param['Card Type']
        self.CardName = param['Name']
        self.CardCost = param['Cost']
        self.DiscountedCost = param['Cost']
        self.MoneyEarned = param['Money']
        self.VPEarned = param['VP']
        self.CardStatus = param['Status']
        self.isUpgradable = param['IsUpgradable']
        self.UpgradeValue = param['Upgrade Value']
        self.isSpecialCard = param['IsSpecialCard']
        self.SpecialAbility = param['SpecialAbility']
        self.CardClass = param['Class']
        self.Row = 0
        self.CardDiscount = 0
        self.CardOrder = random ()
