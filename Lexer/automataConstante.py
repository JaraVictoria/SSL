ESTADO_FINAL = "ESTADO ACEPTADO"
ESTADO_NO_FINAL = "ESTADO NO ACEPTADO"
ESTADO_TRAMPA = "ESTADO TRAMPA"

def automata_constante(cadena):
	estado = 0
	estados_finales = [1]

	for caracter in cadena:
		if estado == 0 and (caracter == "-" or caracter.isnumeric()): #Lo unico malo que le veo, es que acepta el "-0".
			estado = 1
		elif estado == 1 and caracter.isnumeric():
			estado = 1	
		else:
			estado = -1
			break

	if estado == -1:
		return ESTADO_TRAMPA
	if estado in estados_finales:
		return ESTADO_FINAL
	else:
		return ESTADO_NO_FINAL

assert automata_constante("979") == ESTADO_FINAL
assert automata_constante("98.9.") == ESTADO_TRAMPA