import uuid
import struct

player_uuid = [-835314499, 1463189310, -1736693748, 385857499]

def uuid_from_ints(int_array):
  bytes_data = struct.pack('>iiii', *int_array)
  return uuid.UUID(bytes=bytes_data)

real_player_id = uuid_from_ints(player_uuid)
print(f'player_{real_player_id}.json')
