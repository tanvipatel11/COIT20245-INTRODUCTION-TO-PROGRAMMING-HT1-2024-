# Task 3 Start #

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
# Task 3 End #
# To run your code you want to type this in command 
# species melbourne # 