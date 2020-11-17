import ply.lex as lex

reserved = {
    "atom":"ATOM",

    "for":"FOR",
    "if":"IF",

    "and":"AND",
    "not":"NOT",

    "def":"DEF", #definicion de variables
    "defn":"DEFN",


    "nil":"NIL",
    "println":"PRINT",

    "join":"JOIN_STR",
    "split":"SPLIT_STR",
    
    "count":"COUNT_COLL",
    "conj":"CONJ_COLL",

    "find":"FIND_MAP",

    "get":"GET_VEC"
    
}

tokens = [

    "COMMENT",

    "STRING",
    "CHARACTER",

    "DISPATCH",
    "QUOTE",

    "RESET",

    "INCLUDE_STR",

    "INDEXOF_VEC",

] + list(reserved.values())

t_SUMA = r"\+"
t_MULT = r"\*"
t_DIVI = r"\/"

t_IGUAL = r"="
t_MENOR = r"<"
t_MAYOR = r">"

t_STRING = r'\"(.+?)?\"'
t_CHARACTER = r"\\."
t_COMMENT = r";.*"

t_DISPATCH = r"\#"
t_QUOTE = r"'"

t_ignore = ' ,\t\r'

def t_NUMBER(t):
    r'[\+\-]?(\d+(\.\d+)?)'
    t.type = reserved.get(t.value, 'NUMBER')
    return t

def t_RESTA(t):
    r'\-'
    t.type = reserved.get(t.value, 'RESTA')
    return t

def t_KEYWORD(t):
    r'\:[\w\-\.]+'
    t.value = t.value[1:]
    return t

def t_SWAP(t):
    r'swap\!'
    t.type = reserved.get(t.value, 'SWAP')
    return t

def t_RESET(t):
    r'reset\!'
    t.type = reserved.get(t.value, 'RESET')
    return t

def t_INCLUDE_STR(t):
    r'includes\?'
    t.type = reserved.get(t.value, 'INCLUDE_STR')
    return t

def t_INDEXOF_VEC(t):
    r'\.indexOf'
    t.type = reserved.get(t.value, 'INDEXOF_VEC')
    return t


lexer = lex.lex()

#LEER
archivo = open("prueba.txt")
for linea in archivo:
    print(">>"+linea)
    lexer.input(linea)
    while linea!='\n':
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)
