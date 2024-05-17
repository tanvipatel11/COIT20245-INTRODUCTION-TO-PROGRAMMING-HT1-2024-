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