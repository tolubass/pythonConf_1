def print_file_content(input_file):
    try:
        with open(input_file,"p") as file_object:
            file_content = file_object.read()
    except FileNotFoundError as e:
        print(f"The file {input_file} is not found.")
        print(f"Error details:{e}")
    else:
        print(file_content)
    print_file_content('C:\\TestData\\OriginalFile.txt')