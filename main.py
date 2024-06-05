from read import read_land_data
from operation import rent_land, return_land
from write import generate_invoice

def main():
    """ 
    Main function to run the TechnoPropertyNepal Land Renting System.
    
    Reads land data from a file using the `read_land_data` function. Then, it presents
    a menu for users to choose options like renting land, returning land, or exiting the system.
    It interacts with the user through the command line interface.

    Note:
        - This function relies on other functions such as `read_land_data`, `rent_land`,
          `return_land`, and `generate_invoice`, which should be defined elsewhere in the code.
        - Ensure that the user inputs are properly handled to avoid potential errors.

    Raises:
        Any exceptions raised by the underlying functions may propagate up to this function.

    Example:
        Running `main()` will start the TechnoPropertyNepal Land Renting System.
        It will display a menu prompting the user to choose options until they decide to exit.
    """
    lands_data, lands_data_dictionary = read_land_data()
    
    print("Welcome to TechnoPropertyNepal Land Renting System")
    while True:
        print("\nPlease Choose an option")
        print("\n1. Rent Land")
        print("2. Return Land")
        print("3. Exit")
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            name = input("\nEnter your name: ")
            contact_no = input("Enter your contact number: ")
            print("Renting Land")
            rent_data = rent_land(lands_data, lands_data_dictionary)
            generate_invoice(name, contact_no, rent_data, lands_data_dictionary)
            
        elif choice == "2":
            name = input("\nEnter your name: ")
            contact_no = input("Enter your contact number: ")
            print("Returning Land")
            rent_data = return_land(lands_data, lands_data_dictionary)
            generate_invoice(name, contact_no, rent_data, lands_data_dictionary)
            
        elif choice == "3":
            print("\nThank you for using TechnoPropertyNepal Land Renting System!")
            break
        else:
            print("Invalid choice. Please try again.")

main()