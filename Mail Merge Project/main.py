with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()
    names = [name.rstrip() for name in names]
with open("./Input/Letters/starting_letter.txt") as file:
    letter_text = file.read()
for name in names:
    new_letter_text = letter_text.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}", "w") as letter:
        letter.write(new_letter_text)
