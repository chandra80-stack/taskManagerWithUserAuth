import hashlib

from src.com.iitk.constants.TaskMgmtConstants import ENTER_USER_AUTH_CHOICE, FILEPATH, USER_FILENAME
from src.com.iitk.service.TaskManagerServiceMenu import execute_task_manager_menu
from src.com.iitk.utils.FileOperationUtils import load_file, save_file


# Function to start registration process
def registration():
    user_name_temp = ""
    password_temp = ""
    while True:
        csv_file_path = FILEPATH + USER_FILENAME
        user_data_list_loaded = load_file(csv_file_path)
        user_name = input("Enter a username: ")
        username_list = [item["username"] for item in user_data_list_loaded]
        if username_list:
            if user_name in username_list:
                print("Entered user is already existed , please enter different user name ")
            else:
                user_name_temp = user_name
                break
        else:
            user_name_temp = user_name
            break
    while True:
        password = input("Enter user password: ")
        if 8 <= len(password) <= 12:
            password_temp = password
            break
        else:
            print("Input too long. Please enter a string with a minimum 8 and maximum of 12 characters.")
    user_data_ds = {"username": user_name_temp, "password": hash_password(password_temp)}
    user_data_list_loaded.append(user_data_ds)
    csv_file_path = FILEPATH + USER_FILENAME
    if save_file(user_data_list_loaded, csv_file_path):
        print("User registration is done successfully ...")
    else:
        print("No data to Save")


# Function to perform Login process
def login():
    while True:
        is_user_matched = False
        user_name = input("Enter a username : ")
        password = input("Enter user password : ")
        csv_file_path = FILEPATH + USER_FILENAME
        user_data_list = load_file(csv_file_path)
        if user_data_list:
            username_password = [(item["username"], item["password"]) for item in user_data_list]
            for user_data in username_password:
                if user_name in user_data[0]:
                    if verify_password(user_data[1], password):
                        is_user_matched = True
                        print("successfully logged in")
                        execute_task_manager_menu()
                        break
        else:
            print("user_data_list is empty")
            break
        if is_user_matched:
            break
        else:
            print("Invalid username or password ..")


# Function to verify entered password is valid or not
def verify_password(stored_password, provided_password):
    return stored_password == hash_password(provided_password)


# Function to apply hashing to password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Function to prompt the user to choose the option from auth menu
def user_auth_menu():
    print("please enter the choice")
    print("1. Registration")
    print("2. Login")
    print("3. Exit")
    while True:
        choice = input(ENTER_USER_AUTH_CHOICE)
        if choice.isdigit() and 1 <= int(choice) <= 3:
            choice = int(choice)  # Convert to integer after validation
            if choice == 1:
                print("User registration process is started")
                registration()
                break
            elif choice == 2:
                print("User login process is started")
                login()
                break
            elif choice == 3:
                print("Exiting..")
                break
