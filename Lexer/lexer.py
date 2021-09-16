"""import Automatas.automataAceptar #.automata_Aceptar
import Automatas.automataConstante
import Automatas.automataDesde
import Automatas.automataEntonces #.automata_Entonces
import Automatas.automataHasta
import Automatas.automataIdentificador #.automata_Identificador
import Automatas.automataIgual
import Automatas.automataLlaveAbrir
import Automatas.automataLlaveCerrar
import Automatas.automataMas
import Automatas.automataMostrar #.automata_Mostrar
import Automatas.automataPara
import Automatas.automataParentesisAbrir
import Automatas.automataParentesisCerrar
import Automatas.automataPor
import Automatas.automataPuntoComa
import Automatas.automataSi #.automata_Si
import Automatas.automataSino #.automata_Sino

TOKENS_POSIBLES = [
  ("aceptar", Automatas.automataAceptar.automata_aceptar),
  ("cte", Automatas.automataConstante.automata_constante),
  ("desde", Automatas.automataDesde.automata_desde),
  ("entonces", Automatas.automataEntonces.automata_entonces),
  ("hasta", Automatas.automataHasta.automata_hasta),
  ("id", Automatas.automataIdentificador.automata_identificador),
  ("=", Automatas.automataIgual.automata_igual),
  ("{", Automatas.automataLlaveAbrir.automata_llaveAbrir),
  ("}", Automatas.automataLlaveCerrar.automata_llaveCerrar),
  ("+", Automatas.automataMas.automata_mas),
  ("mostrar", Automatas.automataMostrar.automata_mostrar),
  ("para", Automatas.automataPara.automata_para),
  ("(", Automatas.automataParentesisAbrir.automata_parentesisAbrir),
  (")", Automatas.automataParentesisCerrar.automata_parentesisCerrar),
  ("*", Automatas.automataPor.automata_por),
  (";", Automatas.automataPuntoComa.automata_puntoComa),
  ("si", Automatas.automataSi.automata_si),
  ("sino", Automatas.automataSino.automata_sino)]
  """

"""def lexer(codigo_fuente):
  tokens = []
  posicion_actual = 0
  while posicion_actual < len(codigo_fuente):
    while codigo_fuente[posicion_actual].isspace():
      posicion_actual = posicion_actual + 1

    comienzo_lexema = posicion_actual
    posibles_tokens = []
    posibles_tokens_con_un_caracter_mas = []
    lexema = ""
    var_aux_todos_en_estado_trampa = False

    while not var_aux_todos_en_estado_trampa:
      var_aux_todos_en_estado_trampa = True
      lexema = codigo_fuente[comienzo_lexema:posicion_actual +1]
      posibles_tokens = posibles_tokens_con_un_caracter_mas
      posibles_tokens_con_un_caracter_mas = []

      for (un_tipo_de_token, afd) in TOKENS_POSIBLES:
        simulacion_afd = afd(lexema)
        if simulacion_afd == ESTADO_FINAL:
          posibles_tokens_con_un_caracter_mas.append(un_tipo_de_token)
          var_aux_todos_en_estado_trampa = False
        elif simulacion_afd == ESTADO_NO_FINAL:
          var_aux_todos_en_estado_trampa = False

      posicion_actual = posicion_actual + 1

    if len(posibles_tokens) == 0:
      print("ERROR: TOKEN DESCONOCIDO" + lexema)

    un_tipo_de_token = posibles_tokens[0]

    token = (un_tipo_de_token, lexema)
    tokens.append(token)

  return tokens
"""
from automataAceptar import automata_aceptar
from automataConstante import automata_constante
from automataDesde import automata_desde
from automataEntonces import automata_entonces
from automataHasta import automata_hasta
from automataIdentificador import automata_identificador
from automataIgual import automata_igual
from automataLlaveAbrir import automata_llaveAbrir
from automataLlaveCerrar import automata_llaveCerrar
from automataMas import automata_mas
from automataMostrar import automata_mostrar
from automataPara import automata_para
from automataParentesisAbrir import automata_parentesisAbrir
from automataParentesisCerrar import automata_parentesisCerrar
from automataPor import automata_por
from automataPuntoComa import automata_puntoComa
from automataSi import automata_si
from automataSino import automata_sino

ESTADO_FINAL = "ESTADO ACEPTADO"
ESTADO_NO_FINAL = "ESTADO NO ACEPTADO"
ESTADO_TRAMPA = "ESTADO TRAMPA"

TOKENS_POSIBLES = [
  ("aceptar", automata_aceptar),
  ("cte", automata_constante),
  ("desde", automata_desde),
  ("entonces", automata_entonces),
  ("hasta", automata_hasta),
  ("=", automata_igual),
  ("{", automata_llaveAbrir),
  ("}", automata_llaveCerrar),
  ("+", automata_mas),
  ("mostrar", automata_mostrar),
  ("para", automata_para),
  ("(", automata_parentesisAbrir),
  (")", automata_parentesisCerrar),
  ("*", automata_por),
  (";", automata_puntoComa),
  ("si", automata_si),
  ("sino", automata_sino),
  ("id", automata_identificador)]

def calcCandidates(source):
  allTrapped = True
  candidates = []
  #print("**********************************************************************")
  for (token_kind, automata) in TOKENS_POSIBLES:
    result = automata(source)
    #print("********************************************************************")
    #print("ALLTRAPPED: ", allTrapped)
    #print("TOKEN_KIND: ", token_kind)
    #print("AUTOMATA: ", automata)
    #print("RESULT: ", result)


    if result == ESTADO_FINAL:
      allTrapped = False
      candidates.append(token_kind)
      #print("CANDIDATES: ", candidates)
    if result == ESTADO_NO_FINAL:
      allTrapped = False


  if len(candidates) == 0:
    return ((allTrapped, []))

  #print("SOURCE: ", source)
  #print("token_kind: ", candidates[0])
  #print("**********************************************************************")
  return ((allTrapped, candidates[0]))

# FUNCION "PRINCIPAL" DEL LEXER:
# RECIBE UN STRING COMO INPUT Y DEVUELVE UNA LISTA DE TUPLAS,
# CADA TUPLA SE LLAMA "TOKEN",
# EL PRIMER ELEMENTO DEL TOKEN ES EL TIPO DE TOKEN,
# EL SEGUNDO ELEMENTO ES EL LEXEME.

# EL LEXEME ES UNA PALABRA QUE ESTA CONTENIDA EN EL INPUT,
# EL TIPO DE TOKEN ES LA CLASIFICACION QUE LE CORRESPONDE A ESA PALABRA SEGUN LA GRAMATICA DADA.

def lexer(source):
  source +=" "
  index = 0
  tokens = []

  while index < len(source):
    if source[index] == " ":
      index += 1
      continue

    #print("INDEX COMIENZA EN: ", index)
    candidates = []
    start = index

    while True:
      next = calcCandidates(source[start:index + 1])
      #print("CANDIDATOS: ", next[1])
      if next[0]:
        break

      candidates = next[1]
      #print("CANDIDATOS: ", candidates)
      index += 1

    if len(candidates) == 0:
      candidates = "TOKEN_DESCONOCIDO"

    token_kind = candidates
    lexeme = source[start:index]
    token = ((token_kind, lexeme))

    tokens.append(token)
  # AGREGO UN ULTIMO TOKEN QUE SIEMPRE DEBE ESTAR EN LA LISTA DE TOKEN: ("EOF", "EOF")
  tokens.append(("EOF", "EOF"))
  #print("SOURCE: ", source)
  #print(tokens)    #( DESCOMENTAR PARA MOSTRAR POR CONSOLA LA LISTA DE TOKENS QUE
  #                  DEVUELVE CADA LLAMADA A LA FUNCION lexer )
  return tokens

assert lexer("hola } 32") == [('id','hola'), ('}', '}'), ('cte', '32'), ('EOF','EOF')]
assert lexer("2 + 2 = 4") == [('cte','2'), ('+', '+'),('cte','2'), ('=', '='), ('cte', '4'), ('EOF', 'EOF')]
assert lexer("(hola}") == [('(','('), ('id', 'hola'), ('}', '}'), ('EOF','EOF')]
assert lexer("para; y desde") == [('para','para'), (';',';'), ('id', 'y'), ('desde', 'desde'), ('EOF', 'EOF')]
assert lexer("2 * 4 = 8") == [('cte','2'), ('*', '*'), ('cte', '4'), ('=', '='), ('cte', '8'), ('EOF','EOF')]
assert lexer("entonces;hasta cuando") == [('entonces','entonces'), (';', ';'), ('hasta', 'hasta'), ('id', 'cuando'), ('EOF','EOF')]
assert lexer("francisss;si") == [('id','francisss'), (';', ';'), ('si', 'si'), ('EOF','EOF')]
assert lexer("hola23+") == [('id','hola23'), ('+', '+'), ('EOF','EOF')]
assert lexer("{=}") == [('{','{'), ('=', '='), ('}', '}'), ('EOF','EOF')]
assert lexer("(chau)") == [("(","("), ("id","chau"), (")",")"), ("EOF", "EOF")]