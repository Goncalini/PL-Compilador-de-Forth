import ply.lex as lex

states = (
    ('inloop','inclusive'),
    ('charrec','exclusive'),
)

literals= ['.','"',':',';','!','?','@','(',')']

tokens = (
    'NUMB',
    'STRING',
    'WORD',
    'ADD',
    'SUB',
    'DIV',
    'MUL',
    'MOD',
    'NOT',
    'AND',
    'OR',
    'BIGGERTHEN',
    'SMALLERTHEN',
    'EQUAL',
    'BIGOREQ',
    'SMALOREQ',
    'CHAR',
    'LETTER',
    'IF',
    'THEN',
    'ELSE',
    'BEGIN',
    'UNTIL',
    'WHILE',
    'REPEAT',
    'DO',
    'LOOP',
    'LOOPI',
    'VARIABLE',
    'COMENT',
    'EMIT',
    'CR',
    'SWAP',
    'DUP',
    'DROP',
    'KEY',
    'SPACE',
    'SPACES',
    'ATOI',
    'MAIS_EXCLAMACAO',
)

def t_INITIAL_MAIS_EXCLAMACAO(t):
    r'\+!'
    return t


def t_INITIAL_NUMB(t):
    r'-?\d+'
    return t

def t_INITIAL_ADD(t):
    r'\+'
    return t
def t_INITIAL_SUB(t):
    r'-'
    return t
def t_INITIAL_DIV(t):
    r'\/'
    return t
def t_INITIAL_MUL(t):
    r'\*'
    return t
def t_INITIAL_MOD(t):
    r'\%'
    return t
def t_INITIAL_NOT(t):
    r'\bNOT\b'
    return t
def t_INITIAL_AND(t):
    r'\bAND\b'
    return t
def t_INITIAL_OR(t):
    r'\bOR\b'
    return t
def t_INITIAL_EQUAL(t):
    r'='
    return t
def t_INITIAL_BIGGERTHEN(t):
    r'>'
    return t
def t_INITIAL_SMALLERTHEN(t):
    r'<'
    return t
def t_INITIAL_BIGOREQ(t):
    r'(>=)'
    return t
def t_INITIAL_SMALOREQ(t):
    r'(<=)'
    return t

def t_inloop_LOOPI(t):
    r'\bI\b'
    return t

def t_INITIAL_CHAR(t):
    r'\bCHAR\b'
    t.lexer.begin('charrec')
    return t

def t_INITIAL_VARIABLE(t):
    r'\bVARIABLE\b'
    return t

def t_INITIAL_EMIT(t):
    r'\bEMIT\b'
    return t


#def t_INITIAL_DROP(t):
#    r'\bDROP\b'
#    return t

def t_INITIAL_DROP(t):
    r'\b[\d+]?DROP\b'
    if t.value != "DROP":
        t.value = int(t.value[:-3])
    else :t.value = 1
    return t


def t_INITIAL_SWAP(t):
    r'\bSWAP\b'
    return t


##def t_INITIAL_DUP(t):
##    r'\bDUP\b'
##    return t


def t_INITIAL_DUP(t):
    r'\b[\d+]?DUP\b'
    if t.value != "DUP":
        t.value = int(t.value[:-3])
    else :t.value = 1
    return t

def t_INITIAL_CR(t):
    r'\bCR\b'
    return t

def t_INITIAL_ATOI(t):
    r'\bATOI\b'
    return t

def t_INITIAL_KEY(t):
    r'\bKEY\b'
    return t

def t_INITIAL_SPACES(t):
    r'\bSPACES\b'
    return t

def t_INITIAL_SPACE(t):
    r'\bSPACE\b'
    return t

def t_INITIAL_IF(t):
    r'\bIF\b'
    return t

def t_INITIAL_THEN(t):
    r'\bTHEN\b'
    return t

def t_INITIAL_ELSE(t):
    r'\bELSE\b'
    return t

def t_INITIAL_BEGIN(t):
    r'\bBEGIN\b'
    return t

def t_INITIAL_REPEAT(t):
    r'\bREPEAT\b'
    return t

def t_INITIAL_UNTIL(t):
    r'\bUNTIL\b'
    return t

def t_INITIAL_DO(t):
    r'\bDO\b'
    t.lexer.begin('inloop')
    return t

def t_INITIAL_LOOP(t):
    r'\bLOOP\b'
    t.lexer.begin('INITIAL')
    return t

#def t_inloop_DO(t):
#    r'\bDO\b'
#    t.lexer.begin('inloop')
#    return t
#
#def t_inloop_LOOP(t):
#    r'\bLOOP\b'
#    t.lexer.begin('INITIAL')
#    return t


def t_INITIAL_WHILE(t):
    r'\bWHILE\b'
    return t

def t_charrec_LETTER(t):
    r'.'
    t.value = t.value[0]
    t.lexer.begin('INITIAL')
    return t


def t_INITIAL_WORD(t):
    r'[a-zA-Z_\/\?\\][a-zA-Z_0-9>\/]*(?![\/\\?]|$)'
    return t

def t_INITIAL_COMENT(t):
    r'\(.+\)'
    return t

def t_INITIAL_STRING(t):
    r'\"[^"]*\"'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ANY_ignore = ' \t'

def t_ANY_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    return t



lexer = lex.lex()

"""
def main (args):
    if len(args) < 2:
        return
    with open(args[1], 'r') as file:
        data = file.read()
        lexer = lex.lex() 
        lexer.input(data)
        for tok in lexer:
            print(tok) 

if __name__ == '__main__':
    main(args=sys.argv)
"""