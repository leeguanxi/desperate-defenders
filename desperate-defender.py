import random

# Game variables
game_vars = {
    'turn': 0,                      # Current Turn
    'monster_kill_target': 20,      # Number of kills needed to win
    'monsters_killed': 0,           # Number of monsters killed so far
    'num_monsters': 0,              # Number of monsters in the field
    'gold': 10,                     # Gold for purchasing units
    'threat': 0,                    # Current threat metre level
    'max_threat': 10,               # Length of threat metre
    'danger_level': 1,              # Rate at which threat increases
    'upgrade_unit_price': 8
    }

defender_list = ['ARCHR', 'WALL']
monster_list = ['ZOMBI', 'WWOLF']

defenders = {'ARCHR': {'shortform':'ARCHR',
                       'name': 'Archer',
                       'maxHP': 5,
                       'min_damage': 1,
                       'max_damage': 4,
                       'price': 5,
                       },
             
             'WALL': {'shortform':'WALL',
                      'name': 'Wall',
                      'maxHP': 20,
                      'min_damage': 0,
                      'max_damage': 0,
                      'price': 3,
                      }
                      

             }

monsters = {'ZOMBI': {'shortform': 'ZOMBI',
                      'name': 'Zombie',
                      'maxHP': 15,
                      'min_damage': 3,
                      'max_damage': 6,
                      'moves' : 1,
                      'reward': 2
                      },

            'WWOLF': {'shortform': 'WWOLF',
                      'name': 'Werewolf',
                      'maxHP': 10,
                      'min_damage': 1,
                      'max_damage': 4,
                      'moves' : 2,
                      'reward': 3
                      }
            }

field = [ [None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None]] # for testing: ['ZOMBI',15,15] ['WWOLF',10,10]


#----------------------------------------------------------------------
# draw_field()
#
#    Draws the field of play
#    The column numbers only go to 3 since players can only place units
#      in the first 3 columns
#----------------------------------------------------------------------

def draw_field(field):

    print('   1     2     3') # print col 1, 2, 3
    for row in range(rows): 
        print(' ', end='')
        for column in range(columns):
            print('+-----', end = '') # prints top
        print('+')
        print(lane[row], end='') # print A,B,C,D,E

        for column in range(columns): # print each row's first line
            if field[row][column] == None:
                field[row][column] = '     '
            try:
                print('|{:<5}'.format(field[row][column][0]), end = '') # prints unit name
            except:
                print('|{:<5}'.format(field[row][column]), end = '') # prints blank
        print('|')

        print(' ',end = '')
        for column in range(columns): # prints each row's second line
            if field[row][column] != '     ':
                print('|{:>2}/{:<2}'.format(field[row][column][1],field[row][column][2]),end = '') # prints HP

            else:
                print('|{:<5}'.format(field[row][column]), end = '') # prints blank
        print('|')

    print(' ',end='')
    for column in range(columns): # prints bottom
        print('+-----', end = '')
    print('+')
    
    return

#----------------------------
# show_combat_menu()
#
#    Displays the combat menu
#----------------------------
def show_combat_menu(game_vars):
    print('Turn  {}     Threat = [{:<10}]     Danger Level {}'\
          .format(game_vars.get('turn'),'-'*game_vars.get('threat'),\
                  game_vars.get('danger_level')))
    print('Gold = {}    Monsters killed = {}/{}'\
          .format(game_vars.get('gold'),game_vars.get('monsters_killed')\
                  ,game_vars.get('monster_kill_target')))
    print("1. Buy unit     2. Heal units (5 gold)   3. Upgrade units ({} gold)".format(game_vars['upgrade_unit_price']))
    print("4. End turn     5. Save game             6. Quit")
        

#----------------------------
# show_main_menu()
#
#    Displays the main menu
#----------------------------
def show_main_menu():
    print("Desperate Defenders")
    print("-------------------")
    print("Defend the city from undead monsters!")
    print()
    print("1. Start new game")
    print("2. Load saved game")
    print("3. Options")
    print("4. Quit")

#-----------------------------------------------------
# place_unit()
#
#    Places a unit at the given position
#    This function works for both defender and monster
#    Returns False if the position is invalid
#       - Position is not on the field of play
#       - Position is occupied
#       - Defender is placed past the first 3 columns
#    Returns True if placement is successful
#-----------------------------------------------------

def place_unit(field, position, row, column):#, position, unit_name):

    if field[row][column] != '     ':
        print('-'*25)
        print('{:^25}'.format('! POSITION OCCUPIED !'))
        print('-'*25)
        return False

    elif len(position) != 2:
        print('-'*25)
        print('{:^25}'.format('! INVALID POSITION !'))
        print('-'*25)
        return False

    elif column < 0 or column > 2:
        print('-'*45)
        print('{:^45}'.format('UNITS CAN ONLY BE PLACED IN COLUMNS 1 TO 3.'))
        print('-'*45)
        return False
    else:
        return True



#-------------------------------------------------------------------
# buy_unit()
#
#    Allows player to buy a unit and place it using place_unit()
#-------------------------------------------------------------------
def buy_unit(field, game_vars):

    print('What unit do you wish to buy?')
    print('1. Archer (5 gold)')
    print('2. Wall (3 gold)')
    #print('3. Mine (8 gold)')
    print('3. Don\'t buy')

    buy_unit_list = ['archer','wall','dont buy']
    choice = int(input('Your choice? '))

    if buy_unit_list[choice-1] == 'archer':
        
        if game_vars['gold'] >= defenders['ARCHR']['price']:
            enough_gold = True
            unit_name = defenders['ARCHR']
        else:
            enough_gold = False
            unit_name = None

    elif buy_unit_list[choice-1] == 'wall':
         
        if game_vars['gold'] >= defenders['WALL']['price']:
            enough_gold = True
            unit_name = defenders['WALL']
        else:
            enough_gold = False
            unit_name = None

    elif buy_unit_list[choice-1] == 'dont buy':
        enough_gold = 'dont buy'
        unit_name = None

    return enough_gold, unit_name

    #elif buy_unit_list[choice-1] == 'mine':
        
       # if game_vars['gold'] >= defenders['MINE']['price']:
            #enough_gold = True
            #unit_name = defenders['MINE']
        #else:
            #enough_gold = False
            #unit_name = None
    
    

#-----------------------------------------------------------
# defender_attack()
#
#    Defender unit attacks.
#
#-----------------------------------------------------------
def defender_attack(field): #defender_name, field, row, column):

    for row in range(rows):
        row_units = [] # temp stores units in same row
        
        for column in range(columns):
            
            if field[row][column][0] == 'ARCHR' or field[row][column][0] in monster_list: #check if archer and monster in same row

                if row_units.count('ZOMBI') == 1 or row_units.count('WWOLF') == 1: # append only 1 monster to the list (can only attack 1 monster)
                    continue
                else:
                    row_units.append(field[row][column][0])

        #for unit in range(len(row_units)):

        if ('ARCHR' in row_units) and ('ZOMBI' in row_units or 'WWOLF' in row_units): 
                archer_count = row_units.count('ARCHR') # count num of archers in same row
                #print(row_units)

                for i in range(archer_count):
                    damage = random.randint(defenders['ARCHR']['min_damage'],defenders['ARCHR']['max_damage'])

                    for j in range(columns): # loop through row to locate monster and deduct HP

                        if field[row][j][0] in monster_list:
                            
                            unit_name = monsters[field[row][j][0]]['name']
                            field[row][j][1] -= damage # give damage to monster
                            print('Archer in lane {} shoots {} for {} damage!'.format(lane[row], unit_name, damage))

                            if field[row][j][1] <= 0: # if monster HP <= 0
                                monster_died = field[row][j][0]
                                field[row][j] = '     '
                                game_vars['num_monsters'] -= 1
                                print('{} in lane {} died.'.format(monsters[monster_died]['name'], lane[row]))

                                game_vars['threat'] += monsters[monster_died]['reward']
                                game_vars['monsters_killed'] += 1
                                game_vars['gold'] += monsters[monster_died]['reward']
                                print('You\'ve gained {} gold as a reward!'.format(monsters[monster_died]['reward']))
                                

                            break

                '''if (field[row][column][0] in monster_list) and (field[row][column-1][0] == 'MINE'): 

                    monster_died = mine_attack(field, row, column)
                    field[row][column- 1] = '     '
                    print(monster_died)
                    print('{} in lane {} died.'.format(monsters[monster_died]['name'], lane[row]))
                    return monster_died'''

#-----------------------------------------------------------
# monster_advance()
#
#    Monster unit advances.
#       - If it lands on a defender, it deals damage
#       - If it lands on a monster, it does nothing
#       - If it goes out of the field, player loses
#-----------------------------------------------------------
def monster_advance(field, rows, columns): #monster_name, field, row, column):

     for row in range(rows):
        for column in range(columns):

            if field[row][column][0] in monster_list:
                moves = monsters[field[row][column][0]]['moves']

            # check if monster & defender are next to each other
            if (field[row][column][0] in monster_list) and (field[row][column-1][0] in defender_list):

                if field[row][column][0] in monster_list: # ZOMBI or WWOLF
                    damage = random.randint(monsters[field[row][column][0]]['min_damage'],monsters[field[row][column][0]]['max_damage'])
                    field[row][column-1][1] -= damage # give damage to defender
                    unit_name = monsters[field[row][column][0]]['name']
                    print('{} in lane {} gave {} {} damage!'.format(unit_name,lane[row], defenders[field[row][column-1][0]]['name'],damage))

                    if field[row][column-1][1] <= 0: # check if defender HP is <= 0
                        field[row][column-1] = '     ' # remove defender

            # if there is a unit infront, monster dont move
            elif (field[row][column][0] in monster_list) and (field[row][column - 1][0] in defender_list+monster_list):
                field[row][column] =field[row][column] # dont move
            
            # if monster has 2 or more moves that will overlap another unit
            elif (field[row][column][0] in monster_list) and (field[row][column - moves][0] in defender_list+monster_list): # column - moves
                field[row][column-(moves - 1)] = field[row][column] # monster moves next to unit
                field[row][column] = '     '
            

            # Monster moving
            elif field[row][column][0] in monster_list:

                if column - moves <= -1: # lose game if monster exits field
                    #print(column, moves, column-moves) # debugging
                    lose = True
                    return lose

                else:
                    unit_name = monsters[field[row][column][0]]['name']
                    field[row][column - moves] = field[row][column] # get monster moves
                    field[row][column] = '     '
                    
                    print('{} in lane {} advances!'.format(unit_name, lane[row]))

#---------------------------------------------------------------------------------
# mine_attack() *NOT IN USE* ;(
#
#    When a monster walks onto a mine, it explodes to deal 10 damages
#    to all monsters in the 9 square surrounding it (including its own position)
#---------------------------------------------------------------------------------
'''def mine_attack(field, row, column): # NOT IN USE

    for i in range(3):

        if (row - 1) < 0 or (column - 1 + i) < 0: # ensure row and columns are not negative values
            continue

        else:
        
            if field[row - 1][column - 1 + i][0] in monster_list:      # scan first 3 columns
                field[row - 1][column - 1 + i][1] -= defenders['MINE']['damage'] # give damage
                unit_name = monsters[field[row - 1][column - 1 + i][0]]['name'] 

                print('Mine gave {} {} damages!'.format(unit_name, defenders['MINE']['damage']))

                if field[row - 1][column - 1 + i][1] <= 0:
                    monster = field[row - 1][column - 1 + i][0] # WWOLF
                    field[row - 1][column - 1 + i] = '     '
                    #print(monster)
                    return monster

    for i in range(3):

        if (column - 1 + i) < 0:
            continue

        else:
            
            if field[row][column - 1 + i][0] in monster_list:          # scan second 3 columns
                field[row][column - 1 + i][1] -= defenders['MINE']['damage'] # give damage
                unit_name = monsters[field[row][column - 1 + i][0]]['name']

                print('Mine gave {} {} damages!'.format(unit_name, defenders['MINE']['damage']))

                if field[row][column - 1 + i][1] <= 0:
                    monster = field[row][column - 1 + i][0]
                    field[row][column - 1 + i] = '     '
                    #print(monster)
                    return monster
                
    for i in range(3):

        if (row + 1) > (rows - 1) or (column - 1 + i) < 0:
            continue

        else:
        
            if field[row + 1][column - 1 + i][0] in monster_list:      # scan third 3 columns
                field[row + 1][column - 1 + i][1] -= defenders['MINE']['damage'] # give damage
                unit_name = monsters[field[row + 1][column - 1 + i][0]]['name']

                print('Mine gave {} {} damages!'.format(unit_name, defenders['MINE']['damage']))

                if field[row + 1][column - 1 + i][1] <= 0:
                    monster = field[row + 1][column - 1 + i][0]
                    field[row + 1][column - 1 + i] = '     '
                    #print(monster)
                    return monster
'''
#---------------------------------------------------------------------
# spawn_monster()
#
#    Spawns a monster in a random lane on the right side of the field.
#    Assumes you will never place more than 5 monsters in one turn.
#---------------------------------------------------------------------
def spawn_monster(field, monster_list):
    
    random_monster = random.choice(monster_list) # spawn either zombie or wolf
    spawn = random.randint(0,4)
    unit_list = []
    unit_list += [monsters[random_monster]['shortform']] + [monsters[random_monster]['maxHP']] +[monsters[random_monster]['maxHP']]
    field[spawn][columns-1] = unit_list # spawn zombie on random lane on col 7
    print('{} spawned in lane {}.'.format(monsters[random_monster]['name'], lane[spawn]))
    game_vars['num_monsters'] += 1

    return

#---------------------------------------------------------------------
# heal()
#
#    Allows players to spend 5 gold to allow all defender units in
#    a 3x3 square to recover 5 HP
#---------------------------------------------------------------------
def heal(field,row, column):

    for i in range(3):

        if (row - 1) < 0 or (column - 1 + i) < 0: # ensure row and columns are not negative values
            continue

        else:
        
            if field[row - 1][column - 1 + i][0] in defender_list:      # scan first 3 columns
                hp_difference = field[row - 1][column - 1 + i][2] - field[row - 1][column - 1 + i][1]
                unit_name = defenders[field[row - 1][column - 1 + i][0]]['name']
                
                if hp_difference <= 5: # if difference is less than 5 HP, recover HP to maxHP
                    field[row - 1][column - 1 + i][1] += hp_difference  # prevent current HP from exceeding maxHP

                else:
                    field[row - 1][column - 1 + i][1] += 5 # if diff more than 5, just add 5 HP

                print('{} in lane {} was healed.'.format(unit_name, lane[row-1]))

    for i in range(3):

        if (column - 1 + i) < 0:
            continue

        else:
            
            if field[row][column - 1 + i][0] in defender_list:          # scan second 3 columns
                hp_difference = field[row][column - 1 + i][2] - field[row][column - 1 + i][1]
                unit_name = defenders[field[row][column - 1 + i][0]]['name']

                
                if hp_difference <= 5:
                    field[row][column - 1 + i][1] += hp_difference

                else:
                    field[row][column - 1 + i][1] += 5 

                print('{} in lane {} was healed.'.format(unit_name, lane[row]))

    for i in range(3):

        if (row + 1) > (rows - 1) or (column - 1 + i) < 0:
            continue

        else:
        
            if field[row + 1][column - 1 + i][0] in defender_list:      # scan third 3 columns
                hp_difference = field[row + 1][column - 1 + i][2] - field[row + 1][column - 1 + i][1]
                unit_name = defenders[field[row + 1][column - 1 + i][0]]['name']
                
                if hp_difference <= 5:
                    field[row + 1][column - 1 + i][1] += hp_difference

                else:
                    field[row + 1][column - 1 + i][1] += 5 

                print('{} in lane {} was healed.'.format(unit_name, lane[row+1]))

#---------------------------------------------------------------------
# upgrade_unit()
#
#    Upgrades Archer and Wall units with:
#       + 1 min/max damage (for archer)
#       + 5 HP (for wall)
#       Costs: 8 gold (+2 gold every upgrade)
#---------------------------------------------------------------------
def upgrade_unit():
    if game_vars['gold'] >= game_vars['upgrade_unit_price']:
        game_vars['gold'] -= game_vars['upgrade_unit_price']
        game_vars['upgrade_unit_price'] += 2
        defenders['ARCHR']['min_damage'] += 1
        defenders['ARCHR']['max_damage'] += 1
        defenders['WALL']['maxHP'] += 5
        print('Archers and Walls have been upgraded !')

        for row in range(rows):
            for column in range(columns):
                if field[row][column][0] == 'WALL':
                    field[row][column][2] = defenders['WALL']['maxHP']
                else:
                    continue

    else:
        print('-'*25)
        print('{:^25}'.format('! NOT ENOUGH GOLD !'))
        print('-'*25)

    

#-----------------------------------------
# save_game()
#
#    Saves the game in the file 'save.txt'
#-----------------------------------------
def save_game():
    
    file = open('save.txt','w')

    # SAVE FIELD
    for row in range(rows):
        store_row = '' # stores each row temporarily

        for column in range(columns):

            if field[row][column] != '     ': # if got list in column

                for i in range(len(field[row][column])): # get length of list in column (3)
                    if i == len(field[row][column])-1: 
                        store_row += str(field[row][column][i]) # don't add ';' for last element
                    else:
                        store_row += str(field[row][column][i]) + ';' # add ';' for splitting

                if column != (columns-1): # add ',' behind the unit list if the unit list is not at column 7
                        store_row += ','    

            else:
                if column == (columns-1): 
                    store_row += str(field[row][column]) # don't add ',' to the last column

                else:
                    store_row += str(field[row][column]) +',' # add ',' to each column for splitting

        file.write(store_row + '\n') # write each row to store field
    file.write('---\n')

    # SAVE GAME VARS
    for i in game_vars:
        file.write(str(i) + ':' + str(game_vars[i]) + '\n')

    file.write('---\n')

    # SAVE MONSTERS
    for j in monsters:
        for k in monsters[j]:
            file.write(str(k) + ':' + str(monsters[j][k]) +'\n')
        file.write('---\n')

    # SaVE DEFENDERS
    for j in defenders:
        for k in defenders[j]:
            file.write(str(k) + ':' + str(defenders[j][k]) +'\n')
        file.write('---\n')


    file.close()
    print('-'*25)
    print('{:^25}'.format('Game saved!'))
    print('-'*25)

#-----------------------------------------
# load_game()
#
#    Loads the game from 'save.txt'
#-----------------------------------------
def load_game(game_vars, monsters, defenders):
    
    file = open('save.txt','r')
    field = []

    # FIELD
    for line in file:

        if line == '---\n':
            break

        else:
            line = line.replace('\n','')
            line = line.split(',')

            for i in range(len(line)): 
                if line[i] != '     ': # if column is not blank
                    line[i] = line[i].split(';') # create the unit list

                    for j in range(len(line[i])):
                        
                        if line[i][j].isdigit() == True: # convert HP to integer
                            line[i][j] = int(line[i][j])

                        else:
                            continue

            field.append(line)

        
    # GAME VAR
    for line in file:

        if line == '---\n':
            break

        else:
            line = line.replace('\n','')
            line = line.split(':') # line = ['turn', '0']
    
            for i in range(len(line)):
                game_vars[line[0]] = int(line[1]) # update game_vars dict with saved data

    # ZOMBI
    for line in file:

        if line == '---\n':
            break

        else:
            line = line.replace('\n','')
            line = line.split(':')  # line = ['shortform', 'ZOMBI']

            for i in range(len(line)):

                if line[1].isdigit() == True:
                    monsters['ZOMBI'][line[0]] = int(line[1])

                else:
                    monsters['ZOMBI'][line[0]] = line[1]

    # WWOLF
    for line in file:

        if line == '---\n':
            break

        else:
            line = line.replace('\n','')
            line = line.split(':')  # line = ['shortform', 'WWOLF']

            for i in range(len(line)):

                if line[1].isdigit() == True:
                    monsters['WWOLF'][line[0]] = int(line[1])

                else:
                    monsters['WWOLF'][line[0]] = line[1]

    # ARCHERS
    for line in file:

        if line == '---\n':
            break

        else:
            line = line.replace('\n','')
            line = line.split(':')  # line = ['shortform', 'ARCHR']

            for i in range(len(line)):

                if line[1].isdigit() == True:
                    defenders['ARCHR'][line[0]] = int(line[1])

                else:
                    defenders['ARCHR'][line[0]] = line[1]

    # WALLS
    for line in file:

        if line == '---\n':
            break

        else:
            line = line.replace('\n','')
            line = line.split(':')  # line = ['shortform', 'ARCHR']

            for i in range(len(line)):

                if line[1].isdigit() == True:
                    defenders['WALL'][line[0]] = int(line[1])

                else:
                    defenders['WALL'][line[0]] = line[1]
    
    file.close()
    return field ,game_vars, monsters, defenders

#-----------------------------------------------------
# initialize_game()
#
#    Initializes all the game variables for a new game
#-----------------------------------------------------
def initialize_game():
    game_vars['turn'] = 0
    game_vars['monster_kill_target'] = 20
    game_vars['monsters_killed'] = 0
    game_vars['num_monsters'] = 0
    game_vars['gold'] = 10
    game_vars['threat'] = 0
    game_vars['danger_level'] = 1
    game_vars['upgrade_unit_price'] = 8
    field = [ [None, None, None, None, None, None, None],
              [None, None, None, None, None, None, None],
              [None, None, None, None, None, None, None],
              [None, None, None, None, None, None, None],
              [None, None, None, None, None, None, None] ] # for testing: ['ZOMBI',15,15] ['WWOLF',10,10] ['ARCHR',5,5] ['WALL',20,20]

    monsters = {'ZOMBI': {'shortform': 'ZOMBI',
                      'name': 'Zombie',
                      'maxHP': 15,
                      'min_damage': 3,
                      'max_damage': 6,
                      'moves' : 1,
                      'reward': 2
                      },

            'WWOLF': {'shortform': 'WWOLF',
                      'name': 'Werewolf',
                      'maxHP': 10,
                      'min_damage': 1,
                      'max_damage': 4,
                      'moves' : 2,
                      'reward': 3
                      }
            }

    defenders = {'ARCHR': {'shortform':'ARCHR',
                       'name': 'Archer',
                       'maxHP': 5,
                       'min_damage': 1,
                       'max_damage': 4,
                       'price': 5,
                       },
             
             'WALL': {'shortform':'WALL',
                      'name': 'Wall',
                      'maxHP': 20,
                      'min_damage': 0,
                      'max_damage': 0,
                      'price': 3,
                      }
                      

             }

    return field, monsters, defenders

    

#-----------------------------------------
#               MAIN GAME
#-----------------------------------------


# TO DO: ADD YOUR CODE FOR THE MAIN GAME HERE!

rows = len(field) #5
columns = len(field[0]) #7 
lane = ['A','B','C','D','E']
#unit_list = []
start_game = True
kill_target = 20

while start_game: 
    try:
        show_main_menu()
        main_menu_list = ['start','load','options','quit']
        choice = int(input('Your choice? '))

        if choice <= 0:
            print('-'*25)
            print('{:^25}'.format('! INVALID OPTION !'))
            print('-'*25)
        
        elif main_menu_list[choice-1] == 'start' or main_menu_list[choice-1] == 'load':

            if main_menu_list[choice-1] == 'start':
                field, monsters, defenders = initialize_game()
                game_vars['monster_kill_target'] = kill_target
                game_vars['turn'] = 1
                spawn_monster(field, monster_list)

            # LOAD SAVE
            elif main_menu_list[choice-1] == 'load':
                field, game_vars, monsters, defenders = load_game(game_vars, monsters, defenders)

            # MAIN GAME
            while True:

                draw_field(field)
                show_combat_menu(game_vars)
                combat_menu_list = ['buy','heal','upgrade','end turn','save', 'quit']
                try:
                    choice = int(input('Your choice? '))

                    if choice <= 0:
                        print('-'*25)
                        print('{:^25}'.format('! INVALID OPTION !'))
                        print('-'*25)

                    elif choice == 1106: # CHEAT MODE (for fun only pls ignore)
                        game_vars['gold'] = 999
                        defenders['ARCHR']['min_damage'] = 98
                        defenders['ARCHR']['max_damage'] = 99
                        defenders['ARCHR']['maxHP'] = 99
                        defenders['WALL']['maxHP'] = 99
                        print('-'*45)
                        print('{:^45}'.format('Yoshi! CHEAT MODE ENABLED !!! ᕦ(ò_óˇ)ᕤ'))
                        print('-'*45)
                        continue 

                    # BUY UNIT
                    elif combat_menu_list[choice-1] == 'buy':

                        enough_gold, unit_name = buy_unit(field,game_vars)

                        if enough_gold == True: # enough gold then prompt placement
                            try:

                                position = input('Place where? ').upper()
                                row,column = lane.index(position[0]),int(position[1])-1

                                if place_unit(field,position, row, column): # placement successful will deduct gold
                                    game_vars['gold'] = game_vars['gold'] - unit_name['price']
                                    unit_list = []
                                    unit_list += [unit_name['shortform']] + [unit_name['maxHP']] +[unit_name['maxHP']] 
                                    field[row][column] = unit_list # appendinig units to field
                                    continue

                            except:
                                print('-'*25)
                                print('{:^25}'.format('! INVALID POSITION !'))
                                print('-'*25)
                            

                            

                        elif enough_gold == 'dont buy': # go back to combat menu
                            continue

                        else:
                            print('-'*25)
                            print('{:^25}'.format('! NOT ENOUGH GOLD !'))
                            print('-'*25)

                    # END TURN
                    elif combat_menu_list[choice-1] == 'end turn':
                        game_vars['turn'] += 1
                        game_vars['gold'] += 1
                        game_vars['threat'] += random.randint(1,game_vars['danger_level']) # random threat increase
                        defender_attack(field)
                        lose = monster_advance(field,rows,columns)

                        if game_vars['monsters_killed'] >= game_vars['monster_kill_target']: # if target met
                            print('-------------------------------------')
                            print('You have protected the city! You win!')
                            print('-------------------------------------')
                            print('Thanks for playing! :D')
                            #start_game = False
                            break

                        if game_vars['num_monsters'] == 0:
                            spawn_monster(field,monster_list) # spawn random monster

                        elif lose == True: # if lose == True
                            print('You died.')
                            print('-'*25)
                            print('{:^25}'.format('GAME OVER'))
                            print('-'*25)
                            #start_game = False
                            break


                        if game_vars['threat'] >= game_vars['max_threat']:
                            print('! THREAT METRE MAXED ! New monster spawned.')
                            game_vars['threat'] -= 10
                            spawn_monster(field,monster_list)

                        if game_vars['turn'] % 12 == 0:
                            print('! DANGER LEVEL INCREASED ! Monsters are buffer now!')
                            game_vars['danger_level'] += 1

                            for i in monster_list:
                                monsters[i]['min_damage'] += 1
                                monsters[i]['max_damage'] += 1
                                monsters[i]['reward'] += 1
                                monsters[i]['maxHP'] += 1

                    # HEAL
                    elif combat_menu_list[choice-1] == 'heal':

                        if game_vars['gold'] >= 5: # check enough gold for buying Heal
                            game_vars['gold'] -= 5
                            position = input('Place where? (x to cancel) ').upper()
                        
                            if position == 'X':
                                continue

                            else:

                                try:
                                
                                    row,column = lane.index(position[0]),int(position[1])-1

                                    if len(position) == 2:

                                        if (column <= 2 or column >= 0):
                                        
                                            heal(field, row, column)

                                        else:
                                            print('-'*45)
                                            print('{:^45}'.format('UNITS CAN ONLY BE PLACED IN COLUMNS 1 TO 3.'))
                                            print('-'*45)

                                    else:
                                        print('-'*25)
                                        print('{:^25}'.format('! INVALID POSITION !'))
                                        print('-'*25)

                                except:
                                    print('-'*25)
                                    print('{:^25}'.format('! INVALID POSITION !'))
                                    print('-'*25)

                        else:
                            print('-'*25)
                            print('{:^25}'.format('! NOT ENOUGH GOLD !'))
                            print('-'*25)
                    
                    # UPGRADE UNIT # BONUS
                    elif combat_menu_list[choice-1] == 'upgrade':
                        upgrade_unit()
                        continue
                    
                    # SAVE GAME
                    elif combat_menu_list[choice-1] == 'save':
                        save_game()
                        #start_game = False
                        break

                    # QUIT
                    elif combat_menu_list[choice-1] == 'quit':
                        print('-'*25)
                        print('{:^25}'.format('Goodbye!'))
                        print('-'*25)
                        start_game = False
                        break  
                          
                    
                except:
                    print('-'*25)
                    print('{:^25}'.format('! INVALID OPTION !'))
                    print('-'*25)

        # OPTIONS
        elif main_menu_list[choice-1] == 'options':

            print()
            print('Game options:')
            print('1. Change kill target')
            print('2. Return to main menu.')
            option_list = ['target', 'return']

            try:
                choice = int(input('Your choice? '))

                if choice <= 0:
                    print('-'*25)
                    print('{:^25}'.format('! INVALID OPTION !'))
                    print('-'*25)

                elif option_list[choice-1] == 'target':
                    kill_target = int(input('Kill Target: '))
                    print('Option saved!')
                    continue

                elif option_list[choice-1] == 'return':
                    continue

            except:
                print('-'*25)
                print('{:^25}'.format('! INVALID OPTION !'))
                print('-'*25)

        elif main_menu_list[choice-1] == 'quit':
            print('-'*25)
            print('{:^25}'.format('Goodbye!'))
            print('-'*25)
            start_game = False

    except:
        print('-'*25)
        print('{:^25}'.format('! INVALID OPTION !'))
        print('-'*25)
