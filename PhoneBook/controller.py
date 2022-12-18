import mech
from os import system


def Start_Program():
    system("cls")
    book = mech.get_base()
    mech.main_menu(book)
    enter = input()

