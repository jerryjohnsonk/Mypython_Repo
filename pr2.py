from tkinter import Y


def gen(n):
    for i in range(1,n+1):
        print(i)
    
r = 'y'
while(r=='y') :
 print("Enter the number for generating the list:")
 n =int(input())
 print("The List is:")
 gen(n)
 print("Do you want to continue(y/n):")
 r = input()

print("Number of elements:",n)
 
