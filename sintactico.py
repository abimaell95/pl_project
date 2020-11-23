import ply.yacc as yacc
from lexer import tokens


def p_algoritmo(p):
    '''algoritmo : imprimir
                    | definition
                    | expresion
    '''

def p_expresion(p):
    '''expresion : valor
    '''

def p_definition(p):
    'definition : DEF VARIABLE valor'


def p_expression_aritmetica(p):
    'expresion : PIZQ operadorMat expresion expresion PDER'

def p_operMat(p):
    '''operadorMat : SUMA
                   | RESTA
                   | MULT
                   | DIVI
    '''
def p_imprimir(p):
    'imprimir : PRINT valor'

def p_valor(p):
    '''valor : NUMBER
            | VARIABLE
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
