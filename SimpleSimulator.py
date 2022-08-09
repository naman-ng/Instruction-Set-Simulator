# Naman Garg
# IIIT - DELHI 
# ROLL NO - 2021171
# BRANCH - ECE

# If you are a reader of this code, it would be difficult for you to understand purpose of each and every line of code.
# There were sooo many edge cases that could only be handled with multiple "If-Else" statements.
# So the main part was correct placement of these "If-Else" so that I don't miss any edge case for error gen and print the ouput correctly.
# Wrote the code cleanest possible by me at this time.
# Will update the code later to make it more clean if possible 🙂


# uncomment these 2 lines for taking input through console
# import sys
# code = sys.stdin.read().splitlines()


# uncomment these 2 lines for taking input through file reading
with open('test_case1.txt') as f:  # here test_case1.txt is an input file with assembly code
    code = f.read().splitlines()

assembly = []
label = {}
var = {}
extra = {}
global labelCount
global varCount
labelCount = 1
varCount = 1
var_value = {}
register_val = {}
flagv = 0 
flagl = 0 
flagg = 0
flage = 0

reg_map = {
    "000": "R0",
    "001": "R1",
    "010": "R2",
    "011": "R3",
    "100": "R4", 
    "101": "R5",
    "110": "R6",
    "111": "FLAG"
}

for i in reg_map.values():
    register_val[i] = 0

op_mapping = {
    "10000": ["add", "A"],
    "10001": ["sub", "A"],
    "10010": ["movi", "B"],
    "10011": ["movr", "C"],
    "10100": ["ld", "D"],
    "10101": ["st", "D"],
    "10110": ["mul", "A"],
    "10111": ["div", "C"],
    "11000": ["rs", "B"],
    "11001": ["ls", "B"],
    "11010": ["xor", "A"],
    "11011": ["or", "A"],
    "11100": ["and", "A"],
    "11101": ["not", "C"],
    "11110": ["cmp", "C"],
    "11111": ["jmp", "E"],
    "01100": ["jlt", "E"],
    "01101": ["jgt", "E"],
    "01111": ["je", "E"],
    "01010": ["hlt", "F"],
    "00000": ["addf","A"],
    "00001": ["subf","A"],
    "00010": ["movf","B"]
}



def binaryTodecimal(str):
    return int(str, 2)


def float_To_binary(my_number):
    places = 5
    my_number = float(my_number)
    whol, dec = str(my_number).split(".")
    dec = int (dec)
    whol = int(whol)
    res = bin(whol).lstrip("0b") + "."
    for _ in range(places):
            if (dec != 0):
                whol, dec = str((dec_converter(dec)) * 2).split(".")
                dec = int(dec)
                res += whol
            else:
                break

    ment = ""
    a, b = res.split(".")
    c = a[1:]
    d = c+b
    e = len(c)

    if len(d) > 5:
        ment = d[:5]
    else:
        ment = d + "0"*(5-len(d))
    tt = e 
    if tt > 7:
        tt = 7
    g = bin(tt)[2:]
    g = "0"*(3-len(g)) + g
    return ("00000000" + g + ment)

def dec_converter(num):
   while num > 1:
        num /= 10
   return num


def binaryToFloat(str):
    b = int((str[:3]), 2)
    # print(b)
    d = 1
    f = 0
    e = str[3:]
    # print(e)
    g = 2**b
    for i, j in zip(e, range(len(e))):
        if (i == "1"):
            f += 2**-(j+1)

    # print(f)
    return (g*(f+d))


def typeA(line):
    listA = []
    listA.append(op_mapping[line[0:5]][0])
    listA.append(reg_map[line[7:10]])
    listA.append(reg_map[line[10:13]])
    listA.append(reg_map[line[13:16]])
    assembly.append(listA)


def typeB(line):
    listB = []
    listB.append(op_mapping[line[0:5]][0])
    listB.append(reg_map[line[5:8]])
    if listB[0] == "movf":
        x = binaryToFloat(line[8:])
    else:
        x = binaryTodecimal(line[8:16])
    listB.append(int(x))
    assembly.append(listB)


def typeC(line):
    listC = []
    listC.append(op_mapping[line[0:5]][0])
    listC.append(reg_map[line[10:13]])
    listC.append(reg_map[line[13:16]])
    assembly.append(listC)


def typeD(line):
    global varCount
    listD = []
    listD.append(op_mapping[line[0:5]][0])
    listD.append(reg_map[line[5:8]])
    x = binaryTodecimal(line[8:16])
    if (line[8:16] not in var):
        var[line[8:16]] = "var" + str(varCount)
        varCount += 1

    listD.append(var[line[8:16]])
    assembly.append(listD)


def typeE(line):
    global labelCount
    listE = []
    listE.append(op_mapping[line[0:5]][0])
    if (line[8:16] not in label):
        label[line[8:16]] = "label" + str(labelCount)
        labelCount += 1

    listE.append(label[line[8:16]])
    assembly.append(listE)


for line in code:

    if (len(line)>0):
        type = op_mapping[line[0:5]][1]
        if type == "A":
            typeA(line)
        elif type == "B":
            typeB(line)
        elif type == "C":
            typeC(line)
        elif type == "D":
            typeD(line)
        elif type == "E":
            typeE(line)
        elif type == "F":
            # print("hlt")
            assembly.append(["hlt"])


# --------------------------------------------------------------------------------------------------------------------------------------
def c8(deci):
    binary = bin(deci)[2:]
    len_deci = binary[::-1]
    while len(len_deci) < 8:
        len_deci += '0'
    binary = len_deci[::-1]
    return (binary)


def c16(deci):
    binary = bin(deci)[2:]
    len_deci = binary[::-1]
    while len(len_deci) < 16:
        len_deci += '0'
    binary = len_deci[::-1]
    return (binary)


def flagval(flagv, flagl, flagg, flage):
    flagv = str(flagv)
    flagl = str(flagl)
    flagg = str(flagg)
    flage = str(flage)
    Flagfin = "000000000000"+flagv+flagl+flagg+flage
    return Flagfin

def reset_flag():
    global flagv, flagl, flagg, flage
    flagv = 0
    flagl = 0
    flagg = 0
    flage = 0


def overflow(reg):
    global flagv
    if(reg < 0):
        reg = 0
        flagv = 1

    if(reg > 65535):
        flagv = 1
        reg = lower_16(reg)
    return reg


def lower_16(n):
    n = int(n)%(2**16)
    return n


def add(x1, x2):
    res = x1+x2
    res = overflow(res)
    return res


def sub(x1, x2):
    res = x1-x2
    res = overflow(res)
    return res


def divide(x1, x2):
    global R0, R1
    R0 = x1//x2
    R1 = x1 % x2


def mul(x1, x2):
    res = x1*x2
    res = overflow(res)
    return res


def xor(x1, x2):
    res = x1 ^ x2
    return res


def andop(x1, x2):
    res = x1 & x2
    return res


def orop(x1, x2):
    res = x1 | x2
    return res


def notop(x1):
    res = x1^65535
    return res


def ls(reg, imm):
    res = reg << imm
    res = overflow(res)
    return res


def rs(reg, imm):
    res = reg >> imm
    res = overflow(res)
    return res


def ld(var):
    if var not in var_value:
        var_value[var] = 0
    return var_value[var]


def st(reg, var):
    var_value[var] = reg
    

def cmp(x1, x2):
    global flagg, flagl, flage
    if x1 > x2:
        flagg = 1
    elif x1 < x2:
        flagl = 1
    elif x1 == x2:
        flage = 1




# -----------------------------------------------------------------------------------------------------------------------------------

R0 = 0
R1 = 0
R2 = 0
R3 = 0
R4 = 0
R5 = 0
R6 = 0
pc = -1

list_label_key = list(label.keys())
list_label_value = list(label.values())
programBinary = []
programDecimal = []

TypeE= ["je", "jlt", "jgt"]

i = 0
kk =0
while(2>1):
    kk +=1
    valueofflag = binaryTodecimal(flagval(flagv, flagl, flagg, flage))

    if (i>0):
        if (assembly[i][0] not in TypeE) or (assembly[i-1][0] in TypeE):
            reset_flag()
    
    if (assembly[i][0] == "add"):
        register_val[assembly[i][3]] = add(register_val[assembly[i][1]], register_val[assembly[i][2]])
        pc = pc+1
        i = i+1

    elif (assembly[i][0] == "sub"):
        register_val[assembly[i][3]] = sub(register_val[assembly[i][1]], register_val[assembly[i][2]])
        pc = pc+1
        i = i+1

    elif (assembly[i][0] == "mul"):
        register_val[assembly[i][3]] = mul(register_val[assembly[i][1]], register_val[assembly[i][2]])
        pc = pc+1
        i = i+1

    elif (assembly[i][0] == "div"):
        divide(register_val[assembly[i][1]], register_val[assembly[i][2]])
        register_val["R0"] = R0
        register_val["R1"] = R1
        pc = pc+1
        i = i+1

    elif (assembly[i][0] == "or"):
        register_val[assembly[i][3]] = orop(register_val[assembly[i][1]], register_val[assembly[i][2]])
        pc = pc+1
        i = i+1

    elif (assembly[i][0] == "and"):
        register_val[assembly[i][3]] = andop(register_val[assembly[i][1]], register_val[assembly[i][2]])
        pc = pc+1
        i = i+1

    elif (assembly[i][0] == "xor"):
        register_val[assembly[i][3]] = xor(register_val[assembly[i][1]], register_val[assembly[i][2]])
        pc = pc+1
        i = i+1

    elif (assembly[i][0] == "ls"):
        register_val[assembly[i][1]] = ls(register_val[assembly[i][1]], assembly[i][2])
        pc = pc+1
        i = i+1

    elif (assembly[i][0] == "rs"):
        register_val[assembly[i][1]] = rs(register_val[assembly[i][1]], assembly[i][2])
        pc = pc+1
        i = i+1

    elif (assembly[i][0] == "movi"):
        register_val[assembly[i][1]] = assembly[i][2]
        pc = pc+1
        i = i+1

    elif (assembly[i][0] == "movr"):
        if assembly[i][1] == "FLAG":
            register_val[assembly[i][2]] = valueofflag
        else:    
            register_val[assembly[i][2]] = register_val[assembly[i][1]]
        pc = pc+1
        i = i+1

    elif (assembly[i][0] == "ld"):
        for aa in var.keys():
            if var[aa] == assembly[i][2]:
                extra[kk] = int(aa, 2)
                break

        register_val[assembly[i][1]] = ld(assembly[i][2])
        pc = pc+1
        i = i+1

    elif (assembly[i][0] == "st"):
        for aa in var.keys():
            if var[aa] == assembly[i][2]:
                extra[kk] = int(aa, 2)
                break

        st(register_val[assembly[i][1]], assembly[i][2])
        pc = pc+1
        i = i+1

    elif (assembly[i][0] == "not"):
        register_val[assembly[i][2]] = notop(register_val[assembly[i][1]])
        pc = pc+1
        i = i+1

    elif (assembly[i][0] == "cmp"):
        cmp(register_val[assembly[i][1]], register_val[assembly[i][2]])
        pc = pc+1
        i = i+1

    elif (assembly[i][0] == "jmp"):
        position = list_label_value.index(assembly[i][1])
        pc = pc+1
        i = i+1
        
        programBinary.append([c8(pc), c16(register_val["R0"]), c16(register_val["R1"]), c16(register_val["R2"]), c16(register_val["R3"]), c16(register_val["R4"]), c16(register_val["R5"]), c16(register_val["R6"]), flagval(flagv, flagl, flagg, flage)])
        programDecimal.append([pc, register_val["R0"], register_val["R1"], register_val["R2"], register_val["R3"], register_val["R4"], register_val["R5"], register_val["R6"], [flagv, flagl, flagg, flage]])

        i = binaryTodecimal(list_label_key[position])
        pc = i-1
        continue
    
    elif (assembly[i][0] == "jlt"):
        if(flagl == 1):
            position = list_label_value.index(assembly[i][1])
            pc = pc+1
            i = i+1
            reset_flag()
            
            programBinary.append([c8(pc), c16(register_val["R0"]), c16(register_val["R1"]), c16(register_val["R2"]), c16(register_val["R3"]), c16(register_val["R4"]), c16(register_val["R5"]), c16(register_val["R6"]), flagval(flagv, flagl, flagg, flage)])
            programDecimal.append([pc, register_val["R0"], register_val["R1"], register_val["R2"], register_val["R3"], register_val["R4"], register_val["R5"], register_val["R6"], [flagv, flagl, flagg, flage]])

            i = binaryTodecimal(list_label_key[position])
            pc = i-1
            continue
        else:
            reset_flag()
            pc = pc+1
            i = i+1

    elif (assembly[i][0] == "jgt"):
        if(flagg == 1):
            position = list_label_value.index(assembly[i][1])
            pc = pc+1
            i = i+1
            reset_flag()
            
            programBinary.append([c8(pc), c16(register_val["R0"]), c16(register_val["R1"]), c16(register_val["R2"]), c16(register_val["R3"]), c16(register_val["R4"]), c16(register_val["R5"]), c16(register_val["R6"]), flagval(flagv, flagl, flagg, flage)])
            programDecimal.append([pc, register_val["R0"], register_val["R1"], register_val["R2"], register_val["R3"], register_val["R4"], register_val["R5"], register_val["R6"], [flagv, flagl, flagg, flage]])

            i = binaryTodecimal(list_label_key[position])
            pc = i-1
            continue
        else:
            reset_flag()      
            pc = pc+1
            i = i+1

    elif (assembly[i][0] == "je"):
        if(flage == 1):
            position = list_label_value.index(assembly[i][1])
            pc = pc+1
            i = i+1
            reset_flag()
            
            programBinary.append([c8(pc), c16(register_val["R0"]), c16(register_val["R1"]), c16(register_val["R2"]), c16(register_val["R3"]), c16(register_val["R4"]), c16(register_val["R5"]), c16(register_val["R6"]), flagval(flagv, flagl, flagg, flage)])
            programDecimal.append([pc, register_val["R0"], register_val["R1"], register_val["R2"], register_val["R3"], register_val["R4"], register_val["R5"], register_val["R6"], [flagv, flagl, flagg, flage]])

            i = binaryTodecimal(list_label_key[position])
            pc = i-1
            continue
        else:
            reset_flag()
            pc = pc+1
            i = i+1

    elif (assembly[i][0] == "addf"):
        listx = []
        listy = []
        oo1 = binaryTodecimal(str(c16(register_val[assembly[i][1]]))[8:])
        oo2 = binaryTodecimal(str(c16(register_val[assembly[i][2]]))[8:])
        register_val[assembly[i][3]] = add(oo1, oo2)
        pc = pc+1
        # i = i+1
        listx.append(c8(pc))
        listy.append(pc)
        for t in register_val:
            if t == assembly[i][3]:
                if 0 < register_val[assembly[i][3]] < 253:
                    listx.append(float_To_binary(register_val[assembly[i][3]]))
                else:
                    flagv = 1
                    if register_val[t] < 0:
                        listx.append("0000000000000000")
                    if register_val[t] > 253:
                        listx.append("0000000011111111")
            else:
                listx.append(c16(register_val[t]))
            listy.append(register_val[t])
        i +=1
        listx.append(flagval(flagv, flagl, flagg, flage))
        listy.append([flagv, flagl, flagg, flage])

        programBinary.append(listx)
        programDecimal.append(listy)
        continue

    elif (assembly[i][0] == "subf"):
        listx = []
        listy = []
        oo1 = binaryTodecimal(str(c16(register_val[assembly[i][1]]))[8:])
        oo2 = binaryTodecimal(str(c16(register_val[assembly[i][2]]))[8:])
        register_val[assembly[i][3]] = sub(oo1, oo2)
        pc = pc+1
        # i = i+1
        listx.append(c8(pc))
        listy.append(pc)
        for t in register_val:
            if t == assembly[i][3]:
                if 0 < register_val[assembly[i][3]] < 253:
                    listx.append(float_To_binary(register_val[assembly[i][3]]))
                else:
                    flagv = 1
                    if register_val[t] < 0:
                        listx.append("0000000000000000")
                    if register_val[t] > 253:
                        listx.append("0000000011111111")
            else:
                listx.append(c16(register_val[t]))
            listy.append(register_val[t])

        i +=i
        listx.append(flagval(flagv, flagl, flagg, flage))
        listy.append([flagv, flagl, flagg, flage])

        programBinary.append(listx)
        programDecimal.append(listy)
        continue

    elif (assembly[i][0] == "movf"):
        listx = []
        listy = []
        
        oo1 = binaryTodecimal(str(c16(assembly[i][2]))[8:])
        register_val[assembly[i][1]] = oo1
        pc = pc+1
        
        listx.append(c8(pc))
        listy.append(pc)
        for t in register_val:
            if t == assembly[i][1]:
                if 0 < float(assembly[i][2]) < 253:
                    listx.append(float_To_binary(int(assembly[i][2])))
                else:
                    flagv = 1
                    if register_val[t] < 0:
                        listx.append("0000000000000000")
                    if register_val[t] > 253:
                        listx.append("0000000011111111")
            else:
                listx.append(c16(register_val[t]))
            listy.append(register_val[t])
        i +=1
        listx.append(flagval(flagv, flagl, flagg, flage))
        listy.append([flagv, flagl, flagg, flage])

        programBinary.append(listx)
        programDecimal.append(listy)

        continue


    elif (assembly[i][0] == "hlt"):
        pc += 1
        i = i+1

        programBinary.append([c8(pc), c16(register_val["R0"]), c16(register_val["R1"]), c16(register_val["R2"]), c16(register_val["R3"]), c16(register_val["R4"]), c16(register_val["R5"]), c16(register_val["R6"]), flagval(flagv, flagl, flagg, flage)])

        programDecimal.append([pc, register_val["R0"], register_val["R1"], register_val["R2"], register_val["R3"], register_val["R4"], register_val["R5"], register_val["R6"], [flagv, flagl, flagg, flage]])

        break
    
    
    programBinary.append([c8(pc), c16(register_val["R0"]), c16(register_val["R1"]), c16(register_val["R2"]), c16(register_val["R3"]), c16(register_val["R4"]), c16(register_val["R5"]), c16(register_val["R6"]), flagval(flagv, flagl, flagg, flage)])

    programDecimal.append([pc, register_val["R0"], register_val["R1"], register_val["R2"], register_val["R3"], register_val["R4"], register_val["R5"], register_val["R6"], [flagv, flagl, flagg, flage]])



for i in programBinary:
    print(*i)

lenC = 0
for i in code:
    if len(i)>0:
        lenC += 1
        print(i)


lenV = 0
for i in sorted(var.keys()):
    lenV +=1
    if var[i] in var_value:
        print(c16(var_value[var[i]]))
    else:
        print("0000000000000000")

for i in range(256 - lenV - lenC):
    print("0000000000000000")



# # Q4 -------------------GRAPH PLOT---------------------------------------------------------------
# x_axis = []
# y_axis = []

# i = 0
# while (i < len(programDecimal)):
#     if (i+1) in extra:
#         x_axis.append(i+1)
#         y_axis.append(extra[i+1])
#         x_axis.append(i+1)
#         y_axis.append(programDecimal[i][0])
#         i +=1
#     else:
#         x_axis.append(i+1)
#         y_axis.append(programDecimal[i][0])
#         i +=1


# #-----------------Plotting Part------------------------------------------------------
# import matplotlib.pyplot as plt
# import numpy as np

# plt.scatter(np.array(x_axis),np.array(y_axis),marker="*")

# plt.xlabel("Cycle")
# plt.ylabel("Memory Address in Decimal")
# plt.show()