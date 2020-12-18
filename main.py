
from display_recipes import display_recipes  #import display_recipes(dietary_recipes)
from choose_recipe import choose_recipe 
from food_parameters import food_parameters  #import food_parameters(included_ingredients, excluded_ingredients, dietary_requirements, food_intolerances, cuisines)
from api_get_results import api_get_results
from recipe_to_file import recipe_to_file



def main():
    
    try:

        # Create variable based on user entered parameters
        search_parameters = food_parameters()

        # Create variable of raw recipe results from user parameters 
        my_request = api_get_results(search_parameters)

        # Format recipe objects and display
        my_recipe_results = display_recipes(my_request)

        # User selects recipe
        chosen_recipe = choose_recipe(my_recipe_results)

        # Chosen recipe can be added to existing or new recipe book
        recipe_to_file(chosen_recipe) 

    # This catches all errors from the programs and alerts the user the an error occured    
    except Exception as exception:

        print(f'\n{exception}: An error occurred. Please try again later...')

if __name__ == '__main__':
    main()
