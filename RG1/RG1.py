#RG1 document encryption system
#Credait to Ryan Grange and Zac Perkines-Jonnes
#Version 0.02

#Import Modules
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import Image
import hashlib
from tkinter import filedialog
#from Resources import NodeListA
from Resources import NodeListA

#loop to allow rerun without having to close and reopen
run = 1
while run == 1:
    run = 0
    

    #Opening the Tkinter window and adding the logo
    root = Tk()
    logo = PhotoImage(file="Resources/Logo.gif")
    logoin = Label(root, image=logo).grid(row=0,columnspan="4")
    root.wm_title("~RG1 Encryption~")
    Continue=0
    root.filename = ""
    messagelength = 0
    Label(root, text="Click to open the importer for the file to be modified").grid(row=4, column=1)
    
    while Continue==0:
        #Creating/Clearing Tempfile for later use
        temp=open("Resources/tempfile.txt","w")
        temp.write("")
        temp.close()
        def close_window(root):
            root.quit()

        #Boxes to enter the information and their labels
        #Open File
        Label(root, text="Find the file you wish to encrypt/decrypt\n and enter a new/existing password.\n\n").grid(row=1, columnspan=4)

        

        #Enter Password
        Password = Entry(root)
        Password.config(show="*");
        Password.grid(row=5,column=2)
        Label(root, text="New password to encrypt, or existing password to decrypt").grid(row=5, column=1)

        #Buttons for the Tkinter window, and the code for clearing the boxes, and to open file dialog
        def clear_text(root):
            Password = Entry(root)
            Password.insert(0, '',)
            Password.config(show="*");
            Password.grid(row=5,column=2)
            
        def open_file(root):
            root.filename = filedialog.askopenfilename(filetypes=(("text files","*.txt"), ("all files","*")))

            validateName = root.filename[-4:]
            print(validateName)                

            if root.filename != "":
                Label(root, text="                                  File Imported                                   ").grid(row=4, column=1)
                root.update()
            
            if root.filename == "":
                Label(root, text="                              Please select a file.                                   ").grid(row=4, column=1) 
                root.update()

            if validateName != ".txt":
                Label(root, text="                      Unsupported file type, select a .txt file                       ").grid(row=4, column=1)
                messagelength = 0
                root.filename=""
                root.update()             

        Button(root, text="Begin", command=lambda: close_window(root)).grid(row=7, column=1)
        Button(root, text="Clear Password", command=lambda: clear_text(root)).grid(row=7, column=2)
        Button(root, text="Open File", command=lambda: open_file(root)).grid(row=4, column=2)      
            
        root.mainloop()
        
        #creates the password hash to encrypt from
        userpass=str(Password.get())

        def hash_password(password):
            return hashlib.sha512(password.encode()).hexdigest()
            
        passhash = hash_password(userpass)
        print(passhash)

        
            
        #importing the user defined file to be read from

        if root.filename!="":
            importfile = open(root.filename,"r")
            userimportfile = str(importfile.read())

            #creating the tempary document to save to
            filey = open("Resources/tempfile.txt","a")
            """filey.close()"""

            #ensuring it ends correctly
            messagelength = (len(str(userimportfile)))
            

            userimportfile=str(userimportfile)
            print(userimportfile)

            output = "1"
            #This chooses the message letter's placement from 0 up
            letter = 0
            messagetotal=messagelength

            if messagelength == 0:
                Label(root, text="                               Selected file cannot be blank                                     ").grid(row=4, column=1) 
                root.update()
            
        if messagelength != 0:
            Continue=1


            
    while messagelength > 0:
        passlen=len(passhash)
        print(passlen)
        passlen=passlen-1

        counter=0
        while passlen and messagelength > -1 and letter < messagetotal:
            split1=userimportfile[letter]

            if passhash[passlen] == "a":
                NodeListA.nodea(split1)
                
            if passhash[passlen] == "b":
                NodeListA.nodeb(split1)
               
            if passhash[passlen] == "c":
                NodeListA.nodec(split1)
                
            if passhash[passlen] == "d":
                NodeListA.noded(split1)
                
            if passhash[passlen] == "e":
                NodeListA.nodee(split1)
                
            if passhash[passlen] == "f":
                NodeListA.nodef(split1)
                
            if passhash[passlen] == "1":
                NodeListA.node1(split1)
              
            if passhash[passlen] == "2":
                NodeListA.node2(split1)
                
            if passhash[passlen] == "3":
                NodeListA.node3(split1)
               
            if passhash[passlen] == "4":
                NodeListA.node4(split1)
                
            if passhash[passlen] == "5":
                NodeListA.node5(split1)
                
            if passhash[passlen] == "6":
                NodeListA.node6(split1)
                
            if passhash[passlen] == "7":
                NodeListA.node7(split1)
                  
            if passhash[passlen] == "8":
                NodeListA.node8(split1)
                
            if passhash[passlen] == "9":
                NodeListA.node9(split1)
                
            if passhash[passlen] == "0":
                NodeListA.node0(split1)
            counter=counter+1 
               

    #For testing purposes, the file will read 1 if the code made it to here w/o crashing
            letter=letter+1    
            passlen = passlen - 1
            messagelength = messagelength - 1

    tempfile = open("Resources/tempfile.txt","r")
    tempfile = str(tempfile.read())
    print(tempfile)
    print(counter)

    root.destroy()

    #defining the rerun function
    def rerun(root):
        run = 1
        root.destroy()
        
    #defining the quit function
    def quit_window(root):
        run = 0
        root.destroy()

    #defining the save function for the final product
    def save_output(root):
        
        root.filename=filedialog.asksaveasfilename(filetypes=(("text files","*.txt"), ("all files","*")))
        if ".txt" in root.filename:
            root.filename=root.filename.replace(".txt","")
            
        
        outputfile = open("Resources/tempfile.txt","r")
        tempmove = str(outputfile.read())
        outputfile.close()

        usersavefile = open(root.filename+".txt","w")
        usersavefile.write(tempmove)
        usersavefile.close()
        
        Label(root, text="Save Successful").grid(row=2, columnspan=4)
        root.update()
        
    #Opening a save dialog for the user to save their text after the code has run

    root = Tk()

    logo = PhotoImage(file="Resources/Logo.gif")
    logoin = Label(root, image=logo).grid(row=0,columnspan="4")
    root.wm_title("~RG1 Encryption~")

    Label(root, text="Encrypt/decrypt ran sucsesfully, please choose where to save the output file.").grid(row=1, columnspan=4)
    Button(root, text="Quit", command=lambda: quit_window(root)).grid(row=3, column=2)
    Button(root, text="Save", command=lambda: save_output(root)).grid(row=3, column=1)
    Button(root, text="Re Run", command=lambda: rerun(root)).grid(row=3, column=3)

    root.mainloop()
    tempfile = open("Resources/tempfile.txt","w")
    tempfile.write("")
    tempfile.close()
    














