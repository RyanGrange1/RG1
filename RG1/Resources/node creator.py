alphabet=0

#symbol set 1. For each node move first charictor to last

symbols1=("D","C","B","A","9","8","7","6","5","4","3",
         "2","1","0","z","y","x","w","v","u","t","s","r","q","p","o"
         ,"n","m","l","k","j","i","h","g","f","e","d","c","b","a","|"
         ," ","?",">","<","/",".",",","~","@",":","#","'",";","}","{","]"
         ,"[","+","_","=","-",")","(","*","&","^","%","$","£",'"',"!",
         "¦","`","¬","Z","Y","X","W","V","U","T","©","™","®","S","R","Q","P",
          "O","N","M","L","K","J","I","H","G","F","E",)

#symbol set 2. Constant set.

symbols2=("|"," ","?",">","<","/",".",",","~","@",":","#","'",";","}","{","]","[","+","_","=","-",")","(","*","&","^","%","$","£",'"',"!",
               "¦","`","¬","Z","Y","X","W","V","U","T","©","™","®","S","R","Q","P","O","N","M","L","K","J","I","H","G","F","E","D","C","B","A","9","8","7",
               "6","5","4","3","2","1","0","z","y","x","w","v","u","t","s","r","q","p","o","n","m","l","k","j","i","h","g","f","e","d","c","b","a")
number=96
system=97
random=0


print('def nodef(split1):\n    output = ""\n    encryptinput = split1\n')
#change number ^ to represent the node you are on



#Is constant, does not change as this writes the code out that is defined above
while system!=0:
    print('    if encryptinput == "'+symbols1[number]+'":')
    number=number-1
    print('        output = "'+symbols2[random]+'"\n')
    random=random+1
    system=system-1

print('    filey = open("Resources/tempfile.txt","a")\n    filey.write(str(output))\n    filey.close()\n\n')
