#Es una especie de pseudocódigo, no se puede correr tal cual está.

import lexer

no_terminales = ['Programa', 'Asignacion', 'Estructura', 'Expresion', 'Valor', 'ListaExpresiones', 'Termino', 'Factor'] #no está completo, hay que agregar algo más (no se el que, lo dijo en el 10:30 aprox). Guardar, en una variable, todos los no terminales de la gramática
terminales =  lexer.TOKENS_POSIBLES
#['aceptar', 'cte', 'desde', 'entonces', 'hasta', '=', '{', '}', '+', 'mostrar', 'para', '(', ')', '*', ';', 'si', 'sino', 'id'] #no es la salida del lexer, sino los que determinamos

producciones = { #estructura de diccionarios: llaves/claves y valores asignados a esa llave/clave. Hay que poner las producciones de los no terminales
	'Programa': [
				['Asignacion'], #se agregó para reemplazar al "lambda". 49:40
				['Asignacion', 'Programa'], 
				['Estructura'], #se agregó para reemplazar al "lambda". 49:40
				['Estructura', 'Programa']
				#[] Para este algoritmo, la gramática no tiene que tener recursividad izquierda ni símbolos anulables, por lo que "lambda" se arregla con las líneas de código 11 y 13
	], #producciones['Programa'][1] --> ['Estructura', 'Programa']
	
	'Asignacion': [
				  ['id', '=', 'Expresion']
	],
	
	'Estructura': [
				  ['para', 'id', 'desde', 'Valor', 'hasta', 'Valor', '{', 'Programa', '}'], 
				  ['si', 'Expresion', 'entonces', '{', 'Programa', '}', 'sino', '{', 'Programa', '}'], 
				  ['si', 'Expresion', 'entonces', '{', 'Programa', '}'], 
				  ['mostrar', 'ListaExpresiones'], 
				  ['aceptar', 'id']
	],

	'Valor': [
			 ['id'],
			 ['cte']
	],	
	
#	'Expresion': [
#				 ['Expresion', '+', 'Termino'], #ARREGLAR RECURSIVIDAD IZQUIERDA. 1:24:00 // 1:57:00
#				 ['Termino']
#	],

	'Expresion': [
				 ['Termino', 'Expresion*'], #'Expresion*' es necesario para eliminar la recursividad izquierda. 
	],

	'Expresion*': [
				  ['+', 'Termino'] #Con esta produccion se reemplaza el "lambda".
				  ['+', 'Termino', 'Expresion*']
				  #[]
	],

#	'Termino': [
#			   ['Termino', '*', 'Factor'], #ARREGLAR RECURSIVIDAD IZQUIERDA. 1:24:00 // 1:57:00
#			   ['Factor'] 
#	],

	'Termino': [
			   ['Factor', 'Termino*'], #'Termino*' es necesario para eliminar la recursividad izquierda. 
	],

	'Termino*': [
				['*', 'Factor'], #Con esta produccion se reemplaza el "lambda".
				['*', 'Factor', 'Termino*']
				#[]
	],

	'Factor': [
			  ['(', 'Expresion', ')'],
			  ['id'],
			  ['cte']
	],

	'ListaExpresiones': [
			  ['Expresion', ';', 'ListaExpresiones'],
			  ['Expresion']
	]
}

def parser(lista_tokens): #lista_tokens es la salida del lexer, lista_tokens = lexer(codigo_fuente). Es la "w".
	datos_parser = {
		'tokens': lexer.lexer(lista_tokens),
		'posicion_indice': 0, #es la "t", seria en que posicion de la cadena de entrada estoy apuntando, es decir, una posicion dentro de nuestra lista_tokens
		'error': False, #variable que controla el funcionamiento del parser, se pone en "false", asumiendo que no hay ningun error en el procesamiento. Si llega a haber un error, es decir que es "true", la cadena no pertenece
	}

	def principal():
		pni('Programa') #pni hace referencia al simbolo distinguido de la gramatica con la posicion
		token_actual = datos_parser['tokens'][datos_parser['posicion_indice']][0]
		if token_actual != 'EOF' or datos_parser['error']:
			print('La cadena no pertenece al lenguaje')
			return False

		return True

	def pni(no_terminal):
		for parteDerecha in producciones[no_terminal]: #parteDerecha es una variable que se refiere a c/u de las "listitas" de las producciones.
			posicion_a_retroceder = datos_parser['posicion_indice'] #"marca" de retroceso en el arbol, por si no se puede continuar por un camino, para regresar y continuar por el otro.
			procesar(parteDerecha)
			if datos_parser['error'] == True:
				datos_parser['posicion_indice'] = posicion_a_retroceder #si hay un error, es decir, si no se puede continuar por el camino, se vuelve a la "marca".
			else:
				break #si no hay error, no hace falta controlar las otras porque ya encontre una que funciona.

	def procesar(parteDerecha):
		for simbolo in parteDerecha:
			token_actual = datos_parser['tokens'][datos_parser['posicion_indice']][0]
			datos_parser['error'] = False
			if simbolo in terminales: #si el simbolo es un terminal...
				if simbolo == token_actual:
					datos_parser['posicion_indice'] += 1 #si son iguales, avanza
				else:
					datos_parser['error'] = True 
					break #sino se pone la variable en error y se corta el ciclo

			elif simbolo in no_terminales: #en cambio, si el simbolo es un no terminal...
				pni(simbolo) #llama recursivamente a pni
				if datos_parser['error']:
					break #si hay un error, se corta el ciclo porque no hace falta seguir probando lo de ese no_terminal 

	return principal()

#parser([(token1,lexema1), (token2,lexema2), ..., ('EOF', 'EOF')])
parser([terminales, ('EOF', 'EOF')])