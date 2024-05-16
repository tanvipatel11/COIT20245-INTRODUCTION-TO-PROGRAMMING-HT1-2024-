# wildlife.py
import requests
import json

def get_species_list(latitude, longitude, radius):
    """
    Retrieve a list of species in a specified area using the Queensland wildlife data API.

    Args:
        latitude (float): Latitude coordinate.
        longitude (float): Longitude coordinate.
        radius (int): Radius in meters defining the search area.

    Returns:
        list: List of species dictionaries containing selected information.
    """
    base_url = "https://apps.des.qld.gov.au/species/"
    endpoint = "index.php"
    params = {
        "op": "getspecieslist",
        "kingdom": "animals",
        "circle": f"{latitude},{longitude},{radius}"
    }

    try:
        response = requests.get(base_url + endpoint, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad status codes (e.g., 404, 500)
        data = response.json()

        species_summaries = data.get("SpeciesSightingSummariesContainer", {}).get("SpeciesSightingSummary", [])
        
        # Extract specific information for each species
        extracted_species = []
        for summary in species_summaries:
            species_info = summary.get("Species", {})
            accepted_common_name = species_info.get("AcceptedCommonName")
            pest_status = species_info.get("PestStatus")
            TaxonIDs=species_info.get("TaxonID")
            # Create a dictionary with the desired format
            species_dict = {
                "Species":{
                "TaxonID":TaxonIDs,
                "AcceptedCommonName": accepted_common_name,
                "PestStatus": pest_status
                }
            }

            # Append the species dictionary to the list
            extracted_species.append(species_dict)

        return extracted_species

    except requests.RequestException as e:
        print(f"Error fetching species list: {e}")
        return []


def get_surveys_by_species(taxon_id, latitude, longitude, radius):
    """
    Retrieve surveys for a specific species within a defined geographic area.

    Args:
        taxon_id (int): Taxon ID of the species.
        latitude (float): Latitude coordinate.
        longitude (float): Longitude coordinate.
        radius (int): Radius in meters defining the search area.

    Returns:
        dict or None: JSON response containing surveys for the specified species,
                      or None if there's an error or no data.
    """
    # https://apps.des.qld.gov.au/species/?op=getsurveysbyspecies&taxonid=860&&circle=-16.92,145.777,100000
    # f"https://apps.des.qld.gov.au/species/?op=getsurveysbyspecies&taxonid={taxonid}&&circle={coordinate},{radius}"
    # latitude, longitude = coordinate

    base_url = "https://apps.des.qld.gov.au/species/"
    endpoint = "index.php"
    params = {
        "op": "getsurveysbyspecies",
        "taxonid": taxon_id,
        "circle": f"{latitude},{longitude},{radius}"
    }

    try:
        response = requests.get(base_url + endpoint,params= params)

        response.raise_for_status()  # Raise an HTTPError for bad status codes (e.g., 404, 500)
        data = response.json()
        return data
        
    except requests.RequestException as e:
        print(f"Error fetching surveys for species {taxon_id}: {e}")
        return None
      
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

def earliest(sightings):
    """
    Find the sighting with the earliest start date.

    Args:
        sightings (list): List of sighting dictionaries containing 'StartDate' key.

    Returns:
        dict or None: The sighting with the earliest start date, or None if the list is empty.
    """
    if not sightings:
        return None
    
    # Find the dictionary with the minimum 'StartDate'
    earliest_sighting = min(sightings, key=lambda x: x['properties']['StartDate'])
    return earliest_sighting

def sort_by_date(sightings):
    """
    Sort sightings by start date.

    Args:
        sightings (list): List of sighting dictionaries containing 'StartDate' key.

    Returns:
        list: Sorted list of sighting dictionaries by start date.
    """
    sorted_sightings = []
    
    # Copy the input list to avoid modifying the original
    remaining_sightings = sightings[:]
    
    while remaining_sightings:
        # Find the earliest remaining sighting
        earliest_sighting = earliest(remaining_sightings)
        
        # Append the earliest sighting to the sorted list
        sorted_sightings.append(earliest_sighting)
        
        # Remove the earliest sighting from the remaining list
        remaining_sightings.remove(earliest_sighting)
    
    return sorted_sightings

def display_sightings(sightings):
    """
    Display the list of sightings.

    Args:
        sightings (list): List of sighting dictionaries.
    """
    # Sort sightings by date
    sorted_sightings = sort_by_date(sightings)
    
    # Display sorted sightings
    if sorted_sightings:
        print("Sorted Sightings by Date:")
        for sighting in sorted_sightings:
            print(json.dumps(sighting, indent=4))
    else:
        print("No sightings to display.")

def     extract_specific_info(features):
    """
    Extract specific information from each feature.

    Args:
        features (list): List of feature dictionaries.

    Returns:
        list: List of dictionaries containing selected information (TaxonID, StartDate, LocalityDetails).
    """
    extracted_info = []

    for feature in features:
        properties = feature.get('properties', {})
        taxon_id = properties.get('TaxonID')
        start_date = properties.get('StartDate')
        locality_details = properties.get('LocalityDetails')

        # Create a new dictionary with the desired information
        info_dict = {
            'properties':{
            'TaxonID': taxon_id,
            'StartDate': start_date,
            'LocalityDetails': locality_details
            }
        }

        # Append the dictionary to the list
        extracted_info.append(info_dict)

    return extracted_info


def abc():
    # Get user input for location details
    latitude = float(input("Enter latitude coordinate: "))
    longitude = float(input("Enter longitude coordinate: "))
    radius = int(input("Enter search radius in meters: "))

    # Retrieve species list based on user input
    species_data = get_species_list(latitude, longitude, radius)

    if species_data:
        # Save species data to a JSON file
        file_path = "species_list.json"
        save_to_json(species_data, file_path)

if __name__ == "__main__":
    abc()
