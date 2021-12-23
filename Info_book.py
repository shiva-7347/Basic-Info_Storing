import os.path
import sys

existance=os.path.isfile("Contactfile.txt")
if existance == 0:
    f = open('Contactfile.txt','a+')
    f.write("Name\t\t\t"+"First Name\t\t\t"+"Last name\t\t\t"+"Phone number\n")
    f.close()

def clear():os.system('cls')
def quit1(): sys.exit()

def msg():
    print(
        "1) Add contacts to the list\n"
        "2) Delete [ALL] contact from list\n"
        "3) Delete selected contact from list\n"
        "4) Search contact in list\n"
        "5) Display all contact in the list\n"
        "6) Exit program\n")

def begin():
    while True:
        match=int(input("Enter choice:- "))
        if match==1:
            adcontact()
        elif match==2:
            delacontact()
        elif match==3:
            remove()
        elif match==4:
            sercontact()
        elif match==5:
            dispfull()
        elif match==6:
            quitpro()
        else:
            print("Invalid choice")

def adcontact(): 
    stname=input("Enter 1st name of the contact: \n")
    snname=input("Enter 2nd name of the contact: \n")
    name=stname+snname
    number=input("Enter the number of contact: \n")
    c = open('contactfile.txt','a')
    c.write(name+'\t\t        '+stname+'\t\t\t\t'+snname+'\t\t\t\t'+number+'\n')
    c.close()
    clear()
    print(stname+" "+snname+" Contact saved")
    msg()

def sercontact():
    name=input("Enter the name to be searched:- ")
    cl = open('contactfile.txt','r')
    for l in cl.readlines():
        s=l
        found=s.find(name)
        if found != -1:
            print(l)
            cl.close()
    if found==-1:
        print("No such contact")
        cl.close()
        print(l)
 
def delcontact():
    name=print("Wiping all data")
    cl=open("contactfile.txt",'w+')
    for l in cl.readlines():
        s=l
        found=s.find(name)
        if found !=-1:
            cl.write(" ")
            break
        else:
            print("No such contact")
            cl.close()
    clear()
    print("All contact has been deleted...")
    cl = open('contactfile.txt','a+')
    cl.write("Name\t\t\t"+"First Name\t\t\t"+"Last name\t\t\t"+"Phone number\n")
    cl.close()
    c=input("Would you like to save another contact ?")
    if c.upper()=="Y":
        adcontact()
    elif c.upper() !="Y":
        msg()
        begin()

def remove():
    n=input("Enter the name:-")
    ce=open('contactfile.txt', 'r')
    cl=[]
    for l in ce.readlines():
        if l.find(n)!= -1:
            continue
        cl.append(l)
    ce=open('contactfile.txt', 'w')
    for i in range(0, len(cl)):
        ce.write(cl[i])
    ce.close()
    print("Contact has been deleted")
    clear()
    msg()
    
def dispfull():
    c=open('contactfile.txt','r')
    print(c.read())
    c.close()
    msg()

def quitpro():
    choice=input("Retry your choice with (Y) or exit contact list with (N)...: ")
    if choice.upper()=="Y":
        begin()
    elif choice.upper()!="Y":
        quit1()
        file.close()
        print("Exting the program :).....")
        sys.exit(0)

msg()
begin()
