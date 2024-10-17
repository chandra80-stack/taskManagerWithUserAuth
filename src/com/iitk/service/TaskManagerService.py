from src.com.iitk.utils.FileOperationUtils import save_file


# Adding new task to list
def add_task(task_list, csv_file_path):
    task_desc = input("Enter task description: ")
    task_status = 'pending'
    task_ds = []
    if task_list:
        taskid_list = [data_row['task_id'] for data_row in task_list]
        while True:
            task_id = input("Enter task id: ")
            if task_id in taskid_list:
                print("Entered Task Id is already existed , please enter unique task id ")
            else:
                task_ds = {"task_description": task_desc, "task_id": task_id, "task_status": task_status}
                break

    else:
        task_id = input("Enter task id: ")
        task_ds = {"task_description": task_desc, "task_id": task_id, "task_status": task_status}
    task_list.append(task_ds)
    if save_file(task_list, csv_file_path):
        return True
    else:
        return False


# View task list
def view_task(task_list):
    if task_list:
        for data_row in task_list:
            print(data_row)
    else:
        print("No task information is available:")


# Mark given task as completed
def mark_status(task_list, csv_file_path):
    is_taskid_existed = False
    taskid = input("Enter taskid to change the status as completed :")
    if task_list:
        for data_row in task_list:
            if taskid == data_row["task_id"]:
                is_taskid_existed = True
                if data_row["task_status"] != 'completed':
                    data_row["task_status"] = 'completed'
                    break
                else:
                    print("Status for entered taskid is already completed ")
                    break
    if not is_taskid_existed:
        return False
    else:
        if save_file(task_list, csv_file_path):
            return True
        else:
            return False


# Delete task from list
def delete_task(task_list, csv_file_path):
    is_taskid_existed = False
    taskid = input("Enter taskid to delete the task :")
    if task_list:
        for data_row in task_list:
            if taskid == data_row["task_id"]:
                is_taskid_existed = True
                task_list.remove(data_row)
                break
    if not is_taskid_existed:
        return False
    else:
        if save_file(task_list, csv_file_path):
            return True
        else:
            return False
