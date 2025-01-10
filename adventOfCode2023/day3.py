file_path = "data/day3.txt"
line_list = []
symbols = set()
sequences = {
    'numbers': [],
    'symbols': []
}

with open(file_path, 'r') as f:
    for line in f.readlines():
        line_list.append(list(line.strip()))

        numbers_seq = []
        symbols_seq = []
        start_index = None

        for i, char in enumerate(line):
            # PART 1
            # if char != '.' and not char.isdigit() and char != '\n':
            #     symbols.add(char)

            # PART 2
            if char == "*":
                symbols.add(char)

            if char.isdigit():
                if start_index is None:
                    start_index = i
            elif start_index is not None:
                numbers_seq.append((start_index, i - 1))
                start_index = None
            if char in symbols:
                symbols_seq.append(i)

        if start_index is not None:
            numbers_seq.append((start_index, len(line) - 1))
        sequences['numbers'].append(numbers_seq)
        sequences['symbols'].append(symbols_seq)


def get_true_concatenated_tuples(numbers_list, symbols_list, lines):
    result = []

    for index, number_tuples in enumerate(numbers_list):
        temp = []
        for number_tuple in number_tuples:
            range_start, range_end = number_tuple
            symbol_values = symbols_list[index - 1 if index > 0 else 0] + symbols_list[index] + symbols_list[index + 1 if index < len(symbols_list) - 1 else len(symbols_list) - 1]

            if any(range_start-1 <= value <= range_end+1 for value in symbol_values):
                digits = ''.join(lines[index][range_start:range_end + 1])
                temp.append(int(digits))
        result.append(temp)

    return result


def get_gear_ratio(numbers_list, symbols_list, lines):
    result = []

    for index, number_tuples in enumerate(numbers_list):
        temp = []
        for number_tuple in number_tuples:
            range_start, range_end = number_tuple
            symbol_values = symbols_list[index - 1 if index > 0 else 0] + symbols_list[index] + symbols_list[index + 1 if index < len(symbols_list) - 1 else len(symbols_list) - 1]

            if any(range_start-1 <= value <= range_end+1 for value in symbol_values):
                temp.append(number_tuple)
        result.append(temp)

    return result



# PART 1

# parts = get_true_concatenated_tuples(sequences['numbers'], sequences['symbols'], line_list)
# print(parts)
# print(sum(parts))

# PART 2

parts = get_gear_ratio(sequences['numbers'], sequences['symbols'], line_list)
print(parts)
print(sequences['symbols'])
