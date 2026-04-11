import nbtlib
from datetime import datetime
from pprint import pprint

# path to .dat files
path_level_dat = '/Users/ehen/Library/Application Support/PrismLauncher/instances/26.1.2/minecraft/saves/etl/level.dat'

# load .dat
level_dat = nbtlib.load(path_level_dat)

# pull out desired data
world_name = level_dat['Data']['LevelName']
world_type = level_dat['Data']['GameType']
world_difficulty = level_dat['Data']['difficulty_settings']['difficulty']
is_hardcore = level_dat['Data']['difficulty_settings']['hardcore']
current_dimension = level_dat['Data']['spawn']['dimension']
last_played = level_dat['Data']['LastPlayed']

# dictionary of data
raw_data = {
  'world name': world_name,
  'world type': world_type,
  'hardcore': is_hardcore,
  'world difficulty': world_difficulty,
  'current dimension': current_dimension,
  'last played': last_played,
}

# print dict
pprint(raw_data, indent=4, width=50, sort_dicts=False)