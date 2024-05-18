import sys
import ply.yacc as yacc
from Yaccer import parser


def finish(parser, codigo):
    if parser.exito:
        with open("output", "w") as f:
            f.write("pushn " + str(parser.global_space_alocated) + "\n") 
            f.write(codigo)
        print("Sintaxe correta!")

def init(file, parser):
    parser.exito = True
    parser.lines = 1
    parser.elseIndex = 0
    parser.thenIndex = 0
    parser.loopIndex = 0
    parser.stack_index_loop = []
    parser.global_scope = {}
    parser.global_space_alocated = 0
    parser.functions = {}
    parser.onfunction = False

    with open(file, "r") as f:
        fonte = f.read()
    codigo = parser.parse(fonte)
    finish(parser, codigo)

if __name__ == "__main__":
    parser = yacc.yacc()
    init(sys.argv[1], parser)