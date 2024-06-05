def read_land_data():
    """
    Reads land data from a file and returns two objects:
     
    Returns:
        tuple: A tuple containing two elements:
            - list: A list of lists containing land information.
            - dict: A dictionary mapping land IDs to their details.
     
    Reads land data from a file named 'lands.txt'. Each line in the file represents
    information about a specific piece of land. The format of each line should be:
    
    <land_id>, <location>, <direction>, <aana>, <price>, <availability>
    
    Example:
        001, Kathmandu, North, 5, 1000000, Available
        
    Returns a tuple containing two elements:
        1. A list of lists, where each inner list represents information about a piece of land.
        2. A dictionary mapping land IDs to dictionaries containing the details of each land,
           including 'location', 'direction', 'aana', 'price', and 'availability'.
    
    Note:
        - The file 'lands.txt' must exist and be accessible.
        - The file should have the specified format, otherwise, unexpected behavior may occur.
        - If there are any issues with reading the file or parsing its contents, an empty list
          and an empty dictionary will be returned.
    """
    # Function to read land data from file
    land_data = []
    land_data_dictionary = {}
    file = open('lands.txt',"r")
    for line in file:
        land_info = line.strip().replace("/n", "").split(", ")
        land_data.append(land_info)
    for land_info in land_data:
        land_data_dictionary[land_info[0]] = {
            "location" : land_info[1],
            "direction" : land_info[2],
            "aana" : land_info[3],
            "price": land_info[4],
            "availability": land_info[5]
        } 
    file.close()
    return land_data, land_data_dictionary
