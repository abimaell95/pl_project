import ply.lex as lex

reserved = {
    "atom":"ATOM",

    "for":"FOR",

    "not":"NOT",

    "def":"DEF", #definicion de variables


    "nil":"NIL",
    "println":"PRINT",

    "join":"JOIN_STR",
    "split":"SPLIT_STR"
    
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



t_STRING = r'\"(.+?)?\"'
t_CHARACTER = r"\\."
t_COMMENT = r";.*"

t_DISPATCH = r"\#"
t_QUOTE = r"'"

t_ignore = ' ,\t\r'


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
