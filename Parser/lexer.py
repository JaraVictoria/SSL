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

  for (token_kind, automata) in TOKENS_POSIBLES:
    result = automata(source)

    if result == ESTADO_FINAL:
      allTrapped = False
      candidates.append(token_kind)
      
    if result == ESTADO_NO_FINAL:
      allTrapped = False

  if len(candidates) == 0:
    return ((allTrapped, []))

  return ((allTrapped, candidates[0]))

# Función "Principal" del LEXER: 
  # Recibe un STRING como INPUT y devuelve una LISTA DE TUPLAS,
  # Cada TUPLA se llama "TOKEN",
    # El primer elemento del TOKEN es el TIPO DE TOKEN, 
    # El segundo elemento del TOKEN es el LEXEME.

# El LEXEME es una palabra que está contenida en el INPUT,
# El TIPO DE TOKEN es la clasificación que le corresponde a esa palabra según la gramática dada.

def lexer(source):
  source += " "
  index = 0
  tokens = []

  while index < len(source):
    if source[index] == " ":
      index += 1
      continue

    candidates = []
    start = index

    while True:
      next = calcCandidates(source[start:index + 1])
      
      if next[0]:
        break

      candidates = next[1]
      
      index += 1

    if len(candidates) == 0:
      candidates = "TOKEN_DESCONOCIDO"
      break

    token_kind = candidates
    lexeme = source[start:index]
    token = ((token_kind, lexeme))

    tokens.append(token)

  # Agrego un último TOKEN que siempre debe estar en la LISTA DE TOKEN: ("EOF", "EOF")
  tokens.append(("EOF", "EOF"))
  # Muestra por CONSOLA, la LISTA DE TOKENS que devuelve cada LLAMADA a la FUNCIÓN "lexer", es decir, cada ASSERT.
  #print(tokens)    
  return tokens

assert lexer("hola } 32") == [('id','hola'), ('}', '}'), ('cte', '32'), ("EOF", "EOF")]
assert lexer("2 + 2 = 4") == [('cte','2'), ('+', '+'),('cte','2'), ('=', '='), ('cte', '4'), ("EOF", "EOF")]
assert lexer("(hola}") == [('(','('), ('id', 'hola'), ('}', '}'), ("EOF", "EOF")]
assert lexer("para; y desde") == [('para','para'), (';',';'), ('id', 'y'), ('desde', 'desde'), ("EOF", "EOF")]
assert lexer("2 * 4 = 8") == [('cte','2'), ('*', '*'), ('cte', '4'), ('=', '='), ('cte', '8'), ("EOF", "EOF")]
assert lexer("entonces;hasta cuando") == [('entonces','entonces'), (';', ';'), ('hasta', 'hasta'), ('id', 'cuando'), ("EOF", "EOF")]
assert lexer("francisss;si") == [('id','francisss'), (';', ';'), ('si', 'si'), ("EOF", "EOF")]
assert lexer("hola23+") == [('id','hola23'), ('+', '+'), ("EOF", "EOF")]
assert lexer("{=}") == [('{','{'), ('=', '='), ('}', '}'), ("EOF", "EOF")]
assert lexer("(chau)") == [("(","("), ("id","chau"), (")",")"), ("EOF", "EOF")]