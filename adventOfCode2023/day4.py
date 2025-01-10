import re

file_path = "data/day4.txt"
games = []

with open(file_path, 'r') as file:
    for line in file.readlines():

        card = line.split(": ")
        match = re.search(r'\d+', card[0])
        if match:
            index = int(match.group())

        numbers_dict = {}

        numbers = card[1].strip().split(" | ")

        winning_number = numbers[0].strip().split(' ')
        player_number = numbers[1].strip().split(' ')
        numbers_dict['winning'] = [number for number in winning_number if number != '']
        numbers_dict['player'] = [number for number in player_number if number != '']
        numbers_dict['counter'] = 1

        games.append(numbers_dict)

# scores = []

# for index, game in enumerate(games):
#     successes = [number for number in game['player'] if number in game['winning']]
#     print(successes)
#     score = 0
#     if len(successes) > 0:
#         score = 2**(len(successes) - 1)
#     scores.append(score)


for index, game in enumerate(games):
    successes = [number for number in game['player'] if number in game['winning']]
    for j in range(index + 1, index + 1 + len(successes)):
        for k in range(game['counter']):
            games[j]['counter'] += 1


card_sum = sum(d.get('counter', 0) for d in games)
print(card_sum)

