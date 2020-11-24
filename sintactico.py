import ply.yacc as yacc
from lexer import tokens


def p_algoritmo(p):
    '''algoritmo : imprimir
                    | definition
                    | expresion
                    | collection
                    | comparacion
                    | count_coll
                    | conj_coll
                    | leerDatos
                    | sentenciaFor
                    | funcion
                    | variable_manipulation
    '''

def p_expresion(p):
    '''expresion : valor
    '''

def p_definition(p):
    'definition : PIZQ DEF VARIABLE valor PDER'

def p_imprimir(p):
    'imprimir : PIZQ PRINT valor PDER'

def p_expresion_aritmetica(p):
    'expresion : PIZQ operadorMat expresion expresion PDER'

def p_operMat(p):
    '''operadorMat : SUMA
                   | RESTA
                   | MULT
                   | DIVI
    '''
# Doménica Barreiro
def p_leerDatos(p):
    '''leerDatos : PIZQ DEF VARIABLE PIZQ READ_LINE PDER PDER
                | PIZQ READ_LINE PDER
    '''

# Doménica Barreiro
def p_comparacion(p):
    'comparacion : PIZQ operadorComp expresion expresion PDER'

# Doménica Barreiro
def p_operComp(p):
    '''operadorComp : IGUAL
                   | MENOR
                   | MAYOR
                   | MENOR_IGUAL
                   | MAYOR_IGUAL
    '''
# Doménica Barreiro
def p_count_coll(p):
    'count_coll : PIZQ COUNT_COLL collection PDER'

# Doménica Barreiro
def p_conj_coll(p):
    'conj_coll : PIZQ CONJ_COLL collection secuencia PDER'

# Doménica Barreiro
def p_collection_lista(p):
    '''collection : QUOTE PIZQ secuencia PDER
                | QUOTE PIZQ PDER
    '''

# Doménica Barreiro
def p_sentenciaFor(p):
    'sentenciaFor : PIZQ FOR CIZQ VARIABLE collection CDER algoritmo PDER'

def p_secuencia(p):
    '''secuencia : valor 
                | valor secuencia'''


def p_funcion(p):
    '''funcion : PIZQ FN parametro expresion PDER
                | PIZQ DEFN VARIABLE parametro expresion PDER
    '''

def p_parametro(p):
    '''parametro : VARIABLE 
                    | VARIABLE parametro
    '''

def p_parametro_fn(p):
    'parametro : CIZQ parametro CDER'






def p_valor(p):
    '''valor : dato
            | VARIABLE
            | atom
    '''

def p_variable_manipulation(p):
    '''variable_manipulation :  swap
                            |  reset
    '''

def p_reset(p):
    'reset : PIZQ RESET atom_value valor PDER'

def p_swap(p):
    'swap : PIZQ SWAP atom_value funcion PDER'

def p_atom_value(p):
    '''atom_value : VARIABLE
                |   atom
    '''



def p_atom(p):
    'atom : PIZQ ATOM dato PDER'

def p_dato(p):
    '''dato : NUMBER
                | STRING
                | BOOLEAN
                | KEYWORD
                | CHARACTER
                | NIL
    '''

#Errores lexicos
def p_error(p):
    print("Syntax error in input")

parser = yacc.yacc()

while True:
    try:
        s=input("calc >> ")
    except EOFError:
        break
    if not s : continue
    result = parser.parse(s)
    print(result)
