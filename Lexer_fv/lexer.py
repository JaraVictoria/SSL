"""from automataAceptar import automata_aceptar
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
from automataSino import automata_sino"""

import Automatas.automataAceptar #.automata_Aceptar
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

ESTADO_FINAL = "ESTADO ACEPTADO"
ESTADO_NO_FINAL = "ESTADO NO ACEPTADO"
ESTADO_TRAMPA = "ESTADO TRAMPA"

"""TOKENS_POSIBLES = [
  ("aceptar", automata_aceptar),
  ("cte", automata_constante),
  ("desde", automata_desde),
  ("entonces", automata_entonces),
  ("hasta", automata_hasta),
  ("id", automata_identificador),
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
  ("sino", automata_sino)]"""

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

def lexer(codigo_fuente):
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

#assert lexer("(chau)") == [("(","("), ("ID","chau"), (")",")"), ("EOF", "EOF")]

#assert lexer("+ (") == [("+","+"), ("(", "(")]

"""
assert lexer("hola } 32") == [(['id'],'hola'), (['}'], '}'), (['cte'], '32')]
assert lexer("2 + 2 = 4") == [(['cte'],'2'), (['+'], '+'),(['cte'],'2'), (['='], '='), (['cte'], '4')]
assert lexer("(hola}") == [(['('],'('), (['id'], 'hola'), (['}'], '}')]
assert lexer("para y desde") == [(['para'],'para'), (['id'], 'y'), (['desde'], 'desde')]
assert lexer("2 * 4 = 8") == [(['cte'],'2'), (['*'], '*'), (['cte'], '4'), (['='], '='), (['cte'], '8')]
assert lexer("entonces;hasta cuando") == [(['entonces'],'entonces'), ([';'], ';'), (['hasta'], 'hasta'), (['id'], 'cuando')]
assert lexer("francisss;si}") == [(['id'],'francisss'), ([';'], ';'), (['si'], 'si')]
assert lexer("hola23+") == [(['id'],'hola23'), (['+'], '+')]
assert lexer("{=}") == [(['{'],'{'), (['='], '='), (['}'], '}')]"""

#------------
#capaz hay que hacerlo asi: 
#assert lexer("(chau)") == [("(","("), ("ID","chau"), (")",")"), ("EOF", "EOF")]
#------------