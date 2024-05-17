# sighting.py
from nominatim import gps_coordinate
from wildlife import get_species_list,get_surveys_by_species,display_sightings,sort_by_date,extract_specific_info
import json

def display_menu():
    """Display the menu options."""
    print("Welcome to Wildlife Sighting Tracker!")
    print("a.(Task 1) Print help menu")
    print("b.(Task 2) Exit the program")
    print("c.(Task 3,4) Display animal species in a city")
    print("d.(Task 5) Display venomous species with the city")
    print("e.(Task 7) Enter City and Get latitude and Longitude")
    print("f.(Task 9,10) Enter city and Get Wildlife Module Get Surveys by Species With the Sorting Data:--")


def print_help_menu():
    """Display the help menu."""
    print("Help Menu:")
    print("This program allows you to track wildlife sightings.")
    print("You can enter specific sightings and manage your records.")

def save_to_json(data, file_path):
    """
    Save data to a JSON file.

    Args:
        data (dict): Data to be saved.
        file_path (str): File path to save the JSON data.
    """
    try:
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data saved to {file_path}")
    except IOError as e:
        print(f"Error saving data to JSON file: {e}")


def display_species(species_data_list):
    """
    Print species information including TaxonID, AcceptedCommonName, and PestStatus.

    Args:
        species_data_list (list): List of dictionaries containing species information.

    Returns:
        None
    """
    for species_data in species_data_list:
        if "Species" in species_data:
            species = species_data["Species"]
            taxon_id = species.get("TaxonID", "N/A")
            accepted_common_name = species.get("AcceptedCommonName", "N/A")
            pest_status = species.get("PestStatus", "N/A")

            print(f"TaxonID: {taxon_id}")
            print(f"Accepted Common Name: {accepted_common_name}")
            print(f"Pest Status: {pest_status}")
            print()
        else:
            print("Invalid species data format.")

def filter_venomous(species_list):
    """
    Filter species to include only venomous species.

    Args:
        species_list (list): List of species dictionaries.

    Returns:
        list: Filtered list containing only venomous species dictionaries.
    """
    return [entry for entry in species_list if entry['Species']['PestStatus'] == 'Venomous']

def print_species_data(species_data_list):
    """
    Print species data including TaxonID, StartDate, and LocalityDetails.

    Args:
        species_data_list (list): List of dictionaries containing species data.

    Returns:
        None
    """
    for entry in species_data_list:
        if "properties" in entry:
            properties = entry["properties"]
            taxon_id = properties.get("TaxonID", "N/A")
            start_date = properties.get("StartDate", "N/A")
            locality_details = properties.get("LocalityDetails", "N/A")

            print(f"TaxonID: {taxon_id}")
            print(f"Start Date: {start_date}")
            print(f"Locality Details: {locality_details}")
            print()
        else:
            print("Invalid species data format.")

def main():
    """Main function to run the Wildlife Sighting Tracker program."""
    while True:
        display_menu()
        choice = input("Enter your choice (a/b/c/d/e/f): ").strip().lower()

        if choice == 'a':
            print_help_menu()
        elif choice == 'b':
            print("Exiting the program. Goodbye!")
            break
        elif choice == 'c':
            city = input("Enter the city name: ").strip()
            radius=10000
            coordinates = gps_coordinate(city)
            species_data = get_species_list(coordinates['latitude'], coordinates['longitude'], radius)
            display_species(species_data)

        elif choice == 'd':
            city = input("Enter the city name: ").strip()
            radius=10000
            coordinates = gps_coordinate(city)
            species_data = get_species_list(coordinates['latitude'], coordinates['longitude'], radius)
            venomous_species_list = filter_venomous(species_data)
            display_species(venomous_species_list)

        elif  choice == 'e':
             city = input("Enter the city name: ").strip()
             coordinates=gps_coordinate(city)
             print(f"Latitude: {coordinates['latitude']}, Longitude: {coordinates['longitude']}")

        elif choice == 'f':
             city = input("Enter the city name: ").strip()
             taxon_id = input("Enter the taxon_id name: ").strip()

             radius = 10000
            # radius = int(input("Enter search radius in meters: ").strip())

            # Retrieve geographic coordinates for the specified city
             coordinates = gps_coordinate(city)
             if not coordinates:
                 print(f"Coordinates not found for {city}. Exiting...")
                 return

             # Retrieve species list for the specified coordinates and radius
             species_data = get_species_list(coordinates['latitude'], coordinates['longitude'], radius)
             abc = get_surveys_by_species(int(taxon_id), coordinates['latitude'], coordinates['longitude'], radius)

             if abc:
             # Save species data to a JSON file
                 file_path = f"{city}_abc_species_list.json"
                 save_to_json(species_data, file_path)

             # Display sorted sightings by date
                 if 'features' in abc:
                    #  display_sightings(abc['features'])
                     file_patha = f"{city}_extract_specific_info.json"
                     aaa = sort_by_date(abc['features'])
                     save_to_json(extract_specific_info(aaa), file_patha)
                     print_species_data(extract_specific_info(aaa))
                    #  print(extract_specific_info(aaa))
                 else:
                     print("No sightings data to display.")

             else:
                 print(f"No species data found for {city} within {radius} meters.")


if __name__ == "__main__":
    main()
