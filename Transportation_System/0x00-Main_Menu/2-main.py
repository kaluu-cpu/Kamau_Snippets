## This program allows the user to select different choices as many times as they like
##
## This is done by the use of an infinite loop using the while statement
## Remember infinite loops? Whoever told you they are very bad is a partial liar.
##
## Its implementation is in the main_menu() function
## No new functions created here
## Remember that we have added line 71 only...see how a single line of code changes everything?
##
## I have also added code for clearing the screen to make stuff spicier
## Can your create a separate function for clearing the screen and call it when needed?

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
    time.sleep(5)
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

    # True will forever be true, hence making it an infinite loop
    while True:
        # Try to remove this line to understand what it is doing here
        time.sleep(1)

        # This line clears the screen
        print("\033[2J\033[1;1H")
        
        print(menu)
        choice = int(input("Select a choice from the main menu: "))
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
            print("Invalid input. Please try again")


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
