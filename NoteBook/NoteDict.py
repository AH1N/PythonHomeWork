import Zametka
import json

class MyDict():
    def __init__(self):
        self.notes = []

    def __iter__(self):
        return iter(self.notes)
    
    def to_dict(self):
        return {
            "notes": [b.__dict__ for b in self.notes]
        }
    
    def to_json(self):
        note_list = [{"di": note.uid,"name": note.name, "age": note.date, "data": note.data} for note in self.notes]
        return json.dumps({"Note": note_list})

    def getMyDict(self):
        if not(self.notes):
            print("записей нет")
        for element in self.notes:
            element.getNote()
      

    
    def add_element(self, key, value):
        self.notes.append(value)

    def suportFindNotes(self,search_data):
        elementList = []
        for element in self.notes: 
            if element.name == search_data or element.uid == search_data:
                elementList.append(element)
        return elementList

    def findNote(self,search_data):
        elementList = MyDict.suportFindNotes(self,search_data)
        if len(elementList) == 0:
            return print(f"нет такой записи")
        elif len(elementList) == 1:
            print(f"да, есть такая запись")
            print(len(elementList))
            print("************************************************")
            elementList[0].getNote()
            return elementList[0]
        else:
            for element in elementList:
                print(f"номер записи --> {elementList.index(element)}")
                element.getNote()
            print(f"записей с таким названием --> {elementList.index(element)+1}")
            noteID = input("выберите номер заметки, которую хотите открыть:  ")
            if noteID =='' or not noteID.isdigit()or int(noteID) <0 or int(noteID) == None or int(noteID) > len(elementList)-1:
                print("не следовало тебе играть со мной Кожаный мешок")
            else:
                return elementList[int(noteID)]
            
    
    def removeNote(self, note):
        self.notes.remove(note)  
          

# def findNote(self,search_data):
        
#         elementList = MyDict.supportFindNotes(self,search_data)
#         for element in self.notes: 
#             if element.name == search_data or element.uid == search_data:
#                 elementList.append(element)
#                 if len(elementList) == 1:
#                     print(f"да, есть такая запись")
#                     print("************************************************")
#                     element.getNote()
#                     return element
#                 else:
#                     for element in elementList:
#                         print(elementList[element]+1)
#                         element.getNote()
#                     noteID = input("заметку с каим ID вы хотите открыть?")
#                     MyDict.findNote(self,noteID)