def gps(city):
    # For now, just return Brisbane's GPS coordinate
    return {"latitude": -27.4689682, "longitude": 153.0234991}

def search_species(city):
    # Call gps(city) to get the coordinates
    coordinates = gps(city)
    
    # This is a partial stub, return some example data for now
    species_list = [
        {"name": "Kangaroo", "type": "Mammal"},
        {"name": "Koala", "type": "Mammal"},
        {"name": "Emu", "type": "Bird"}
    ]
    
    return species_list

# Assert statements to check if Brisbane returns the correct GPS coordinate
assert gps("Brisbane") == {"latitude": -27.4689682, "longitude": 153.0234991}
