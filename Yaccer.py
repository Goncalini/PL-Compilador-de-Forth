import ply.yacc as yacc
import sys
import os
from Lexer import tokens


def p_line1(p):
    "Line : Line Elem"

    p[0] = p[1] + p[2]
    #return p[0]
    return p

#def p_line2(p):
#    "Line : Line Function"
#
#
#    parser.funclist[parser.nf].append(p[2])
#    parser.funclist.append([])
#    parser.nf += 1
#
#    #p[0] = p[1] + p[2]

def p_line3(p):
    "Line : "

    p[0] = ""
    #return p[0]
    return p

def p_exec1(p):
    "Exec : Exec Elem"
    #print(p[1])
    #print(p[2])
    p[0] = p[1] + p[2]
    #return p[0]
    return p

def p_exec2(p):
    "Exec : Elem"

    p[0] = p[1]
    return p

def p_elem1(p):
    "Elem : NUMB"

    p[0] = "pushi" + " " + p[1] + "\n"
    return p

def p_elem2(p):	
    "Elem : Operador"

    p[0] = p[1]
    return p

def p_elem3(p):
    "Elem : '.' "

    p[0] = "writei" + "\n"
    return p

def p_elem4(p):
    "Elem : '.' STRING "
    
    p[0] = "pushs" + " " + p[2] + "\n" + "writes" + "\n"
    return p

def p_elem5(p):
    "Elem : CHAR LETTER"

    p[0] = f"pushs \"{p[2]}\"\nchrcode\n"
    return p
    
def p_elem8(p):
    "Elem : Loop"

    p[0] = p[1]
    return p

#def p_elem9(p):
#    "Elem : LOOPI"
#
#    loopiactual = parser.looporder[-1]
#    p[0] = f"pushg {parser.varpointer[f'LOOP{loopiactual - 1}'][0]}" + "\n"
#    return p
#
#def p_elem11(p):
#    "Elem : VARIABLE WORD"
#
#    if p[2] in parser.varpointer:
#        parser.success = False
#        print(f"Variable already exists in line {p.lineno}")
#    else:
#        parser.varpointer[p[2]] = parser.pushncount
#        parser.pushncount = parser.pushncount + 1
#
#    p[0] = ""
#    return p

#def p_elem12(p):
#    "Elem : WORD '!' "
#
#    if p[1] not in parser.varpointer:
#        print(f"Variable non existence in line in line {p.lineno}")
#        parser.success = False
#    
#    p[0] = p[0] = f"storeg {parser.varpointer[p[1]]}" + "\n"
#    return p
#
#def p_elem13(p):
#    "Elem : WORD '?' "
#
#    if p[1] not in parser.varpointer:
#        print(f"Variable non existence in line {p.lineno}")
#
#        parser.success = False
#
#    aux = f"pushg {parser.varpointer[p[1]][0]}"
#    aux2 = f"writei"
#    
#    p[0] = aux + "\n" + aux2 + "\n"
#    return p
#
#def p_elem14(p):
#    "Elem : WORD '@' "
#
#    if p[1] not in parser.varpointer:
#        print(f"Variable non existence in line {p.lineno}")
#        parser.success = False
#
#    p[0] = f"pushg {parser.varpointer[p[1]]}" + "\n"
#    return p
#

def p_elem10(p):
    "Elem : Var"

    p[0] = p[1]
    return p

def p_elem15(p):
    "Elem : COMENT"

    p[0] = ""
    return p

def p_elem16(p):
    "Elem : EMIT"

    p[0] = "writechr" + "\n"
    return p

def p_elem17(p):
    "Elem : CR"

    p[0] = "writeln" + "\n"
    return p

def p_elem19(p):
    "Elem : SWAP"

    p[0] = "swap" + "\n"
    return p

def p_elem20(p):
    "Elem : DUP"

    p[0] = f"dup {p[1]}" + "\n"
    return p

def p_elem21(p):
    "Elem : DROP"

    p[0] = f"pop {p[1]}" + "\n"
    return p

def p_elem22(p):
    "Elem : KEY"

    p[0] = "read" + "\n" + "chrcode" + "\n"
    return p

def p_elem23(p):
    "Elem : SPACE"

    p[0] = "pushs \" \"" + "\nwrites" + "\n"
    return p

def p_elem24(p):
    "Elem : Function"

    p[0] = p[1]
    return p

def p_elem25(p):
    "Elem : Word"

    p[0] = p[1]
    return p

def p_operador1(p):
    "Operador : ADD"

    p[0] = "add" + "\n"
    return p

def p_operador2(p):
    "Operador : SUB"

    p[0] = "sub" + "\n"
    return p

def p_operador3(p):
    "Operador : DIV"

    p[0] = "div" + "\n" + "ftoi" + "\n"
    return p

def p_operador4(p):
    "Operador : MUL"

    p[0] = "mul" + "\n"
    return p

def p_operador5(p):
    "Operador : MOD"

    p[0] = "mod" + "\n"
    return p

def p_operador6(p):
    "Operador : NOT"

    p[0] = "not" + "\n"
    return p

def p_operador7(p):
    "Operador : AND"

    p[0] = "and" + "\n"
    return p

def p_operador8(p):
    "Operador : OR"

    p[0] = "or" + "\n"
    return p

def p_operador9(p):
    "Operador : EQUAL"

    p[0] = "equal" + "\n"
    return p

def p_operador10(p):
    "Operador : BIGGERTHEN"

    p[0] = "sup" + "\n"
    return p

def p_operador11(p):
    "Operador : SMALLERTHEN"

    p[0] = "inf" + "\n"
    return p

def p_operador12(p):
    "Operador : BIGOREQ"

    p[0] = "supeq" + "\n"
    return p

def p_operador13(p):
    "Operador : SMALOREQ"

    p[0] = "infeq" + "\n"
    return p
#-------------------Variáveis-------------------
def p_var1(p):
    "Var : VARIABLE WORD"

    if p[2] in parser.varpointer:
        parser.success = False
        print(f"Variable already exists in line {p.lineno}")
    else:
        parser.varpointer[p[2]] = parser.pushncount
        parser.pushncount = parser.pushncount + 1

    p[0] = ""
    return p


def p_var2(p):
    "Var : LOOPI"

    #loopiactual = parser.looporder[-1]
    #p[0] = f"pushg {parser.varpointer[f'LOOP{loopiactual - 1}'][0]}" + "\n"
    p[0] = f"pushg {parser.varpointer[f'LOOP{parser.loopcount - 1}'][0]}\n"
    return p

def p_var3(p):
    "Var : WORD '!' "

    if p[1] not in parser.varpointer:
        print(f"Variable non existence in line in line {p.lineno}")
        parser.success = False
    
    p[0] = p[0] = f"storeg {parser.varpointer[p[1]]}" + "\n"
    return p

def p_var4(p):
    "Var : WORD '?' "

    if p[1] not in parser.varpointer:
        print(f"Variable non existence in line {p.lineno}")

        parser.success = False

    aux = f"pushg {parser.varpointer[p[1]]}"
    aux2 = f"writei"
    
    p[0] = aux + "\n" + aux2 + "\n"
    return p

def p_Var14(p):
    "Var : WORD '@' "

    if p[1] not in parser.varpointer:
        print(f"Variable non existence in line {p.lineno}")
        parser.success = False

    p[0] = f"pushg {parser.varpointer[p[1]]}" + "\n"
    return p

def p_var5(p):
    "Var : WORD MAIS_EXCLAMACAO"

    if p[1] not in parser.varpointer:
        print(f"Variable non existence in line {p.lineno}")
        parser.success = False
    aux1 = f"pushg {parser.varpointer[p[1]]}"
    aux2 = "add"
    aux3 = f"storeg {parser.varpointer[p[1]]}"

    p[0] = aux1 + "\n" + aux2 + "\n" + aux3 + "\n"
    return p

#-------------------Condicionais-------------------
def p_elem6(p):
    "Elem : IF Exec THEN"
    
    p[0] = f"jz endif{parser.thencount}" + "\n" + p[2] + f"endif{parser.thencount}:" + "\n"
    
    parser.thencount += 1

    return p


def p_elem7(p):
    "Elem : IF Exec ELSE Exec THEN"

    p[0] = f"jz else{parser.elsecount}" + "\n" + p[2] + f"jump endif{parser.thencount}"+"\n" + f"else{parser.elsecount}:" + "\n" + p[4] + f"endif{parser.thencount}:" + "\n"
    
    parser.thencount += 1
    parser.elsecount += 1
    
    return p


#def p_if1(p):
#    "If : IF"
#
#
#def p_else1(p):
#    "Else : ELSE"
#
#def p_then1(p):
#    "Then : THEN"
#-----------------------Loops----------------------------
def p_loop1(p):
    "Loop : Begin Exec UNTIL"

    loopiactual = parser.looporder.pop()
    aux1 = f"jz loop{loopiactual}"
    aux2 = f"jump endloop{loopiactual}"
    aux3 = f"endloop{loopiactual}:"

    p[0] = p[1] + p[2] + aux1 + "\n" + aux2 + "\n" + aux3 + "\n"
    return p

def p_loop2(p):
    "Loop : Begin Exec WHILE Exec REPEAT"


    loopiactual = parser.looporder.pop()
    aux = f"jz endloop{loopiactual}"
    aux2 = f"jump loop{loopiactual}"
    aux3 = f"endloop{loopiactual}:"

    p[0] = p[1] + p[2] + aux + "\n" + p[4] + aux2 + "\n" + aux3 + "\n"
    return p

def p_loop4(p):
    "Loop : Do Exec LOOP"


    loopiactual = parser.looporder.pop()

    aux1 = f"pushg {parser.varpointer[f'LOOP{loopiactual}'][0]}"
    aux2 = "pushi 1"
    aux3 = "add"
    aux4 = f"storeg {parser.varpointer[f'LOOP{loopiactual}'][0]}"
    aux5 = f"jump loop{loopiactual}"
    aux6 = f"endloop{loopiactual}:"

    p[0] = p[1] + p[2] + aux1 + "\n" + aux2 + "\n" + aux3 + "\n" + aux4 + "\n" + aux5 + "\n" + aux6 + "\n"
    return p

def p_begin1(p):
    "Begin : BEGIN"

    loopiactual = parser.loopcount
    parser.loopcount += 1
    parser.looporder.append(loopiactual)
    aux1 = f"jump loop{loopiactual}"
    aux2 = f"loop{loopiactual}:"

    p[0] = aux1 + "\n" + aux2 + "\n"
    return p

def p_do1(p):
    "Do : DO"

    
    parser.varpointer[f"LOOP{parser.loopcount}"] = (parser.pushncount, parser.pushncount + 1)
    parser.pushncount += 2
    loopiactual = parser.loopcount
    parser.loopcount += 1
    parser.looporder.append(loopiactual)
    aux1 = f"storeg {parser.varpointer[f'LOOP{loopiactual}'][0]}"
    aux2 = f"storeg {parser.varpointer[f'LOOP{loopiactual}'][1]}"
    aux3 = f"jump loop{loopiactual}"
    aux4 = f"loop{loopiactual}:"
    aux5 = f"pushg {parser.varpointer[f'LOOP{loopiactual}'][0]}"
    aux6 = f"pushg {parser.varpointer[f'LOOP{loopiactual}'][1]}"
    aux7 = "sub"
    aux8 = f"jz endloop{loopiactual}"

    p[0] = aux1 + "\n" + aux2 + "\n" + aux3 + "\n" + aux4 + "\n" + aux5 + "\n" + aux6 + "\n" + aux7 + "\n" + aux8 + "\n"
    return p

#def p_loop3(p):
#    "Loop : Do Exec Loopfinal"
#
#def p_stop1(p):
#    "Stop : While Exec Repeat"
#
#def p_stop2(p):
#    "Stop : UNTIL"
    
#def p_until1(p):
#    "Until : UNTIL"

#def p_while1(p):
#    "While : WHILE"
#
#def p_repeat1(p):
#    "Repeat : REPEAT"

#def p_loopfinal1(p):
#    "Loopfinal : LOOP"

#--------------------Funções-----------------------------------
def p_function1(p):
    "Function : Dots WORD Exec ';'"
    
    p[0] = ""
    #print(parser.funcflag)
    if not parser.funcflag:
        print(f"Syntaxe not permited {p.lineno}")
        exit(0)
    else:
        #print("entrou")
        if p[2] in parser.dicfunc:
            print(f"Function already existes in line {p.lineno}")
            parser.success = False
        else:
            #print(p[2])
            parser.dicfunc[p[2]] = p[3]
            #print(parser.dicfunc)
            parser.funcflag = False
    return p

def p_Dots1(p):
    "Dots : ':' "
    parser.funcflag = True
    p[0] = ""
    return p

def p_word1(p):
    "Word : WORD"
    #print(p[1])
    #print(parser.varpointer)
    #print(parser.dicfunc)
    if p[1] in parser.dicfunc:
        p[0] = parser.dicfunc[p[1]]
    else:
        print(f"Function non existence in line {p.lineno}")
        parser.success = False
    return p

def p_word2(p):
    "Word : SPACES"
    
    loopiactual = parser.loopcount
    parser.varpointer[f"LOOP{loopiactual}"] = (parser.pushncount, parser.pushncount + 1)
    parser.pushncount += 2
    parser.loopcount += 1
    aux1 = f"pushi 0"
    aux2 = f"storeg {parser.varpointer[f'LOOP{loopiactual}'][0]}"
    aux3 = f"storeg {parser.varpointer[f'LOOP{loopiactual}'][1]}"
    aux4 = f"jump loop{loopiactual}"
    aux5 = f"loop{loopiactual}:"
    aux6 = f"pushg {parser.varpointer[f'LOOP{loopiactual}'][0]}"
    aux7 = f"pushg {parser.varpointer[f'LOOP{loopiactual}'][1]}"
    aux8 = "sub"
    aux9 = f"jz endloop{loopiactual}"
    aux10 = f"pushs " ""
    aux11 = "writes"
    aux12 = f"pushi 1"
    aux13 = f"pushg {parser.varpointer[f'LOOP{loopiactual}'][0]}"
    aux14 = "add"
    aux15 = f"storeg {parser.varpointer[f'LOOP{loopiactual}'][0]}"
    aux16 = f"jump loop{loopiactual}"
    aux17 = f"endloop{loopiactual}:"

    p[0] = aux1 + "\n" + aux2 + "\n" + aux3 + "\n" + aux4 + "\n" + aux5 + "\n" + aux6 + "\n" + aux7 + "\n" + aux8 + "\n" + aux9 + "\n" + aux10 + "\n" + aux11 + "\n" + aux12 + "\n" + aux13 + "\n" + aux14 + "\n" + aux15 + "\n" + aux16 + "\n" + aux17 + "\n"
    return p

#def p_function1(p):
#    "Function : Dots Funcname"
#
#    parser.dicfunc[p[1]] = p[2]
#
#def p_dots1(p):
#    "Dots : ':' WORD"
#
#    parser.dicfunc[p[2]] = 0
#    parser.funcorder.append(p[2])
#    p[0] = p[2]
#
#def p_funcname1(p):
#    "Funcname : Exec ';'"
#
#def p_elem18(p):
#    "Elem : ATOI"
#
#    p[0] = "atoi" + "\n"
#    return p

def p_error(p):
    print(f"Syntax error in input in line {p.lineno}",p)
    parser.success=False


#parser = yacc.yacc()
#parser.success = True
#parser.dicfunc = {}
"""
def parsing(parser, input):
    if parser.success:
        i = 1
        name = ""
        with open("output", "w") as f:
            f.write("pushn " + str(parser.pushncount) + "\n")
            f.write("start\n")
            f.write(input)
            f.write("stop\n")
            while i < len(parser.funcorder):
            #pôr a parte inicial e os loads de argumentos
                name = parser.funcorder[i-1]
                f.write(f"{name}:\n")
                numbloads = parser.dicfunc[name]
                while numbloads > 0:
                    f.write(f"\tpushfp\n\tload -{numbloads}\n")
                    numbloads -= 1
                #pôr as instruções
                for elem in parser.list[i-1]:
                    f.write(f"\t{elem}\n")
                #guardar na memoria e return
                f.write(f"\tstoreg{list(parser.funtionANDVarNames.keys()).index(name)}\n")
                f.write("\treturn\n")
                i+=1
        print("Parsing was successfull!")

"""
def parsing(parser, input):
    if parser.success:
        with open("output", "w") as f:
            f.write("pushn " + str(parser.pushncount) + "\n")
            f.write(input)
        print("Parsing was successfull!")

def constutor(file, parser):
    parser.success = True
    parser.elsecount = 0
    parser.thencount = 0
    parser.loopcount = 0
    parser.varpointer = {}
    parser.pushncount = 0
    parser.looporder = []
    parser.dicfunc = {}
    parser.funcorder = []
    parser.funclist = [[]]
    parser.funcflag = False
    parser.nf = 0

    with open(file, "r") as f:
        fonte = f.read()
    input = parser.parse(fonte)
    parsing(parser, input)

if __name__ == "__main__":
    parser = yacc.yacc()
    constutor(sys.argv[1], parser)
