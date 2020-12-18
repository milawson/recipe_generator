import os

# Prints chosen recipe to a user's recipe book
def recipe_to_file(recipe):

    try:

        # Enter folder path for where file should be saved
        save_path = input('Where would you like to save the folder? Enter in the folder path: ') 
        #An example path is: /Users/mitchelllawson/Documents/Northeastern University/Education/CS5001 Intensive Foundations/Mastery Project/Recipes Modular Final

        # Raise error if folder path doesn't exist
        if not os.path.exists(save_path):
            raise FileNotFoundError(save_path)

        # Enter user's name, so recipe can be added to their book
        user_name = input('Who\'s recipe book is this (e.g. What is your name)? ')
        
        #Raise error if user name is not Type: string
        if not isinstance(user_name, str):
            raise TypeError(user_name)
    
        # Creates file name
        file_name = user_name + '\'s' + ' Recipes.txt'
        
        # Folder path + file name
        complete_path = os.path.join(save_path, user_name + "\'sRecipeBook.txt") 
        
        print(f'Your recipe will be saved to {complete_path}')

        # Appends recipe if file already exists
        if os.path.exists(complete_path):
            with open(complete_path, 'a') as contents:
                contents.write(str(recipe))
                print(f'Success! The recipe has been added to your existing recipe book {user_name}!')

        # Creates a new recipe book otherwise
        else:
            with open(complete_path, 'w') as contents:
                contents.write(str(recipe))
                print(f'Success! You have added this recipe to a new book {user_name}!')
 
    # Exceptions below are for possible errors that coule be encountered while reading, writing, appending, finding file path, etc.
    
    # If a type error is raised because user enters a non-string, the function is recursively called so that the user can re-enter
    # a string input
    except FileNotFoundError as folder_path:
        print(f'"{folder_path}" is an incorrect folder path. Please try again...\n\n')
        recipe_to_file(recipe)
    except TypeError as name:
        print(f'file_name: "{name}" must be a string. Please try again...\n\n')
        recipe_to_file(recipe)
    except PermissionError:
        print(f'Permission denied when trying to open {file_name}')
    except OSError:
        print(f'An error occurred while checking {file_name}')
