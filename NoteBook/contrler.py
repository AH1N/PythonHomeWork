import NoteDict
import supportmethods
from os import system

def startProgram():
    my_dict2 = NoteDict.MyDict()
    system("cls")
    supportmethods.main_menu(my_dict2)
    enter = input()

