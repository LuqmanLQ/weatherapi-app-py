    # Color Codes
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"  # This is vital! It stops the color from bleeding into the next line.

import json
import os

def save_tasks(tasks):
    with open("todolist.json", "w") as f:
        json.dump(tasks, f)

def load_tasks():
    if os.path.exists("todolist.json"):
        with open("todolist.json", "r") as f:
            return json.load(f)
    return []  # Return an empty list if no file exists yet

def main():
    os.system('')
    to_do_items = load_tasks() #this creating the list to store the data
    print(f"DEBUG: Loaded {len(to_do_items)} tasks from file.")

    while True:
        print(f"{BLUE}\n--- TO-DO LIST MANAGER ---{RESET}")
        print("1. Add a Task")
        print("2. View Tasks")
        print("3. Remove a Tasks")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
                print("You chose to add a task")
                task = input("Enter the task you want to add: ")
                to_do_items.append(task) #this is the line to add any tasks to the list.
                save_tasks(to_do_items)
                print(f"{GREEN}'{task}' added successfully! {RESET}")
        
        elif choice == "2":
            if len(to_do_items) == 0: #to check whether is there empty task in the storage.
                    print("No tasks availab1le. Please add a task first.")
            else:
                    print(f" {GREEN} Your current tasks are: {RESET}") #to display the current task in the storage.
                    for index, item in enumerate(to_do_items, start=1):
                        print(f"{index}. {item}")

        elif choice == "3":
                if len(to_do_items) == 0: #to check whether is there empty task in the storage.
                    print("No tasks available. Please add a tasks first.")
                else:
                    print("Your current tasks are: ")
                    for index, item in enumerate(to_do_items, start=1):
                        print(f"{index}. {item}")
                    
                        try:
                            index = int(input("Enter the task number that you want to remove")) -1
                            if 0 <= index < len(to_do_items): # validates the index to prevent IndexError for out-of-range.
                              removed_item = to_do_items.pop(index)
                              save_tasks(to_do_items)
                              print(f" {GREEN}Task '{removed_item}' removed successfully! {RESET}")
                            else:
                                print(f" {RED}Invalid tasks number. Please try again. {RESET}")
                        except ValueError: #to handle if there is non-numeric input so it will come out as an error.
                            print(f"{RED}Invalid input. Please enter a valid tasks number {RESET}")
        elif choice == "4":
             print("Exiting the app. Goodbye!")
             break
        else:
             print(f" {RED}Invalid choice. Try again {RESET}")

             

if __name__ == "__main__":
    main()


                            



