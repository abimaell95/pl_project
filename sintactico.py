import ply.yacc as yacc
from lexer import tokens


def p_algoritmo(p):
    '''algoritmo : imprimir
                    | definition
                    | expresion
                    | collection
                    | vector_function
                    | if_structure
                    | string_function
    '''

def p_expresion(p):
    '''expresion : valor
    '''
#NICOLE GARCIA
def p_definition(p):
    'definition : PIZQ DEF VARIABLE valor PDER'

#NICOLE GARCIA
def p_expression_aritmetica(p):
    'expresion : PIZQ operadorMat expresion expresion PDER'

#NICOLE GARCIA
def p_operMat(p):
    '''operadorMat : SUMA
                   | RESTA
                   | MULT
                   | DIVI
    '''

#NICOLE GARCIA    
#impresion por consola
def p_imprimir(p):
    'imprimir : PIZQ PRINT valor PDER'

#NICOLE GARCIA
def p_secuencia(p):
    '''secuencia : valor 
                    | valor secuencia'''

#NICOLE GARCIA
def p_valor(p):
    '''valor : dato
            | VARIABLE
            | atom
    '''

#NICOLE GARCIA
#Funciones de vectores
def p_vector_function(p):
    '''vector_function : get_vec
                        | indexOf_vec
                        | subvec
    ''' 

#NICOLE GARCIA
#get
def p_get_vec(p):
    'get_vec : PIZQ GET_VEC vector NUMBER PDER'

#NICOLE GARCIA
#indexOF
def p_indexOf_vec(p):
    'indexOf_vec : PIZQ INDEXOF_VEC vector NUMBER PDER'

#NICOLE GARCIA
#subvec/slicing
def p_subvec(p):
    'subvec : PIZQ SUBVEC vector index_vec PDER'

#NICOLE GARCIA
def p_index_vec(p):
    '''index_vec :  NUMBER 
                | NUMBER NUMBER
    '''

#NICOLE GARCIA
#vector
def p_vector(p):
    'vector : CIZQ secuencia CDER'

#NICOLE GARCIA
#if
def p_if_structure(p):
    'if_structure : PIZQ IF BOOLEAN body_if PDER'

#NICOLE GARCIA
#funciones de strings
def p_string_function(p):
    '''string_function : include_str
                        | join_str
                        | split_str
    '''

#NICOLE GARCIA
def p_include_str(p):
    'include_str : PIZQ INCLUDE_STR string string PDER'


#NICOLE GARCIA
def p_join_str(p):
    'join_str : PIZQ JOIN_STR string collection PDER'


#NICOLE GARCIA
def p_split_str(p):
    'split_str : PIZQ SPLIT_STR string string PDER'


#NICOLE GARCIA
def p_string(p):
    '''string : STRING
                | VARIABLE
                | ATOM
    '''

#NICOLE GARCIA
def p_body_if(p):
    '''body_if : expresion 
                | expresion expresion
    '''

def p_collection(p):
    ''' collection : vector
    '''

#NICOLE GARCIA
#atomo
def p_atom(p):
    'atom : PIZQ ATOM dato PDER'

#NICOLE GARCIA
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
