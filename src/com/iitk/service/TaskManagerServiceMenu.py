from src.com.iitk.constants.TaskMgmtConstants import PRINT_MANU, ADD_TASK, VIEW_TASK, MARK_TASK, DELETE_TASK, LOGOUT, \
    ENTER_CHOICE, FILEPATH, TASK_FILENAME
from src.com.iitk.service.TaskManagerService import add_task, view_task, mark_status, delete_task
from src.com.iitk.utils.FileOperationUtils import load_file


# Function to display an interactive menu to prompt the user for expense details
def print_menu():
    print("\n", PRINT_MANU)
    print(ADD_TASK)
    print(VIEW_TASK)
    print(MARK_TASK)
    print(DELETE_TASK)
    print(LOGOUT)


# Function to execute Each option in menu based on the user input
def execute_task_manager_menu():
    # Loading the CSV file details to list
    csv_file_path = FILEPATH + TASK_FILENAME
    task_list = load_file(csv_file_path)
    if not task_list:
        task_list = []

    # Looping the menu till user enter exit option
    while True:
        print_menu()
        choice = input(ENTER_CHOICE)

        # Check if the input is a digit and between 1 and 5
        if choice.isdigit() and 1 <= int(choice) <= 5:
            choice = int(choice)  # Convert to integer after validation
            if choice == 1:
                print("Adding expensive details...")
                isTaskAdded = add_task(task_list,csv_file_path)
                if isTaskAdded:
                    print("Task is added successfully ")
                else:
                    print("Task is added unsuccessful ")
            elif choice == 2:
                print("View user task details...")
                view_task(task_list)
            elif choice == 3:
                print("changing the task status as completed...")
                if mark_status(task_list,csv_file_path):
                    print("Entered task status changed successfully ")
                else:
                    print("Invalid taskid is entered ")
            elif choice == 4:
                print("Deleting the user task...")
                if delete_task(task_list,csv_file_path):
                    print("Entered task is deleted successfully ")
                else:
                    print("Invalid taskid is entered ")
            elif choice == 5:
                print("Exiting...")
                break
        else:
            print("Invalid input! Please enter a number between 1 and 5.")
