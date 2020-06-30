#Ntombekazi Sibetyu
from car_data import cars
from car_class import Cars

#defining a function that will display the second set of options when option 1 ischosen from the first questions
def second_options():

    #getting the car id of the car the user wants
    user_input = int(input("Please type in the car id\n"))

    #getting the action that the user wants to do with the car
    second_option = int(input("""Please select an option
    1. Display the properties of the car
    2. Calculate fuel usage
    3. Calculate resell value
    4. Go back to main menu
    
    answer:"""))


    #when the option 1 is selected, program must look for the car in the dictionary using the id the user typed in
    if second_option == 1:

        for car in cars:
            if cars['id'] == user_input:
                print(car)

    #when option 2 is selected,calculate the resell value and display
    if second_option == 2:
        selected_car = Cars(car.car_id,car.year_model,car.distance_driven,car.base_price,
                            car.tank_size,car.kilometers_per_tank,car.make)
        selected_car.resell_value()

    #when the option 3 is selected, calculate the fuel usage for the car and display
    if second_option == 3:
        selected_car.fuel_usage()

    if second_option == 4:
        exit()




