import ply.yacc as yacc
from lexer import tokens


def p_algoritmo(p):
    '''algoritmo : imprimir
                    | definition
                    | expresion
                    | collection
    '''

def p_expresion(p):
    '''expresion : valor
    '''

def p_definition(p):
    'definition : PIZQ DEF VARIABLE valor PDER'


def p_expression_aritmetica(p):
    'expresion : PIZQ operadorMat expresion expresion PDER'

def p_operMat(p):
    '''operadorMat : SUMA
                   | RESTA
                   | MULT
                   | DIVI
    '''
def p_imprimir(p):
    'imprimir : PIZQ PRINT valor PDER'

def p_collection(p):
    'collection : PIZQ secuencia PDER'

def p_secuencia(p):
    '''secuencia : valor 
                    | valor secuencia'''
def p_valor(p):
    '''valor : dato
            | VARIABLE
            | atom
    '''

def p_atom(p):
    'atom : PIZQ ATOM dato PDER'


def p_dato(p):
    '''dato : NUMBER
                | STRING
                | BOOLEAN
                | KEYWORD
                | CHARACTER
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
