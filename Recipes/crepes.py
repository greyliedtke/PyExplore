from allrecipes import AllRecipes


crepe_url = 'https://www.allrecipes.com/recipe/16383/basic-crepes/'

detailed_recipe = AllRecipes.get(crepe_url)  # Get the details of the first returned recipe (most relevant in our case)

# Display result :
print("## %s :" % detailed_recipe['name'])  # Name of the recipe

for ingredient in detailed_recipe['ingredients']:  # List of ingredients
    print("- %s" % ingredient)

for step in detailed_recipe['steps']:  # List of cooking steps
    print("# %s" % step)