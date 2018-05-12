import random

tablero=[0,1,2,3,4,5,6,7,8]

print tablero

def pantalla():
	print tablero[0],"||",tablero[1],"||",tablero[2]
	print "_____________"
	print tablero[3],"||",tablero[4],"||",tablero[5]
	print "_______________"
	print tablero[6],"||",tablero[7],"||",tablero[8]

print pantalla()

def gana():
    #Filas
    if tablero[0]==tablero[1] and tablero[1]==tablero[2]:
        return True
    elif tablero[3]==tablero[4] and tablero[4]==tablero[5]:
        return True
    elif tablero[6]==tablero[7] and tablero[7]==tablero[8]:
        return True
    #Diagonales
    elif tablero[0]==tablero[4] and tablero[4]==tablero[8]:
        return True
    elif tablero[6]==tablero[4] and tablero[4]==tablero[2]:
        return True
    #Columnas
    elif tablero[0]==tablero[3] and tablero[3]==tablero[6]:
        return True
    elif tablero[1]==tablero[4] and tablero[4]==tablero[7]:
        return True
    elif tablero[2]==tablero[5] and tablero[5]==tablero[8]:
        return True
    #Default
    return False

while gana()==False:
	usuario=int(raw_input("Eliga un lugar del 0 al 8: "))
	if tablero[usuario]!='X' and tablero[usuario]!='O':
		tablero[usuario]='X'
		maquina=random.randint(0,8)
                while tablero[maquina]=='O':
                        maquina=random.randint(0,8)
                        if tablero[maquina]!='O' and tablero[maquina]!='X':
                            tablero[maquina]='O'
	else:
		print "Este espacio ya esta usado"
		print "  "

	pantalla()
	print gana()



