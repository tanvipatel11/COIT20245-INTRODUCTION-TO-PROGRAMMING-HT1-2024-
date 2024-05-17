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
