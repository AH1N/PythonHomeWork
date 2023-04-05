from os import system
import json
import NoteDict
import Zametka

gl = "█░░░░░█░░░░█░░░░█░██░███░░░██░░░░█░░░░█░██░░██\n█░███░█░████░████░█░░███░█░██░██░█░██░█░█░░███\n█░█████░░░██░░░██░░░████░░░░█░██░█░██░█░░░████\n█░██░░█░████░████░█░░███░██░█░██░█░██░█░██░███\n█░░░░░█░░░░█░░░░█░███░██░░░░█░░░░█░░░░█░███░██\n█████░████████████████████████████████████████"

def tojson(my_dict):
    with open('nootebook.json', 'w', encoding='utf-8') as f:
        json.dump(my_dict, f, ensure_ascii=False, indent=4)

def main_menu(my_dict2):
    system("cls")
    print(gl)
    print("Список команд:\n[1]- Поиск/Изменение/Удаление [2]- Добавление [3]- Весь справочник [5]- Выйти из программы")
    command = input("Введите номер команды: ")
    match command.split():
        case ["1"]: system("cls"), print("Поиск/Изменение/Удаление >>>\n"), intermenu1(my_dict2.findNote(Data(my_dict2)),my_dict2),\
                                                                 input("для продолжения нажмите любую клавишу"),\
                                                                 main_menu(my_dict2)
                                                                    
        case ["2"]: system("cls"), print("Добавление >>>\n"), print(addnote(my_dict2)),tojson(my_dict2.to_dict()),input("для продолжения нажмите любую клавишу"), main_menu(my_dict2)
        case ["3"]: system("cls"), print("Вся записная книга >>>\n"),my_dict2.getMyDict(),\
                                                                    input("для продолжения нажмите любую клавишу"),\
                                                                    main_menu(my_dict2)
                                                                    
        case ["5"]: print("Выйти из программы"), quit()
        case unknown_command: print (f"Команда '{command}' не расспознана, введите команду ещё раз"),main_menu(my_dict2)

def addnote(my_dict2):
    name = input("введите название заметки:  ")
    description = input("напишите заметку:  ")
    my_dict2.add_element(name, Zametka.Onenote(name,description))


def intermenu1(element,my_dict2):
    print("Список команд:\n[1]- Изменение [2]- Удаление [3]- Выйти из меню")
    if element == None:
        print("нет такой записи")
        input()
        main_menu(my_dict2)
    else:
        command = input("Введите номер команды: ")
    match command.split():
        case ["1"]: system("cls"), print("Изменение >>>\n"), intermenu2(element,my_dict2) 
        case ["2"]: system("cls"), print("Удаление >>>\n"),my_dict2.removeNote(element),\
                                                            tojson(my_dict2.to_dict()),\
                                                            main_menu(my_dict2)

        case ["3"]: system("cls"), print("Выйти из меню >>>\n"), main_menu(my_dict2)
        case unknown_command: print (f"Команда '{command}' не расспознана, введите команду ещё раз"), intermenu1(element,my_dict2)

def intermenu2(element,my_dict2):
    print("Список команд:\n[1]- Измененить Название [2]- Измененить заметку [3]- Выйти из меню")
    command = input("Введите номер команды: ")
    match command.split():
        case ["1"]: system("cls"), print("Изменение названия >>>\n"),element.changeNote(1),tojson(my_dict2.to_dict())
        case ["2"]: system("cls"), print("Изменения текста заметки >>>\n"),element.changeNote(2),tojson(my_dict2.to_dict())
        case ["3"]: system("cls"), print("Выйти из меню >>>\n"),intermenu1(element,my_dict2)
        case unknown_command: print (f"Команда '{command}' не расспознана, введите команду ещё раз"), intermenu2(element,my_dict2)


def Data(my_dict2):
    data = input("Что ищем? ")
    if data == '' or not data.isdigit:
        print("вы ввели чтото не то")
        main_menu(my_dict2)
    else: 
        return data