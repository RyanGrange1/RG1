def node0(split1):
    output = ""
    encryptinput = split1

    if encryptinput == "+":
        output = "|"

    if encryptinput == "[":
        output = " "

    if encryptinput == "]":
        output = "?"

    if encryptinput == "{":
        output = ">"

    if encryptinput == "}":
        output = "<"

    if encryptinput == ";":
        output = "/"

    if encryptinput == "'":
        output = "."

    if encryptinput == "#":
        output = ","

    if encryptinput == ":":
        output = "~"

    if encryptinput == "@":
        output = "@"

    if encryptinput == "~":
        output = ":"

    if encryptinput == ",":
        output = "#"

    if encryptinput == ".":
        output = "'"

    if encryptinput == "/":
        output = ";"

    if encryptinput == "<":
        output = "}"

    if encryptinput == ">":
        output = "{"

    if encryptinput == "?":
        output = "]"

    if encryptinput == " ":
        output = "["

    if encryptinput == "|":
        output = "+"

    if encryptinput == "a":
        output = "_"

    if encryptinput == "b":
        output = "="

    if encryptinput == "c":
        output = "-"

    if encryptinput == "d":
        output = ")"

    if encryptinput == "e":
        output = "("

    if encryptinput == "f":
        output = "*"

    if encryptinput == "g":
        output = "&"

    if encryptinput == "h":
        output = "^"

    if encryptinput == "i":
        output = "%"

    if encryptinput == "j":
        output = "$"

    if encryptinput == "k":
        output = "£"

    if encryptinput == "l":
        output = "'"

    if encryptinput == "m":
        output = "!"

    if encryptinput == "n":
        output = "¦"

    if encryptinput == "o":
        output = "`"

    if encryptinput == "p":
        output = "¬"

    if encryptinput == "q":
        output = "Z"

    if encryptinput == "r":
        output = "Y"

    if encryptinput == "s":
        output = "X"

    if encryptinput == "t":
        output = "W"

    if encryptinput == "u":
        output = "V"

    if encryptinput == "v":
        output = "U"

    if encryptinput == "w":
        output = "T"

    if encryptinput == "x":
        output = "©"

    if encryptinput == "y":
        output = "™"

    if encryptinput == "z":
        output = "®"

    if encryptinput == "0":
        output = "S"

    if encryptinput == "1":
        output = "R"

    if encryptinput == "2":
        output = "Q"

    if encryptinput == "3":
        output = "P"

    if encryptinput == "4":
        output = "O"

    if encryptinput == "5":
        output = "N"

    if encryptinput == "6":
        output = "M"

    if encryptinput == "7":
        output = "L"

    if encryptinput == "8":
        output = "K"

    if encryptinput == "9":
        output = "J"

    if encryptinput == "A":
        output = "I"

    if encryptinput == "B":
        output = "H"

    if encryptinput == "C":
        output = "G"

    if encryptinput == "D":
        output = "F"

    if encryptinput == "E":
        output = "E"

    if encryptinput == "F":
        output = "D"

    if encryptinput == "G":
        output = "C"

    if encryptinput == "H":
        output = "B"

    if encryptinput == "I":
        output = "A"

    if encryptinput == "J":
        output = "9"

    if encryptinput == "K":
        output = "8"

    if encryptinput == "L":
        output = "7"

    if encryptinput == "M":
        output = "6"

    if encryptinput == "N":
        output = "5"

    if encryptinput == "O":
        output = "4"

    if encryptinput == "P":
        output = "3"

    if encryptinput == "Q":
        output = "2"

    if encryptinput == "R":
        output = "1"

    if encryptinput == "S":
        output = "0"

    if encryptinput == "®":
        output = "z"

    if encryptinput == "™":
        output = "y"

    if encryptinput == "©":
        output = "x"

    if encryptinput == "T":
        output = "w"

    if encryptinput == "U":
        output = "v"

    if encryptinput == "V":
        output = "u"

    if encryptinput == "W":
        output = "t"

    if encryptinput == "X":
        output = "s"

    if encryptinput == "Y":
        output = "r"

    if encryptinput == "Z":
        output = "q"

    if encryptinput == "¬":
        output = "p"

    if encryptinput == "`":
        output = "o"

    if encryptinput == "¦":
        output = "n"

    if encryptinput == "!":
        output = "m"

    if encryptinput == "'":
        output = "l"

    if encryptinput == "£":
        output = "k"

    if encryptinput == "$":
        output = "j"

    if encryptinput == "%":
        output = "i"

    if encryptinput == "^":
        output = "h"

    if encryptinput == "&":
        output = "g"

    if encryptinput == "*":
        output = "f"

    if encryptinput == "(":
        output = "e"

    if encryptinput == ")":
        output = "d"

    if encryptinput == "-":
        output = "c"

    if encryptinput == "=":
        output = "b"

    if encryptinput == "_":
        output = "a"

    filey = open("Resources/tempfile.rg1","a")
    filey.write(str(output))
    filey.close()


def node1(split1):
    output = ""
    encryptinput = split1

    if encryptinput == "[":
        output = "|"

    if encryptinput == "]":
        output = " "

    if encryptinput == "{":
        output = "?"

    if encryptinput == "}":
        output = ">"

    if encryptinput == ";":
        output = "<"

    if encryptinput == "'":
        output = "/"

    if encryptinput == "#":
        output = "."

    if encryptinput == ":":
        output = ","

    if encryptinput == "@":
        output = "~"

    if encryptinput == "~":
        output = "@"

    if encryptinput == ",":
        output = ":"

    if encryptinput == ".":
        output = "#"

    if encryptinput == "/":
        output = "'"

    if encryptinput == "<":
        output = ";"

    if encryptinput == ">":
        output = "}"

    if encryptinput == "?":
        output = "{"

    if encryptinput == " ":
        output = "]"

    if encryptinput == "|":
        output = "["

    if encryptinput == "a":
        output = "+"

    if encryptinput == "b":
        output = "_"

    if encryptinput == "c":
        output = "="

    if encryptinput == "d":
        output = "-"

    if encryptinput == "e":
        output = ")"

    if encryptinput == "f":
        output = "("

    if encryptinput == "g":
        output = "*"

    if encryptinput == "h":
        output = "&"

    if encryptinput == "i":
        output = "^"

    if encryptinput == "j":
        output = "%"

    if encryptinput == "k":
        output = "$"

    if encryptinput == "l":
        output = "£"

    if encryptinput == "m":
        output = "'"

    if encryptinput == "n":
        output = "!"

    if encryptinput == "o":
        output = "¦"

    if encryptinput == "p":
        output = "`"

    if encryptinput == "q":
        output = "¬"

    if encryptinput == "r":
        output = "Z"

    if encryptinput == "s":
        output = "Y"

    if encryptinput == "t":
        output = "X"

    if encryptinput == "u":
        output = "W"

    if encryptinput == "v":
        output = "V"

    if encryptinput == "w":
        output = "U"

    if encryptinput == "x":
        output = "T"

    if encryptinput == "y":
        output = "©"

    if encryptinput == "z":
        output = "™"

    if encryptinput == "0":
        output = "®"

    if encryptinput == "1":
        output = "S"

    if encryptinput == "2":
        output = "R"

    if encryptinput == "3":
        output = "Q"

    if encryptinput == "4":
        output = "P"

    if encryptinput == "5":
        output = "O"

    if encryptinput == "6":
        output = "N"

    if encryptinput == "7":
        output = "M"

    if encryptinput == "8":
        output = "L"

    if encryptinput == "9":
        output = "K"

    if encryptinput == "A":
        output = "J"

    if encryptinput == "B":
        output = "I"

    if encryptinput == "C":
        output = "H"

    if encryptinput == "D":
        output = "G"

    if encryptinput == "E":
        output = "F"

    if encryptinput == "F":
        output = "E"

    if encryptinput == "G":
        output = "D"

    if encryptinput == "H":
        output = "C"

    if encryptinput == "I":
        output = "B"

    if encryptinput == "J":
        output = "A"

    if encryptinput == "K":
        output = "9"

    if encryptinput == "L":
        output = "8"

    if encryptinput == "M":
        output = "7"

    if encryptinput == "N":
        output = "6"

    if encryptinput == "O":
        output = "5"

    if encryptinput == "P":
        output = "4"

    if encryptinput == "Q":
        output = "3"

    if encryptinput == "R":
        output = "2"

    if encryptinput == "S":
        output = "1"

    if encryptinput == "®":
        output = "0"

    if encryptinput == "™":
        output = "z"

    if encryptinput == "©":
        output = "y"

    if encryptinput == "T":
        output = "x"

    if encryptinput == "U":
        output = "w"

    if encryptinput == "V":
        output = "v"

    if encryptinput == "W":
        output = "u"

    if encryptinput == "X":
        output = "t"

    if encryptinput == "Y":
        output = "s"

    if encryptinput == "Z":
        output = "r"

    if encryptinput == "¬":
        output = "q"

    if encryptinput == "`":
        output = "p"

    if encryptinput == "¦":
        output = "o"

    if encryptinput == "!":
        output = "n"

    if encryptinput == "'":
        output = "m"

    if encryptinput == "£":
        output = "l"

    if encryptinput == "$":
        output = "k"

    if encryptinput == "%":
        output = "j"

    if encryptinput == "^":
        output = "i"

    if encryptinput == "&":
        output = "h"

    if encryptinput == "*":
        output = "g"

    if encryptinput == "(":
        output = "f"

    if encryptinput == ")":
        output = "e"

    if encryptinput == "-":
        output = "d"

    if encryptinput == "=":
        output = "c"

    if encryptinput == "_":
        output = "b"

    if encryptinput == "+":
        output = "a"

    filey = open("Resources/tempfile.rg1","a")
    filey.write(str(output))
    filey.close()


def node2(split1):
    output = ""
    encryptinput = split1

    if encryptinput == "]":
        output = "|"

    if encryptinput == "{":
        output = " "

    if encryptinput == "}":
        output = "?"

    if encryptinput == ";":
        output = ">"

    if encryptinput == "'":
        output = "<"

    if encryptinput == "#":
        output = "/"

    if encryptinput == ":":
        output = "."

    if encryptinput == "@":
        output = ","

    if encryptinput == "~":
        output = "~"

    if encryptinput == ",":
        output = "@"

    if encryptinput == ".":
        output = ":"

    if encryptinput == "/":
        output = "#"

    if encryptinput == "<":
        output = "'"

    if encryptinput == ">":
        output = ";"

    if encryptinput == "?":
        output = "}"

    if encryptinput == " ":
        output = "{"

    if encryptinput == "|":
        output = "]"

    if encryptinput == "a":
        output = "["

    if encryptinput == "b":
        output = "+"

    if encryptinput == "c":
        output = "_"

    if encryptinput == "d":
        output = "="

    if encryptinput == "e":
        output = "-"

    if encryptinput == "f":
        output = ")"

    if encryptinput == "g":
        output = "("

    if encryptinput == "h":
        output = "*"

    if encryptinput == "i":
        output = "&"

    if encryptinput == "j":
        output = "^"

    if encryptinput == "k":
        output = "%"

    if encryptinput == "l":
        output = "$"

    if encryptinput == "m":
        output = "£"

    if encryptinput == "n":
        output = "'"

    if encryptinput == "o":
        output = "!"

    if encryptinput == "p":
        output = "¦"

    if encryptinput == "q":
        output = "`"

    if encryptinput == "r":
        output = "¬"

    if encryptinput == "s":
        output = "Z"

    if encryptinput == "t":
        output = "Y"

    if encryptinput == "u":
        output = "X"

    if encryptinput == "v":
        output = "W"

    if encryptinput == "w":
        output = "V"

    if encryptinput == "x":
        output = "U"

    if encryptinput == "y":
        output = "T"

    if encryptinput == "z":
        output = "©"

    if encryptinput == "0":
        output = "™"

    if encryptinput == "1":
        output = "®"

    if encryptinput == "2":
        output = "S"

    if encryptinput == "3":
        output = "R"

    if encryptinput == "4":
        output = "Q"

    if encryptinput == "5":
        output = "P"

    if encryptinput == "6":
        output = "O"

    if encryptinput == "7":
        output = "N"

    if encryptinput == "8":
        output = "M"

    if encryptinput == "9":
        output = "L"

    if encryptinput == "A":
        output = "K"

    if encryptinput == "B":
        output = "J"

    if encryptinput == "C":
        output = "I"

    if encryptinput == "D":
        output = "H"

    if encryptinput == "E":
        output = "G"

    if encryptinput == "F":
        output = "F"

    if encryptinput == "G":
        output = "E"

    if encryptinput == "H":
        output = "D"

    if encryptinput == "I":
        output = "C"

    if encryptinput == "J":
        output = "B"

    if encryptinput == "K":
        output = "A"

    if encryptinput == "L":
        output = "9"

    if encryptinput == "M":
        output = "8"

    if encryptinput == "N":
        output = "7"

    if encryptinput == "O":
        output = "6"

    if encryptinput == "P":
        output = "5"

    if encryptinput == "Q":
        output = "4"

    if encryptinput == "R":
        output = "3"

    if encryptinput == "S":
        output = "2"

    if encryptinput == "®":
        output = "1"

    if encryptinput == "™":
        output = "0"

    if encryptinput == "©":
        output = "z"

    if encryptinput == "T":
        output = "y"

    if encryptinput == "U":
        output = "x"

    if encryptinput == "V":
        output = "w"

    if encryptinput == "W":
        output = "v"

    if encryptinput == "X":
        output = "u"

    if encryptinput == "Y":
        output = "t"

    if encryptinput == "Z":
        output = "s"

    if encryptinput == "¬":
        output = "r"

    if encryptinput == "`":
        output = "q"

    if encryptinput == "¦":
        output = "p"

    if encryptinput == "!":
        output = "o"

    if encryptinput == "'":
        output = "n"

    if encryptinput == "£":
        output = "m"

    if encryptinput == "$":
        output = "l"

    if encryptinput == "%":
        output = "k"

    if encryptinput == "^":
        output = "j"

    if encryptinput == "&":
        output = "i"

    if encryptinput == "*":
        output = "h"

    if encryptinput == "(":
        output = "g"

    if encryptinput == ")":
        output = "f"

    if encryptinput == "-":
        output = "e"

    if encryptinput == "=":
        output = "d"

    if encryptinput == "_":
        output = "c"

    if encryptinput == "+":
        output = "b"

    if encryptinput == "[":
        output = "a"

    filey = open("Resources/tempfile.rg1","a")
    filey.write(str(output))
    filey.close()


def node3(split1):
    output = ""
    encryptinput = split1

    if encryptinput == "{":
        output = "|"

    if encryptinput == "}":
        output = " "

    if encryptinput == ";":
        output = "?"

    if encryptinput == "'":
        output = ">"

    if encryptinput == "#":
        output = "<"

    if encryptinput == ":":
        output = "/"

    if encryptinput == "@":
        output = "."

    if encryptinput == "~":
        output = ","

    if encryptinput == ",":
        output = "~"

    if encryptinput == ".":
        output = "@"

    if encryptinput == "/":
        output = ":"

    if encryptinput == "<":
        output = "#"

    if encryptinput == ">":
        output = "'"

    if encryptinput == "?":
        output = ";"

    if encryptinput == " ":
        output = "}"

    if encryptinput == "|":
        output = "{"

    if encryptinput == "a":
        output = "]"

    if encryptinput == "b":
        output = "["

    if encryptinput == "c":
        output = "+"

    if encryptinput == "d":
        output = "_"

    if encryptinput == "e":
        output = "="

    if encryptinput == "f":
        output = "-"

    if encryptinput == "g":
        output = ")"

    if encryptinput == "h":
        output = "("

    if encryptinput == "i":
        output = "*"

    if encryptinput == "j":
        output = "&"

    if encryptinput == "k":
        output = "^"

    if encryptinput == "l":
        output = "%"

    if encryptinput == "m":
        output = "$"

    if encryptinput == "n":
        output = "£"

    if encryptinput == "o":
        output = "'"

    if encryptinput == "p":
        output = "!"

    if encryptinput == "q":
        output = "¦"

    if encryptinput == "r":
        output = "`"

    if encryptinput == "s":
        output = "¬"

    if encryptinput == "t":
        output = "Z"

    if encryptinput == "u":
        output = "Y"

    if encryptinput == "v":
        output = "X"

    if encryptinput == "w":
        output = "W"

    if encryptinput == "x":
        output = "V"

    if encryptinput == "y":
        output = "U"

    if encryptinput == "z":
        output = "T"

    if encryptinput == "0":
        output = "©"

    if encryptinput == "1":
        output = "™"

    if encryptinput == "2":
        output = "®"

    if encryptinput == "3":
        output = "S"

    if encryptinput == "4":
        output = "R"

    if encryptinput == "5":
        output = "Q"

    if encryptinput == "6":
        output = "P"

    if encryptinput == "7":
        output = "O"

    if encryptinput == "8":
        output = "N"

    if encryptinput == "9":
        output = "M"

    if encryptinput == "A":
        output = "L"

    if encryptinput == "B":
        output = "K"

    if encryptinput == "C":
        output = "J"

    if encryptinput == "D":
        output = "I"

    if encryptinput == "E":
        output = "H"

    if encryptinput == "F":
        output = "G"

    if encryptinput == "G":
        output = "F"

    if encryptinput == "H":
        output = "E"

    if encryptinput == "I":
        output = "D"

    if encryptinput == "J":
        output = "C"

    if encryptinput == "K":
        output = "B"

    if encryptinput == "L":
        output = "A"

    if encryptinput == "M":
        output = "9"

    if encryptinput == "N":
        output = "8"

    if encryptinput == "O":
        output = "7"

    if encryptinput == "P":
        output = "6"

    if encryptinput == "Q":
        output = "5"

    if encryptinput == "R":
        output = "4"

    if encryptinput == "S":
        output = "3"

    if encryptinput == "®":
        output = "2"

    if encryptinput == "™":
        output = "1"

    if encryptinput == "©":
        output = "0"

    if encryptinput == "T":
        output = "z"

    if encryptinput == "U":
        output = "y"

    if encryptinput == "V":
        output = "x"

    if encryptinput == "W":
        output = "w"

    if encryptinput == "X":
        output = "v"

    if encryptinput == "Y":
        output = "u"

    if encryptinput == "Z":
        output = "t"

    if encryptinput == "¬":
        output = "s"

    if encryptinput == "`":
        output = "r"

    if encryptinput == "¦":
        output = "q"

    if encryptinput == "!":
        output = "p"

    if encryptinput == "'":
        output = "o"

    if encryptinput == "£":
        output = "n"

    if encryptinput == "$":
        output = "m"

    if encryptinput == "%":
        output = "l"

    if encryptinput == "^":
        output = "k"

    if encryptinput == "&":
        output = "j"

    if encryptinput == "*":
        output = "i"

    if encryptinput == "(":
        output = "h"

    if encryptinput == ")":
        output = "g"

    if encryptinput == "-":
        output = "f"

    if encryptinput == "=":
        output = "e"

    if encryptinput == "_":
        output = "d"

    if encryptinput == "+":
        output = "c"

    if encryptinput == "[":
        output = "b"

    if encryptinput == "]":
        output = "a"

    filey = open("Resources/tempfile.rg1","a")
    filey.write(str(output))
    filey.close()


def node4(split1):
    output = ""
    encryptinput = split1

    if encryptinput == "}":
        output = "|"

    if encryptinput == ";":
        output = " "

    if encryptinput == "'":
        output = "?"

    if encryptinput == "#":
        output = ">"

    if encryptinput == ":":
        output = "<"

    if encryptinput == "@":
        output = "/"

    if encryptinput == "~":
        output = "."

    if encryptinput == ",":
        output = ","

    if encryptinput == ".":
        output = "~"

    if encryptinput == "/":
        output = "@"

    if encryptinput == "<":
        output = ":"

    if encryptinput == ">":
        output = "#"

    if encryptinput == "?":
        output = "'"

    if encryptinput == " ":
        output = ";"

    if encryptinput == "|":
        output = "}"

    if encryptinput == "a":
        output = "{"

    if encryptinput == "b":
        output = "]"

    if encryptinput == "c":
        output = "["

    if encryptinput == "d":
        output = "+"

    if encryptinput == "e":
        output = "_"

    if encryptinput == "f":
        output = "="

    if encryptinput == "g":
        output = "-"

    if encryptinput == "h":
        output = ")"

    if encryptinput == "i":
        output = "("

    if encryptinput == "j":
        output = "*"

    if encryptinput == "k":
        output = "&"

    if encryptinput == "l":
        output = "^"

    if encryptinput == "m":
        output = "%"

    if encryptinput == "n":
        output = "$"

    if encryptinput == "o":
        output = "£"

    if encryptinput == "p":
        output = "'"

    if encryptinput == "q":
        output = "!"

    if encryptinput == "r":
        output = "¦"

    if encryptinput == "s":
        output = "`"

    if encryptinput == "t":
        output = "¬"

    if encryptinput == "u":
        output = "Z"

    if encryptinput == "v":
        output = "Y"

    if encryptinput == "w":
        output = "X"

    if encryptinput == "x":
        output = "W"

    if encryptinput == "y":
        output = "V"

    if encryptinput == "z":
        output = "U"

    if encryptinput == "0":
        output = "T"

    if encryptinput == "1":
        output = "©"

    if encryptinput == "2":
        output = "™"

    if encryptinput == "3":
        output = "®"

    if encryptinput == "4":
        output = "S"

    if encryptinput == "5":
        output = "R"

    if encryptinput == "6":
        output = "Q"

    if encryptinput == "7":
        output = "P"

    if encryptinput == "8":
        output = "O"

    if encryptinput == "9":
        output = "N"

    if encryptinput == "A":
        output = "M"

    if encryptinput == "B":
        output = "L"

    if encryptinput == "C":
        output = "K"

    if encryptinput == "D":
        output = "J"

    if encryptinput == "E":
        output = "I"

    if encryptinput == "F":
        output = "H"

    if encryptinput == "G":
        output = "G"

    if encryptinput == "H":
        output = "F"

    if encryptinput == "I":
        output = "E"

    if encryptinput == "J":
        output = "D"

    if encryptinput == "K":
        output = "C"

    if encryptinput == "L":
        output = "B"

    if encryptinput == "M":
        output = "A"

    if encryptinput == "N":
        output = "9"

    if encryptinput == "O":
        output = "8"

    if encryptinput == "P":
        output = "7"

    if encryptinput == "Q":
        output = "6"

    if encryptinput == "R":
        output = "5"

    if encryptinput == "S":
        output = "4"

    if encryptinput == "®":
        output = "3"

    if encryptinput == "™":
        output = "2"

    if encryptinput == "©":
        output = "1"

    if encryptinput == "T":
        output = "0"

    if encryptinput == "U":
        output = "z"

    if encryptinput == "V":
        output = "y"

    if encryptinput == "W":
        output = "x"

    if encryptinput == "X":
        output = "w"

    if encryptinput == "Y":
        output = "v"

    if encryptinput == "Z":
        output = "u"

    if encryptinput == "¬":
        output = "t"

    if encryptinput == "`":
        output = "s"

    if encryptinput == "¦":
        output = "r"

    if encryptinput == "!":
        output = "q"

    if encryptinput == "'":
        output = "p"

    if encryptinput == "£":
        output = "o"

    if encryptinput == "$":
        output = "n"

    if encryptinput == "%":
        output = "m"

    if encryptinput == "^":
        output = "l"

    if encryptinput == "&":
        output = "k"

    if encryptinput == "*":
        output = "j"

    if encryptinput == "(":
        output = "i"

    if encryptinput == ")":
        output = "h"

    if encryptinput == "-":
        output = "g"

    if encryptinput == "=":
        output = "f"

    if encryptinput == "_":
        output = "e"

    if encryptinput == "+":
        output = "d"

    if encryptinput == "[":
        output = "c"

    if encryptinput == "]":
        output = "b"

    if encryptinput == "{":
        output = "a"

    filey = open("Resources/tempfile.rg1","a")
    filey.write(str(output))
    filey.close()


def node5(split1):
    output = ""
    encryptinput = split1

    if encryptinput == ";":
        output = "|"

    if encryptinput == "'":
        output = " "

    if encryptinput == "#":
        output = "?"

    if encryptinput == ":":
        output = ">"

    if encryptinput == "@":
        output = "<"

    if encryptinput == "~":
        output = "/"

    if encryptinput == ",":
        output = "."

    if encryptinput == ".":
        output = ","

    if encryptinput == "/":
        output = "~"

    if encryptinput == "<":
        output = "@"

    if encryptinput == ">":
        output = ":"

    if encryptinput == "?":
        output = "#"

    if encryptinput == " ":
        output = "'"

    if encryptinput == "|":
        output = ";"

    if encryptinput == "a":
        output = "}"

    if encryptinput == "b":
        output = "{"

    if encryptinput == "c":
        output = "]"

    if encryptinput == "d":
        output = "["

    if encryptinput == "e":
        output = "+"

    if encryptinput == "f":
        output = "_"

    if encryptinput == "g":
        output = "="

    if encryptinput == "h":
        output = "-"

    if encryptinput == "i":
        output = ")"

    if encryptinput == "j":
        output = "("

    if encryptinput == "k":
        output = "*"

    if encryptinput == "l":
        output = "&"

    if encryptinput == "m":
        output = "^"

    if encryptinput == "n":
        output = "%"

    if encryptinput == "o":
        output = "$"

    if encryptinput == "p":
        output = "£"

    if encryptinput == "q":
        output = "'"

    if encryptinput == "r":
        output = "!"

    if encryptinput == "s":
        output = "¦"

    if encryptinput == "t":
        output = "`"

    if encryptinput == "u":
        output = "¬"

    if encryptinput == "v":
        output = "Z"

    if encryptinput == "w":
        output = "Y"

    if encryptinput == "x":
        output = "X"

    if encryptinput == "y":
        output = "W"

    if encryptinput == "z":
        output = "V"

    if encryptinput == "0":
        output = "U"

    if encryptinput == "1":
        output = "T"

    if encryptinput == "2":
        output = "©"

    if encryptinput == "3":
        output = "™"

    if encryptinput == "4":
        output = "®"

    if encryptinput == "5":
        output = "S"

    if encryptinput == "6":
        output = "R"

    if encryptinput == "7":
        output = "Q"

    if encryptinput == "8":
        output = "P"

    if encryptinput == "9":
        output = "O"

    if encryptinput == "A":
        output = "N"

    if encryptinput == "B":
        output = "M"

    if encryptinput == "C":
        output = "L"

    if encryptinput == "D":
        output = "K"

    if encryptinput == "E":
        output = "J"

    if encryptinput == "F":
        output = "I"

    if encryptinput == "G":
        output = "H"

    if encryptinput == "H":
        output = "G"

    if encryptinput == "I":
        output = "F"

    if encryptinput == "J":
        output = "E"

    if encryptinput == "K":
        output = "D"

    if encryptinput == "L":
        output = "C"

    if encryptinput == "M":
        output = "B"

    if encryptinput == "N":
        output = "A"

    if encryptinput == "O":
        output = "9"

    if encryptinput == "P":
        output = "8"

    if encryptinput == "Q":
        output = "7"

    if encryptinput == "R":
        output = "6"

    if encryptinput == "S":
        output = "5"

    if encryptinput == "®":
        output = "4"

    if encryptinput == "™":
        output = "3"

    if encryptinput == "©":
        output = "2"

    if encryptinput == "T":
        output = "1"

    if encryptinput == "U":
        output = "0"

    if encryptinput == "V":
        output = "z"

    if encryptinput == "W":
        output = "y"

    if encryptinput == "X":
        output = "x"

    if encryptinput == "Y":
        output = "w"

    if encryptinput == "Z":
        output = "v"

    if encryptinput == "¬":
        output = "u"

    if encryptinput == "`":
        output = "t"

    if encryptinput == "¦":
        output = "s"

    if encryptinput == "!":
        output = "r"

    if encryptinput == "'":
        output = "q"

    if encryptinput == "£":
        output = "p"

    if encryptinput == "$":
        output = "o"

    if encryptinput == "%":
        output = "n"

    if encryptinput == "^":
        output = "m"

    if encryptinput == "&":
        output = "l"

    if encryptinput == "*":
        output = "k"

    if encryptinput == "(":
        output = "j"

    if encryptinput == ")":
        output = "i"

    if encryptinput == "-":
        output = "h"

    if encryptinput == "=":
        output = "g"

    if encryptinput == "_":
        output = "f"

    if encryptinput == "+":
        output = "e"

    if encryptinput == "[":
        output = "d"

    if encryptinput == "]":
        output = "c"

    if encryptinput == "{":
        output = "b"

    if encryptinput == "}":
        output = "a"

    filey = open("Resources/tempfile.rg1","a")
    filey.write(str(output))
    filey.close()


def node6(split1):
    output = ""
    encryptinput = split1

    if encryptinput == "'":
        output = "|"

    if encryptinput == "#":
        output = " "

    if encryptinput == ":":
        output = "?"

    if encryptinput == "@":
        output = ">"

    if encryptinput == "~":
        output = "<"

    if encryptinput == ",":
        output = "/"

    if encryptinput == ".":
        output = "."

    if encryptinput == "/":
        output = ","

    if encryptinput == "<":
        output = "~"

    if encryptinput == ">":
        output = "@"

    if encryptinput == "?":
        output = ":"

    if encryptinput == " ":
        output = "#"

    if encryptinput == "|":
        output = "'"

    if encryptinput == "a":
        output = ";"

    if encryptinput == "b":
        output = "}"

    if encryptinput == "c":
        output = "{"

    if encryptinput == "d":
        output = "]"

    if encryptinput == "e":
        output = "["

    if encryptinput == "f":
        output = "+"

    if encryptinput == "g":
        output = "_"

    if encryptinput == "h":
        output = "="

    if encryptinput == "i":
        output = "-"

    if encryptinput == "j":
        output = ")"

    if encryptinput == "k":
        output = "("

    if encryptinput == "l":
        output = "*"

    if encryptinput == "m":
        output = "&"

    if encryptinput == "n":
        output = "^"

    if encryptinput == "o":
        output = "%"

    if encryptinput == "p":
        output = "$"

    if encryptinput == "q":
        output = "£"

    if encryptinput == "r":
        output = "'"

    if encryptinput == "s":
        output = "!"

    if encryptinput == "t":
        output = "¦"

    if encryptinput == "u":
        output = "`"

    if encryptinput == "v":
        output = "¬"

    if encryptinput == "w":
        output = "Z"

    if encryptinput == "x":
        output = "Y"

    if encryptinput == "y":
        output = "X"

    if encryptinput == "z":
        output = "W"

    if encryptinput == "0":
        output = "V"

    if encryptinput == "1":
        output = "U"

    if encryptinput == "2":
        output = "T"

    if encryptinput == "3":
        output = "©"

    if encryptinput == "4":
        output = "™"

    if encryptinput == "5":
        output = "®"

    if encryptinput == "6":
        output = "S"

    if encryptinput == "7":
        output = "R"

    if encryptinput == "8":
        output = "Q"

    if encryptinput == "9":
        output = "P"

    if encryptinput == "A":
        output = "O"

    if encryptinput == "B":
        output = "N"

    if encryptinput == "C":
        output = "M"

    if encryptinput == "D":
        output = "L"

    if encryptinput == "E":
        output = "K"

    if encryptinput == "F":
        output = "J"

    if encryptinput == "G":
        output = "I"

    if encryptinput == "H":
        output = "H"

    if encryptinput == "I":
        output = "G"

    if encryptinput == "J":
        output = "F"

    if encryptinput == "K":
        output = "E"

    if encryptinput == "L":
        output = "D"

    if encryptinput == "M":
        output = "C"

    if encryptinput == "N":
        output = "B"

    if encryptinput == "O":
        output = "A"

    if encryptinput == "P":
        output = "9"

    if encryptinput == "Q":
        output = "8"

    if encryptinput == "R":
        output = "7"

    if encryptinput == "S":
        output = "6"

    if encryptinput == "®":
        output = "5"

    if encryptinput == "™":
        output = "4"

    if encryptinput == "©":
        output = "3"

    if encryptinput == "T":
        output = "2"

    if encryptinput == "U":
        output = "1"

    if encryptinput == "V":
        output = "0"

    if encryptinput == "W":
        output = "z"

    if encryptinput == "X":
        output = "y"

    if encryptinput == "Y":
        output = "x"

    if encryptinput == "Z":
        output = "w"

    if encryptinput == "¬":
        output = "v"

    if encryptinput == "`":
        output = "u"

    if encryptinput == "¦":
        output = "t"

    if encryptinput == "!":
        output = "s"

    if encryptinput == "'":
        output = "r"

    if encryptinput == "£":
        output = "q"

    if encryptinput == "$":
        output = "p"

    if encryptinput == "%":
        output = "o"

    if encryptinput == "^":
        output = "n"

    if encryptinput == "&":
        output = "m"

    if encryptinput == "*":
        output = "l"

    if encryptinput == "(":
        output = "k"

    if encryptinput == ")":
        output = "j"

    if encryptinput == "-":
        output = "i"

    if encryptinput == "=":
        output = "h"

    if encryptinput == "_":
        output = "g"

    if encryptinput == "+":
        output = "f"

    if encryptinput == "[":
        output = "e"

    if encryptinput == "]":
        output = "d"

    if encryptinput == "{":
        output = "c"

    if encryptinput == "}":
        output = "b"

    if encryptinput == ";":
        output = "a"

    filey = open("Resources/tempfile.rg1","a")
    filey.write(str(output))
    filey.close()


def node7(split1):
    output = ""
    encryptinput = split1

    if encryptinput == "#":
        output = "|"

    if encryptinput == ":":
        output = " "

    if encryptinput == "@":
        output = "?"

    if encryptinput == "~":
        output = ">"

    if encryptinput == ",":
        output = "<"

    if encryptinput == ".":
        output = "/"

    if encryptinput == "/":
        output = "."

    if encryptinput == "<":
        output = ","

    if encryptinput == ">":
        output = "~"

    if encryptinput == "?":
        output = "@"

    if encryptinput == " ":
        output = ":"

    if encryptinput == "|":
        output = "#"

    if encryptinput == "a":
        output = "'"

    if encryptinput == "b":
        output = ";"

    if encryptinput == "c":
        output = "}"

    if encryptinput == "d":
        output = "{"

    if encryptinput == "e":
        output = "]"

    if encryptinput == "f":
        output = "["

    if encryptinput == "g":
        output = "+"

    if encryptinput == "h":
        output = "_"

    if encryptinput == "i":
        output = "="

    if encryptinput == "j":
        output = "-"

    if encryptinput == "k":
        output = ")"

    if encryptinput == "l":
        output = "("

    if encryptinput == "m":
        output = "*"

    if encryptinput == "n":
        output = "&"

    if encryptinput == "o":
        output = "^"

    if encryptinput == "p":
        output = "%"

    if encryptinput == "q":
        output = "$"

    if encryptinput == "r":
        output = "£"

    if encryptinput == "s":
        output = "'"

    if encryptinput == "t":
        output = "!"

    if encryptinput == "u":
        output = "¦"

    if encryptinput == "v":
        output = "`"

    if encryptinput == "w":
        output = "¬"

    if encryptinput == "x":
        output = "Z"

    if encryptinput == "y":
        output = "Y"

    if encryptinput == "z":
        output = "X"

    if encryptinput == "0":
        output = "W"

    if encryptinput == "1":
        output = "V"

    if encryptinput == "2":
        output = "U"

    if encryptinput == "3":
        output = "T"

    if encryptinput == "4":
        output = "©"

    if encryptinput == "5":
        output = "™"

    if encryptinput == "6":
        output = "®"

    if encryptinput == "7":
        output = "S"

    if encryptinput == "8":
        output = "R"

    if encryptinput == "9":
        output = "Q"

    if encryptinput == "A":
        output = "P"

    if encryptinput == "B":
        output = "O"

    if encryptinput == "C":
        output = "N"

    if encryptinput == "D":
        output = "M"

    if encryptinput == "E":
        output = "L"

    if encryptinput == "F":
        output = "K"

    if encryptinput == "G":
        output = "J"

    if encryptinput == "H":
        output = "I"

    if encryptinput == "I":
        output = "H"

    if encryptinput == "J":
        output = "G"

    if encryptinput == "K":
        output = "F"

    if encryptinput == "L":
        output = "E"

    if encryptinput == "M":
        output = "D"

    if encryptinput == "N":
        output = "C"

    if encryptinput == "O":
        output = "B"

    if encryptinput == "P":
        output = "A"

    if encryptinput == "Q":
        output = "9"

    if encryptinput == "R":
        output = "8"

    if encryptinput == "S":
        output = "7"

    if encryptinput == "®":
        output = "6"

    if encryptinput == "™":
        output = "5"

    if encryptinput == "©":
        output = "4"

    if encryptinput == "T":
        output = "3"

    if encryptinput == "U":
        output = "2"

    if encryptinput == "V":
        output = "1"

    if encryptinput == "W":
        output = "0"

    if encryptinput == "X":
        output = "z"

    if encryptinput == "Y":
        output = "y"

    if encryptinput == "Z":
        output = "x"

    if encryptinput == "¬":
        output = "w"

    if encryptinput == "`":
        output = "v"

    if encryptinput == "¦":
        output = "u"

    if encryptinput == "!":
        output = "t"

    if encryptinput == "'":
        output = "s"

    if encryptinput == "£":
        output = "r"

    if encryptinput == "$":
        output = "q"

    if encryptinput == "%":
        output = "p"

    if encryptinput == "^":
        output = "o"

    if encryptinput == "&":
        output = "n"

    if encryptinput == "*":
        output = "m"

    if encryptinput == "(":
        output = "l"

    if encryptinput == ")":
        output = "k"

    if encryptinput == "-":
        output = "j"

    if encryptinput == "=":
        output = "i"

    if encryptinput == "_":
        output = "h"

    if encryptinput == "+":
        output = "g"

    if encryptinput == "[":
        output = "f"

    if encryptinput == "]":
        output = "e"

    if encryptinput == "{":
        output = "d"

    if encryptinput == "}":
        output = "c"

    if encryptinput == ";":
        output = "b"

    if encryptinput == "'":
        output = "a"

    filey = open("Resources/tempfile.rg1","a")
    filey.write(str(output))
    filey.close()


def node8(split1):
    output = ""
    encryptinput = split1

    if encryptinput == ":":
        output = "|"

    if encryptinput == "@":
        output = " "

    if encryptinput == "~":
        output = "?"

    if encryptinput == ",":
        output = ">"

    if encryptinput == ".":
        output = "<"

    if encryptinput == "/":
        output = "/"

    if encryptinput == "<":
        output = "."

    if encryptinput == ">":
        output = ","

    if encryptinput == "?":
        output = "~"

    if encryptinput == " ":
        output = "@"

    if encryptinput == "|":
        output = ":"

    if encryptinput == "a":
        output = "#"

    if encryptinput == "b":
        output = "'"

    if encryptinput == "c":
        output = ";"

    if encryptinput == "d":
        output = "}"

    if encryptinput == "e":
        output = "{"

    if encryptinput == "f":
        output = "]"

    if encryptinput == "g":
        output = "["

    if encryptinput == "h":
        output = "+"

    if encryptinput == "i":
        output = "_"

    if encryptinput == "j":
        output = "="

    if encryptinput == "k":
        output = "-"

    if encryptinput == "l":
        output = ")"

    if encryptinput == "m":
        output = "("

    if encryptinput == "n":
        output = "*"

    if encryptinput == "o":
        output = "&"

    if encryptinput == "p":
        output = "^"

    if encryptinput == "q":
        output = "%"

    if encryptinput == "r":
        output = "$"

    if encryptinput == "s":
        output = "£"

    if encryptinput == "t":
        output = "'"

    if encryptinput == "u":
        output = "!"

    if encryptinput == "v":
        output = "¦"

    if encryptinput == "w":
        output = "`"

    if encryptinput == "x":
        output = "¬"

    if encryptinput == "y":
        output = "Z"

    if encryptinput == "z":
        output = "Y"

    if encryptinput == "0":
        output = "X"

    if encryptinput == "1":
        output = "W"

    if encryptinput == "2":
        output = "V"

    if encryptinput == "3":
        output = "U"

    if encryptinput == "4":
        output = "T"

    if encryptinput == "5":
        output = "©"

    if encryptinput == "6":
        output = "™"

    if encryptinput == "7":
        output = "®"

    if encryptinput == "8":
        output = "S"

    if encryptinput == "9":
        output = "R"

    if encryptinput == "A":
        output = "Q"

    if encryptinput == "B":
        output = "P"

    if encryptinput == "C":
        output = "O"

    if encryptinput == "D":
        output = "N"

    if encryptinput == "E":
        output = "M"

    if encryptinput == "F":
        output = "L"

    if encryptinput == "G":
        output = "K"

    if encryptinput == "H":
        output = "J"

    if encryptinput == "I":
        output = "I"

    if encryptinput == "J":
        output = "H"

    if encryptinput == "K":
        output = "G"

    if encryptinput == "L":
        output = "F"

    if encryptinput == "M":
        output = "E"

    if encryptinput == "N":
        output = "D"

    if encryptinput == "O":
        output = "C"

    if encryptinput == "P":
        output = "B"

    if encryptinput == "Q":
        output = "A"

    if encryptinput == "R":
        output = "9"

    if encryptinput == "S":
        output = "8"

    if encryptinput == "®":
        output = "7"

    if encryptinput == "™":
        output = "6"

    if encryptinput == "©":
        output = "5"

    if encryptinput == "T":
        output = "4"

    if encryptinput == "U":
        output = "3"

    if encryptinput == "V":
        output = "2"

    if encryptinput == "W":
        output = "1"

    if encryptinput == "X":
        output = "0"

    if encryptinput == "Y":
        output = "z"

    if encryptinput == "Z":
        output = "y"

    if encryptinput == "¬":
        output = "x"

    if encryptinput == "`":
        output = "w"

    if encryptinput == "¦":
        output = "v"

    if encryptinput == "!":
        output = "u"

    if encryptinput == "'":
        output = "t"

    if encryptinput == "£":
        output = "s"

    if encryptinput == "$":
        output = "r"

    if encryptinput == "%":
        output = "q"

    if encryptinput == "^":
        output = "p"

    if encryptinput == "&":
        output = "o"

    if encryptinput == "*":
        output = "n"

    if encryptinput == "(":
        output = "m"

    if encryptinput == ")":
        output = "l"

    if encryptinput == "-":
        output = "k"

    if encryptinput == "=":
        output = "j"

    if encryptinput == "_":
        output = "i"

    if encryptinput == "+":
        output = "h"

    if encryptinput == "[":
        output = "g"

    if encryptinput == "]":
        output = "f"

    if encryptinput == "{":
        output = "e"

    if encryptinput == "}":
        output = "d"

    if encryptinput == ";":
        output = "c"

    if encryptinput == "'":
        output = "b"

    if encryptinput == "#":
        output = "a"

    filey = open("Resources/tempfile.rg1","a")
    filey.write(str(output))
    filey.close()


def node9(split1):
    output = ""
    encryptinput = split1

    if encryptinput == "@":
        output = "|"

    if encryptinput == "~":
        output = " "

    if encryptinput == ",":
        output = "?"

    if encryptinput == ".":
        output = ">"

    if encryptinput == "/":
        output = "<"

    if encryptinput == "<":
        output = "/"

    if encryptinput == ">":
        output = "."

    if encryptinput == "?":
        output = ","

    if encryptinput == " ":
        output = "~"

    if encryptinput == "|":
        output = "@"

    if encryptinput == "a":
        output = ":"

    if encryptinput == "b":
        output = "#"

    if encryptinput == "c":
        output = "'"

    if encryptinput == "d":
        output = ";"

    if encryptinput == "e":
        output = "}"

    if encryptinput == "f":
        output = "{"

    if encryptinput == "g":
        output = "]"

    if encryptinput == "h":
        output = "["

    if encryptinput == "i":
        output = "+"

    if encryptinput == "j":
        output = "_"

    if encryptinput == "k":
        output = "="

    if encryptinput == "l":
        output = "-"

    if encryptinput == "m":
        output = ")"

    if encryptinput == "n":
        output = "("

    if encryptinput == "o":
        output = "*"

    if encryptinput == "p":
        output = "&"

    if encryptinput == "q":
        output = "^"

    if encryptinput == "r":
        output = "%"

    if encryptinput == "s":
        output = "$"

    if encryptinput == "t":
        output = "£"

    if encryptinput == "u":
        output = "'"

    if encryptinput == "v":
        output = "!"

    if encryptinput == "w":
        output = "¦"

    if encryptinput == "x":
        output = "`"

    if encryptinput == "y":
        output = "¬"

    if encryptinput == "z":
        output = "Z"

    if encryptinput == "0":
        output = "Y"

    if encryptinput == "1":
        output = "X"

    if encryptinput == "2":
        output = "W"

    if encryptinput == "3":
        output = "V"

    if encryptinput == "4":
        output = "U"

    if encryptinput == "5":
        output = "T"

    if encryptinput == "6":
        output = "©"

    if encryptinput == "7":
        output = "™"

    if encryptinput == "8":
        output = "®"

    if encryptinput == "9":
        output = "S"

    if encryptinput == "A":
        output = "R"

    if encryptinput == "B":
        output = "Q"

    if encryptinput == "C":
        output = "P"

    if encryptinput == "D":
        output = "O"

    if encryptinput == "E":
        output = "N"

    if encryptinput == "F":
        output = "M"

    if encryptinput == "G":
        output = "L"

    if encryptinput == "H":
        output = "K"

    if encryptinput == "I":
        output = "J"

    if encryptinput == "J":
        output = "I"

    if encryptinput == "K":
        output = "H"

    if encryptinput == "L":
        output = "G"

    if encryptinput == "M":
        output = "F"

    if encryptinput == "N":
        output = "E"

    if encryptinput == "O":
        output = "D"

    if encryptinput == "P":
        output = "C"

    if encryptinput == "Q":
        output = "B"

    if encryptinput == "R":
        output = "A"

    if encryptinput == "S":
        output = "9"

    if encryptinput == "®":
        output = "8"

    if encryptinput == "™":
        output = "7"

    if encryptinput == "©":
        output = "6"

    if encryptinput == "T":
        output = "5"

    if encryptinput == "U":
        output = "4"

    if encryptinput == "V":
        output = "3"

    if encryptinput == "W":
        output = "2"

    if encryptinput == "X":
        output = "1"

    if encryptinput == "Y":
        output = "0"

    if encryptinput == "Z":
        output = "z"

    if encryptinput == "¬":
        output = "y"

    if encryptinput == "`":
        output = "x"

    if encryptinput == "¦":
        output = "w"

    if encryptinput == "!":
        output = "v"

    if encryptinput == "'":
        output = "u"

    if encryptinput == "£":
        output = "t"

    if encryptinput == "$":
        output = "s"

    if encryptinput == "%":
        output = "r"

    if encryptinput == "^":
        output = "q"

    if encryptinput == "&":
        output = "p"

    if encryptinput == "*":
        output = "o"

    if encryptinput == "(":
        output = "n"

    if encryptinput == ")":
        output = "m"

    if encryptinput == "-":
        output = "l"

    if encryptinput == "=":
        output = "k"

    if encryptinput == "_":
        output = "j"

    if encryptinput == "+":
        output = "i"

    if encryptinput == "[":
        output = "h"

    if encryptinput == "]":
        output = "g"

    if encryptinput == "{":
        output = "f"

    if encryptinput == "}":
        output = "e"

    if encryptinput == ";":
        output = "d"

    if encryptinput == "'":
        output = "c"

    if encryptinput == "#":
        output = "b"

    if encryptinput == ":":
        output = "a"

    filey = open("Resources/tempfile.rg1","a")
    filey.write(str(output))
    filey.close()


def nodea(split1):
    output = ""
    encryptinput = split1

    if encryptinput == "~":
        output = "|"

    if encryptinput == ",":
        output = " "

    if encryptinput == ".":
        output = "?"

    if encryptinput == "/":
        output = ">"

    if encryptinput == "<":
        output = "<"

    if encryptinput == ">":
        output = "/"

    if encryptinput == "?":
        output = "."

    if encryptinput == " ":
        output = ","

    if encryptinput == "|":
        output = "~"

    if encryptinput == "a":
        output = "@"

    if encryptinput == "b":
        output = ":"

    if encryptinput == "c":
        output = "#"

    if encryptinput == "d":
        output = "'"

    if encryptinput == "e":
        output = ";"

    if encryptinput == "f":
        output = "}"

    if encryptinput == "g":
        output = "{"

    if encryptinput == "h":
        output = "]"

    if encryptinput == "i":
        output = "["

    if encryptinput == "j":
        output = "+"

    if encryptinput == "k":
        output = "_"

    if encryptinput == "l":
        output = "="

    if encryptinput == "m":
        output = "-"

    if encryptinput == "n":
        output = ")"

    if encryptinput == "o":
        output = "("

    if encryptinput == "p":
        output = "*"

    if encryptinput == "q":
        output = "&"

    if encryptinput == "r":
        output = "^"

    if encryptinput == "s":
        output = "%"

    if encryptinput == "t":
        output = "$"

    if encryptinput == "u":
        output = "£"

    if encryptinput == "v":
        output = "'"

    if encryptinput == "w":
        output = "!"

    if encryptinput == "x":
        output = "¦"

    if encryptinput == "y":
        output = "`"

    if encryptinput == "z":
        output = "¬"

    if encryptinput == "0":
        output = "Z"

    if encryptinput == "1":
        output = "Y"

    if encryptinput == "2":
        output = "X"

    if encryptinput == "3":
        output = "W"

    if encryptinput == "4":
        output = "V"

    if encryptinput == "5":
        output = "U"

    if encryptinput == "6":
        output = "T"

    if encryptinput == "7":
        output = "©"

    if encryptinput == "8":
        output = "™"

    if encryptinput == "9":
        output = "®"

    if encryptinput == "A":
        output = "S"

    if encryptinput == "B":
        output = "R"

    if encryptinput == "C":
        output = "Q"

    if encryptinput == "D":
        output = "P"

    if encryptinput == "E":
        output = "O"

    if encryptinput == "F":
        output = "N"

    if encryptinput == "G":
        output = "M"

    if encryptinput == "H":
        output = "L"

    if encryptinput == "I":
        output = "K"

    if encryptinput == "J":
        output = "J"

    if encryptinput == "K":
        output = "I"

    if encryptinput == "L":
        output = "H"

    if encryptinput == "M":
        output = "G"

    if encryptinput == "N":
        output = "F"

    if encryptinput == "O":
        output = "E"

    if encryptinput == "P":
        output = "D"

    if encryptinput == "Q":
        output = "C"

    if encryptinput == "R":
        output = "B"

    if encryptinput == "S":
        output = "A"

    if encryptinput == "®":
        output = "9"

    if encryptinput == "™":
        output = "8"

    if encryptinput == "©":
        output = "7"

    if encryptinput == "T":
        output = "6"

    if encryptinput == "U":
        output = "5"

    if encryptinput == "V":
        output = "4"

    if encryptinput == "W":
        output = "3"

    if encryptinput == "X":
        output = "2"

    if encryptinput == "Y":
        output = "1"

    if encryptinput == "Z":
        output = "0"

    if encryptinput == "¬":
        output = "z"

    if encryptinput == "`":
        output = "y"

    if encryptinput == "¦":
        output = "x"

    if encryptinput == "!":
        output = "w"

    if encryptinput == "'":
        output = "v"

    if encryptinput == "£":
        output = "u"

    if encryptinput == "$":
        output = "t"

    if encryptinput == "%":
        output = "s"

    if encryptinput == "^":
        output = "r"

    if encryptinput == "&":
        output = "q"

    if encryptinput == "*":
        output = "p"

    if encryptinput == "(":
        output = "o"

    if encryptinput == ")":
        output = "n"

    if encryptinput == "-":
        output = "m"

    if encryptinput == "=":
        output = "l"

    if encryptinput == "_":
        output = "k"

    if encryptinput == "+":
        output = "j"

    if encryptinput == "[":
        output = "i"

    if encryptinput == "]":
        output = "h"

    if encryptinput == "{":
        output = "g"

    if encryptinput == "}":
        output = "f"

    if encryptinput == ";":
        output = "e"

    if encryptinput == "'":
        output = "d"

    if encryptinput == "#":
        output = "c"

    if encryptinput == ":":
        output = "b"

    if encryptinput == "@":
        output = "a"

    filey = open("Resources/tempfile.rg1","a")
    filey.write(str(output))
    filey.close()


def nodeb(split1):
    output = ""
    encryptinput = split1

    if encryptinput == ",":
        output = "|"

    if encryptinput == ".":
        output = " "

    if encryptinput == "/":
        output = "?"

    if encryptinput == "<":
        output = ">"

    if encryptinput == ">":
        output = "<"

    if encryptinput == "?":
        output = "/"

    if encryptinput == " ":
        output = "."

    if encryptinput == "|":
        output = ","

    if encryptinput == "a":
        output = "~"

    if encryptinput == "b":
        output = "@"

    if encryptinput == "c":
        output = ":"

    if encryptinput == "d":
        output = "#"

    if encryptinput == "e":
        output = "'"

    if encryptinput == "f":
        output = ";"

    if encryptinput == "g":
        output = "}"

    if encryptinput == "h":
        output = "{"

    if encryptinput == "i":
        output = "]"

    if encryptinput == "j":
        output = "["

    if encryptinput == "k":
        output = "+"

    if encryptinput == "l":
        output = "_"

    if encryptinput == "m":
        output = "="

    if encryptinput == "n":
        output = "-"

    if encryptinput == "o":
        output = ")"

    if encryptinput == "p":
        output = "("

    if encryptinput == "q":
        output = "*"

    if encryptinput == "r":
        output = "&"

    if encryptinput == "s":
        output = "^"

    if encryptinput == "t":
        output = "%"

    if encryptinput == "u":
        output = "$"

    if encryptinput == "v":
        output = "£"

    if encryptinput == "w":
        output = "'"

    if encryptinput == "x":
        output = "!"

    if encryptinput == "y":
        output = "¦"

    if encryptinput == "z":
        output = "`"

    if encryptinput == "0":
        output = "¬"

    if encryptinput == "1":
        output = "Z"

    if encryptinput == "2":
        output = "Y"

    if encryptinput == "3":
        output = "X"

    if encryptinput == "4":
        output = "W"

    if encryptinput == "5":
        output = "V"

    if encryptinput == "6":
        output = "U"

    if encryptinput == "7":
        output = "T"

    if encryptinput == "8":
        output = "©"

    if encryptinput == "9":
        output = "™"

    if encryptinput == "A":
        output = "®"

    if encryptinput == "B":
        output = "S"

    if encryptinput == "C":
        output = "R"

    if encryptinput == "D":
        output = "Q"

    if encryptinput == "E":
        output = "P"

    if encryptinput == "F":
        output = "O"

    if encryptinput == "G":
        output = "N"

    if encryptinput == "H":
        output = "M"

    if encryptinput == "I":
        output = "L"

    if encryptinput == "J":
        output = "K"

    if encryptinput == "K":
        output = "J"

    if encryptinput == "L":
        output = "I"

    if encryptinput == "M":
        output = "H"

    if encryptinput == "N":
        output = "G"

    if encryptinput == "O":
        output = "F"

    if encryptinput == "P":
        output = "E"

    if encryptinput == "Q":
        output = "D"

    if encryptinput == "R":
        output = "C"

    if encryptinput == "S":
        output = "B"

    if encryptinput == "®":
        output = "A"

    if encryptinput == "™":
        output = "9"

    if encryptinput == "©":
        output = "8"

    if encryptinput == "T":
        output = "7"

    if encryptinput == "U":
        output = "6"

    if encryptinput == "V":
        output = "5"

    if encryptinput == "W":
        output = "4"

    if encryptinput == "X":
        output = "3"

    if encryptinput == "Y":
        output = "2"

    if encryptinput == "Z":
        output = "1"

    if encryptinput == "¬":
        output = "0"

    if encryptinput == "`":
        output = "z"

    if encryptinput == "¦":
        output = "y"

    if encryptinput == "!":
        output = "x"

    if encryptinput == "'":
        output = "w"

    if encryptinput == "£":
        output = "v"

    if encryptinput == "$":
        output = "u"

    if encryptinput == "%":
        output = "t"

    if encryptinput == "^":
        output = "s"

    if encryptinput == "&":
        output = "r"

    if encryptinput == "*":
        output = "q"

    if encryptinput == "(":
        output = "p"

    if encryptinput == ")":
        output = "o"

    if encryptinput == "-":
        output = "n"

    if encryptinput == "=":
        output = "m"

    if encryptinput == "_":
        output = "l"

    if encryptinput == "+":
        output = "k"

    if encryptinput == "[":
        output = "j"

    if encryptinput == "]":
        output = "i"

    if encryptinput == "{":
        output = "h"

    if encryptinput == "}":
        output = "g"

    if encryptinput == ";":
        output = "f"

    if encryptinput == "'":
        output = "e"

    if encryptinput == "#":
        output = "d"

    if encryptinput == ":":
        output = "c"

    if encryptinput == "@":
        output = "b"

    if encryptinput == "~":
        output = "a"

    filey = open("Resources/tempfile.rg1","a")
    filey.write(str(output))
    filey.close()


def nodec(split1):
    output = ""
    encryptinput = split1

    if encryptinput == ".":
        output = "|"

    if encryptinput == "/":
        output = " "

    if encryptinput == "<":
        output = "?"

    if encryptinput == ">":
        output = ">"

    if encryptinput == "?":
        output = "<"

    if encryptinput == " ":
        output = "/"

    if encryptinput == "|":
        output = "."

    if encryptinput == "a":
        output = ","

    if encryptinput == "b":
        output = "~"

    if encryptinput == "c":
        output = "@"

    if encryptinput == "d":
        output = ":"

    if encryptinput == "e":
        output = "#"

    if encryptinput == "f":
        output = "'"

    if encryptinput == "g":
        output = ";"

    if encryptinput == "h":
        output = "}"

    if encryptinput == "i":
        output = "{"

    if encryptinput == "j":
        output = "]"

    if encryptinput == "k":
        output = "["

    if encryptinput == "l":
        output = "+"

    if encryptinput == "m":
        output = "_"

    if encryptinput == "n":
        output = "="

    if encryptinput == "o":
        output = "-"

    if encryptinput == "p":
        output = ")"

    if encryptinput == "q":
        output = "("

    if encryptinput == "r":
        output = "*"

    if encryptinput == "s":
        output = "&"

    if encryptinput == "t":
        output = "^"

    if encryptinput == "u":
        output = "%"

    if encryptinput == "v":
        output = "$"

    if encryptinput == "w":
        output = "£"

    if encryptinput == "x":
        output = "'"

    if encryptinput == "y":
        output = "!"

    if encryptinput == "z":
        output = "¦"

    if encryptinput == "0":
        output = "`"

    if encryptinput == "1":
        output = "¬"

    if encryptinput == "2":
        output = "Z"

    if encryptinput == "3":
        output = "Y"

    if encryptinput == "4":
        output = "X"

    if encryptinput == "5":
        output = "W"

    if encryptinput == "6":
        output = "V"

    if encryptinput == "7":
        output = "U"

    if encryptinput == "8":
        output = "T"

    if encryptinput == "9":
        output = "©"

    if encryptinput == "A":
        output = "™"

    if encryptinput == "B":
        output = "®"

    if encryptinput == "C":
        output = "S"

    if encryptinput == "D":
        output = "R"

    if encryptinput == "E":
        output = "Q"

    if encryptinput == "F":
        output = "P"

    if encryptinput == "G":
        output = "O"

    if encryptinput == "H":
        output = "N"

    if encryptinput == "I":
        output = "M"

    if encryptinput == "J":
        output = "L"

    if encryptinput == "K":
        output = "K"

    if encryptinput == "L":
        output = "J"

    if encryptinput == "M":
        output = "I"

    if encryptinput == "N":
        output = "H"

    if encryptinput == "O":
        output = "G"

    if encryptinput == "P":
        output = "F"

    if encryptinput == "Q":
        output = "E"

    if encryptinput == "R":
        output = "D"

    if encryptinput == "S":
        output = "C"

    if encryptinput == "®":
        output = "B"

    if encryptinput == "™":
        output = "A"

    if encryptinput == "©":
        output = "9"

    if encryptinput == "T":
        output = "8"

    if encryptinput == "U":
        output = "7"

    if encryptinput == "V":
        output = "6"

    if encryptinput == "W":
        output = "5"

    if encryptinput == "X":
        output = "4"

    if encryptinput == "Y":
        output = "3"

    if encryptinput == "Z":
        output = "2"

    if encryptinput == "¬":
        output = "1"

    if encryptinput == "`":
        output = "0"

    if encryptinput == "¦":
        output = "z"

    if encryptinput == "!":
        output = "y"

    if encryptinput == "'":
        output = "x"

    if encryptinput == "£":
        output = "w"

    if encryptinput == "$":
        output = "v"

    if encryptinput == "%":
        output = "u"

    if encryptinput == "^":
        output = "t"

    if encryptinput == "&":
        output = "s"

    if encryptinput == "*":
        output = "r"

    if encryptinput == "(":
        output = "q"

    if encryptinput == ")":
        output = "p"

    if encryptinput == "-":
        output = "o"

    if encryptinput == "=":
        output = "n"

    if encryptinput == "_":
        output = "m"

    if encryptinput == "+":
        output = "l"

    if encryptinput == "[":
        output = "k"

    if encryptinput == "]":
        output = "j"

    if encryptinput == "{":
        output = "i"

    if encryptinput == "}":
        output = "h"

    if encryptinput == ";":
        output = "g"

    if encryptinput == "'":
        output = "f"

    if encryptinput == "#":
        output = "e"

    if encryptinput == ":":
        output = "d"

    if encryptinput == "@":
        output = "c"

    if encryptinput == "~":
        output = "b"

    if encryptinput == ",":
        output = "a"

    filey = open("Resources/tempfile.rg1","a")
    filey.write(str(output))
    filey.close()


def noded(split1):
    output = ""
    encryptinput = split1

    if encryptinput == "/":
        output = "|"

    if encryptinput == "<":
        output = " "

    if encryptinput == ">":
        output = "?"

    if encryptinput == "?":
        output = ">"

    if encryptinput == " ":
        output = "<"

    if encryptinput == "|":
        output = "/"

    if encryptinput == "a":
        output = "."

    if encryptinput == "b":
        output = ","

    if encryptinput == "c":
        output = "~"

    if encryptinput == "d":
        output = "@"

    if encryptinput == "e":
        output = ":"

    if encryptinput == "f":
        output = "#"

    if encryptinput == "g":
        output = "'"

    if encryptinput == "h":
        output = ";"

    if encryptinput == "i":
        output = "}"

    if encryptinput == "j":
        output = "{"

    if encryptinput == "k":
        output = "]"

    if encryptinput == "l":
        output = "["

    if encryptinput == "m":
        output = "+"

    if encryptinput == "n":
        output = "_"

    if encryptinput == "o":
        output = "="

    if encryptinput == "p":
        output = "-"

    if encryptinput == "q":
        output = ")"

    if encryptinput == "r":
        output = "("

    if encryptinput == "s":
        output = "*"

    if encryptinput == "t":
        output = "&"

    if encryptinput == "u":
        output = "^"

    if encryptinput == "v":
        output = "%"

    if encryptinput == "w":
        output = "$"

    if encryptinput == "x":
        output = "£"

    if encryptinput == "y":
        output = "'"

    if encryptinput == "z":
        output = "!"

    if encryptinput == "0":
        output = "¦"

    if encryptinput == "1":
        output = "`"

    if encryptinput == "2":
        output = "¬"

    if encryptinput == "3":
        output = "Z"

    if encryptinput == "4":
        output = "Y"

    if encryptinput == "5":
        output = "X"

    if encryptinput == "6":
        output = "W"

    if encryptinput == "7":
        output = "V"

    if encryptinput == "8":
        output = "U"

    if encryptinput == "9":
        output = "T"

    if encryptinput == "A":
        output = "©"

    if encryptinput == "B":
        output = "™"

    if encryptinput == "C":
        output = "®"

    if encryptinput == "D":
        output = "S"

    if encryptinput == "E":
        output = "R"

    if encryptinput == "F":
        output = "Q"

    if encryptinput == "G":
        output = "P"

    if encryptinput == "H":
        output = "O"

    if encryptinput == "I":
        output = "N"

    if encryptinput == "J":
        output = "M"

    if encryptinput == "K":
        output = "L"

    if encryptinput == "L":
        output = "K"

    if encryptinput == "M":
        output = "J"

    if encryptinput == "N":
        output = "I"

    if encryptinput == "O":
        output = "H"

    if encryptinput == "P":
        output = "G"

    if encryptinput == "Q":
        output = "F"

    if encryptinput == "R":
        output = "E"

    if encryptinput == "S":
        output = "D"

    if encryptinput == "®":
        output = "C"

    if encryptinput == "™":
        output = "B"

    if encryptinput == "©":
        output = "A"

    if encryptinput == "T":
        output = "9"

    if encryptinput == "U":
        output = "8"

    if encryptinput == "V":
        output = "7"

    if encryptinput == "W":
        output = "6"

    if encryptinput == "X":
        output = "5"

    if encryptinput == "Y":
        output = "4"

    if encryptinput == "Z":
        output = "3"

    if encryptinput == "¬":
        output = "2"

    if encryptinput == "`":
        output = "1"

    if encryptinput == "¦":
        output = "0"

    if encryptinput == "!":
        output = "z"

    if encryptinput == "'":
        output = "y"

    if encryptinput == "£":
        output = "x"

    if encryptinput == "$":
        output = "w"

    if encryptinput == "%":
        output = "v"

    if encryptinput == "^":
        output = "u"

    if encryptinput == "&":
        output = "t"

    if encryptinput == "*":
        output = "s"

    if encryptinput == "(":
        output = "r"

    if encryptinput == ")":
        output = "q"

    if encryptinput == "-":
        output = "p"

    if encryptinput == "=":
        output = "o"

    if encryptinput == "_":
        output = "n"

    if encryptinput == "+":
        output = "m"

    if encryptinput == "[":
        output = "l"

    if encryptinput == "]":
        output = "k"

    if encryptinput == "{":
        output = "j"

    if encryptinput == "}":
        output = "i"

    if encryptinput == ";":
        output = "h"

    if encryptinput == "'":
        output = "g"

    if encryptinput == "#":
        output = "f"

    if encryptinput == ":":
        output = "e"

    if encryptinput == "@":
        output = "d"

    if encryptinput == "~":
        output = "c"

    if encryptinput == ",":
        output = "b"

    if encryptinput == ".":
        output = "a"

    filey = open("Resources/tempfile.rg1","a")
    filey.write(str(output))
    filey.close()


def nodee(split1):
    output = ""
    encryptinput = split1

    if encryptinput == "<":
        output = "|"

    if encryptinput == ">":
        output = " "

    if encryptinput == "?":
        output = "?"

    if encryptinput == " ":
        output = ">"

    if encryptinput == "|":
        output = "<"

    if encryptinput == "a":
        output = "/"

    if encryptinput == "b":
        output = "."

    if encryptinput == "c":
        output = ","

    if encryptinput == "d":
        output = "~"

    if encryptinput == "e":
        output = "@"

    if encryptinput == "f":
        output = ":"

    if encryptinput == "g":
        output = "#"

    if encryptinput == "h":
        output = "'"

    if encryptinput == "i":
        output = ";"

    if encryptinput == "j":
        output = "}"

    if encryptinput == "k":
        output = "{"

    if encryptinput == "l":
        output = "]"

    if encryptinput == "m":
        output = "["

    if encryptinput == "n":
        output = "+"

    if encryptinput == "o":
        output = "_"

    if encryptinput == "p":
        output = "="

    if encryptinput == "q":
        output = "-"

    if encryptinput == "r":
        output = ")"

    if encryptinput == "s":
        output = "("

    if encryptinput == "t":
        output = "*"

    if encryptinput == "u":
        output = "&"

    if encryptinput == "v":
        output = "^"

    if encryptinput == "w":
        output = "%"

    if encryptinput == "x":
        output = "$"

    if encryptinput == "y":
        output = "£"

    if encryptinput == "z":
        output = "'"

    if encryptinput == "0":
        output = "!"

    if encryptinput == "1":
        output = "¦"

    if encryptinput == "2":
        output = "`"

    if encryptinput == "3":
        output = "¬"

    if encryptinput == "4":
        output = "Z"

    if encryptinput == "5":
        output = "Y"

    if encryptinput == "6":
        output = "X"

    if encryptinput == "7":
        output = "W"

    if encryptinput == "8":
        output = "V"

    if encryptinput == "9":
        output = "U"

    if encryptinput == "A":
        output = "T"

    if encryptinput == "B":
        output = "©"

    if encryptinput == "C":
        output = "™"

    if encryptinput == "D":
        output = "®"

    if encryptinput == "E":
        output = "S"

    if encryptinput == "F":
        output = "R"

    if encryptinput == "G":
        output = "Q"

    if encryptinput == "H":
        output = "P"

    if encryptinput == "I":
        output = "O"

    if encryptinput == "J":
        output = "N"

    if encryptinput == "K":
        output = "M"

    if encryptinput == "L":
        output = "L"

    if encryptinput == "M":
        output = "K"

    if encryptinput == "N":
        output = "J"

    if encryptinput == "O":
        output = "I"

    if encryptinput == "P":
        output = "H"

    if encryptinput == "Q":
        output = "G"

    if encryptinput == "R":
        output = "F"

    if encryptinput == "S":
        output = "E"

    if encryptinput == "®":
        output = "D"

    if encryptinput == "™":
        output = "C"

    if encryptinput == "©":
        output = "B"

    if encryptinput == "T":
        output = "A"

    if encryptinput == "U":
        output = "9"

    if encryptinput == "V":
        output = "8"

    if encryptinput == "W":
        output = "7"

    if encryptinput == "X":
        output = "6"

    if encryptinput == "Y":
        output = "5"

    if encryptinput == "Z":
        output = "4"

    if encryptinput == "¬":
        output = "3"

    if encryptinput == "`":
        output = "2"

    if encryptinput == "¦":
        output = "1"

    if encryptinput == "!":
        output = "0"

    if encryptinput == "'":
        output = "z"

    if encryptinput == "£":
        output = "y"

    if encryptinput == "$":
        output = "x"

    if encryptinput == "%":
        output = "w"

    if encryptinput == "^":
        output = "v"

    if encryptinput == "&":
        output = "u"

    if encryptinput == "*":
        output = "t"

    if encryptinput == "(":
        output = "s"

    if encryptinput == ")":
        output = "r"

    if encryptinput == "-":
        output = "q"

    if encryptinput == "=":
        output = "p"

    if encryptinput == "_":
        output = "o"

    if encryptinput == "+":
        output = "n"

    if encryptinput == "[":
        output = "m"

    if encryptinput == "]":
        output = "l"

    if encryptinput == "{":
        output = "k"

    if encryptinput == "}":
        output = "j"

    if encryptinput == ";":
        output = "i"

    if encryptinput == "'":
        output = "h"

    if encryptinput == "#":
        output = "g"

    if encryptinput == ":":
        output = "f"

    if encryptinput == "@":
        output = "e"

    if encryptinput == "~":
        output = "d"

    if encryptinput == ",":
        output = "c"

    if encryptinput == ".":
        output = "b"

    if encryptinput == "/":
        output = "a"

    filey = open("Resources/tempfile.rg1","a")
    filey.write(str(output))
    filey.close()


def nodef(split1):
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
        output = "'"

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

    if encryptinput == "'":
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

    if encryptinput == ".":
        output = "c"

    if encryptinput == "/":
        output = "b"

    if encryptinput == "<":
        output = "a"

    filey = open("Resources/tempfile.rg1","a")
    filey.write(str(output))
    filey.close()
