spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

# Define a function get_names() that takes a list of spicy_foods and returns a list of strings with the names of each spicy food.
def get_names(spicy_foods):
        # We are working with a dictionary.
        # I want to use list comprehension iterate over each dictionry in spicy_foods list => 'for in' loop. [expression for item in iterable]
        # extract the value associated with the key 'name' => food['name']
        # construct a new list with these values. [Green Curry, Buffalo Wings, Mapo Tofu]
    return [food["name"] for food in spicy_foods]



# Define a function get_spiciest_foods() that takes a list of spicy_foods and returns a list of dictionaries where the heat level of the food is greater than 5.
def get_spiciest_foods(spicy_foods):
    # Goal here is to define a function that takes a list of dictionaries, and returns a new list of dictionaries where each dictionary represents a food with a heat level greater than 5. 
    # 1. function takes in a parameter, which is a list of dictionaries.
    # 2. Iterate over each dictionary
    # 3. Filter the dictionary based on the value of the heat level (greater than 5)
    # 4. Return a new list of dictionaries containing only the dictionaries where heat level is greater than 5.

    # use list comprehension because we want to create a new list based on an existing list. 
    return [food for food in spicy_foods if food["heat_level"] > 5]




def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
            print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')
    

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
         if food["cuisine"] == cuisine:
              return food
    

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)


def get_average_heat_level(spicy_foods):
    # sum = total/count
    return sum([food["heat_level"] for food in spicy_foods]) / len(spicy_foods)
    pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
