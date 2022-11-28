## This program allows the user to select from the main menu
## Its implementation is in the main_menu function
## New functions in this script:
##  1. register_driver()
##  2. register_vehicle()
##  3. register_passenger()
##  4. register_trip()
##  1. view_drivers()
##  1. view_drivers()
##  1. view_drivers()
##  1. view_drivers()
##  9. exit_program()
##
## Note that the functions for viewing and registering just display a statement
## These functions shall be implemented later
## exit_program() function is implemented - around Line 57

#importing time allows us to user time.sleep(5) in the exit_program() function - Line 57
import time

def register_vehicle():
    print("This funtion registers a vehicle")


def register_driver():
    print("This funtion registers a driver")


def register_passenger():
    print("This funtion registers a passenger")


def register_trip():
    print("This funtion registers a trip")


def view_vehicles():
    print("This functions allows viewing of registered vehicles")


def view_passengers():
    print("This functions allows viewing of registered passengers")


def view_drivers():
    print("This functions allows viewing of registered drivers")


def view_trips():
    print("This functions allows viewing of registered trips")


def exit_program():
    print("Exiting program in 5 seconds...")
    
    # Program waits for 5 seconds before program it terminated
    time.sleep(5)

    #program is terminated using the exit() function
    exit()


def main_menu():
    menu = """
    ************************************************************
    *                                                          *
    *                MALKIA TRANSPORTERS LIMITED               *
    *                                                          *
    ************************************************************
    *                                                          *
    *  1. Register Vehicle                                     *
    *  2. Register Driver                                      *
    *  3. Register Passenger                                   *
    *  4. Register Trip                                        *
    *  5. View Registered Vehicles                             *
    *  6. View Registered Drivers                              *
    *  7. View Registered Passengers                           *
    *  8. View Registered Trips                                *
    *  0. Exit Program                                         *
    *                                                          *
    ************************************************************
    """
    print(menu)
    
    # How to take user input and convert it into an integer
    # Try to use choice = input("Select a choice from the main menu: ") and see what happens
    choice = int(input("Select a choice from the main menu: "))
    
    # A good use of the if..else statement. Remember there is no switch..case in Python
    if choice == 1:
        register_vehicle()

    elif choice == 2:
        register_driver()

    elif choice == 3:
        register_passenger()

    elif choice == 4:
        register_trip()

    elif choice == 5:
        view_vehicles()

    elif choice == 6:
        view_drivers()

    elif choice == 7:
        view_passengers()

    elif choice == 8:
        view_trips()

    elif choice == 0:
        exit_program()

    else:
        print("Invalid input. Try again next time...")


def welcome_statement():
    statement = """
    ************************************************************
    *                                                          *
    *                MALKIA TRANSPORTERS LIMITED               *
    *                                                          *
    ************************************************************
    *                                                          *
    *  Welcome to Malkia Transporters Limited. We offer        *
    *  transporation services countrywide ranging from parcels *
    *  to passengers.                                          *
    *                                                          *
    *             `` Your comfort is our pride ``              *
    *                                                          *
    ************************************************************
    """
    print(statement)

def main():
    welcome_statement()
    main_menu()

if __name__ == '__main__':
    main()
