import ply.lex as lex

reserved = {
    "atom":"ATOM",

    "for":"FOR",
    "if":"IF",
    "while":"WHILE",

    "and":"AND",
    "or":"OR",
    "not":"NOT",

    "def":"DEF", #definicion de variables
    "fn":"FN", #definicion de funciones anonimas
    "defn":"DEFN",
    
    "inc":"INC", 
    "dec":"DEC",
    "quot":"QUOT",
    "rem":"REM",

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
    "SUMA",
    "RESTA",
    "MULT",
    "DIVI",

    "COMMENT",
    
    "NUMBER",
    "STRING",
    "KEYWORD",
    "CHARACTER",
    
    "PIZQ",
    "PDER",
    "LIZQ",
    "LDER",
    "CIZQ",
    "CDER",
    
    "IGUAL",
    "MENOR",
    "MAYOR",

    "DISPATCH",
    "QUOTE",

    "SWAP",
    "RESET",

    "INCLUDE_STR",

    "INDEXOF_VEC",
    
    "VARIABLE"

] + list(reserved.values())

t_SUMA = r"\+"
t_MULT = r"\*"
t_DIVI = r"\/"

t_IGUAL = r"="
t_MENOR = r"<"
t_MAYOR = r">"

t_LIZQ = r"\{"
t_LDER = r"\}"
t_CIZQ = r"\["
t_CDER = r"\]"
t_PIZQ = r"\("
t_PDER = r"\)"

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

def t_VARIABLE(t):
    r'[a-zA-Z\-\._]+[\w\-\.]*'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("No es reconocido '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

#LEER ARCHIVOS
def leer_archivo(file):
    archivo = open(file)
    for linea in archivo:
        print(">>"+linea)
        lexer.input(linea)
        while linea!='\n':
            tok = lexer.token()
            if not tok:
                break  # No more input
            print(tok)
leer_archivo("pruebas_camilo.txt")
leer_archivo("ejemplos_Barreiro.txt")
leer_archivo("ejemplos_Garcia.txt")
