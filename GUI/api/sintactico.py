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
                    | funciones_aritmeticas
                    | map_functions
                    | while_structure
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
    'imprimir : PIZQ PRINT expresion PDER'

#NICOLE GARCIA
def p_secuencia(p):
    '''secuencia : valor 
                    | valor secuencia'''
def p_boolean_operator(p):
    '''boolean_operator : AND
                        | OR
    '''

#Camilo G
def p_expresion_booleana(p):
    'expresion : PIZQ boolean_operator algoritmo algoritmo PDER'

#Camilo G
def p_expresion_booleana_unary(p):
    'expresion : PIZQ NOT algoritmo PDER'


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
    'count_coll : PIZQ COUNT_COLL iterable PDER'

# Doménica Barreiro
def p_conj_coll(p):
    'conj_coll : PIZQ CONJ_COLL iterable secuencia PDER'

# Doménica Barreiro
def p_lista(p):
    '''lista : QUOTE PIZQ secuencia PDER
                | QUOTE PIZQ PDER
    '''

#Camilo G
def p_set(p):
    '''set : DISPATCH LIZQ secuencia LDER
                |   DISPATCH LIZQ LDER
    '''

#Camilo G
def p_map(p):
    '''map : LIZQ pair_key_value LDER
                |   LIZQ LDER
    '''

#Camilo G
def p_pair_key_value(p):
    '''pair_key_value : KEYWORD dato 
                        | KEYWORD dato pair_key_value
    '''

# Doménica Barreiro
def p_iterable(p):
    '''iterable : collection
                | VARIABLE
    '''

#Camilo G
def p_map_functions(p):
    'map_functions : find'

def p_find(p):
    '''find : PIZQ FIND_MAP map KEYWORD PDER
            |  PIZQ FIND_MAP VARIABLE KEYWORD PDER
    ''' 

# Doménica Barreiro
def p_sentenciaFor(p):
    'sentenciaFor : PIZQ FOR CIZQ VARIABLE iterable CDER body PDER'


#Camilo G
def p_funcion(p):
    '''funcion : PIZQ FN parametro expresion PDER
                | PIZQ DEFN VARIABLE parametro expresion PDER
    '''


#Camilo G
def p_parametro(p):
    '''parametro : CIZQ VARIABLE CDER
                    | CIZQ VARIABLE parametro CDER
    '''

#Camilo G
def p_parametro_fn(p):
    'parametro : CIZQ parametro CDER'

#Camilo G
def p_funciones_aritmeticas(p):
    '''funciones_aritmeticas : inc
                            | dec
                            | quot
                            | rem
    '''

def p_inc(p):
    'inc : PIZQ INC numeric_value PDER'

def p_dec(p):
    'dec : PIZQ DEC numeric_value PDER'

def p_quot(p):
    'quot : PIZQ QUOT numeric_value numeric_value PDER'

def p_rem(p):
    'rem : PIZQ REM numeric_value numeric_value PDER'


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
    'get_vec : PIZQ GET_VEC vector_value NUMBER PDER'

#NICOLE GARCIA
#indexOF
def p_indexOf_vec(p):
    'indexOf_vec : PIZQ INDEXOF_VEC vector_value NUMBER PDER'

#NICOLE GARCIA
#subvec/slicing
def p_subvec(p):
    'subvec : PIZQ SUBVEC vector_value index_vec PDER'

#NICOLE GARCIA
def p_index_vec(p):
    '''index_vec :  NUMBER 
                | NUMBER NUMBER
    '''
def p_vector_value(p):
    '''vector_value : vector
                    | VARIABLE
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

#Camilo G
def p_while_structure(p):
    'while_structure : PIZQ WHILE algoritmo body PDER'

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

#Camilo G
def p_reset(p):
    'reset : PIZQ RESET atom_value valor PDER'

def p_swap(p):
    'swap : PIZQ SWAP atom_value funcion PDER'

def p_atom_value(p):
    '''atom_value : VARIABLE
                |   atom
    '''



def p_numeric_value(p):
    '''numeric_value : NUMBER 
                    | VARIABLE
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

result = []
def p_error(p):
    result.append("Error")

parser = yacc.yacc()

def get_production(string):
    result.clear()
    parser.parse(string)
    return result


#LEER ARCHIVOS
def leer_archivo(file):
    archivo = open(file)
    for linea in archivo:
        print(">> "+linea)
        while linea!='\n':
            result = parser.parse(linea)
            if not result:
                break  # No more input
            print(result)
            
#leer_archivo("algoritmo_Barreiro.txt")