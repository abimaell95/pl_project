import ply.yacc as yacc
from lexer import tokens


def p_algoritmo(p):
    '''algoritmo : imprimir
                    | definition
                    | COMMENT
                    | expresion
                    | vector_function
                    | if_structure
                    | string_function
                    | comparacion
                    | leerDatos
                    | sentenciaFor
                    | funciones_collection
                    | funcion
                    | variable_manipulation
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
def p_collection(p):
    '''collection : lista
                    | vector
                    | set
                    | map
    '''

# Doménica Barreiro
def p_funciones_collection(p):
    '''funciones_collection : count_coll
                          | conj_coll
    '''

# Doménica Barreiro
def p_count_coll(p):
    'count_coll : PIZQ COUNT_COLL collection PDER'

# Doménica Barreiro
def p_conj_coll(p):
    'conj_coll : PIZQ CONJ_COLL collection secuencia PDER'

# Doménica Barreiro
def p_lista(p):
    '''lista : QUOTE PIZQ secuencia PDER
                | QUOTE PIZQ PDER
    '''

def p_set(p):
    '''set : DISPATCH LIZQ secuencia LDER
                |   DISPATCH LIZQ LDER
    '''

def p_map(p):
    '''map : LIZQ pair_key_value LDER
                |   LIZQ LDER
    '''

def p_pair_key_value(p):
    '''pair_key_value : KEYWORD dato 
                        | KEYWORD dato pair_key_value
    '''

# Doméncia Barreiro
def p_iterable(p):
    '''iterable : collection
                | VARIABLE
    '''

# Doménica Barreiro
def p_sentenciaFor(p):
    'sentenciaFor : PIZQ FOR CIZQ VARIABLE iterable CDER body PDER'


def p_funcion(p):
    '''funcion : PIZQ FN parametro expresion PDER
                | PIZQ DEFN VARIABLE parametro expresion PDER
    '''

def p_parametro(p):
    '''parametro : CIZQ VARIABLE CDER
                    | CIZQ VARIABLE parametro CDER
    '''




def p_valor(p):
    '''valor : dato
            | VARIABLE
            | atom
            | collection
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
    '''vector : CIZQ secuencia CDER
                | CIZQ CDER
    '''

#NICOLE GARCIA
#if
def p_if_structure(p):
    'if_structure : PIZQ IF algoritmo body PDER'

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
def p_body(p):
    '''body : algoritmo 
                | algoritmo algoritmo
    '''


#NICOLE GARCIA
#atomo
def p_atom(p):
    'atom : PIZQ ATOM dato PDER'

#NICOLE GARCIA
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
