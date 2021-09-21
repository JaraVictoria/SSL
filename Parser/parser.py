#Es una especie de pseudocódigo, no se puede correr tal cual está.

no_terminales = ['Programa', 'Asignacion', 'Estructura', 'Expresion', 'Valor', 'ListaExpresiones', 'Termino', 'Factor'] #no está completo, hay que agregar algo más (no se el que, lo dijo en el 10:30 aprox). Guardar, en una variable, todos los no terminales de la gramática
terminales = tokens_posibles #no es la salida del lexer, sino los que determinamos

producciones = { #estructura de diccionarios: llaves/claves y valores asignados a esa llave/clave. Hay que poner las producciones de los no terminales
	'Noterminal1': [['token1', 'Noterminalj', ..., 'tokenN'], ..., [ladoderechoK1]]
	...
	'Noterminalp' [[ladoderecho1], ..., [ladoderechoKp]]
}

def parser(lista_tokens): #lista_tokens es la salida del lexer
	datos_parser = {
		'tokens': lista_tokens,
		'posicion_indice': 0,
		'error': False,
	}

	def principal():
		pni('S')
		token_actual = datos_parser['tokens'][datos_parser['posicion_indice']][0]
		if token_actual != 'eof' or datos_parser['error']:
			print('La cadena no pertenece al lenguaje')
			return False

		return True

	def pni(no_terminal):
		for parteDerecha in producciones[no_terminal]:
			posicion_a_retroceder = datos_parser['posicion_indice']
			procesar(parteDerecha)
			if datos_parser['error'] == True:
				datos_parser['posicion_indice'] = posicion_a_retroceder
			else:
				break

	def procesar(parteDerecha):
		for simbolo in parteDerecha:
			token_actual = datos_parser['tokens'][datos_parser['posicion_indice']][0]
			datos_parser['error'] = False
			if simbolo in terminales:
				if simbolo == token_actual:
					datos_parser['posicion_indice'] += 1
				else:
					datos_parser['error'] = True
					break

			elif simbolo in no_terminales:
				pni(simbolo)
				if datos_parser['error']:
					break

	return principal()

parser([(token1,lexema1), (token2,lexema2), ..., ('eof', 'eof')])