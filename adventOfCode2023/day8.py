# array = []
# mapping_dict = {}
# filepath = 'data/day8.txt'
#
# with open(filepath, 'r') as file:
#     lines = file.readlines()
#
# for line in lines:
#     line = line.strip()
#
#     if line:
#         parts = line.split(' = ')
#         if not array:
#             array = [1 if letter == 'R' else 0 for letter in parts[0]]
#         else:
#             key = parts[0].strip()
#             value_str = parts[1].strip()
#             value = tuple(map(str.strip, value_str.strip('()').split(',')))
#             mapping_dict[key] = value
#
# print("Array:", array)
# print("Dictionary:", mapping_dict)
#
# index = 0
# iterations = 0
# step = 'AAA'
# while step != 'ZZZ':
#     step = mapping_dict[step][array[index]]
#     iterations += 1
#     index = (index + 1) % len(array)
#
# print(iterations)
array = []
mapping_dict = {}
filepath = 'data/day8.txt'

with open(filepath, 'r') as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()

    if line:
        parts = line.split(' = ')
        if not array:
            array = [1 if letter == 'R' else 0 for letter in parts[0]]
        else:
            key = parts[0].strip()
            value_str = parts[1].strip()
            value = tuple(map(str.strip, value_str.strip('()').split(',')))
            mapping_dict[key] = value

print("Array:", array)
print("Dictionary:", mapping_dict)

nodes_step = [key for key in mapping_dict if key.endswith('A')]

iterations = 0
index = 0
while any(node_step[-1] != 'Z' for node_step in nodes_step):
    nodes_step = [mapping_dict[node_step][array[index]] for node_step in nodes_step]
    iterations += 1
    print(iterations)
    index = (index + 1) % len(array)


print("Iterations:", iterations)
with open('result.txt', 'w') as r:
    r.write(str(iterations))
