from os import system
import json
import time

gl = "█░░░░░█░░░░█░░░░█░██░███░░░██░░░░█░░░░█░██░░██\n█░███░█░████░████░█░░███░█░██░██░█░██░█░█░░███\n█░█████░░░██░░░██░░░████░░░░█░██░█░██░█░░░████\n█░██░░█░████░████░█░░███░██░█░██░█░██░█░██░███\n█░░░░░█░░░░█░░░░█░███░██░░░░█░░░░█░░░░█░███░██\n█████░████████████████████████████████████████"
# достаём базу из файла, конвертируем её в LIST
def get_base():
    base = []
    out = []
    file_file = 'test.txt'
    with open(file_file,"r", encoding='utf-8') as file:
        base = file.readlines()
        for elem in base:
            out.append(elem.split())
    return out

book = get_base()

# достаём из базы клиента >>> номер команды - [1]
def get_person(base):
    find_item = input('Введите имя: ')
    gonext = False
    for person in base:
        if find_item.title() in person:
            print(*person)
            gonext = True
    print(gonext)
    gonext = input("Нажмите любую клавишу для продолжения")
    del gonext

def get_all(base): 
    for person in base:
        print(*person)
    gonext = input("Нажмите любую клавишу для продолжения")
    
    del gonext
    
    main_menu(base)

# МЕНЮ операций с клиентами(работниками или студентами)
def main_menu(base):
    system("cls")
    print(gl)
    print("Список команд:\n[1]- Поиск [2]- Добавление [3]- Изменение [4]- Удаление [5]- Весь справочник [6]- Выйти из программы")
    command = input("Введите номер команды: ")
    match command.split():
        case ["1"]: system("cls"), print("Поиск >>>\n"), get_person(base), main_menu(base)
        case ["2"]: system("cls"), print("Добавление >>>\n"), add_person(base) 
        case ["3"]: system("cls"), print("Изменение >>>\n"), edit_person(base) 
        case ["4"]: system("cls"), print("Удаление >>>\n"), delit_person(base) 
        case ["5"]: system("cls"), print("Весь справочник >>>\n"), get_all(base)
        case ["6"]: print("Выйти из программы"), quit()
        case unknown_command: print (f"Команда '{command}' не расспознана, введите команду ещё раз"),main_menu(base)

# Метод УДАЛЕННИЯ клиента из базы >>> номер команды - [1]
def delit_person(base):
    get_person(base)
    del_id = input('Введите ID, которое нужно удалить: ')
    for person in base:
        if del_id in person:
            base.remove(person)
    del del_id
    Yes_Or_no(base)
# delit_person(book)
# print(book)

# Метод ДОБАВЛЕНИЯ клиента в базу
def add_person(base):
    id = int((base[len(base)-2])[0])+2
    name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    phone_number = input('Введите телефон: ')
    base.append([str(id),name,last_name,phone_number])
    Yes_Or_no(base)
# add_person(book)
# print(book)


# Метод ИЗМЕНЕНИЯ клиента в базе
def edit_person(base):
    get_person(base)
    id = input('Введите id, кого исправляем: ')
    for person in base:
        if id in person:
            command = input("Введите номер команды(1 - изменить имя, 2 - изменить фамилию, 3 - изменить телефон): ")
            match command.split():
                case ["1"]: person[1] = input('Введите новое имя: ')
                case ["2"]: person[2] = input('Введите новую фамилию: ')
                case ["3"]: person[3] = input('Введите новый номер телефона: ')
                case unknown_command: print (f"Command '{command}' not understood")
    Yes_Or_no(base)
# edit_person(book)
# print(book)

# Метод ПЕРЕЗАПИСИ базы после операций с ней
def save_base(base):
    out = ""  
    with open('test.txt', "w", encoding='utf-8') as file:
        for elem in base:
            time.sleep(0.15)
            file.writelines(f"{str(elem[0])} {str(elem[1])} {str(elem[2])} {str(elem[3])}\n")
            print(f"{elem} - saving complete")
# save_base(book)

def Yes_Or_no(base):
    command = input("Сохранить?\n да - 1\n нет - 2:\n")
    match command.split():
        case ["1"]: save_base(base),Json_maker(base)
        case ["2"]: main_menu(base)
        case unknown_command: print(f"Command '{command}' not understood"),Yes_Or_no(base)
    
    main_menu(base)

def Json_maker(base):
    file_file = 'test.txt'
    j_out = {}
    for person in base:
        print(person)
        print(person[1])
        j_out.update({str(person[1]+" "+person[2]):person[3]}) 
    print(j_out)
    with open("data_file.json", "w") as write_file:
        json.dump(j_out, write_file)
    return j_out

# Json_maker(book)

# print(book)
    