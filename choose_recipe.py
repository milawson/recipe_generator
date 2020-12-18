# User chooses recipe from results
def choose_recipe(possible_recipes):

    chosen_recipe_title = None
    
    try:
        
        # User must enter a recipe title that is Type: string
        while not isinstance(chosen_recipe_title, str):

            chosen_recipe_title = input(f'\nPlease enter the title of the recipe you would you like to make: ')

        # If the title matches, the recipe object is returned
        if chosen_recipe_title in possible_recipes:

            return possible_recipes[chosen_recipe_title]

        # If title does not match, a key error is raised because it is not in the possible recipes (dictionary data structure)
        else:

            raise KeyError(chosen_recipe_title)

    # The key error is handled by first printing the incorrect title, then shows the user possible titles, then recursively calls
    # the function again, prompting the user to reselect a valid recipe title.
    except KeyError as recipe_title:
        
        print(f'\nKeyError: {recipe_title} is not a valid recipe title. Valid titles include:\n')

        for key in possible_recipes:
            print(f'{key}')

        print(f'\nPlease try again... \n')
        
        return choose_recipe(possible_recipes)




    
    