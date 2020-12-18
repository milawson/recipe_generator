
def food_parameters(): 

    # Initialize search parameters dictionary
    food_parameters = {}

    # Initialize user inputs for while loop
    included_ingredients_input = None
    excluded_ingredients_input = None
    dietary_requirements_input = None
    food_intolerances_input = None
    cuisine_input = None

    # Possible user options to determine whether parameter is used or not
    user_options = ['yes', 'no']

    # User prompted to answer "yes" or "no" if search parameter is relevant to them
    # If yes, user is asked to enter more information used in the search results
    print(f'\nAnswer preliminary questions with "yes" or "no", then answer the subsequent questions with comma ("," or ", ") separated values.')
    while included_ingredients_input not in user_options:
        included_ingredients_input = input(f'\nAre there specific ingredients that you would like to use? Please answer "yes" or "no": ').lower()
        if included_ingredients_input == 'yes':
            included_ingredients = input('What ingredients do you have in the fridge that you would like to include? (Examples include: tomato, onion, garlic, thyme, etc.) ').lower()
            food_parameters['includeIngredients'] = included_ingredients.split(', ' or ',')

    while excluded_ingredients_input not in user_options:
        excluded_ingredients_input = input(f'\nLet us know if there\'s any ingredients that you would like to exclude from possible recipes? Please answer "yes" or "no": ').lower()
        if excluded_ingredients_input == 'yes':
            excluded_ingredients = input('What are the ingredients that you would like to exclude? (Examples include: tomato, peanuts, garlic, thyme, etc.) ')
            food_parameters['excludeIngredients'] = excluded_ingredients.split(', ')

    while dietary_requirements_input not in user_options:
        dietary_requirements_input = input(f'\nDo you have any type of dietary requirements? Please answer "yes" or "no": ').lower()
        if dietary_requirements_input == 'yes':
            dietary_requirements = input('What is your dietary requirement? (Examples include: pescetarian, vegan, vegetarian, ketogenic, etc.) ')
            food_parameters['diet'] = dietary_requirements.split(', ')

    while food_intolerances_input not in user_options:
        food_intolerances_input = input(f'\nDo you have any food intolerances? Please answer "yes" or "no": ').lower()
        if food_intolerances_input == 'yes':
            food_intolerances = input('What food intolerances do you have? (Examples include: dairy, egg, gluten, peanut, shellfish, etc.) ')
            food_parameters['intolerances'] = food_intolerances.split(', ')
    
    while cuisine_input not in user_options:
        cuisine_input = input(f'\nDo you have a cuisine (region) preference? Please answer "yes" or "no": ').lower()
        if cuisine_input == 'yes':
            cuisine = input('What cuisine are you interested in? (Examples include: Greek, French, Italian, Chinese, etc.) ')
            food_parameters['cuisine'] = cuisine.split(', ')

    return food_parameters