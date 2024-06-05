from write import write_land_data

def rent_land(lands_data, lands_data_dictionary):
    """
    Allows users to rent land from the available options.

    Args:
        lands_data (list): A list of lists containing land information.
        lands_data_dictionary (dict): A dictionary mapping land IDs to their details.
    
    Returns:
        list: A list containing details of the lands rented by the user. Each element
        of the list is a list containing information about a rented land, including
        kitta number, rented time (in months), and other details.

    Allows users to select and rent land from the available options. It presents
    a list of lands with their details such as kitta number, location, direction, aana,
    price, and availability. The user can input the kitta number of the land they want
    to rent along with the rental period in months. The function validates user inputs
    to ensure correctness. Once rented, the availability status of the land is updated
    to 'Not Available' in both the `lands_data` list and the `lands_data_dictionary`.
    The function also writes the updated land data back to the file.

    Returns a list containing details of the lands rented by the user. Each element of
    the list is a list containing information about a rented land, including kitta number,
    rented time (in months), and other details.

    Note:
        - This function depends on the availability of the `write_land_data` function,
          which should be defined elsewhere in the code.
        - User inputs are validated to ensure correct data entry.

    Raises:
        Any exceptions raised by the underlying functions may propagate up to this function.
    """
    rent_data = []
    # Using loop to let user select multiple lands
    while True:
        # Printing Land data
        print("\nChoose the lands you want to rent from below")
        print("Please Select Which Lands You Want To Rent\n")
        print("----------------------------------------------------------------------------------------------------------")
        print("Kitta No.\tLocation\tDirection\tAana\t\tPrice\t\tAvailability\t\t|")
        print("----------------------------------------------------------------------------------------------------------")

        for land_info in lands_data:
            for details in land_info:
                # Add enough spaces to make the columns aligned
                print(f"{details.ljust(12)}", end="\t")
            print("\t|")
        print("----------------------------------------------------------------------------------------------------------")
        # Letting user Select land by taking input from them
        error = True
        # Running loop till user inputs a valid kitta no
        while error == True:
            kitta_no = input("Enter the kitta no of land you want to rent: ")
            # Tries to find the key in our land dictionary
            try:
                if lands_data_dictionary[kitta_no]["availability"] == "Not Available":
                        print("Land is unavailable at the moment!")
                else:
                    # break the loop if available
                    error = False
            # If the key is not present i.e. the land kitta no is not in our file then message is printed
            except: 
                print("Enter a valid kitta no!")
            
        # Rent time for how much user is renting
        error = True
        while error == True:
            try:
                rented_time = input("Enter for how many months you want to rent this land: ")
                print(rented_time)
                if int(rented_time) > 0:
                    error = False
                else:
                    print("Please enter a valid number!")
            except:
                print("Please enter a valid number!2")
            
            
        # Using loop till user specifies the exact aana that is available
        error = True
        while error == True:
            aana = input("Enter the aana for land you are renting: ")
            if lands_data_dictionary[kitta_no]["aana"] == aana:
                error = False
            else:
                print("You must rent the exact aana that is available")
    
        # Changing the data of selected land to Not Available
        for land_info in lands_data:
            if land_info[0] == kitta_no:
                land_info[5] = "Not Available"
        lands_data_dictionary[kitta_no]["availability"] = "Not Available"
        
        # Updating Data to the lands.txt file
        rent_data.append([kitta_no, rented_time, 0, False])
        write_land_data(lands_data)
        
        # Asking user if they want more lands to rent
        yes_no = input("Do you want to rent more lands? (Y/N): ")
        if yes_no.upper() == "N":
            break
    return rent_data

def return_land(lands_data, lands_data_dictionary):
    """
    Allows users to return land that they had previously rented.

    Args:
        lands_data (list): A list of lists containing land information.
        lands_data_dictionary (dict): A dictionary mapping land IDs to their details.

    Returns:
        list: A list containing details of the lands returned by the user. Each element
        of the list is a list containing information about a returned land, including
        kitta number, rented time (in months), returned time (in months), and a boolean
        indicating if the land was successfully returned.

    Allows users to select and return land that they had previously rented. It presents
    a list of lands that are currently not available (i.e., already rented) along with
    their details such as kitta number, location, direction, aana, price, and availability.
    The user can input the kitta number of the land they want to return along with the
    rented time and returned time (both in months). The function validates user inputs
    to ensure correctness. Once returned, the availability status of the land is updated
    to 'Available' in both the `lands_data` list and the `lands_data_dictionary`. The
    function also writes the updated land data back to the file.

    Returns a list containing details of the lands returned by the user. Each element of
    the list is a list containing information about a returned land, including kitta number,
    rented time (in months), returned time (in months), and a boolean indicating if the land
    was successfully returned.

    Note:
        - This function depends on the availability of the `write_land_data` function,
          which should be defined elsewhere in the code.
        - User inputs are validated to ensure correct data entry.

    Raises:
        Any exceptions raised by the underlying functions may propagate up to this function.
    """
    rent_data = []
    # Using loop to let user select multiple lands
    while True:
        # Printing Land data
        print("\nChoose the lands you want to return from below")
        print("Please Select Which Lands You Want To Return\n")
        print("----------------------------------------------------------------------------------------------------------")
        print("Kitta No.\tLocation\tDirection\tAana\t\tPrice\t\tAvailability\t\t|")
        print("----------------------------------------------------------------------------------------------------------")

        for land_info in lands_data:
            if land_info[5] == "Not Available":
                for details in land_info:
                    # Add enough spaces to make the columns aligned
                    print(f"{details.ljust(12)}", end="\t")
                print("\t|")
        print("----------------------------------------------------------------------------------------------------------")
        # Letting user Select land by taking input from them
        error = True
        # Running loop till user inputs a valid kitta no
        while error == True:
            kitta_no = input("Enter the kitta no of land you want to return: ")
            # Tries to find the key in our land dictionary
            try:
                if lands_data_dictionary[kitta_no]["availability"] == "Available":
                        print("Enter a valid kitta no of land to return")
                else:
                    # break the loop if available
                    error = False
            # If the key is not present i.e. the land kitta no is not in our file then message is printed
            except: 
                print("Enter a valid kitta no of land to return")
            
        # Rent time for how much user is renting
        error = True
        while error == True:
            try:
                rented_time = input("Enter for how many months you had rented this land: ")
                returned_time = input("Enter for after how many months you have returned this land: ")
                if int(rented_time) > 0 and int(returned_time) > 0:
                    error = False
                else:
                    print("Please enter a valid number!")
            except:
                print("Please enter a valid number!")
    
        # Changing the data of selected land to Not Available
        for land_info in lands_data:
            if land_info[0] == kitta_no:
                land_info[5] = "Available"
        lands_data_dictionary[kitta_no]["availability"] = "Available"
        
        # Updating Data to the lands.txt file
        rent_data.append([kitta_no, rented_time, returned_time, True])
        write_land_data(lands_data)
        
        # Asking user if they want more lands to rent
        yes_no = input("Do you want to return more lands? (Y/N): ")
        if yes_no.upper() == "N":
            break
    return rent_data