def change_function():
    change = input('Введите команду: ')
    if change == 'a':
        writing_in_file()
    if change == 'b':
        read_file()

def writing_in_file():
       with open(file_path, 'a') as f:
            message_1 = input("Введите ФИО и телефон: ")
            f.write(message_1)

def read_file():
       with open(file_path, 'r') as f:
            # for line in file_path:
            #     print(line)
            f.read(file_path)

file_path = r'telephon_list.txt'

change_function()

