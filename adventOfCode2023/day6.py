filepath = 'data/day6.txt'

with open(filepath, 'r') as f:
    lines = f.readlines()
    # PART 1
    time_values = [int(value) for value in lines[0].split(':')[1].strip().split()]
    distance_values = [int(value) for value in lines[1].split(':')[1].strip().split()]
    # race_tuples = [(time, distance) for time, distance in zip(time_values, distance_values)]

    # PART 2
    time_value = int(''.join(map(str, time_values)))
    distance_value = int(''.join(map(str, distance_values)))

# PART 1
races_options = 0
# for race_tuple in race_tuples:
#     race_options = 0
#     for time in range(race_tuple[0]):
#         if time * (race_tuple[0] - time) > race_tuple[1]:
#             race_options += 1
#     if races_options:
#         races_options *= race_options
#     else:
#         races_options = race_options

# PART2
for time in range(time_value):
    if time * (time_value - time) > distance_value:
        races_options += 1

print(races_options)
