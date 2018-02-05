#RG1 document encryption system
#Credait to Ryan Grange and Zac Perkines-Jonnes
#Version 0.03

#Import Modules
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import Image
import hashlib
from tkinter import filedialog
#from Resources import NodeListA
from Resources import NodeListA, NodeListB, NodeListC, NodeListD, NodeListE, NodeListF 


#closes the window to allow the program to move on
def close_window(root):
    root.quit()

#clears the input boxes
def clear_text(root):
    Password = Entry(root)
    Password.insert(0, '',)
    Password.config(show="*");
    Password.grid(row=5,column=2)

#opens the import file dialog
def open_file(root):
    root.filename = filedialog.askopenfilename(filetypes=(("Un-Encrypted Text Files","*.txt"), ("Encrypted RG1 Files","*.rg1"), ("All Other Files","*")))

#hashes the users passwors
def hash_passwordmd5(password):
    return hashlib.md5(password.encode()).hexdigest()

def hash_passwordsha(password):
    return hashlib.sha512(password.encode()).hexdigest()

#defining the rerun function
def rerun(root):
    run = 1
    root.destroy()
            
#defining the quit function
def quit_window(root):
    run = 0
    root.destroy()

    
#main program
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
        temp=open("Resources/tempfile.rg1","w")
        temp.write("")
        temp.close()
            

        #Boxes to enter the information and their labels
        #Open File
        Label(root, text="Find the file you wish to encrypt/decrypt\n and enter a new/existing password.\n\n").grid(row=1, columnspan=4)

            

        #Enter Password
        Password = Entry(root)
        Password.config(show="*");
        Password.grid(row=5,column=2)
        Label(root, text="New password to encrypt, or existing password to decrypt").grid(row=5, column=1)

        #Buttons for the Tkinter window, and the code for clearing the boxes, and to open file dialog

        validateName = root.filename[-4:]
        print(validateName)                

        if root.filename != "":
            Label(root, text="                                  File Imported                                   ").grid(row=4, column=1)
            root.update()
            
        elif root.filename == "":
            Label(root, text="                              Please select a file.                                   ").grid(row=4, column=1) 
            root.update()
                
        if validateName != ".txt" or ".rg1" or ".py":
            Label(root, text="                  Unsupported file type, select a .txt / .rg1 file                  ").grid(row=4, column=1)
            messagelength = 0
            root.filename=""
            root.update()             

        Button(root, text="Begin", command=lambda: close_window(root)).grid(row=7, column=1)
        Button(root, text="Clear Password", command=lambda: clear_text(root)).grid(row=7, column=2)
        Button(root, text="Open File", command=lambda: open_file(root)).grid(row=4, column=2)
                
        root.mainloop()

        #Working out if to encrypt/decrypt based on file extension type

        if validateName == ".rg1":
            decrypt = True

        else:
            decrypt = False
            
        #creates the password hash to encrypt from
        userpass=str(Password.get())



            
                
        SHApasshash = hash_passwordsha(userpass)
        print("SHA hash = ",SHApasshash)


            
            

        MD5passhash = hash_passwordmd5(userpass)
        print("MD5 hash = ",MD5passhash)
            
                
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
            print("Message  = " ,userimportfile)

            output = "1"
            #This chooses the message letter's placement from 0 up
            letter = 0
            messagetotal=messagelength

        if messagelength == 0:
            Label(root, text="                               Selected file cannot be blank                                     ").grid(row=4, column=1) 
            root.update()
                
        if messagelength != 0:
            Continue=1

        NodeListVar = NodeListA
                
        while messagelength > 0:
            SHApasslen = 128
            MD5passlen = 32
            
            SHApasslen = SHApasslen - 1
            MD5passlen = MD5passlen - 1

            
            counter=0
            while SHApasslen and messagelength > -1 and letter < messagetotal:
                split1=userimportfile[letter]

                if SHApasshash[SHApasslen] == "a":
                    (NodeListVar).nodea(split1)
                    
                if SHApasshash[SHApasslen] == "b":
                    (NodeListVar).nodeb(split1)
                   
                if SHApasshash[SHApasslen] == "c":
                    (NodeListVar).nodec(split1)
                    
                if SHApasshash[SHApasslen] == "d":
                    (NodeListVar).noded(split1)
                    
                if SHApasshash[SHApasslen] == "e":
                    (NodeListVar).nodee(split1)
                    
                if SHApasshash[SHApasslen] == "f":
                    (NodeListVar).nodef(split1)
                    
                if SHApasshash[SHApasslen] == "1":
                    (NodeListVar).node1(split1)
                  
                if SHApasshash[SHApasslen] == "2":
                    (NodeListVar).node2(split1)
                    
                if SHApasshash[SHApasslen] == "3":
                    (NodeListVar).node3(split1)
                   
                if SHApasshash[SHApasslen] == "4":
                    (NodeListVar).node4(split1)
                    
                if SHApasshash[SHApasslen] == "5":
                    (NodeListVar).node5(split1)
                    
                if SHApasshash[SHApasslen] == "6":
                    (NodeListVar).node6(split1)
                    
                if SHApasshash[SHApasslen] == "7":
                    (NodeListVar).node7(split1)
                      
                if SHApasshash[SHApasslen] == "8":
                    (NodeListVar).node8(split1)
                    
                if SHApasshash[SHApasslen] == "9":
                    (NodeListVar).node9(split1)
                    
                if SHApasshash[SHApasslen] == "0":
                    (NodeListVar).node0(split1)
                counter=counter+1 
                   

        #For testing purposes, the file will read 1 if the code made it to here w/o crashing
                letter=letter+1    
                SHApasslen = SHApasslen - 1
                MD5passlen = MD5passlen - 1
                messagelength = messagelength - 1

        tempfile = open("Resources/tempfile.rg1","r")
        tempfile = str(tempfile.read())
        print(tempfile)
        print(counter)

        root.destroy()



        #defining the save function for the final product
        def save_output(root):
            
            root.filename=filedialog.asksaveasfilename(filetypes=(("Default Output","*.txt/.rg1"), ("all files","*")))
            if ".txt" in root.filename:
                root.filename=root.filename.replace(".txt","")
            if ".rg1" in root.filename:
                root.filename=root.filename.replace(".rg1","")
                
            
            outputfile = open("Resources/tempfile.rg1","r")
            tempmove = str(outputfile.read())
            outputfile.close()

            if decrypt == True:
                usersavefile = open(root.filename+".txt","w")

            elif decrypt == False: 
                usersavefile = open(root.filename+".rg1","w")

            usersavefile.write(tempmove)
            usersavefile.close()
            
            tempfile = open("Resources/tempfile.rg1","w")
            tempfile.write("")
            tempfile.close()
            
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
        
    
        













