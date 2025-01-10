import pandas as pd
import re

file_path = "data/day2.txt"
data = {}

with open(file_path, 'r') as file:
    for line in file.readlines():
        result = []

        game = line.split(":")
        match = re.search(r'\d+', game[0])
        if match:
            index = int(match.group())

        counts = game[1].strip().split("; ")

        for item in counts:
            color_dict = {}
            items_split = item.split(', ')
            for element in items_split:
                quantity, color = element.split(' ')
                color_dict[color] = int(quantity)
            result.append(color_dict)

        data[index] = result


flattened_data = [(key, color, value) for key, color_dict_list in data.items() for color_dict in color_dict_list for color, value in color_dict.items()]

df = pd.DataFrame(flattened_data, columns=['key', 'color', 'value'])

pivot_df = df.pivot_table(index='key', columns='color', values='value', aggfunc='max')

pivot_df = pivot_df.fillna(0).astype(int)

# PART 2

products_series = pivot_df.product(axis='columns')
total_power = sum(list(products_series))
print(total_power)

# PART 1

thresholds = {'blue': 14, 'green': 13, 'red': 12}

threshold_mask = (pivot_df > pd.Series(thresholds, index=pivot_df.columns)).any(axis=1)

filtered_df = pivot_df[~threshold_mask]

sum_of_indices = sum(list(filtered_df.index))


print(sum_of_indices)

