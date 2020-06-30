"""
This is the file containg our car data.

This data should be converted into the three different classes,
based on their make.

For simplicity's sake you have access to a function,
that will return a list of class dictionaries based on their make.

You are welcome to not use the given function but rather use the list of cars yourself.

The dictionary structure is as follows:
{
    id,
    year_model,
    distance_driven,
    base_price,
    tank_size,
    kilometers_per_tank,
    make
}

Refer to the function's docstring for its usage.

NB: if you do not convert this data into the requried class instances then you will get 0
"""

def get_cars_based_on_make(make):
    """
    This function takes a string as input and will filter the list of cars,
    and return the list of filtered cars.

    Options: 'Volkswagen', 'Mercedes', 'Toyota'
    """
    filtered_cars = []
    for car in cars:
        if car['make'] == make:
            filtered_cars.append(car)
    return filtered_cars

# This is our list of cars, written as a list containing a dictionary for each car
# This is in this format instead of a file or database for ease of use

cars = [
    {
        'id': 1,
        'year_model': 1995,
        'distance_driven': 240000,
        'base_price': 200000,
        'tank_size': 30,
        'kilometers_per_tank': 100,
        'make': 'Volkswagen'
    },
    {
        'id': 2,
        'year_model': 2010,
        'distance_driven': 10000,
        'base_price': 300000,
        'tank_size': 20,
        'kilometers_per_tank': 120,
        'make': 'Volkswagen'
    },
    {
        'id': 3,
        'year_model': 2017,
        'distance_driven': 300000,
        'base_price': 900000,
        'tank_size': 15,
        'kilometers_per_tank': 80,
        'make': 'Volkswagen'
    },
    {
        'id': 4,
        'year_model': 1982,
        'distance_driven': 560000,
        'base_price': 50000,
        'tank_size': 25,
        'kilometers_per_tank': 150,
        'make': 'Mercedes'
    },
    {
        'id': 5,
        'year_model': 2012,
        'distance_driven': 30000,
        'base_price': 500000,
        'tank_size': 20,
        'kilometers_per_tank': 90,
        'make': 'Mercedes'
    },
    {
        'id': 6,
        'year_model': 2019,
        'distance_driven': 10000,
        'base_price': 1000000,
        'tank_size': 15,
        'kilometers_per_tank': 100,
        'make': 'Mercedes'
    },
    {
        'id': 7,
        'year_model': 2000,
        'distance_driven': 600000,
        'base_price': 250000,
        'tank_size': 25,
        'kilometers_per_tank': 200,
        'make': 'Toyota'
    },
    {
        'id': 8,
        'year_model': 2015,
        'distance_driven': 30000,
        'base_price': 350000,
        'tank_size': 20,
        'kilometers_per_tank': 100,
        'make': 'Toyota'
    },
    {
        'id': 9,
        'year_model': 2018,
        'distance_driven': 2000,
        'base_price': 800000,
        'tank_size': 25,
        'kilometers_per_tank': 200,
        'make': 'Toyota'
    },
]

def list_cars():
    for car in cars:
        print(car)


