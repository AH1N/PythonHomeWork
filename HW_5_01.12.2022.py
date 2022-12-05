from random import randint
from os import system 
system("cls")


k = int(input(" ВВЕДИТЕ СТЕПЕНЬ МНОГОЧЛЕНА:  "))

mnCHLEN = []

def CHLEN(koeficient,stepen):
    if stepen == 1:
        stepen = ""
    else:
        stepen = "**"+str(stepen)
    if koeficient == 0:
        Virazhenie = ""
    elif koeficient == -1:
        Virazhenie = " " + "-" + "X" + str(stepen)  
    elif koeficient == 1 :
        Virazhenie = " " + "+" + "X" + str(stepen)
    elif koeficient > 1:
        Virazhenie = " " + "+" + str(koeficient) + "X"+ str(stepen)
    else: 
        Virazhenie = " " + str(koeficient) + "X"+ str(stepen)

    return Virazhenie

def CreateMnogochlen(list = mnCHLEN):
    MnogoCHLEN = ""
    for i in range(k,0,-1):
        koeficient = randint(-5, 6)
        MnogoCHLEN += CHLEN(koeficient,i)
        mnCHLEN.append(koeficient)
 
    svCHLEN = randint(-5, 6)
    mnCHLEN.append(svCHLEN)
    if MnogoCHLEN[1] == "+": 
        MnogoCHLEN = MnogoCHLEN[2:] +" "+ "+" + " " +str(svCHLEN)+" " + "= 0"
        print(MnogoCHLEN)
    else:
        MnogoCHLEN = MnogoCHLEN +" "+ "+" + " "+str(svCHLEN)+" " + "= 0"
        print(MnogoCHLEN)
    return MnogoCHLEN   
    return mnCHLEN
   



mnCHLEN_res = []



fi_le1 = open("Ftext1.txt", "w")
fi_le1.write(str(CreateMnogochlen()))
fi_le1.close()
fi_le2 = open("Ftext2.txt", "w")
fi_le2.write(str(CreateMnogochlen()))
fi_le2.close()

def CreateNewMnogoChlen(k):
    MnogoCHLEN = ""
    for i in range(k+1):
        mnCHLEN_res.append(mnCHLEN[i] - mnCHLEN[i+k])
    print(mnCHLEN_res, "это коэфициенты")

    for i in range(0,k):
        koeficient = mnCHLEN_res[i]
        MnogoCHLEN += CHLEN(koeficient,k-i)
    svCHLEN = mnCHLEN_res[len(mnCHLEN_res)-1]
    print(mnCHLEN)
    if MnogoCHLEN[1] == "+": 
        MnogoCHLEN = MnogoCHLEN[2:] +" "+ "+" + " " +str(svCHLEN)+" " + "= 0"
        print(MnogoCHLEN)
    else:
        MnogoCHLEN = MnogoCHLEN +" "+ "+" + " "+str(svCHLEN)+" " + "= 0"
        print(MnogoCHLEN)
    return MnogoCHLEN   
    return mnCHLEN

fi_le3 = open("Ftext.txt", "w")
fi_le3.write(str(CreateNewMnogoChlen(k)))
fi_le3.close()







