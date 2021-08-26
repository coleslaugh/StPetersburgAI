#--------------------------------------------------------------------------
# Define Global Items for the Game1
#--------------------------------------------------------------------------

#--------------------------------------------------------------------------
# Card Types
#--------------------------------------------------------------------------
WORKER_CARD_TYPE = 0
BUILDING_CARD_TYPE = 1
ARISTOCRAT_CARD_TYPE = 2
TRADING_CARD_TYPE = 3

#--------------------------------------------------------------------------
# Card IDs
#--------------------------------------------------------------------------

# Worker Cards
LUMBERJACK_ID = 0
GOLD_MINER_ID = 1
SHEPHERD_ID = 2
FUR_TRAPPER_ID = 3
SHIP_BUILDER_ID = 4
CZAR_PETER_ID = 5

# Building Cards
MARKET_ID = 6
CUSTOMS_HOUSE_ID = 7
FIREHOUSE_ID = 8
HOSPITAL_ID = 9
LIBRARY_ID = 10
THEATER_ID = 11
ACADEMY_ID = 12
POTJOMKINS_VILLAGE_ID = 13
PUB_ID = 14
WAREHOUSE_ID = 15
OBSERVATORY_ID = 16

# Aristocrat Cards
AUTHOR_ID = 17
ADMINISTRATOR_ID = 18
WAREHOUSE_MANAGER_ID = 19
SECRETARY_ID = 20
CONTROLLER_ID = 21
JUDGE_ID = 22
MISTRESS_OF_CEREMONIES_ID = 23

#--------------------------------------------------------------------------
# Worker Card Class
#--------------------------------------------------------------------------
CLASS_NONE = 0
CLASS_WOOD = 1
CLASS_GOLD = 2
CLASS_WOOL = 3
CLASS_FUR = 4
CLASS_SHIP = 5
CLASS_ALL = 6


#--------------------------------------------------------------------------
# Card Cost
#-------------------------------------------------------------------------- 

#Worker Cards
LUMBERJACK_COST = 3
GOLD_MINER_COST = 4
SHEPHERD_COST = 5
FUR_TRAPPER_COST = 6
SHIP_BUILDER_COST = 7 
CZAR_PETER_COST = 8

#Building Cards
MARKET_COST = 5
CUSTOMS_HOUSE_COST = 8
FIREHOUSE_COST = 11
HOSPITAL_COST = 14
LIBRARY_COST = 17
THEATER_COST = 20
ACADEMY_COST = 23
POTJOMKINS_VILLAGE_COST = 2
PUB_COST = 1
WAREHOUSE_COST = 2
OBSERVATORY_COST = 6

# Aristocrat Cards
AUTHOR_COST = 4
ADMINISTRATOR_COST = 7
WAREHOUSE_MANAGER_COST = 10
SECRETARY_COST = 12
CONTROLLER_COST = 14
JUDGE_COST = 16
MISTRESS_OF_CEREMONIES_COST = 18

#--------------------------------------------------------------------------
# Card Money Earned
#-------------------------------------------------------------------------- 
LUMBERJACK_MONEY = 3
GOLD_MINER_MONEY = 3
SHEPHERD_MONEY = 3
FUR_TRAPPER_MONEY = 3
SHIP_BUILDER_MONEY = 3 
CZAR_PETER_MONEY = 3

#Building Cards
MARKET_MONEY = 0
CUSTOMS_HOUSE_MONEY = 0
FIREHOUSE_MONEY = 0
HOSPITAL_MONEY = 0
LIBRARY_MONEY = 0
THEATER_MONEY = 0
ACADEMY_MONEY = 0
POTJOMKINS_VILLAGE_MONEY = 0
PUB_MONEY = 0
WAREHOUSE_MONEY = 0
OBSERVATORY_MONEY = 0

# Aristocrat Cards
AUTHOR_MONEY = 1
ADMINISTRATOR_MONEY = 2
WAREHOUSE_MANAGER_MONEY = 3
SECRETARY_MONEY = 4
CONTROLLER_MONEY = 4
JUDGE_MONEY = 5
MISTRESS_OF_CEREMONIES_MONEY = 6

#--------------------------------------------------------------------------
# Victory Points Earned
#-------------------------------------------------------------------------- 
LUMBERJACK_VP = 0
GOLD_MINER_VP = 0
SHEPHERD_VP = 0
FUR_TRAPPER_VP = 0
SHIP_BUILDER_VP = 0 
CZAR_PETER_VP = 0

#Building Cards
MARKET_VP = 1
CUSTOMS_HOUSE_VP = 2
FIREHOUSE_VP = 3
HOSPITAL_VP = 4
LIBRARY_VP = 5
THEATER_VP = 6
ACADEMY_VP = 7
POTJOMKINS_VILLAGE_VP = 0
PUB_VP = 0
WAREHOUSE_VP = 0
OBSERVATORY_VP = 1

# Aristocrat Cards
AUTHOR_VP = 0
ADMINISTRATOR_VP = 0
WAREHOUSE_MANAGER_VP = 0
SECRETARY_VP = 0
CONTROLLER_VP = 1
JUDGE_VP = 2
MISTRESS_OF_CEREMONIES_VP = 3



#--------------------------------------------------------------------------
# Card Status
#--------------------------------------------------------------------------
PLAYER_ACTIVE_CARD = 0
PLAYER_HELD_CARD = 1
BOARD_UPPER_ROW = 0
BOARD_LOWER_ROW = -1

#--------------------------------------------------------------------------
# Special Card
#--------------------------------------------------------------------------

IS_NOT_SPECIAL = 0
IS_SPECIAL = 1

#--------------------------------------------------------------------------
# Upgrade Card
#--------------------------------------------------------------------------

IS_NOT_UPGRADABLE = 0
IS_UPGRADABLE = 1

#--------------------------------------------------------------------------
# Special Ability
#--------------------------------------------------------------------------
NO_SPECIAL_ABILITY = 0
TAX_MAN_ABILITY = 1
POTJOMKINS_VILLIAGE_ABILITY = 2
WAREHOUSE_ABILITY = 3
PUB_ABILITY = 4
CZAR_PETER_ABILITY = 5
OBSERVATORY_ABILITY = 6
MARIINSKIJ_THEATER_ABILITY = 7

POTJOMKINS_VILLAGE_UPGRADE_VALUE = 6

#--------------------------------------------------------------------------
# Cards
#--------------------------------------------------------------------------

LUMBERJACK_CARD =               {'ID': LUMBERJACK_ID,               'Card Type': WORKER_CARD_TYPE,      'Name': 'Lumber Jack',              'Cost': LUMBERJACK_COST,                'Money': LUMBERJACK_MONEY,              'VP': LUMBERJACK_VP,                'Status': PLAYER_ACTIVE_CARD,   'IsUpgradable': IS_UPGRADABLE,  'Upgrade Value': LUMBERJACK_COST,                   'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_WOOD}
GOLD_MINER_CARD =               {'ID': GOLD_MINER_ID,               'Card Type': WORKER_CARD_TYPE,      'Name': "Gold Miner",               'Cost': GOLD_MINER_COST,                'Money': GOLD_MINER_MONEY,              'VP': GOLD_MINER_VP,                'Status': PLAYER_ACTIVE_CARD,   'IsUpgradable': IS_UPGRADABLE,  'Upgrade Value': GOLD_MINER_COST,                   'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_GOLD}
SHEPHERD_CARD =                 {'ID': SHEPHERD_ID,                 'Card Type': WORKER_CARD_TYPE,      'Name': "Shepherd",                 'Cost': SHEPHERD_COST,                  'Money': SHEPHERD_MONEY,                'VP': SHEPHERD_VP,                  'Status': PLAYER_ACTIVE_CARD,   'IsUpgradable': IS_UPGRADABLE,  'Upgrade Value': SHEPHERD_COST,                     'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_WOOL}
FUR_TRAPPER_CARD =              {'ID': FUR_TRAPPER_ID,              'Card Type': WORKER_CARD_TYPE,      'Name': "Fur Trapper",              'Cost': FUR_TRAPPER_COST,               'Money': FUR_TRAPPER_MONEY,             'VP': FUR_TRAPPER_VP,               'Status': PLAYER_ACTIVE_CARD,   'IsUpgradable': IS_UPGRADABLE,  'Upgrade Value': FUR_TRAPPER_COST,                  'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_FUR}
SHIP_BUILDER_CARD =             {'ID': SHIP_BUILDER_ID,             'Card Type': WORKER_CARD_TYPE,      'Name': "Ship Builder",             'Cost': SHIP_BUILDER_COST,              'Money': SHIP_BUILDER_MONEY,            'VP': SHIP_BUILDER_VP,              'Status': PLAYER_ACTIVE_CARD,   'IsUpgradable': IS_UPGRADABLE,  'Upgrade Value': SHIP_BUILDER_COST,                 'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_SHIP}
CZAR_PETER_CARD =               {'ID': CZAR_PETER_ID,               'Card Type': WORKER_CARD_TYPE,      'Name': "Czar Peter",               'Cost': CZAR_PETER_COST,                'Money': CZAR_PETER_MONEY,              'VP': CZAR_PETER_VP,                'Status': PLAYER_ACTIVE_CARD,   'IsUpgradable': IS_UPGRADABLE,  'Upgrade Value': CZAR_PETER_COST,                   'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_ALL}
MARKET_CARD =                   {'ID': MARKET_ID,                   'Card Type': BUILDING_CARD_TYPE,    'Name': "Market",                   'Cost': MARKET_COST,                    'Money': MARKET_MONEY,                  'VP': MARKET_VP,                    'Status': PLAYER_ACTIVE_CARD,   'IsUpgradable': IS_UPGRADABLE,  'Upgrade Value': MARKET_COST,                       'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_NONE}
CUSTOMS_HOUSE_CARD =            {'ID': CUSTOMS_HOUSE_ID,            'Card Type': BUILDING_CARD_TYPE,    'Name': "Customs House",            'Cost': CUSTOMS_HOUSE_COST,             'Money': CUSTOMS_HOUSE_MONEY,           'VP': CUSTOMS_HOUSE_VP,             'Status': PLAYER_ACTIVE_CARD,   'IsUpgradable': IS_UPGRADABLE,  'Upgrade Value': CUSTOMS_HOUSE_COST,                'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_NONE}
FIREHOUSE_CARD =                {'ID': FIREHOUSE_ID,                'Card Type': BUILDING_CARD_TYPE,    'Name': "Firehouse",                'Cost': FIREHOUSE_COST,                 'Money': FIREHOUSE_MONEY,               'VP': FIREHOUSE_VP,                 'Status': PLAYER_ACTIVE_CARD,   'IsUpgradable': IS_UPGRADABLE,  'Upgrade Value': FIREHOUSE_COST,                    'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_NONE}
HOSPITAL_CARD =                 {'ID': HOSPITAL_ID,                 'Card Type': BUILDING_CARD_TYPE,    'Name': "Hospital",                 'Cost': HOSPITAL_COST,                  'Money': HOSPITAL_MONEY,                'VP': HOSPITAL_VP,                  'Status': PLAYER_ACTIVE_CARD,   'IsUpgradable': IS_UPGRADABLE,  'Upgrade Value': HOSPITAL_COST,                     'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_NONE}
LIBRARY_CARD =                  {'ID': LIBRARY_ID,                  'Card Type': BUILDING_CARD_TYPE,    'Name': "Library",                  'Cost': LIBRARY_COST,                   'Money': LIBRARY_MONEY,                 'VP': LIBRARY_VP,                   'Status': PLAYER_ACTIVE_CARD,   'IsUpgradable': IS_UPGRADABLE,  'Upgrade Value': LIBRARY_COST,                      'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_NONE}
THEATER_CARD =                  {'ID': THEATER_ID,                  'Card Type': BUILDING_CARD_TYPE,    'Name': "Theater",                  'Cost': THEATER_COST,                   'Money': THEATER_MONEY,                 'VP': THEATER_VP,                   'Status': PLAYER_ACTIVE_CARD,   'IsUpgradable': IS_UPGRADABLE,  'Upgrade Value': THEATER_COST,                      'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_NONE}
ACADEMY_CARD =                  {'ID': ACADEMY_ID,                  'Card Type': BUILDING_CARD_TYPE,    'Name': "Academy",                  'Cost': ACADEMY_COST,                   'Money': ACADEMY_MONEY,                 'VP': ACADEMY_VP,                   'Status': PLAYER_ACTIVE_CARD,   'IsUpgradable': IS_UPGRADABLE,  'Upgrade Value': ACADEMY_COST,                      'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_NONE}
POTJOMKINS_VILLAGE_CARD =       {'ID': POTJOMKINS_VILLAGE_ID,       'Card Type': BUILDING_CARD_TYPE,    'Name': "Potjomkins Village",       'Cost': POTJOMKINS_VILLAGE_COST,        'Money': POTJOMKINS_VILLAGE_MONEY,      'VP': POTJOMKINS_VILLAGE_VP,        'Status': PLAYER_ACTIVE_CARD,   'IsUpgradable': IS_UPGRADABLE,  'Upgrade Value': POTJOMKINS_VILLAGE_UPGRADE_VALUE,  'IsSpecialCard': IS_SPECIAL,        'SpecialAbility': POTJOMKINS_VILLIAGE_ABILITY,  'Class': CLASS_NONE}
PUB_CARD =                      {'ID': PUB_ID,                      'Card Type': BUILDING_CARD_TYPE,    'Name': "Pub",                      'Cost': PUB_COST,                       'Money': PUB_MONEY,                     'VP': PUB_VP,                       'Status': PLAYER_ACTIVE_CARD,   'IsUpgradable': IS_UPGRADABLE,  'Upgrade Value': PUB_COST,                          'IsSpecialCard': IS_SPECIAL,        'SpecialAbility': PUB_ABILITY,                  'Class': CLASS_NONE}
WAREHOUSE_CARD =                {'ID': WAREHOUSE_ID,                'Card Type': BUILDING_CARD_TYPE,    'Name': "Warehouse",                'Cost': WAREHOUSE_COST,                 'Money': WAREHOUSE_MONEY,               'VP': WAREHOUSE_VP,                 'Status': PLAYER_ACTIVE_CARD,   'IsUpgradable': IS_UPGRADABLE,  'Upgrade Value': WAREHOUSE_COST,                    'IsSpecialCard': IS_SPECIAL,        'SpecialAbility': WAREHOUSE_ABILITY,            'Class': CLASS_NONE}
OBSERVATORY_CARD =              {'ID': OBSERVATORY_ID,              'Card Type': BUILDING_CARD_TYPE,    'Name': "Observatory",              'Cost': OBSERVATORY_COST,               'Money': OBSERVATORY_MONEY,             'VP': OBSERVATORY_VP,               'Status': PLAYER_ACTIVE_CARD,   'IsUpgradable': IS_UPGRADABLE,  'Upgrade Value': OBSERVATORY_COST,                  'IsSpecialCard': IS_SPECIAL,        'SpecialAbility': OBSERVATORY_ABILITY,          'Class': CLASS_NONE}
AUTHOR_CARD =                   {'ID': AUTHOR_ID,                   'Card Type': ARISTOCRAT_CARD_TYPE,  'Name': "Author",                   'Cost': AUTHOR_COST,                    'Money': AUTHOR_MONEY,                  'VP': AUTHOR_VP,                    'Status': PLAYER_ACTIVE_CARD,   'IsUpgradable': IS_UPGRADABLE,  'Upgrade Value': AUTHOR_COST,                       'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_NONE}
ADMINISTRATOR_CARD =            {'ID': ADMINISTRATOR_ID,            'Card Type': ARISTOCRAT_CARD_TYPE,  'Name': "Administrator",            'Cost': ADMINISTRATOR_COST,             'Money': ADMINISTRATOR_MONEY,           'VP': ADMINISTRATOR_VP,             'Status': PLAYER_ACTIVE_CARD,   'IsUpgradable': IS_UPGRADABLE,  'Upgrade Value': ADMINISTRATOR_COST,                'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_NONE}
WAREHOUSE_MANAGER_CARD =        {'ID': WAREHOUSE_MANAGER_ID,        'Card Type': ARISTOCRAT_CARD_TYPE,  'Name': "Warehouse Manager",        'Cost': WAREHOUSE_MANAGER_COST,         'Money': WAREHOUSE_MANAGER_MONEY,       'VP': WAREHOUSE_MANAGER_VP,         'Status': PLAYER_ACTIVE_CARD,   'IsUpgradable': IS_UPGRADABLE,  'Upgrade Value': WAREHOUSE_MANAGER_COST,            'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_NONE}
SECRETARY_CARD =                {'ID': SECRETARY_ID,                'Card Type': ARISTOCRAT_CARD_TYPE,  'Name': "Secretary",                'Cost': SECRETARY_COST,                 'Money': SECRETARY_MONEY,               'VP': SECRETARY_VP,                 'Status': PLAYER_ACTIVE_CARD,   'IsUpgradable': IS_UPGRADABLE,  'Upgrade Value': SECRETARY_COST,                    'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_NONE}
CONTROLLER_CARD =               {'ID': CONTROLLER_ID,               'Card Type': ARISTOCRAT_CARD_TYPE,  'Name': "Controller",               'Cost': CONTROLLER_COST,                'Money': CONTROLLER_MONEY,              'VP': CONTROLLER_VP,                'Status': PLAYER_ACTIVE_CARD,   'IsUpgradable': IS_UPGRADABLE,  'Upgrade Value': CONTROLLER_COST,                   'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_NONE}
JUDGE_CARD =                    {'ID': JUDGE_ID,                    'Card Type': ARISTOCRAT_CARD_TYPE,  'Name': "Judge",                    'Cost': JUDGE_COST,                     'Money': JUDGE_MONEY,                   'VP': JUDGE_VP,                     'Status': PLAYER_ACTIVE_CARD,   'IsUpgradable': IS_UPGRADABLE,  'Upgrade Value': JUDGE_COST,                        'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_NONE}
MISTRESS_OF_CEREMONIES_CARD =   {'ID': MISTRESS_OF_CEREMONIES_ID,   'Card Type': ARISTOCRAT_CARD_TYPE,  'Name': "Mistress of Ceremonies",   'Cost': MISTRESS_OF_CEREMONIES_COST,    'Money': MISTRESS_OF_CEREMONIES_MONEY,  'VP': MISTRESS_OF_CEREMONIES_VP,    'Status': PLAYER_ACTIVE_CARD,   'IsUpgradable': IS_UPGRADABLE,  'Upgrade Value': MISTRESS_OF_CEREMONIES_COST,       'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_NONE}






#--------------------------------------------------------------------------
# Total Cards in Each Deck
#--------------------------------------------------------------------------

WORKER_CARDS = [[LUMBERJACK_CARD, 6],
               [GOLD_MINER_CARD, 6],
               [SHEPHERD_CARD, 6],
               [FUR_TRAPPER_CARD,  6],
               [SHIP_BUILDER_CARD, 6],
               [CZAR_PETER_CARD, 1]]

BUILDING_CARDS = [[MARKET_CARD, 5],
               [CUSTOMS_HOUSE_CARD, 5],
               [FIREHOUSE_CARD, 3],
               [HOSPITAL_CARD, 3],
               [LIBRARY_CARD, 3],
               [THEATER_CARD, 2],
               [ACADEMY_CARD, 1],
               [POTJOMKINS_VILLAGE_CARD, 1],
               [PUB_CARD, 2],
               [WAREHOUSE_CARD, 1],
               [OBSERVATORY_CARD, 2]]

ARISTOCRAT_CARDS = [[AUTHOR_CARD, 6],
               [ADMINISTRATOR_CARD, 5],
               [WAREHOUSE_MANAGER_CARD, 5],
               [SECRETARY_CARD, 4],
               [CONTROLLER_CARD, 3],
               [JUDGE_CARD, 2],
               [MISTRESS_OF_CEREMONIES_CARD, 2]]


#--------------------------------------------------------------------------
# Aristocrat Scoring
#--------------------------------------------------------------------------
ARISTOCRAT_SCORING = [1,3,6,10,15,21,28,36,45,55]

#--------------------------------------------------------------------------
# Game Constants
#--------------------------------------------------------------------------

PLAYERS_PER_GAME = 4

PLAYER_GREEN = 0
PLAYER_BLUE = 1
PLAYER_YELLOW = 2
PLAYER_RED = 3

PLAYER_STARTING_MONEY = 25
PLAYER_STARTING_SCORE = 0
PLAYER_MARKER_WORKER = 0
PLAYER_MARKER_BUIDLING = 1
PLAYER_MARKER_ARISTOCRAT = 2
PLAYER_MARKER_TRADING = 3

PHASE_WORKER = 0
PHASE_BUILDING = 1
PHASE_ARISTOCRAT = 2
PHASE_TRADING = 3

ACTION_BUY = 0
ACTION_HOLD = 1
ACTION_PASS =2


MAX_CARDS_ON_BOARD = 8


