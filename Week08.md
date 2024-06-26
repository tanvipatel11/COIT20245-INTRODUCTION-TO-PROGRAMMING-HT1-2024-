
# WEEK 8

# ##Task 1 Display Menu##
 
print("Task 1 Display Menu")

def display_menu():

    print("Menu:")
    print("a. Print help menu")
    print("b. Exit the program")

# Explanation of TASK 1 

This code defines a display_menu() function that prints out the menu options for the application. 
The main() function currently only calls display_menu() for debugging purposes.

# ##Task 2 User Input##

print("Task 2 User Input")

def display_menu():
   
    print("Menu:")
    print("a. Print help menu")
    print("b. Exit the program")

def main():
    
    display_menu()  
    while True:
        user_input = input("wildlife> ")
        if user_input == 'help':
            display_menu()  
        elif user_input == 'exit':
            print("Exiting the program.")
            return  
        else:
            print("Invalid command. Please enter 'help' or 'exit'.")
if __name__ == "__main__":
    main()

# Explanation of TASK 2

# Task 2 involves handling user input in the Queensland Wildlife Sightings Application. Let's delve into the theory behind this task:

**User Input Handling:** In any interactive application, user input is crucial. Task 2 focuses on capturing and processing user input to enable users to interact with the application and perform various tasks.

**Input Functionality:** The application needs to prompt the user for input in a clear and user-friendly manner.

It should provide options for the user to choose from and handle different types of input, such as text or numerical values.

**User Interface Design:** While the application might not have a graphical user interface (GUI), it still needs to provide a text-based interface that guides users through the available options and allows them to make selections.

**Error Handling:** Task 2 also involves error handling to ensure that the application gracefully handles invalid input from the user. This includes detecting input errors and providing appropriate feedback to the user to correct them.

Integration with Application Logic: Once user input is captured, it needs to be processed and integrated with the application's logic to perform the desired actions.

This might involve calling specific functions or methods based on the user's input.

**Iterative Interaction:** The application should continue to prompt the user for input until they explicitly choose to exit or perform another action that terminates the interaction loop.

**Testing and Debugging:** As with any part of software development, Task 2 requires thorough testing and debugging to ensure that user input is captured and processed correctly under various scenarios.


# ##Task 3 List Species in City (Stub)##

def display_menu():

    print("Menu:")
    print("a. Print help menu")
    print("b. Exit the program")
    print("c. Display animal species in a city")

def search_species(city):

    return [
        {"Species": {"TaxonID":"2336","AcceptedCommonName": "dolphin", "PestStatus": "Nil"}},
        {"Species": {"TaxonID":"655","AcceptedCommonName": "snake", "PestStatus": "Venomous"}}
    ]

def display_species(species_list):
  
    print("Species found:")
    for species in species_list:
        name = species["Species"]["AcceptedCommonName"]
        status = species["Species"]["PestStatus"]
        Tax = species["Species"]["TaxonID"]
        print(f"TaxonID: {Tax} , Name: {name}, Pest Status: {status}")

def main():
   
    display_menu() 
    while True:
        user_input = input("wildlife> ")
        if user_input == 'help':
            display_menu()  
        elif user_input == 'exit':
            print("Exiting the program.")
            return  
        elif user_input.startswith('species'):
            city = user_input.split(maxsplit=1)[1].strip()  
            species_list = search_species(city)  
            display_species(species_list)  
        else:
            print("Invalid command. Please enter 'help', 'exit', or 'species <city>'.")


if __name__ == "__main__":
    main()
    
# Explanation of TASK 3

# Functionality Description:

The system needs to display a list of species recorded for a given city. For example, searching for Cairns might return species like dolphins and whipsnakes.

Each species is represented by a dictionary structure containing fields such as TaxonID, AcceptedCommonName, and PestStatus.

**Menu Update:**

Update the display_menu() function to include an option for displaying animal species in a city. 

**Search Species Function:**

Implement a function named search_species(city) that takes the name of a city as input and returns a list of nested species dictionaries.

**Display Species Function:**

Implement a function named display_species(species_list) that takes a list of species dictionaries as input and prints the list of species to the screen.

Decide on an appropriate format for displaying each species. You can choose to display species names, TaxonIDs, PestStatus, or any other relevant information.

**Update Main Function:**

Update the main() function to accept the command "species" followed by a city name.

When this command is received, call the search_species(city) function to retrieve the list of species for the specified city.

Then, call the display_species(species_list) function to print the list of species to the screen.

For now, this function can be implemented as a stub that returns a predefined list of species dictionaries, regardless of the input city.

# ##Task 4 List Animal Sightings in City (Stub)##

# Task 4 Start #

def display_menu():
    print("Menu:")
    print("a. Print help menu")
    print("b. Exit the program")
    print("c. Display animal species in a city")
    print("d. Display animal sightings in a city")

def search_species(city):
    
    return [

       {"Species": {"TaxonID":"1036","AcceptedCommonName": "dolphin", "PestStatus": "Nil"}},
       {"Species": {"TaxonID":"236","AcceptedCommonName": "snake", "PestStatus": "Venomous"}}
    ]

def display_species(species_list):
    print("Species found:")
    for species in species_list:
        name = species["Species"]["AcceptedCommonName"]
        status = species["Species"]["PestStatus"]
        Tax = species["Species"]["TaxonID"]
        print(f"TaxonID: {Tax} , Name: {name}, Pest Status: {status}")

def search_sightings(taxonid, city):
   
    return [
        {"properties": {"Taxonid":"1020","StartDate": "2003-06-22", "LocalityDetails": "Kew","SiteCode":"Incidental"}},
        {"properties": {"Taxonid":"2120","StartDate": "1996-09-21", "LocalityDetails": "Murrumbeena","SiteCode":"Incidental"}},
        {"properties": {"Taxonid":"630","StartDate": "1999-11-15", "LocalityDetails": "Tinaroo","SiteCode":"Incidental"}}
    ]

def display_sightings(sightings):

    print("Animal sightings:")
    for sighting in sightings:
        taxonid = sighting["properties"]["Taxonid"]
        start_date = sighting["properties"]["StartDate"]
        locality = sighting["properties"]["LocalityDetails"]
        sitecode = sighting["properties"]["SiteCode"]
        print(f"taxonid: {taxonid},Start Date: {start_date}, Locality: {locality},sitecode: {sitecode}")

def main():
    
    display_menu()  # Display the initial help menu
    while True:
        user_input = input("wildlife> ")
        if user_input == 'help':
            display_menu()
        elif user_input == 'exit':
            print("Exiting the program.")
            return
        elif user_input.startswith('species'):
            city = user_input.split(maxsplit=1)[1].strip()
            species_list = search_species(city)  
            display_species(species_list)  
        elif user_input.startswith('sightings'):
            _, species, city = user_input.split(maxsplit=2)
            sightings = search_sightings(species, city)  
            display_sightings(sightings)
        else:
            print("Invalid command. Please enter 'help', 'exit', 'species <city>', or 'sightings <species>, <city>'.")

# Debugging and testing the main() function

if __name__ == "__main__":
    main()
# Task 4 End #
# # To run your code you want to type this in command 
# sighthins species melbourne # 



# ##Task 5 List Venomous Animal Sightings in a City##

# Task 5 Start #

def display_menu():
    """
    Display the menu options for the wildlife sighting program.
    """
    print("Menu:")
    print("a. Print help menu")
    print("b. Exit the program")
    print("c. Display animal species in a city")
    print("d. Display animal sightings in a city")
    print("e. Display venomous species")

def search_species(city):
    # Stub implementation, will be replaced with actual functionality
     return [
       {"Species": {"TaxonID":"1023","AcceptedCommonName": "dolphin", "PestStatus": "Nil"}},
       {"Species": {"TaxonID":"562","AcceptedCommonName": "snake", "PestStatus": "Venomous"}}
    ]

def display_species(species_list):
    print("Species found:")
    for species in species_list:
        name = species["Species"]["AcceptedCommonName"]
        status = species["Species"]["PestStatus"]
        Tax = species["Species"]["TaxonID"]
        print(f"TaxonID: {Tax} , Name: {name}, Pest Status: {status}")

def search_sightings(taxonid, city):
    # Stub implementation, will be replaced with actual functionality
    return [
        {"properties": {"StartDate": "1998-11-15", "LocalityDetails": "Tinaroo"}}
    ]

def display_sightings(sightings):

    print("Animal sightings:")
    for sighting in sightings:
        start_date = sighting["properties"]["StartDate"]
        locality = sighting["properties"]["LocalityDetails"]
        print(f"Start Date: {start_date}, Locality: {locality}")

def filter_venomous(species_list):

    return [species for species in species_list if species["Species"]["PestStatus"] == "Venomous"]

def main():
    display_menu()  # Display the initial help menu
    while True:
        user_input = input("wildlife> ").strip().lower()  
        if user_input == 'help':
            display_menu()  
        elif user_input == 'exit':
            print("Exiting the program.")
            return  
        elif user_input.startswith('species'):
            if 'venomous' in user_input:
                city = user_input.split(maxsplit=1)[1].split()[0] 
                species_list = search_species(city)  
                venomous_species = filter_venomous(species_list)  
                display_species(venomous_species)  
            else:
                city = user_input.split(maxsplit=1)[1].strip()  
                species_list = search_species(city)  
                display_species(species_list)  
        elif user_input.startswith('sightings'):
            _, species, city = user_input.split(maxsplit=2)  
            sightings = search_sightings(species, city)  
            display_sightings(sightings)  
        elif user_input == 'venomous':
            city = input("Enter city: ").strip()  
            species_list = search_species(city)  
            venomous_species = filter_venomous(species_list)  
            display_species(venomous_species)  
        else:
            print("Invalid command. Please enter 'help', 'exit', 'species <city>', 'sightings <species>, <city>', or 'venomous'.")


if __name__ == "__main__":
    main()
# Task 5 End #

# To run this code you right this command
#wildlife> venomous
#Enter city: melbourne
#Species found:
#TaxonID: 236 , Name: snake, Pest Status: Venomous
