import csv


# Save file to given path
def save_file(user_data_list, csv_file_path):
    # Save the data to the CSV file
    with open(csv_file_path, 'w', newline='') as csv_file:
        if user_data_list:
            dict_writer = csv.DictWriter(csv_file, fieldnames=user_data_list[0].keys())
            dict_writer.writeheader()
            dict_writer.writerows(user_data_list)
            return True
        else:
            return False


# Load file from given path
def load_file(csv_file_path):
    data_list = []
    # Retrieve data from the CSV file
    try:
        with open(csv_file_path, 'r') as csv_file:
            dict_reader = csv.DictReader(csv_file)
            retrieved_data = list(dict_reader)
            if not retrieved_data:
                return data_list
            else:
                return retrieved_data
    except FileNotFoundError as e:
        print(f"Error: {e}")
        # Handle the error, maybe create the file or log the issue
        open(csv_file_path, 'w')
    # Add the retrieved data to the existing list
    return data_list
