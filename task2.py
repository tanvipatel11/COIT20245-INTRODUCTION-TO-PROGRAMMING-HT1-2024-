def display_menu():
    print("\nCOIT20245 - Assignment 2")
    print("\nMenu : ")
    print("a. Help Menu")
    print("b. Exit")

def main():

    display_menu()

    while True:
        user_input = input("wildlife > ")

        if user_input.lower() == "help":
            display_menu()
        elif user_input.lower() == "exit":
            print("Exiting the program.")
            break
        else:
            print("Error: Invalid command. Please enter 'help' or 'exit'.")


if __name__ == "__main__":
    main()
