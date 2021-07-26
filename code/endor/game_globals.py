# The output is constructing by concatenating out_lines and out_ints
# out_lines is a list of strings preceding numbers
out_lines = [
'Princess Leia, you are leading Calduum Island in the year ',
'The following events happened during the year ',
'* Ewoks Starved to death: ',
'* Ewoks Swam to Calduum: ',
'* Ewoks Swam away from Calduum: ',
'* Ewoks killed by Teeny-weeny-meteors: ',
'* Womp rats destroyed: ',
'* Bushels of Smĭnts harvested: ',
'* Bushels per acre: ',
'Calduum values at the end of the year ',
'* Ewok Population: ',
'* Acres of Land Owned: ',
'* Land value per acre: ',
'* Bushels of Smĭnts in storage: ',
]

# Global variables that represent the state of Calduum
# simulateYear() updates these variables
starved = 0
swam_to = 0
swam_away = 0
meteors_killed = 0
rats_destroyed = 0
bushels_harvested = 0
bushels_per_acre = 0
year = 1000
population = 100
land_owned = 1000
land_value = 20
smints_in_storage = 3000

# out_ints is concatenated on out_lines
out_ints = [
year,
year,
starved,
swam_to,
swam_away,
meteors_killed,
rats_destroyed,
bushels_harvested,
bushels_per_acre,
year,
population,
land_owned,
land_value,
smints_in_storage
]
