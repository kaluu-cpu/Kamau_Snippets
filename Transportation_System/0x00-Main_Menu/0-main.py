def main_menu():
    # Observe the use of triple quotes
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
    # We are going to display this menu herein below
    print(menu)

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
    #we are going to display this welcome statement herein below
    print(statement)

def main():
    #observe how the functions are called and their code is executed
    welcome_statement()
    main_menu()


#######################################################
#                                                     #
#     OUR PROGRAM STARTS EXECUTING FROM HERE          #
#         decorated to attract attention              #
#                                                     #
#######################################################
if __name__ == '__main__':
    #redirected to the main function
    main()
