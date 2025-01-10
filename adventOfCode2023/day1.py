calibers = []
numbers = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
}
with open("data/day1.txt", 'r') as f:
    for line in f.readlines():
        caliber_list = []
        for index, char in enumerate(line):
            if char.isdigit():
                caliber_list.append(char)
                continue
            for number, value in numbers.items():
                if number in line[index:index+len(number)]:
                    caliber_list.append(value)
        caliber_string = caliber_list[0] + caliber_list[-1]
        caliber = int(caliber_string)
        calibers.append(caliber)

print(calibers)
print(sum(calibers))
