import Scraper
import re


def get_recipe(soup):
    recipe = {}
    results = soup.find("div", class_="post recipe")

    # RECIPE'S TITLE
    recipe_title = results.find("h1", class_="heading-1").text.strip()
    recipe["Title"] = recipe_title

    # RECIPE'S PREP & COOK TIME
    prep_and_cook_times_div = results.find("div", class_="cook-and-prep-time")
    prep_and_cook_times = prep_and_cook_times_div.findAll("time")
    prep_time = prep_and_cook_times[0].text.strip()
    cook_time = prep_and_cook_times[1].text.strip()
    recipe["Prep time"] = prep_time
    recipe["Cook time"] = cook_time

    # RECIPE'S SERVINGS
    servings_str = results.find("div", class_="post-header__servings") \
        .find("div", class_="icon-with-text__children") \
        .text.strip()
    servings = re.findall(r'\d', servings_str)
    recipe["Serves"] = servings[0]

    # RECIPE'S INGREDIENTS
    ingredients_section = results.find("section", class_="recipe__ingredients")
    ingredients_sections = ingredients_section.findAll("section")
    ingredients = {}
    for section in ingredients_sections:

        if section.find("h3", class_="heading-5") is None:
            section_title = "Main ingredients"
        else:
            section_title = section.find("h3", class_="heading-5").text.strip()

        section_ingredients = section.findAll("li", class_="list-item")

        section_ingredient_arr = []
        for section_ingredient in section_ingredients:
            section_ingredient = section_ingredient.text.strip()

            words = re.findall(r'\w+', section_ingredient)
            if words[0][-1] == 'g' or words[0][-1] == 'l':
                quantity = re.findall(r'\w+(?=[g ])|\w+(?=[l ])', words[0])[0]
                quantifier = words[0][-1]
                type_of_ingredient = ' '.join(words[1:])
            else:
                quantity = words[0]
                if words[1] == "egg":
                    quantifier = ' '.join(words[1:])
                    type_of_ingredient = "egg"
                else:
                    quantifier = words[1]
                    type_of_ingredient = ' '.join(words[2:])

            ingredient_dict = {"quantity": quantity, "quantifier": quantifier, "of": type_of_ingredient}
            section_ingredient_arr.append(ingredient_dict)
        ingredients[section_title] = section_ingredient_arr

    recipe["Ingredients"] = ingredients

    # RECIPE'S METHOD
    method_section = results.find("section", class_="recipe__method-steps")
    method_step_list = method_section.find("ul", class_="grouped-list__list")
    method_steps = method_step_list.findAll("li", class_="list-item")

    steps = []
    for method_step in method_steps:
        content = method_step.find("div", class_="editor-content").find("p").text.strip()
        steps.append(content)

    recipe["Method"] = steps

    # RETURN
    return recipe


class BbcGoodFoodScraper:
    def __init__(self, url):
        soup = Scraper.get_html(url)
        print(get_recipe(soup))
        # TODO: Store the recipe with a function from Scraper
