import colorgram

filename = input("Gimme the path to your image:\n")
colors = colorgram.extract(filename, 10)
rbg_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    turtle_color = (r, g, b)
    rbg_colors.append(turtle_color)
