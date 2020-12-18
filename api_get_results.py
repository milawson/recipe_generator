import requests 
import json
from food_parameters import food_parameters

#Processes user's food parameters into an API request for recipes
def api_get_results(food_search_parameters):
    
    try:
        # Static search result parameters are set here:
        headers = {'Content-Type': 'application/json'}
        api_key = 'apiKey=115e405dea1f4f1db24f29b516a1f179'
        search_URL = 'https://api.spoonacular.com/recipes/complexSearch?'
        add_recipe_nutrition = 'addRecipeNutrition=True'
        instructions_required = 'instructionsRequired=True'
        
        # Iterate through food parameters to create a string for the api request
        for key in food_search_parameters.keys():
            items = ',+'.join(food_search_parameters[key])
            search_URL += f'&{key}={items}'

        # I create the URL used for the request
        request_URL = search_URL + '&' + add_recipe_nutrition + '&' + instructions_required + '&' + api_key
        response = requests.get(request_URL, headers)
        dietary_recipes_raw = response.json()
        dietary_recipe_results = dietary_recipes_raw['results']

        # If there are no results in the request, a ValueError is raised because there must be >= 1 recipe result
        if len(dietary_recipe_results) == 0:
            raise ValueError

        return dietary_recipe_results

    # Becuase a ValueError is raised when there are no results returned, the user will automatically be able to try again with new search parameters
    except ValueError:
        print(f'\nThere were no results from the API as there were too many search parameters or incorrect parameters entered. Try again...\n' \
            f'1. By answering "no" to one of the prompts for included ingredients, excluded ingredients, dietary requirements, food intolerances or cuisines, or...\n' \
                f'2. Reduce your inputs for each question, or...\n' \
                    f'3. Ensure you entered and spelled parameters correctly.')
        return api_get_results(food_parameters())

    # If there are any errors raised from accessing the API, the error and message will be printed to the user
    except Exception as exception:
        print(f'{exception}: There was an error accessing the API')

