file_path = "test.txt"

def read_file(file_path:str) -> list:
    file_list = []
    try:
        with open(file_path, "r") as file:
            file_list = file.readlines()
    except:
        print(f"Soubor {file_path} nenalezen!")
    return file_list


print(read_file(file_path))
