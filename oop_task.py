#Ntombekazi Sibetyu OOP Task
#from the car_data file import the cars dictionary and th function list_cars
from car_data import cars, list_cars
from cars import second_options

#defining a function that will dispaly the first options and take in the answer of the option from user
def first_options():
    option = int(input("""Please select an option below by typing the option number
    
    1. Select a car based on their id
    2. Display all of the cars in the database
    3. Exit
    answer:"""))

    #when option 1 is chosen, the second options function will be called and will display the second set of options
    if option == 1:

        return second_options()

    #when option 2 is selected the list cars function wll be called to display the whole list of cars in the dicttionary
    if option == 2:
        return list_cars()

    #any other answer typed in the program will exit code
    else:
        exit()

first_options()