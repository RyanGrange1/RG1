alphabet=0

#symbol set 1. For each node move first charictor to last

symbols1=(
    "j","i","h","g","f","e","d","c","b","a","|"," ","?",">","k",
    "<","/",".",",","~","@",":","#","'",";","}","{","]","[","+",
    "_","=","-",")","(","*","&","^","%","$","£",'"',"!","¦","`",
    "¬","Z","Y","X","W","V","U","T","©","™","®","S","R","Q","P",
    "O","N","M","L","K","J","I","H","G","F","E","D","C","B","A",
        "9","8","7","6","5","4","3",
         "2","1","0","z","y","x","w","v","u","t","s","r","q","p","o"
         ,"n","m","l",
          )

#symbol set 2. Constant set.

symbols2=("|"," ","?",">","<","/",".",",","~","@",":","#","'",";","}","{","]","[","+","_","=","-",")","(","*","&","^","%","$","£",'"',"!",
          "¦","`","¬","Z","Y","X","W","V","U","T","©","™","®","S","R","Q","P","O","N","M","L","K","J","I","H","G","F","E","D","C","B","A","9","8","7",
          "6","5","4","3","2","1","0","z","y","x","w","v","u","t","s","r","q","p","o","n","m","l","k","j","i","h","g","f","e","d","c",
          "b","a")

#node deals with which loop its on

node=("0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f",)





loop = 0
while loop != 16:
    
    system = 100
    number = 99
    number = number - loop
    
    random=0
    
    print('def node'+node[loop]+'(split1):\n    output = ""\n    encryptinput = split1\n')
    #change number ^ to represent the node you are on



    #Is constant, does not change as this writes the code out that is defined above
    
    while system!=0:
        print('    if encryptinput == "'+symbols1[number]+'":')
        number = number - 1
        print('        output = "'+symbols2[random]+'"\n')
        random = random + 1

        system = system - 1

    
    
    while system != 0:
        print('    if encryptinput == "'+symbols1[system]+'":')
        
        print('        output = "'+symbols2[random]+'"\n')
        random = random + 1
        system = system - 1

    print('    filey = open("Resources/tempfile.txt","a")\n    filey.write(str(output))\n    filey.close()\n\n')
    loop = loop + 1
















    
