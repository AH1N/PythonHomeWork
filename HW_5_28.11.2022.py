from os import system 
system("cls")

n = int(input())
testList = [0,1,1]
testList1 = [0,1,-1]
newList = []
def CreateFiboList(n,testList):
    for i in range(3,n+1):
        testList.append(testList[i-1]+testList[i-2])
        testList1.append((testList[i-1]+testList[i-2])*(-1)**(i+1))
    print(testList)
    print(testList1)

CreateFiboList(n,testList)

newList = list(reversed(testList1))

for i in range(1,((n)+1)):
    newList.append(testList[i])
print(newList)
