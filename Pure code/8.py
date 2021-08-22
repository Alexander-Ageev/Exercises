# В задании ConquestCampaign вынес обозначения клеток из кода в константы
'0' - FREE_SQUARE    # свободные клетки
'+' - DESCENT_SQUARE # клетки, в которую высадился десант
'*' - OCCUPIED_SQARE # захваченной клетки

char_table - CHAR_COST # PrintingCosts, написал имя в верхнем регистре, изменил его на более информативное
MAJORITY_LIMIT = 50 # MassVote, вынес как константу число, определяющее превосходство победителя

# BastShoe, вынес команды редактора из кода в константы
ADD_COMMAND = '1'
DELETE_COMMAND = '2'
GET_CHAR_COMMAND = '3'
UNDO_COMMAND = '4'
REDO_COMMAND = '5'

# TreeOfLife
MAP - REMOVE_BRANCH_TEMPLATE # Более конкретное имя константы

# white_walkers, вынес константы отдельно, поскольку они могут поменяться
NUM_FOR_CITIZENS = 10
WALKER_SYMBOL = '='
N_UMSYMBOL_FOR_WALKER = 3

# Keymaker,  вынес обозначения открытой и закрытой дверей в константы
CLOSE_DOOR = '0'
OPEN_DOOR = '1'