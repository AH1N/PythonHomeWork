import datetime
import uuid



class Onenote:
    def __init__(self,name,data):
        self.uid = str(uuid.uuid4())[:5]
        self.name = str(name)
        self.date = str(datetime.datetime.now())
        self.data = str(data)

    def toDict(self):
        new_dict = {"id": self.uid, "name": self.name, "date": self.date, "data" : self.data}
        return new_dict

    def getInfo(self):
        print(f"{self.uid}  | {self.name}  | {self.date}  | {self.data}  |")
        print("-----------------------------------------------------------------------------------------")
    
    def getNote(self):
        print(f"id:\t\t{self.uid}")
        print(f"Название:\t{self.name}")
        print(f"Дата:\t\t{self.date}")
        print(f"Заметка:\t{self.data}")
        print("________________________________________________")
    

    def changeNote(self,n):
        if n==1:
            print(f"Название:\t{self.name}")
            new_name = input("напишите новое название: ")
            apply = input("сохранить - [1], отменить и выйти - [любая клавиша]")
            if apply == "1":
                self.name = new_name
                print("название изменено")
            else: 
                print("название НЕ изменено")
        else:
            if n==2:
                print(f"Название:\t{self.data}")
                new_data = input("измкните заметку: ")
                ipply = input("сохранить - [1], отменить и выйти - [любая клавиша]")
                if ipply == "1":
                    self.data = new_data
                    print("заметка изменена") 
                else:
                    print("заметка НЕ изменена")  

    def deleteNote(self):
        del self    
            
