from datetime import datetime, timezone

def write_land_data(lands_data):
    """
    Writes the updated land data into the 'lands2.txt' file in an arranged format.
    
    Args:
        lands_data (list): The updated list of land data.
    
    Writes the updated land data into the 'lands2.txt' file in a structured format.
    Each line in the file represents information about a specific piece of land.
    The format of each line is:
    
    <land_id>, <location>, <direction>, <aana>, <price>, <availability>
    
    Example:
        001, Kathmandu, North, 5, 1000000, Available

    Note:
        - The file 'lands2.txt' will be overwritten with the updated land data.
        - Ensure that the format of the land data in the list `lands_data` matches the
          expected format, otherwise, unexpected behavior may occur.
    """
    with open("lands.txt", "w") as file:
        for land_info in lands_data:
            file.write(", ".join(land_info) + "\n")
            
def generate_invoice(name, contact_no, rent_data, lands_data_dictionary):
    """
    Generates an invoice for land renting transactions.

    Args:
        name (str): The name of the customer.
        contact_no (str): The contact number of the customer.
        rent_data (list): A list containing details of the rented lands.
        lands_data_dictionary (dict): A dictionary mapping land IDs to their details.

    Generates an invoice for land renting transactions based on the provided
    customer name, contact number, rented land data, and land information.
    The function calculates the total rent for each rented land and the grand total.
    It prints the invoice details in the command line interface and also creates
    a text file containing the invoice details.

    Note:
        - The invoice text file is named using the current UTC time in ISO 8601 format
          with timezone information.
        - The file contains detailed information about the rented lands, including kitta number,
          location, direction, aana, price, rental period, fine (if applicable), and total cost.
        - The grand total includes the total cost of all rented lands.

    Raises:
        Any exceptions raised during file writing may propagate up to this function.
    """
    grandTotal = 0
    isReturned = rent_data[0][3]
    # Get the current UTC time
    current_time_utc = datetime.now(timezone.utc)
    # Convert the current UTC time to ISO 8601 format with timezone information
    iso_string = current_time_utc.isoformat().replace(":", "-")
    
    # Printing invoice in the CL
    print("\nInvoice")
    print("----------------------------------------------------Invoice---------------------------------------------------------------------------")
    print("TechnoPropertyNepal Land Renting System")
    print(f"Name: {name}")
    print(f"Contact no: {contact_no}")
    print(f"Date: {iso_string}")
    print("--------------------------------------------------------------------------------------------------------------------------------------")
    if isReturned == False:
        print("Kitta No.\tLocation\tDirection\tAana\t\tPrice\t\tMonth\t\tTotal")
    else:
        print("Kitta No.\tLocation\tDirection\tAana\t\tPrice\t\tMonth\t\tFine\t\tTotal")
    print("--------------------------------------------------------------------------------------------------------------------------------------")
    for data in rent_data:
        print(f"{data[0].ljust(12)}", end="\t")
        for key, value in lands_data_dictionary[data[0]].items():
            if key != "availability":
                print(f"{value.ljust(12)}", end="\t")
        print(f"{data[1].ljust(12)}", end="\t")
        if isReturned == True:
            fine = 0
            month_diff = int(data[2]) - int(data[1])
            total = int(data[1]) * int(lands_data_dictionary[data[0]]['price'])
            if month_diff >= 0:
                fine = (month_diff * int(lands_data_dictionary[data[0]]['price'])) + ((month_diff * 10)/100) * (month_diff * int(lands_data_dictionary[data[0]]['price']))
            print(f"{str(fine).ljust(12)}", end="\t")
            print(f"{fine + total}")
            # Finding the grandTotal
            grandTotal += fine + total
        else:
            print(f"{int(data[1])*int(lands_data_dictionary[data[0]]['price'])}") 
            # Finding the grandTotal
            grandTotal += int(data[1])*int(lands_data_dictionary[data[0]]["price"])
        
    print("--------------------------------------------------------------------------------------------------------------------------------------")
    print(f"\nGrandTotal: {grandTotal}")
    

    # Creating a new .txt for every invoice
    file = open(f"{iso_string}.txt", "w")
    file.write("----------------------------------------------------Invoice---------------------------------------------------------------------------------------------------------------------\n")
    file.write("TechnoPropertyNepal Land Renting System\n")
    file.write(f"Name: {name}\n")
    file.write(f"Contact no: {contact_no}\n")
    file.write(f"Date: {iso_string}\n")
    file.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    if isReturned == False:
        file.write("Kitta No.\t\tLocation\t\tDirection\t\tAana\t\t\tPrice\t\t\tMonth\t\t\tTotal\n")
    else:
        file.write("Kitta No.\t\tLocation\t\tDirection\t\tAana\t\t\tPrice\t\t\tMonth\t\t\tfine\t\t\tTotal\n")
    file.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    for data in rent_data:
        file.write(f"{data[0].ljust(12)}\t\t")
        for key, value in lands_data_dictionary[data[0]].items():
            if key != "availability":
                file.write(f"{value.ljust(12)}\t\t")
        file.write(f"{data[1].ljust(12)}\t\t")
        if isReturned == True:
            month_diff = int(data[2]) - int(data[1])
            if month_diff >= 0:
                fine = (month_diff * int(lands_data_dictionary[data[0]]['price'])) + ((month_diff * 10)/100) * (month_diff * int(lands_data_dictionary[data[0]]['price']))
            total = int(data[1]) * int(lands_data_dictionary[data[0]]['price'])
            file.write(f"{str(fine).ljust(12)}\t\t")
            file.write(f"{fine + total}\n")

        else:
            file.write(f"{int(data[1])*int(lands_data_dictionary[data[0]]['price'])}\n")
            
    file.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    file.write(f"GrandTotal: {grandTotal}\n")
    print("Invoice txt file also has been generated")
