with open('data.txt', 'r') as d:
    lines = d.readlines()

split_lines = {}
for line in lines:
    split_line = line.split(' ')
    split_lines[int(split_line[0])] = split_line[1].strip()

indexes = []
start = 1
while start <= len(split_lines):
    sublist = list(range(start, start + len(indexes) + 1))
    indexes.append(sublist)
    start = start + len(indexes)

secret = []
for sub_list in indexes:
    secret.append(split_lines[sub_list[-1]])

secret_sentence = " ".join(secret)
print(secret_sentence)
