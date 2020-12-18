from Recipe import Recipe

# Recipes are displayed and formatted into recipe objects
def display_recipes(dietary_recipe_results):

    recipes = {}
    recipe_count = 0
    partition = f'_________________________________________________________________________________________________________'

    # Creates formatted recipes from search results and places them in dictionary where:
    # {'recipe title': recipe_object}
    # If no instructions are included: recipe is skipped
    for i in range(len(dietary_recipe_results)):
        if len(dietary_recipe_results[i]['analyzedInstructions']) > 0:
            recipe_count += 1
            recipe = Recipe(dietary_recipe_results[i])
            recipes[recipe.title] = recipe
            print(f'{partition}\n\n' \
                f'{recipe_count}. {recipe.title}\n\n' \
                        + '{title}: {amount} {unit} per serving ({percentOfDailyNeeds}% of daily needs)\n'.format(**recipe.calories_per_serving) \
                            + f'Ready in {recipe.ready_in_minutes} minutes\n\n' \
                                f'Summary: {recipe.summary}\n')
    
    print(partition)

    return recipes



        
        
