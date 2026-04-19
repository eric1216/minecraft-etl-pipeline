from datetime import datetime
from config import root_path
import nbtlib
import json
import os

timestamp = datetime.now().strftime('%Y-%m-%d')
dump_path = f'dump/{timestamp}'
os.makedirs(dump_path, exist_ok=True)

# .dat default for converting objects to json readable format
def nbt_serialize(obj):
    if isinstance(obj, (list, tuple)):
        return list(obj)
    if isinstance(obj, dict):
        return {k: nbt_serialize(v) for k, v in obj.items()}
    if isinstance(obj, (int, float, str, bool, type(None))):
        return obj
    if hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes)):
        return list(obj)
    return str(obj)

# dump .dat into a json file
def dump_dat(dat, file_name):
  try:
    json.dump(dat, open(f'{dump_path}/{file_name}', 'w'), indent=2, default=nbt_serialize)
    print(f'{file_name}.json saved')
  except (IOError, OSError) as e:
    print(f'File error: {e}')
  except TypeError as e:
    print(f'Cant serialize: {e}')
  except Exception as e:
    print(f'Unknown error: {e}')

# path to .dat files
world_name = 'etl'
level_dat_path = f'{root_path}/minecraft/saves/{world_name}/level.dat'
player_dat_dir = f'{root_path}/minecraft/saves/{world_name}/players/data/'
player_stats_dir = f'{root_path}/minecraft/saves/{world_name}/players/stats/'

# get world .dat file
level_dat = nbtlib.load(level_dat_path)
dump_dat(level_dat, 'level_dat')

# get each players .dat file
for player_file in os.listdir(player_dat_dir):
  if player_file.endswith('.dat'):
    player_dat = nbtlib.load(os.path.join(player_dat_dir, player_file))
    uuid = player_file.removesuffix('.dat')
    dump_dat(player_dat, f'player_{uuid}.json')

# copy the player stats json
for stats_file in os.listdir(player_stats_dir):
    if stats_file.endswith('.json'):
        with open(os.path.join(player_stats_dir, stats_file), 'r') as infile:
            data = json.load(infile)
        dump_dat(data, f'stats_{stats_file}')
