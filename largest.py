def Largenum(L1):
    print("Code checking")
    return 5

print('Enter the number of elements:')
n=int(input())
List1=[]
print("Enter the elements:")
for i in range(0,n):
     List1.append(input())
print("Entered array is:")
for i in range(0,n):
    (
        print(List1[i])
    )
lnum = Largenum(List1)
print(lnum)