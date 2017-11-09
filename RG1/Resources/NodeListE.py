def node0(split1):
    output = ""
    encryptinput = split1

    if encryptinput == "?":
        output = "|"

    if encryptinput == " ":
        output = " "

    if encryptinput == "|":
        output = "?"

    if encryptinput == "a":
        output = ">"

    if encryptinput == "b":
        output = "<"

    if encryptinput == "c":
        output = "/"

    if encryptinput == "d":
        output = "."

    if encryptinput == "e":
        output = ","

    if encryptinput == "f":
        output = "~"

    if encryptinput == "g":
        output = "@"

    if encryptinput == "h":
        output = ":"

    if encryptinput == "i":
        output = "#"

    if encryptinput == "j":
        output = "'"

    if encryptinput == "k":
        output = ";"

    if encryptinput == "l":
        output = "}"

    if encryptinput == "m":
        output = "{"

    if encryptinput == "n":
        output = "]"

    if encryptinput == "o":
        output = "["

    if encryptinput == "p":
        output = "+"

    if encryptinput == "q":
        output = "_"

    if encryptinput == "r":
        output = "="

    if encryptinput == "s":
        output = "-"

    if encryptinput == "t":
        output = ")"

    if encryptinput == "u":
        output = "("

    if encryptinput == "v":
        output = "*"

    if encryptinput == "w":
        output = "&"

    if encryptinput == "x":
        output = "^"

    if encryptinput == "y":
        output = "%"

    if encryptinput == "z":
        output = "$"

    if encryptinput == "0":
        output = "£"

    if encryptinput == "1":
        output = "'"

    if encryptinput == "2":
        output = "!"

    if encryptinput == "3":
        output = "¦"

    if encryptinput == "4":
        output = "`"

    if encryptinput == "5":
        output = "¬"

    if encryptinput == "6":
        output = "Z"

    if encryptinput == "7":
        output = "Y"

    if encryptinput == "8":
        output = "X"

    if encryptinput == "9":
        output = "W"

    if encryptinput == "A":
        output = "V"

    if encryptinput == "B":
        output = "U"

    if encryptinput == "C":
        output = "T"

    if encryptinput == "D":
        output = "©"

    if encryptinput == "E":
        output = "™"

    if encryptinput == "F":
        output = "®"

    if encryptinput == "G":
        output = "S"

    if encryptinput == "H":
        output = "R"

    if encryptinput == "I":
        output = "Q"

    if encryptinput == "J":
        output = "P"

    if encryptinput == "K":
        output = "O"

    if encryptinput == "L":
        output = "N"

    if encryptinput == "M":
        output = "M"

    if encryptinput == "N":
        output = "L"

    if encryptinput == "O":
        output = "K"

    if encryptinput == "P":
        output = "J"

    if encryptinput == "Q":
        output = "I"

    if encryptinput == "R":
        output = "H"

    if encryptinput == "S":
        output = "G"

    if encryptinput == "®":
        output = "F"

    if encryptinput == "™":
        output = "E"

    if encryptinput == "©":
        output = "D"

    if encryptinput == "T":
        output = "C"

    if encryptinput == "U":
        output = "B"

    if encryptinput == "V":
        output = "A"

    if encryptinput == "W":
        output = "9"

    if encryptinput == "X":
        output = "8"

    if encryptinput == "Y":
        output = "7"

    if encryptinput == "Z":
        output = "6"

    if encryptinput == "¬":
        output = "5"

    if encryptinput == "`":
        output = "4"

    if encryptinput == "¦":
        output = "3"

    if encryptinput == "!":
        output = "2"

    if encryptinput == "'":
        output = "1"

    if encryptinput == "£":
        output = "0"

    if encryptinput == "$":
        output = "z"

    if encryptinput == "%":
        output = "y"

    if encryptinput == "^":
        output = "x"

    if encryptinput == "&":
        output = "w"

    if encryptinput == "*":
        output = "v"

    if encryptinput == "(":
        output = "u"

    if encryptinput == ")":
        output = "t"

    if encryptinput == "-":
        output = "s"

    if encryptinput == "=":
        output = "r"

    if encryptinput == "_":
        output = "q"

    if encryptinput == "+":
        output = "p"

    if encryptinput == "[":
        output = "o"

    if encryptinput == "]":
        output = "n"

    if encryptinput == "{":
        output = "m"

    if encryptinput == "}":
        output = "l"

    if encryptinput == ";":
        output = "k"

    if encryptinput == "'":
        output = "j"

    if encryptinput == "#":
        output = "i"

    if encryptinput == ":":
        output = "h"

    if encryptinput == "@":
        output = "g"

    if encryptinput == "~":
        output = "f"

    if encryptinput == ",":
        output = "e"

    if encryptinput == ".":
        output = "d"

    filey = open("Resources/tempfile.txt","a")
    filey.write(str(output))
    filey.close()
    
def node1(split1):
    output = ""
    encryptinput = split1

    if encryptinput == ">":
        output = "|"

    if encryptinput == "?":
        output = " "

    if encryptinput == " ":
        output = "?"

    if encryptinput == "|":
        output = ">"

    if encryptinput == "a":
        output = "<"

    if encryptinput == "b":
        output = "/"

    if encryptinput == "c":
        output = "."

    if encryptinput == "d":
        output = ","

    if encryptinput == "e":
        output = "~"

    if encryptinput == "f":
        output = "@"

    if encryptinput == "g":
        output = ":"

    if encryptinput == "h":
        output = "#"

    if encryptinput == "i":
        output = "'"

    if encryptinput == "j":
        output = ";"

    if encryptinput == "k":
        output = "}"

    if encryptinput == "l":
        output = "{"

    if encryptinput == "m":
        output = "]"

    if encryptinput == "n":
        output = "["

    if encryptinput == "o":
        output = "+"

    if encryptinput == "p":
        output = "_"

    if encryptinput == "q":
        output = "="

    if encryptinput == "r":
        output = "-"

    if encryptinput == "s":
        output = ")"

    if encryptinput == "t":
        output = "("

    if encryptinput == "u":
        output = "*"

    if encryptinput == "v":
        output = "&"

    if encryptinput == "w":
        output = "^"

    if encryptinput == "x":
        output = "%"

    if encryptinput == "y":
        output = "$"

    if encryptinput == "z":
        output = "£"

    if encryptinput == "0":
        output = """

    if encryptinput == "1":
        output = "!"

    if encryptinput == "2":
        output = "¦"

    if encryptinput == "3":
        output = "`"

    if encryptinput == "4":
        output = "¬"

    if encryptinput == "5":
        output = "Z"

    if encryptinput == "6":
        output = "Y"

    if encryptinput == "7":
        output = "X"

    if encryptinput == "8":
        output = "W"

    if encryptinput == "9":
        output = "V"

    if encryptinput == "A":
        output = "U"

    if encryptinput == "B":
        output = "T"

    if encryptinput == "C":
        output = "©"

    if encryptinput == "D":
        output = "™"

    if encryptinput == "E":
        output = "®"

    if encryptinput == "F":
        output = "S"

    if encryptinput == "G":
        output = "R"

    if encryptinput == "H":
        output = "Q"

    if encryptinput == "I":
        output = "P"

    if encryptinput == "J":
        output = "O"

    if encryptinput == "K":
        output = "N"

    if encryptinput == "L":
        output = "M"

    if encryptinput == "M":
        output = "L"

    if encryptinput == "N":
        output = "K"

    if encryptinput == "O":
        output = "J"

    if encryptinput == "P":
        output = "I"

    if encryptinput == "Q":
        output = "H"

    if encryptinput == "R":
        output = "G"

    if encryptinput == "S":
        output = "F"

    if encryptinput == "®":
        output = "E"

    if encryptinput == "™":
        output = "D"

    if encryptinput == "©":
        output = "C"

    if encryptinput == "T":
        output = "B"

    if encryptinput == "U":
        output = "A"

    if encryptinput == "V":
        output = "9"

    if encryptinput == "W":
        output = "8"

    if encryptinput == "X":
        output = "7"

    if encryptinput == "Y":
        output = "6"

    if encryptinput == "Z":
        output = "5"

    if encryptinput == "¬":
        output = "4"

    if encryptinput == "`":
        output = "3"

    if encryptinput == "¦":
        output = "2"

    if encryptinput == "!":
        output = "1"

    if encryptinput == """:
        output = "0"

    if encryptinput == "£":
        output = "z"

    if encryptinput == "$":
        output = "y"

    if encryptinput == "%":
        output = "x"

    if encryptinput == "^":
        output = "w"

    if encryptinput == "&":
        output = "v"

    if encryptinput == "*":
        output = "u"

    if encryptinput == "(":
        output = "t"

    if encryptinput == ")":
        output = "s"

    if encryptinput == "-":
        output = "r"

    if encryptinput == "=":
        output = "q"

    if encryptinput == "_":
        output = "p"

    if encryptinput == "+":
        output = "o"

    if encryptinput == "[":
        output = "n"

    if encryptinput == "]":
        output = "m"

    if encryptinput == "{":
        output = "l"

    if encryptinput == "}":
        output = "k"

    if encryptinput == ";":
        output = "j"

    if encryptinput == "'":
        output = "i"

    if encryptinput == "#":
        output = "h"

    if encryptinput == ":":
        output = "g"

    if encryptinput == "@":
        output = "f"

    if encryptinput == "~":
        output = "e"

    if encryptinput == ",":
        output = "d"

    filey = open("Resources/tempfile.txt","a")
    filey.write(str(output))
    filey.close()
