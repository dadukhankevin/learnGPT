import os
current_directory = ""


def create_directory(directory_path):
    full_directory_path = current_directory + directory_path
    if not os.path.exists(full_directory_path):
        os.mkdir(full_directory_path)
        print("Directory created:", full_directory_path)
    else:
        print("Directory already exists:", full_directory_path)


def create_file(file_path, data):
    full_file_path = current_directory + file_path

    file_name, file_extension = os.path.splitext(full_file_path)
    counter = 1
    while os.path.exists(full_file_path):
        new_file_path = f"{file_name}_{counter}{file_extension}"
        counter += 1
        full_file_path = current_directory + new_file_path

    with open(full_file_path, 'w') as file:
        # Perform any desired operations on the file
        file.write(data)

    print("File created:", full_file_path)

def get_file_names(folder_path):
    folder_path = current_directory + folder_path
    file_names = []
    for file_name in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file_name)):
            file_names.append(file_name.replace(".txt",""))
    return file_names

class Saver:
    def __init__(self, path):
        self.path = path

    def create_new_catagory(self, name):
        create_directory(name)

    def create_new_set(self, category, name, data):
        self.create_new_catagory(category)
        name = name + ".txt"
        create_file(category + "/" + name, data)

    def get_set(self, category, name):
        with open(self.path + category + "/" + name + ".txt", "r") as f:
            json = f.read()
        return json
