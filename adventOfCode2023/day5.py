filepath = 'data/day5.txt'

with open(filepath, 'r') as f:
    maps = []
    map = []

    for line in f.readlines():
        line = line.strip()

        if line:
            map.append(line)
        elif map:
            maps.append(map)
            map = []

    if map:
        maps.append(map)

# PART 1
# seeds = [int(seed) for seed in maps[0][0].split(': ')[1].split(' ')]

# PART 2
seeds_list = [int(seed) for seed in maps[0][0].split(': ')[1].split(' ')]
seed_maps = [seeds_list[i:i+2] for i in range(0, len(seeds_list), 2)]

locations = []
break_outer = False

location = 0
for seed_map in seed_maps:
    # PART 1
    # for seed in seeds:
    for seed in range(seed_map[0], seed_map[0] + seed_map[1]):
        print("seed", seed)
        location = seed
        for map_data in maps[1:]:
            try:
                temp_location = [row[0] + (location - row[1]) for row in [list(int(i) for i in line.split()) for line in map_data[1:]] if location in range(row[1], row[1] + row[2])][0]
                if temp_location < location:
                    location = temp_location
            except IndexError:
                pass

print("minimum:", location)