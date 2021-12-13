import sys, os
sys.path.append(os.path.abspath("."))
import aoc

# I hate knapsack

capacity = 100
ingredients = {}

for line in aoc.aoc():
    [name, _, capacity, _, durability, _, flavor, _, texture, _, calories] = line.replace(",", "").split(" ")
    ingredients[name[0:-1]] = (int(capacity), int(durability), int(flavor), int(texture), int(calories))

def optimize(available_ingredients, capacity, recipe = {}):

    if sum(map(lambda ingredient: ingredients[ingredient][4]*recipe[ingredient], recipe.keys())) > 500:
        return 0

    if capacity == 0 or len(available_ingredients) == 0:

        capacity, durability, flavor, texture, calories = 0, 0, 0, 0, 0

        for ingredient in recipe.keys():
            capacity += recipe[ingredient]*ingredients[ingredient][0]
            durability += recipe[ingredient]*ingredients[ingredient][1]
            flavor += recipe[ingredient]*ingredients[ingredient][2]
            texture += recipe[ingredient]*ingredients[ingredient][3]
            calories += recipe[ingredient]*ingredients[ingredient][4]

        score = max(capacity, 0) * max(0, durability) * max(0, flavor) * max(0, texture) * (calories == 500)
        
        #print(recipe, score, "|", capacity, durability, flavor, texture)
        return score # score of recipe
    
    ingredient_to_use = available_ingredients[0]
    left_ingredients = available_ingredients[1:]

    max_score = 0
    for usage in range(0 if len(left_ingredients) != 0 else capacity, capacity+1):
        recipe_cpy = dict(recipe)
        recipe_cpy[ingredient_to_use] = usage
        score = optimize(left_ingredients, capacity-usage, recipe_cpy)
        if score > max_score:
            max_score = score
    return max_score

print(f"The best recipe with exactly 500 calories has a total score of {optimize(list(ingredients.keys()), 100, {})}")