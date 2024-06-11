from csv import DictReader, DictWriter
from os.path import exists

class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt


def info_input ():
    flag = False
    while not flag:
        try:                        
            first_name = input("First name: ")
            if len(first_name) < 2:
                raise NameError('Name too short')
            last_name = input("Last name: ")
            if len(last_name) < 3:
                raise NameError('Last name too short')
            phone_number = input("Phone number: ")
            if len(phone_number) < 11:
                raise NameError('Phone number is incorrect')
        except NameError as err:
            print (err)
        else:
            flag = True             
    return [first_name, last_name, phone_number]


def create_file(file_name):
    with open(file_name, 'w', encoding="utf-8", newline = '') as data:
        f_w = DictWriter(data, fieldnames=['First Name', 'Last Name', 'Phone Number'])
        f_w.writeheader()
        
        
def write_file(file_name):
    res = read_file(file_name)
    user_data = info_input()
    new_object = {'First Name':user_data[0], 'Last Name':user_data[1], 'Phone Number':user_data[2]}
    res.append(new_object)
    standard_write(file_name, res)


def read_file(file_name):
    with open(file_name, encoding="utf-8") as data:
        f_r = DictReader(data)
        return list(f_r)

# Удаление определенной строки по номеру
def remove_row(file_name): 
    search = int(input("Please write row number you need to remove: "))
    res = read_file(file_name)
    if search <= len(res):        
        res.pop(search-1)
        standard_write(file_name, res)
    else:
        print("The row you want to remove doesn't exist")
        
            
# Копирование определенной строки по номеру в новый файл
def copy_row(file_name, second_file_name):
    search = int(input("Please write row number you need to copy: "))
    res = read_file(file_name)
    res2 = read_file(second_file_name)
    if search <= len(res):        
        temp = res.pop(search-1)  
        res2.append(temp)
        standard_write(second_file_name, res2)  
    else:
        print("The row you want to copy doesn't exist")
        
        
# Копирование определенной строки по номеру в новый файл c очисткой предыдущих поисков
def copy_single_row(file_name, search_file_name):
    search = int(input("Please write row number you need to copy: "))
    res = read_file(file_name)
    clearing = open(search_file_name, 'w+', encoding="utf-8")
    clearing.close()
    res2 = read_file(search_file_name)
    if search <= len(res):        
        temp = res.pop(search-1)  
        res2.append(temp)
        standard_write(search_file_name, res2)  
    else:
        print("The row you want to copy doesn't exist")
        

# Создание полной копии справочника в новом файле 
def full_copy(file_name, third_file_name):
    res = read_file(file_name)
    standard_write(third_file_name, res)        
        
        
def standard_write(file_name, res):
    with open(file_name, 'w', encoding="utf-8", newline = '') as data:
            f_w = DictWriter(data, fieldnames=['First Name', 'Last Name', 'Phone Number'])
            f_w.writeheader()
            f_w.writerows(res)


file_name = 'phone_book.csv'  
second_file_name = 'pb_search_results.csv'
third_file_name = 'pb_copy.csv'
search_file_name = 'pb_single_search_result.csv'
  
  
def main():
    while True: 
        command = input('Command input: ')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name)
        elif command == 'r':
            if not exists(file_name):
                print("File doesn't exist, please, create the file")
                continue
            print(*read_file(file_name))
        elif command == 'd':
            if not exists(file_name):
                print("File doesn't exist, please, create the file")
                continue
            remove_row(file_name)
        elif command == 's':
            if not exists(file_name):
                print("File doesn't exist, please, create the file")
                continue
            if not exists(second_file_name):
                create_file(second_file_name)
            copy_row(file_name, second_file_name)
        elif command == 'ss':
            if not exists(file_name):
                print("File doesn't exist, please, create the file")
                continue
            if not exists(search_file_name):
                create_file(search_file_name)
            copy_single_row(file_name, search_file_name)
        elif command == 'c':
            if not exists(file_name):
                print("File doesn't exist, please, create the file")
                continue
            if not exists(third_file_name):
                create_file(third_file_name)
            full_copy(file_name, third_file_name)
                                     
            
main()