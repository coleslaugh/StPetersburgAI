#----------------------------------------------------------------------------------------------------------------------------------------------------------
# St. Petersburg Machine Learning Simulation
# Contents - Contains Global Variables for all Classes
# Author: Mike Slaugh
#----------------------------------------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------
# Card Types
#--------------------------------------------------------------------------
WORKER_CARD_TYPE = 0
BUILDING_CARD_TYPE = 1
ARISTOCRAT_CARD_TYPE = 2
TRADING_CARD_TYPE = 3

#--------------------------------------------------------------------------
# Deck Sizes
#--------------------------------------------------------------------------
NUM_CARDS_WORKER_DECK = 31
NUM_CARDS_BUILDING_DECK = 28
NUM_CARDS_ARISTOCRAT_DECK = 27
NUM_CARDS_TRADING_DECK = 30

#--------------------------------------------------------------------------
# Card Status
#--------------------------------------------------------------------------
PLAYER_ACTIVE_CARD = 0
PLAYER_HELD_CARD = 1
PLAYER_DRAW_CARD = 2
PLAYER_DELT_CARD = 3
PLAYER_DECK_CARD = 4

#--------------------------------------------------------------------------
# Row Position
#--------------------------------------------------------------------------
BOARD_UPPER_ROW = 0
BOARD_LOWER_ROW = 1

#--------------------------------------------------------------------------
# Special Card
#--------------------------------------------------------------------------

IS_NOT_SPECIAL = 0
IS_SPECIAL = 1

#--------------------------------------------------------------------------
# Upgrade Status of Card
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
CARPENTER_WORKSHOP_ABILITY = 8
GOLD_SMELTER_ABILITY = 9

POTJOMKINS_VILLAGE_UPGRADE_VALUE = 6

#--------------------------------------------------------------------------
# Final Scoring
#--------------------------------------------------------------------------
ARISTOCRAT_SCORING = [0,1,3,6,10,15,21,28,36,45,55,55,55,55,55,55,55,55]
MONEY_PER_VP = 10
PENALTY_HELD_CARD = -5

#--------------------------------------------------------------------------
# Game Constants
#--------------------------------------------------------------------------

PLAYERS_PER_GAME = 4


PLAYER_1 = 0
PLAYER_2 = 1
PLAYER_3 = 2
PLAYER_4 = 3

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

WAREHOUSE_BONUS_CARDS = 1

ACTION_BUY = 0
ACTION_HOLD = 1
ACTION_PASS = 2
ACTION_UPGRADE = 3
ACTION_OBSERVATORY = 4
ACTION_PUB = 5
ACTION_DISCARD = 6

MAX_CARDS_ON_BOARD = 8
MAX_CARDS_TO_HOLD = 3
MAX_POINTS_TO_BUY = 5

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

# Trading Cards
CARPENTER_WORKSHOP_ID = 24
GOLD_SMELTER_ID = 25
WEAVING_MILL_ID = 26
FUR_SHOP_ID = 27
WHARF_ID = 28
MARIINSKIJ_THEATER_ID = 29
BANK_ID = 30
PETERHOF_ID = 31
ST_ISAAC_CATHEDRAL_ID = 32
CHURCH_OF_JESUS_CHRIST_ID = 33
HARBOR_ID = 34
SMOLNY_CATHEDRAL_ID = 35
CATHERINE_GREAT_PALACE_ID = 36
HERMITAGE_ID = 37
WINTER_PALACE_ID = 38
POPE_ID = 39
WEAPON_MASTER_ID = 40
CHAMBER_MAID_ID = 41
BUILDER_ID = 42
SENATOR_ID = 43
PATRIARCH_ID = 44
TAX_MAN_ID = 45
ADMIRAL_ID = 46
MINISTER_OF_FA_ID = 47
CZAR_ID = 48

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

# Trading Cards
CARPENTER_WORKSHOP_COST = 4
GOLD_SMELTER_COST = 6
WEAVING_MILL_COST = 8
FUR_SHOP_COST = 10
WHARF_COST = 12
MARIINSKIJ_THEATER_COST = 10
BANK_COST = 13
PETERHOF_COST = 14
ST_ISAAC_CATHEDRAL_COST = 15
CHURCH_OF_JESUS_CHRIST_COST = 16
HARBOR_COST = 16
SMOLNY_CATHEDRAL_COST = 17
CATHERINE_GREAT_PALACE_COST = 17
HERMITAGE_COST = 18
WINTER_PALACE_COST = 19
POPE_COST = 6
WEAPON_MASTER_COST = 8
CHAMBER_MAID_COST = 8
BUILDER_COST = 10
SENATOR_COST = 12
PATRIARCH_COST = 16
TAX_MAN_COST = 17
ADMIRAL_COST = 18
MINISTER_OF_FA_COST = 20
CZAR_COST = 24

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

# Trading Cards
CARPENTER_WORKSHOP_MONEY = 3
GOLD_SMELTER_MONEY = 3
WEAVING_MILL_MONEY = 6
FUR_SHOP_MONEY = 3
WHARF_MONEY = 6
MARIINSKIJ_THEATER_MONEY = 0
BANK_MONEY = 5
PETERHOF_MONEY = 4
ST_ISAAC_CATHEDRAL_MONEY = 3
CHURCH_OF_JESUS_CHRIST_MONEY = 2
HARBOR_MONEY = 5
SMOLNY_CATHEDRAL_MONEY = 4
CATHERINE_GREAT_PALACE_MONEY = 1
HERMITAGE_MONEY = 3
WINTER_PALACE_MONEY = 2
POPE_MONEY = 1
WEAPON_MASTER_MONEY = 4
CHAMBER_MAID_MONEY = 0
BUILDER_MONEY = 5
SENATOR_MONEY = 2
PATRIARCH_MONEY = 0
TAX_MAN_MONEY = 0
ADMIRAL_MONEY = 3
MINISTER_OF_FA_MONEY = 2
CZAR_MONEY = 0

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

# Trading Cards
CARPENTER_WORKSHOP_VP = 0
GOLD_SMELTER_VP = 0
WEAVING_MILL_VP = 0
FUR_SHOP_VP = 2
WHARF_VP = 1
MARIINSKIJ_THEATER_VP = 0
BANK_VP = 1
PETERHOF_VP = 2
ST_ISAAC_CATHEDRAL_VP = 3
CHURCH_OF_JESUS_CHRIST_VP = 4
HARBOR_VP = 2
SMOLNY_CATHEDRAL_VP = 3
CATHERINE_GREAT_PALACE_VP = 5
HERMITAGE_VP = 4
WINTER_PALACE_VP = 5
POPE_VP = 1
WEAPON_MASTER_VP = 0
CHAMBER_MAID_VP = 2
BUILDER_VP = 0
SENATOR_VP = 2
PATRIARCH_VP = 4
TAX_MAN_VP = 0
ADMIRAL_VP = 3
MINISTER_OF_FA_VP = 4
CZAR_VP = 6

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
CLASS_BUILDING = 7
CLASS_ARISTOCRAT = 8
CLASS_TRADING = 9

#--------------------------------------------------------------------------
# Cards
#--------------------------------------------------------------------------

LUMBERJACK_CARD =               {'ID': LUMBERJACK_ID,               'Card Type': WORKER_CARD_TYPE,      'Name': 'Lumber Jack',                  'Cost': LUMBERJACK_COST,                'Money': LUMBERJACK_MONEY,              'VP': LUMBERJACK_VP,                'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_UPGRADABLE,      'Upgrade Value': LUMBERJACK_COST,                   'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_WOOD}
GOLD_MINER_CARD =               {'ID': GOLD_MINER_ID,               'Card Type': WORKER_CARD_TYPE,      'Name': "Gold Miner",                   'Cost': GOLD_MINER_COST,                'Money': GOLD_MINER_MONEY,              'VP': GOLD_MINER_VP,                'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_UPGRADABLE,      'Upgrade Value': GOLD_MINER_COST,                   'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_GOLD}
SHEPHERD_CARD =                 {'ID': SHEPHERD_ID,                 'Card Type': WORKER_CARD_TYPE,      'Name': "Shepherd",                     'Cost': SHEPHERD_COST,                  'Money': SHEPHERD_MONEY,                'VP': SHEPHERD_VP,                  'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_UPGRADABLE,      'Upgrade Value': SHEPHERD_COST,                     'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_WOOL}
FUR_TRAPPER_CARD =              {'ID': FUR_TRAPPER_ID,              'Card Type': WORKER_CARD_TYPE,      'Name': "Fur Trapper",                  'Cost': FUR_TRAPPER_COST,               'Money': FUR_TRAPPER_MONEY,             'VP': FUR_TRAPPER_VP,               'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_UPGRADABLE,      'Upgrade Value': FUR_TRAPPER_COST,                  'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_FUR}
SHIP_BUILDER_CARD =             {'ID': SHIP_BUILDER_ID,             'Card Type': WORKER_CARD_TYPE,      'Name': "Ship Builder",                 'Cost': SHIP_BUILDER_COST,              'Money': SHIP_BUILDER_MONEY,            'VP': SHIP_BUILDER_VP,              'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_UPGRADABLE,      'Upgrade Value': SHIP_BUILDER_COST,                 'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_SHIP}
CZAR_PETER_CARD =               {'ID': CZAR_PETER_ID,               'Card Type': WORKER_CARD_TYPE,      'Name': "Czar Peter",                   'Cost': CZAR_PETER_COST,                'Money': CZAR_PETER_MONEY,              'VP': CZAR_PETER_VP,                'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_UPGRADABLE,      'Upgrade Value': CZAR_PETER_COST,                   'IsSpecialCard': IS_SPECIAL,        'SpecialAbility': CZAR_PETER_ABILITY,           'Class': CLASS_ALL}
MARKET_CARD =                   {'ID': MARKET_ID,                   'Card Type': BUILDING_CARD_TYPE,    'Name': "Market",                       'Cost': MARKET_COST,                    'Money': MARKET_MONEY,                  'VP': MARKET_VP,                    'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_UPGRADABLE,      'Upgrade Value': MARKET_COST,                       'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_BUILDING}
CUSTOMS_HOUSE_CARD =            {'ID': CUSTOMS_HOUSE_ID,            'Card Type': BUILDING_CARD_TYPE,    'Name': "Customs House",                'Cost': CUSTOMS_HOUSE_COST,             'Money': CUSTOMS_HOUSE_MONEY,           'VP': CUSTOMS_HOUSE_VP,             'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_UPGRADABLE,      'Upgrade Value': CUSTOMS_HOUSE_COST,                'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_BUILDING}
FIREHOUSE_CARD =                {'ID': FIREHOUSE_ID,                'Card Type': BUILDING_CARD_TYPE,    'Name': "Firehouse",                    'Cost': FIREHOUSE_COST,                 'Money': FIREHOUSE_MONEY,               'VP': FIREHOUSE_VP,                 'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_UPGRADABLE,      'Upgrade Value': FIREHOUSE_COST,                    'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_BUILDING}
HOSPITAL_CARD =                 {'ID': HOSPITAL_ID,                 'Card Type': BUILDING_CARD_TYPE,    'Name': "Hospital",                     'Cost': HOSPITAL_COST,                  'Money': HOSPITAL_MONEY,                'VP': HOSPITAL_VP,                  'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_UPGRADABLE,      'Upgrade Value': HOSPITAL_COST,                     'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_BUILDING}
LIBRARY_CARD =                  {'ID': LIBRARY_ID,                  'Card Type': BUILDING_CARD_TYPE,    'Name': "Library",                      'Cost': LIBRARY_COST,                   'Money': LIBRARY_MONEY,                 'VP': LIBRARY_VP,                   'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_UPGRADABLE,      'Upgrade Value': LIBRARY_COST,                      'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_BUILDING}
THEATER_CARD =                  {'ID': THEATER_ID,                  'Card Type': BUILDING_CARD_TYPE,    'Name': "Theater",                      'Cost': THEATER_COST,                   'Money': THEATER_MONEY,                 'VP': THEATER_VP,                   'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_UPGRADABLE,      'Upgrade Value': THEATER_COST,                      'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_BUILDING}
ACADEMY_CARD =                  {'ID': ACADEMY_ID,                  'Card Type': BUILDING_CARD_TYPE,    'Name': "Academy",                      'Cost': ACADEMY_COST,                   'Money': ACADEMY_MONEY,                 'VP': ACADEMY_VP,                   'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_UPGRADABLE,      'Upgrade Value': ACADEMY_COST,                      'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_BUILDING}
POTJOMKINS_VILLAGE_CARD =       {'ID': POTJOMKINS_VILLAGE_ID,       'Card Type': BUILDING_CARD_TYPE,    'Name': "Potjomkins Village",           'Cost': POTJOMKINS_VILLAGE_COST,        'Money': POTJOMKINS_VILLAGE_MONEY,      'VP': POTJOMKINS_VILLAGE_VP,        'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_UPGRADABLE,      'Upgrade Value': POTJOMKINS_VILLAGE_UPGRADE_VALUE,  'IsSpecialCard': IS_SPECIAL,        'SpecialAbility': POTJOMKINS_VILLIAGE_ABILITY,  'Class': CLASS_BUILDING}
PUB_CARD =                      {'ID': PUB_ID,                      'Card Type': BUILDING_CARD_TYPE,    'Name': "Pub",                          'Cost': PUB_COST,                       'Money': PUB_MONEY,                     'VP': PUB_VP,                       'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_UPGRADABLE,      'Upgrade Value': PUB_COST,                          'IsSpecialCard': IS_SPECIAL,        'SpecialAbility': PUB_ABILITY,                  'Class': CLASS_BUILDING}
WAREHOUSE_CARD =                {'ID': WAREHOUSE_ID,                'Card Type': BUILDING_CARD_TYPE,    'Name': "Warehouse",                    'Cost': WAREHOUSE_COST,                 'Money': WAREHOUSE_MONEY,               'VP': WAREHOUSE_VP,                 'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_UPGRADABLE,      'Upgrade Value': WAREHOUSE_COST,                    'IsSpecialCard': IS_SPECIAL,        'SpecialAbility': WAREHOUSE_ABILITY,            'Class': CLASS_BUILDING}
OBSERVATORY_CARD =              {'ID': OBSERVATORY_ID,              'Card Type': BUILDING_CARD_TYPE,    'Name': "Observatory",                  'Cost': OBSERVATORY_COST,               'Money': OBSERVATORY_MONEY,             'VP': OBSERVATORY_VP,               'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_UPGRADABLE,      'Upgrade Value': OBSERVATORY_COST,                  'IsSpecialCard': IS_SPECIAL,        'SpecialAbility': OBSERVATORY_ABILITY,          'Class': CLASS_BUILDING}
AUTHOR_CARD =                   {'ID': AUTHOR_ID,                   'Card Type': ARISTOCRAT_CARD_TYPE,  'Name': "Author",                       'Cost': AUTHOR_COST,                    'Money': AUTHOR_MONEY,                  'VP': AUTHOR_VP,                    'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_UPGRADABLE,      'Upgrade Value': AUTHOR_COST,                       'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_ARISTOCRAT}
ADMINISTRATOR_CARD =            {'ID': ADMINISTRATOR_ID,            'Card Type': ARISTOCRAT_CARD_TYPE,  'Name': "Administrator",                'Cost': ADMINISTRATOR_COST,             'Money': ADMINISTRATOR_MONEY,           'VP': ADMINISTRATOR_VP,             'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_UPGRADABLE,      'Upgrade Value': ADMINISTRATOR_COST,                'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_ARISTOCRAT}
WAREHOUSE_MANAGER_CARD =        {'ID': WAREHOUSE_MANAGER_ID,        'Card Type': ARISTOCRAT_CARD_TYPE,  'Name': "Warehouse Manager",            'Cost': WAREHOUSE_MANAGER_COST,         'Money': WAREHOUSE_MANAGER_MONEY,       'VP': WAREHOUSE_MANAGER_VP,         'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_UPGRADABLE,      'Upgrade Value': WAREHOUSE_MANAGER_COST,            'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_ARISTOCRAT}
SECRETARY_CARD =                {'ID': SECRETARY_ID,                'Card Type': ARISTOCRAT_CARD_TYPE,  'Name': "Secretary",                    'Cost': SECRETARY_COST,                 'Money': SECRETARY_MONEY,               'VP': SECRETARY_VP,                 'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_UPGRADABLE,      'Upgrade Value': SECRETARY_COST,                    'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_ARISTOCRAT}
CONTROLLER_CARD =               {'ID': CONTROLLER_ID,               'Card Type': ARISTOCRAT_CARD_TYPE,  'Name': "Controller",                   'Cost': CONTROLLER_COST,                'Money': CONTROLLER_MONEY,              'VP': CONTROLLER_VP,                'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_UPGRADABLE,      'Upgrade Value': CONTROLLER_COST,                   'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_ARISTOCRAT}
JUDGE_CARD =                    {'ID': JUDGE_ID,                    'Card Type': ARISTOCRAT_CARD_TYPE,  'Name': "Judge",                        'Cost': JUDGE_COST,                     'Money': JUDGE_MONEY,                   'VP': JUDGE_VP,                     'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_UPGRADABLE,      'Upgrade Value': JUDGE_COST,                        'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_ARISTOCRAT}
MISTRESS_OF_CEREMONIES_CARD =   {'ID': MISTRESS_OF_CEREMONIES_ID,   'Card Type': ARISTOCRAT_CARD_TYPE,  'Name': "Mistress of Ceremonies",       'Cost': MISTRESS_OF_CEREMONIES_COST,    'Money': MISTRESS_OF_CEREMONIES_MONEY,  'VP': MISTRESS_OF_CEREMONIES_VP,    'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_UPGRADABLE,      'Upgrade Value': MISTRESS_OF_CEREMONIES_COST,       'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_ARISTOCRAT}
CARPENTER_WORKSHOP_CARD =       {'ID': CARPENTER_WORKSHOP_ID,       'Card Type': WORKER_CARD_TYPE,      'Name': "Carpenter Workshop",           'Cost': CARPENTER_WORKSHOP_COST,        'Money': CARPENTER_WORKSHOP_MONEY,      'VP': CARPENTER_WORKSHOP_VP,        'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_NOT_UPGRADABLE,  'Upgrade Value': CARPENTER_WORKSHOP_COST,           'IsSpecialCard': IS_SPECIAL,        'SpecialAbility': CARPENTER_WORKSHOP_ABILITY,   'Class': CLASS_WOOD}
GOLD_SMELTER_CARD =             {'ID': GOLD_SMELTER_ID,             'Card Type': WORKER_CARD_TYPE,      'Name': "Gold Smelter",                 'Cost': GOLD_SMELTER_COST,              'Money': GOLD_SMELTER_MONEY,            'VP': GOLD_SMELTER_VP,              'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_NOT_UPGRADABLE,  'Upgrade Value': GOLD_SMELTER_COST,                 'IsSpecialCard': IS_SPECIAL,        'SpecialAbility': GOLD_SMELTER_ABILITY,         'Class': CLASS_GOLD}
WEAVING_MILL_CARD =             {'ID': WEAVING_MILL_ID,             'Card Type': WORKER_CARD_TYPE,      'Name': "Weaving Mill",                 'Cost': WEAVING_MILL_COST,              'Money': WEAVING_MILL_MONEY,            'VP': WEAVING_MILL_VP,              'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_NOT_UPGRADABLE,  'Upgrade Value': WEAVING_MILL_COST,                 'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_WOOL}
FUR_SHOP_CARD =                 {'ID': FUR_SHOP_ID,                 'Card Type': WORKER_CARD_TYPE,      'Name': "Fur Shop",                     'Cost': FUR_SHOP_COST,                  'Money': FUR_SHOP_MONEY,                'VP': FUR_SHOP_VP,                  'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_NOT_UPGRADABLE,  'Upgrade Value': FUR_SHOP_COST,                     'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_FUR}
WHARF_CARD =                    {'ID': WHARF_ID,                    'Card Type': WORKER_CARD_TYPE,      'Name': "Warf",                         'Cost': WHARF_COST,                     'Money': WHARF_MONEY,                   'VP': WHARF_VP,                     'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_NOT_UPGRADABLE,  'Upgrade Value': WHARF_COST,                        'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_SHIP}
MARIINSKIJ_THEATER_CARD =       {'ID': MARIINSKIJ_THEATER_ID,       'Card Type': BUILDING_CARD_TYPE,    'Name': "Mariinskij Theater",           'Cost': MARIINSKIJ_THEATER_COST,        'Money': MARIINSKIJ_THEATER_MONEY,      'VP': MARIINSKIJ_THEATER_VP,        'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_NOT_UPGRADABLE,  'Upgrade Value': MARIINSKIJ_THEATER_COST,           'IsSpecialCard': IS_SPECIAL,        'SpecialAbility': MARIINSKIJ_THEATER_ABILITY,   'Class': CLASS_BUILDING}
BANK_CARD =                     {'ID': BANK_ID,                     'Card Type': BUILDING_CARD_TYPE,    'Name': "Bank",                         'Cost': BANK_COST,                      'Money': BANK_MONEY,                    'VP': BANK_VP,                      'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_NOT_UPGRADABLE,  'Upgrade Value': BANK_COST,                         'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_BUILDING}
PETERHOF_CARD =                 {'ID': PETERHOF_ID,                 'Card Type': BUILDING_CARD_TYPE,    'Name': "Peterhof",                     'Cost': PETERHOF_COST,                  'Money': PETERHOF_MONEY,                'VP': PETERHOF_VP,                  'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_NOT_UPGRADABLE,  'Upgrade Value': PETERHOF_COST,                     'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_BUILDING}
ST_ISAAC_CATHEDRAL_CARD =       {'ID': ST_ISAAC_CATHEDRAL_ID,       'Card Type': BUILDING_CARD_TYPE,    'Name': "St. Isaac Cathedral",          'Cost': ST_ISAAC_CATHEDRAL_COST,        'Money': ST_ISAAC_CATHEDRAL_MONEY,      'VP': ST_ISAAC_CATHEDRAL_VP,        'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_NOT_UPGRADABLE,  'Upgrade Value': ST_ISAAC_CATHEDRAL_COST,           'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_BUILDING}
CHURCH_OF_JESUS_CHRIST_CARD =   {'ID': CHURCH_OF_JESUS_CHRIST_ID,   'Card Type': BUILDING_CARD_TYPE,    'Name': "Church of Jesus Christ",       'Cost': CHURCH_OF_JESUS_CHRIST_COST,    'Money': CHURCH_OF_JESUS_CHRIST_MONEY,  'VP': CHURCH_OF_JESUS_CHRIST_VP,    'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_NOT_UPGRADABLE,  'Upgrade Value': CHURCH_OF_JESUS_CHRIST_COST,       'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_BUILDING}
HARBOR_CARD =                   {'ID': HARBOR_ID,                   'Card Type': BUILDING_CARD_TYPE,    'Name': "Harbor",                       'Cost': HARBOR_COST,                    'Money': HARBOR_MONEY,                  'VP': HARBOR_VP,                    'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_NOT_UPGRADABLE,  'Upgrade Value': HARBOR_COST,                       'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_BUILDING}
SMOLNY_CATHEDRAL_CARD =         {'ID': SMOLNY_CATHEDRAL_ID,         'Card Type': BUILDING_CARD_TYPE,    'Name': "Smolny Cathedral",             'Cost': SMOLNY_CATHEDRAL_COST,          'Money': SMOLNY_CATHEDRAL_MONEY,        'VP': SMOLNY_CATHEDRAL_VP,          'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_NOT_UPGRADABLE,  'Upgrade Value': SMOLNY_CATHEDRAL_COST,             'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_BUILDING}
CATHERINE_GREAT_PALACE_CARD =   {'ID': CATHERINE_GREAT_PALACE_ID,   'Card Type': BUILDING_CARD_TYPE,    'Name': "Catherine the Great Palace",   'Cost': CATHERINE_GREAT_PALACE_COST,    'Money': CATHERINE_GREAT_PALACE_MONEY,  'VP': CATHERINE_GREAT_PALACE_VP,    'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_NOT_UPGRADABLE,  'Upgrade Value': CATHERINE_GREAT_PALACE_COST,       'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_BUILDING}
HERMITAGE_CARD =                {'ID': HERMITAGE_ID,                'Card Type': BUILDING_CARD_TYPE,    'Name': "Hermitage",                    'Cost': HERMITAGE_COST,                 'Money': HERMITAGE_MONEY,               'VP': HERMITAGE_VP,                 'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_NOT_UPGRADABLE,  'Upgrade Value': HERMITAGE_COST,                    'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_BUILDING}
WINTER_PALACE_CARD =            {'ID': WINTER_PALACE_ID,            'Card Type': BUILDING_CARD_TYPE,    'Name': "Winter Palace",                'Cost': WINTER_PALACE_COST,             'Money': WINTER_PALACE_MONEY,           'VP': WINTER_PALACE_VP,             'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_NOT_UPGRADABLE,  'Upgrade Value': WINTER_PALACE_COST,                'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_BUILDING}
POPE_CARD =                     {'ID': POPE_ID,                     'Card Type': ARISTOCRAT_CARD_TYPE,  'Name': "Pope",                         'Cost': POPE_COST,                      'Money': POPE_MONEY,                    'VP': POPE_VP,                      'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_NOT_UPGRADABLE,  'Upgrade Value': POPE_COST,                         'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_ARISTOCRAT}
WEAPON_MASTER_CARD =            {'ID': WEAPON_MASTER_ID,            'Card Type': ARISTOCRAT_CARD_TYPE,  'Name': "Weapon Master",                'Cost': WEAPON_MASTER_COST,             'Money': WEAPON_MASTER_MONEY,           'VP': WEAPON_MASTER_VP,             'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_NOT_UPGRADABLE,  'Upgrade Value': WEAPON_MASTER_COST,                'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_ARISTOCRAT}
CHAMBER_MAID_CARD =             {'ID': CHAMBER_MAID_ID,             'Card Type': ARISTOCRAT_CARD_TYPE,  'Name': "Chamber Maid",                 'Cost': CHAMBER_MAID_COST,              'Money': CHAMBER_MAID_MONEY,            'VP': CHAMBER_MAID_VP,              'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_NOT_UPGRADABLE,  'Upgrade Value': CHAMBER_MAID_COST,                 'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_ARISTOCRAT}
BUILDER_CARD =                  {'ID': BUILDER_ID,                  'Card Type': ARISTOCRAT_CARD_TYPE,  'Name': "Builder",                      'Cost': BUILDER_COST,                   'Money': BUILDER_MONEY,                 'VP': BUILDER_VP,                   'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_NOT_UPGRADABLE,  'Upgrade Value': BUILDER_COST,                      'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_ARISTOCRAT}
SENATOR_CARD =                  {'ID': SENATOR_ID,                  'Card Type': ARISTOCRAT_CARD_TYPE,  'Name': "Senator",                      'Cost': SENATOR_COST,                   'Money': SENATOR_MONEY,                 'VP': SENATOR_VP,                   'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_NOT_UPGRADABLE,  'Upgrade Value': SENATOR_COST,                      'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_ARISTOCRAT}
PATRIARCH_CARD =                {'ID': PATRIARCH_ID,                'Card Type': ARISTOCRAT_CARD_TYPE,  'Name': "Patriarch",                    'Cost': PATRIARCH_COST,                 'Money': PATRIARCH_MONEY,               'VP': PATRIARCH_VP,                 'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_NOT_UPGRADABLE,  'Upgrade Value': PATRIARCH_COST,                    'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_ARISTOCRAT}
TAX_MAN_CARD =                  {'ID': TAX_MAN_ID,                  'Card Type': ARISTOCRAT_CARD_TYPE,  'Name': "Tax Man",                      'Cost': TAX_MAN_COST,                   'Money': TAX_MAN_MONEY,                 'VP': TAX_MAN_VP,                   'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_NOT_UPGRADABLE,  'Upgrade Value': TAX_MAN_COST,                      'IsSpecialCard': IS_SPECIAL,        'SpecialAbility': TAX_MAN_ABILITY,              'Class': CLASS_ARISTOCRAT}
ADMIRAL_CARD =                  {'ID': ADMIRAL_ID,                  'Card Type': ARISTOCRAT_CARD_TYPE,  'Name': "Admiral",                      'Cost': ADMIRAL_COST,                   'Money': ADMIRAL_MONEY,                 'VP': ADMIRAL_VP,                   'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_NOT_UPGRADABLE,  'Upgrade Value': ADMIRAL_COST,                      'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_ARISTOCRAT}
MINISTER_OF_FA_CARD =           {'ID': MINISTER_OF_FA_ID,           'Card Type': ARISTOCRAT_CARD_TYPE,  'Name': "Minister of Foreign Affairs",  'Cost': MINISTER_OF_FA_COST,            'Money': MINISTER_OF_FA_MONEY,          'VP': MINISTER_OF_FA_VP,            'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_NOT_UPGRADABLE,  'Upgrade Value': MINISTER_OF_FA_COST,               'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_ARISTOCRAT} 
CZAR_CARD =                     {'ID': CZAR_ID,                     'Card Type': ARISTOCRAT_CARD_TYPE,  'Name': "Czar",                         'Cost': CZAR_COST,                      'Money': CZAR_MONEY,                    'VP': CZAR_VP,                      'Status': PLAYER_DECK_CARD,   'IsUpgradable': IS_NOT_UPGRADABLE,  'Upgrade Value': CZAR_COST,                         'IsSpecialCard': IS_NOT_SPECIAL,    'SpecialAbility': NO_SPECIAL_ABILITY,           'Class': CLASS_ARISTOCRAT}

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

TRADING_CARDS = [[CARPENTER_WORKSHOP_CARD, 1], 
                 [GOLD_SMELTER_CARD, 1],
                 [WEAVING_MILL_CARD, 2],
                 [FUR_SHOP_CARD, 3],  
                 [WHARF_CARD, 3],     
                 [MARIINSKIJ_THEATER_CARD, 1],
                 [BANK_CARD, 1],      
                 [PETERHOF_CARD, 1],  
                 [ST_ISAAC_CATHEDRAL_CARD, 1],
                 [CHURCH_OF_JESUS_CHRIST_CARD, 1],
                 [HARBOR_CARD, 1],    
                 [SMOLNY_CATHEDRAL_CARD, 1],
                 [CATHERINE_GREAT_PALACE_CARD, 1],
                 [HERMITAGE_CARD, 1],             
                 [WINTER_PALACE_CARD, 1],         
                 [POPE_CARD, 1],                  
                 [WEAPON_MASTER_CARD, 1],         
                 [CHAMBER_MAID_CARD, 1],          
                 [BUILDER_CARD, 1],               
                 [SENATOR_CARD, 1],               
                 [PATRIARCH_CARD, 1],             
                 [TAX_MAN_CARD, 1],               
                 [ADMIRAL_CARD, 1],               
                 [MINISTER_OF_FA_CARD, 1],         
                 [CZAR_CARD, 1]]

#--------------------------------------------------------------------------
# Friendly Names
#--------------------------------------------------------------------------
PLAYERS = [[PLAYER_1, "Player 1"], [PLAYER_2, "Player 2"], [PLAYER_3, "Player 3"], [PLAYER_4, "Player 4"]]
PLAYER_COLORS = [[PLAYER_GREEN, "Green"], [PLAYER_BLUE, "Blue"], [PLAYER_YELLOW, "Yellow"], [PLAYER_RED, "Red"]]
PHASES = [[PHASE_WORKER, "Worker Phase"], [PHASE_BUILDING, "Building Phase"], [PHASE_ARISTOCRAT, "Aristocrat Phase"], [PHASE_TRADING, "Trading Card Phase"]]
ACTIONS = [[ACTION_BUY, "Buy"], [ACTION_HOLD, "Hold"], [ACTION_PASS, "Pass"],[ACTION_UPGRADE, "Upgrade"],[ACTION_OBSERVATORY, "Observatory"], [ACTION_PUB, "Use the Pub"] ]
MARKERS = [[PLAYER_MARKER_WORKER, "Worker Token"], [PLAYER_MARKER_BUIDLING, "Building Token"], [PLAYER_MARKER_ARISTOCRAT, "Aristocrat Token"], [PLAYER_MARKER_TRADING, "Trading Card Token"]]
DECKS = [[WORKER_CARDS, "Worker Deck"], [BUILDING_CARDS, "Building Deck"], [ARISTOCRAT_CARDS, "Aristocrat Deck"], [TRADING_CARDS, "Trading Deck"]]
CARD_TYPES = [[WORKER_CARD_TYPE, "Worker Card"], [BUILDING_CARD_TYPE, "Building Card"], [ARISTOCRAT_CARD_TYPE, "Aristocrat Card"], [TRADING_CARD_TYPE, "Trading Card"]]

#--------------------------------------------------------------------------
# Brain Constants
#--------------------------------------------------------------------------
DEFAULT_GAMES_PER_SESSION = 10

BRAIN_PHASES = ["W","B","A","T"]
BRAIN_ROUNDS = ["1","2","3","4","5","6","L"]

BRAIN_DEFAULT_VALUE = 500
BRAIN_PASS_DEFAULT_VAULE = 200
BRAIN_RESET_INTERVAL = 100
BRAIN_MAX_ACTION_VALUE = 1000
BRAIN_MIN_ACTION_VALUE = 0

BRAIN_REWARD_VALUE = 3
BRAIN_REWARD_BANDS = 5

BRAIN_PENALTY_VALUE = -3
BRAIN_PENALTY_BANDS = 5

BRAIN_EPSILON = 0.1
BRAIN_EPSILON_INCREMENT = -0.1
BRAIN_EPSILON_INCREMENT_INTERVAL = 10000
BRAIN_EPSILON_MAX = 1
BRAIN_EPSILON_MIN = 0

BRAIN_TARGET_SCORE = 15
BRAIN_TARGET_SCORE_INCREMENT_INTERVAL = 10000
BRAIN_TARGET_SCORE_INCREMENT = 2

BRAIN_PENALTY_HELD_CARD = -20
BRAIN_REWARD_BUY_HELD_CARD = 20
BRAIN_REWARD_BUY_UNIQUE_ARISTOCRAT = 20
BRAIN_REWARD_HOLD_UNIQUE_ARISTOCRAT = 10
BRAIN_REWARD_CARD_MULTIPLIER = 10
BRAIN_REWARD_VP_VALUE = 1
BRAIN_REWARD_MONEY_VALUE = .5

#--------------------------------------------------------------------------
# GUI Constants
#--------------------------------------------------------------------------

GUI_REFRESH_PHASES = True
GUI_REFRESH_ROUNDS = True
GUI_REFRESH_GAME_INTERVAL = 1
GUI_SLEEP_BETWEEN_PHASES = 0.02
GUI_SLEEP_BETWEEN_ROUNDS = 0.02
GUI_SLEEP_BETWEEN_GAMES = .1





