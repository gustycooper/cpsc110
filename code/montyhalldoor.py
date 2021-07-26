from random import choice # choice returns a random value from a list

DEBUG = False
LOOPS = 1000 # number of times to call hall_doors
PICK_VAL = 1
PRIZE_VAL = 2 # PICK_VAL | PRIZE_VAl results in 3

def hall_doors(do_switch):
    doors = [0, 1, 2]
    door_vals = [0, 0, 0]
    prize = choice(doors) # returns a random value from doors
    pick = choice(doors)
    door_vals[prize] |= PRIZE_VAL
    door_vals[pick] |= PICK_VAL # pick and prize the same results in 3 in door_vals
    remove = door_vals.index(0) # 1st door with 0 is not picked nor has prize
    del doors[remove] # doors has two elements at this point
    if do_switch:
        switch_pick = doors[0] if pick == doors[1] else doors[1]
    else:
        switch_pick = pick
    won = door_vals[switch_pick] & 2 == 2
    if DEBUG:
        print("door_vals[", door_vals[0], ',', door_vals[1], ',', door_vals[2], "]", sep='')
        print("doors[", doors[0], ',', doors[1], "]", sep='')
        print("prize: ", prize, "pick:", pick, "switch pick:", switch_pick, "won: ", won)
    return won

count = 0
for i in range(LOOPS):
    count += 1 if hall_doors(True) else 0
print("Switch winning percentage: ", count/LOOPS)

count = 0
for i in range(LOOPS):
    count += 1 if hall_doors(False) else 0
print("Stay winning percentage: ", count/LOOPS)

