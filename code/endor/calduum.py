from endorsmints import *
from random import random, randint

# meteor computes if a meteor hits an if so, the reduced population
# input
#  pop - population
# output
#  population
#  num of ewoks killed by meteor
#  num of ewoks that swam away
#  
def meteor(pop):
    meteor_hit = random()
    if meteor_hit <= game_params["METEOR_HIT"]:
        meteor_kill = int(pop * game_params["METEOR_KILL"])
        swam_away = int(pop * game_params["SWAM_AWAY"])
        pop = pop - (meteor_kill + swam_away)
        return pop, meteor_kill, swam_away
    else:
        return pop, 0, 0
# harvest computes the bushels of smints harvested
# input
#  planted - acres planted
# output
#  bushels of smints harvested
#  bushels per acre (bpa)
def harvest(planted):
    bpa = randint(game_params["YIELD_LOW"], game_params["YIELD_HIGH"])
    return planted * bpa, bpa

# womprat computes if womprat comes and if so how much they ate
# input
#  smints - bushels of smints in storage
# output
#  bushels of smints ate by womprat
def womprat(smints):
    womprat_swam = random()
    if womprat_swam <= game_params["WOMPRAT_SWAM"]:
        atepercent = randint(game_params["EAT_LOW"], game_params["EAT_HIGH"]) / 100
        womprat_ate = int(smints * atepercent)
        smints = smints - womprat_ate
        return womprat_ate
    else:
        return 0
        
# landvalue computes the value of an acre of land
# input
#  none
# ouput
#  value in smints of an acre of land
def landvalue():
    return randint(game_params["VAL_LOW"], game_params["VAL_HIGH"])

# immigration computes number of immigrant Ewoks
# input
#  acres - acres of farm land owned
#  smints - smints in storage
#  pop - population of Ewoks
# output
#  number of immigrant Ewoks
def immigration(acres, smints, pop):
    return int(((20 * acres + smints) / (100 * pop) + 1) * random())

game_params = {}
def init_params():
    infile = open('calduum_params.txt',"r")
    for line in infile:
        param, param_type, param_value = line.split()
        if param_type == 'float':
            param_value = float(param_value)
        else:
            param_value = int(param_value)
        game_params[param] = param_value
    infile.close()

# The output is constructing by concatenating out_lines and out_ints
# out_lines is a list of strings preceding numbers
out_lines = [
'Princess Leia, you are leading Calduum Island in the year ',
'The following events happened during the year ',
'* Num of Ewoks fed this year : ',
'* Num Ewoks starved to death : ',
'* Num Ewoks swam to Calduum  : ',
'* Num Ewoks Swam from Calduum: ',
'* Num Ewoks killed by meteors: ',
'* Bushels of Smĭnts from sell: ',
'* Bushels of Smĭnts from buy : ',
'* Bushels Womp rats destroyed: ',
'* Bushels of Smĭnts harvested: ',
'* Bushels of Smĭnts per acre : ',
'Calduum values at the end of the year ',
'* Your Ewok Population is    : ',
'* Num of Acres of Land Owned : ',
'* Land value bushels per acre: ',
'* Bushels of Smĭnts n storage: ',
]

# Global variables that represent the state of Calduum
# simulateYear() updates these variables
year = 1000
population = 100
acres_owned = 1000
smints_per_acre = 20
smints_in_storage = 3000

# out_ints is concatenated on out_lines
out_ints = [
year,              # year
year,              # year
0,                 # num of Ewoks fed
0,                 # num of Ewoks starved
0,                 # num of Ewoks swam to to Calduum
0,                 # num of Ewoks swam away from Calduum
0,                 # num of Ewoks killed by meteors
0,                 # bushels of smints from sale of land
0,                 # bushels of smints used in buy of land
0,                 # bushels of smints womp rats destroyed
0,                 # smints harvested
0,                 # bushels per acre
year,              # year
population,        # population of Ewoks
acres_owned,       # num of acres owned
smints_per_acre,   # land value in smints per acre
smints_in_storage, # num of bushels of smints in storage
]

def simulateYear(a2buy, a2sell, b2feed, a2plant):
    print("simulateYear", a2buy, a2sell, b2feed, a2plant)
    global year, population, acres_owned, smints_per_acre, smints_in_storage
    t_smints_in_storage = smints_in_storage # do not change global until all error checks pass
    # do you have enough acres to sell and plant
    if a2sell + a2plant > acres_owned:
        return False, "Error, a2sell:a2plant:acres_owned", str(a2sell) + ':' + str(a2plant) + ':' + str(acres_owned)
    # do you have enough Ewoks to plant acres
    if a2plant > (population * game_params["EWOK_CAN_PLANT"]):
        return False, "Error, a2plant:pop can plant:", str(a2plant) + ':' + str(population * game_params["EWOK_CAN_PLANT"])
    # Action 1: perform buying land action
    smints_spent_on_land = a2buy * smints_per_acre
    if smints_spent_on_land > smints_in_storage:
        return False, "Error, smints spent:smints_in_storage:", str(smints_spent_on_land) + ':' + str(smints_in_storage)
    t_smints_in_storage -=  smints_spent_on_land
    # do you have enough smints in storage to plant acres
    smints_planted = a2plant * game_params["BUSHELS_FOR_PLANTING"]
    if smints_planted > t_smints_in_storage:
        return False, "Error, a2plant:smints_planted:smint_in_storage", str(a2plant) + ':' + str(smints_planted) + ':' + str(t_smints_in_storage)
    t_smints_in_storage -= smints_planted
    # Action 2: perform farming action
    bushels_harvested, bushels_per_acre = harvest(a2plant)
    t_smints_in_storage += bushels_harvested
    # Action 3: perform sell land action
    from_land_sold = a2sell * smints_per_acre
    t_smints_in_storage += from_land_sold
    # Action 4: perform womp rat action
    rats_destroyed = womprat(smints_in_storage)
    t_smints_in_storage -= rats_destroyed
    # Did the user select b2feed that is less the smints in storage
    if b2feed > t_smints_in_storage:
        return False, "Error, b2feed:smints_in_storage", str(b2feed) + ':' + str(smints_in_storage)
    # Error checks done, update global variable
    smints_in_storage = t_smints_in_storage
    # Action 5: feed Ewoks
    smints_in_storage = smints_in_storage - b2feed
    smints_needed = population * game_params["SMINTS_PER_EWOK"]
    ewoks_fed = b2feed // game_params["SMINTS_PER_EWOK"]
    if smints_needed <= b2feed:
        starved = 0
        swam_to = immigration(acres_owned, smints_in_storage, population)
        population = population + swam_to
    else:
        starved = population - ewoks_fed
        swam_to = 0
        population = population - starved
    if population <= 52:
        return False, "Game Over", "Goodbye"
    # Action 6: Compute acres owned
    acres_owned = acres_owned + a2buy - a2sell
    # Action 7: Check for meteor
    population, meteors_killed, swam_away = meteor(population)
    # Action 8: Computer landvalue for next year
    smints_per_acre = landvalue()
    year = year + 1
    if year >= 1010:
        return False, "Congratulations, you won!", "Great Job"
    global out_ints
    out_ints = [year,year,ewoks_fed,starved,swam_to,swam_away,meteors_killed,from_land_sold,-smints_spent_on_land,rats_destroyed,bushels_harvested,bushels_per_acre,year,population,acres_owned,smints_per_acre,smints_in_storage]
    return True, out_lines, out_ints
