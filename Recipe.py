# Recipe object is created to easily access recipe information
class Recipe:

    
    def __init__(self, recipe_search_result):
        
        # List of all dictionaries containing nutritional information
        recipe_nutrition = recipe_search_result['nutrition']['nutrients']
        
        # Most important recipe information is assigned to attributes
        self.title = recipe_search_result['title']
        self.summary = recipe_search_result['summary']
        self.ingredients = recipe_search_result['nutrition']['ingredients']
        self.ready_in_minutes =  recipe_search_result['readyInMinutes']
        self.servings = recipe_search_result['servings']
        self.all_nutrition = recipe_nutrition
        
        # Dictionary attribute about nutrition in the following format: 
        # {"title": string of item, "amount": float, "unit": string of unit like g or mg, "percentOfDailyNeeds": float}
        self.calories_per_serving = recipe_nutrition[0]
        self.fat_per_serving = recipe_nutrition[1]
        self.saturated_fat_per_serving = recipe_nutrition[2]
        self.carbohydrates_per_serving = recipe_nutrition[3]
        self.sugar_per_serving = recipe_nutrition[5]
        self.cholesterol_per_serving = recipe_nutrition[6]
        self.sodium_per_serving = recipe_nutrition[7]
        self.protein_per_serving = recipe_nutrition[8]

        # List of dictionaries containing [{'step': instruction, 'number': step#}...]
        self.instructions = recipe_search_result['analyzedInstructions'][0]['steps']
        

    # Recipe method is created so that a recipe step can be changed
    def change_step(self, step_number, step, time_difference = 0):

        self.instructions[step_number]['step'] = step
        self.ready_in_minutes += time_difference


    # Formatted recipe is created printed or str() is used
    def __str__(self):
        
        ingredients_string = ''
        instructions_string = ''
        
        # Formats ingredients into a string where the ingredient, amounts and units are entered on a new line each time
        for i in range(len(self.ingredients)):
            amount = self.ingredients[i]['amount']
            units = self.ingredients[i]['unit']
            ingredient = self.ingredients[i]['name']
            ingredients_string += f'{amount} {units} {ingredient}\n'

        # Formats instructions into a string where the step number and step instruction is entered on a new line each time
        for step in self.instructions:
            step_number = step['number']
            step = step['step']
            instructions_string = instructions_string + f'{step_number}. {step}\n'

        # Returns a fully formatted recipe as a string for printing
        return (f'_________________________________{self.title}_________________________________\n\n' \
                    f'Ready in {self.ready_in_minutes} minutes\n\n' \
                        f'Summary: {self.summary}\n\n' \
                            + 'Nutrition:\n{title}: {amount} {unit} ({percentOfDailyNeeds}% of Daily Value)\n'.format(**self.calories_per_serving) \
                                + '{title}: {amount} {unit} ({percentOfDailyNeeds}% of Daily Value)\n'.format(**self.fat_per_serving) \
                                    + '{title}: {amount} {unit} ({percentOfDailyNeeds}% of Daily Value)\n'.format(**self.saturated_fat_per_serving) \
                                        + '{title}: {amount} {unit} ({percentOfDailyNeeds}% of Daily Value)\n'.format(**self.carbohydrates_per_serving) \
                                            + '{title}: {amount} {unit} ({percentOfDailyNeeds}% of Daily Value)\n'.format(**self.sugar_per_serving) \
                                                + '{title}: {amount} {unit} ({percentOfDailyNeeds}% of Daily Value)\n'.format(**self.cholesterol_per_serving) \
                                                    + '{title}: {amount} {unit} ({percentOfDailyNeeds}% of Daily Value)\n'.format(**self.sodium_per_serving) \
                                                        + '{title}: {amount} {unit} ({percentOfDailyNeeds}% of Daily Value)\n\n'.format(**self.protein_per_serving)
                                                            + f'Ingredients:\n{ingredients_string}\n' \
                                                                f'Instructions:\n{instructions_string}\n\n\n')