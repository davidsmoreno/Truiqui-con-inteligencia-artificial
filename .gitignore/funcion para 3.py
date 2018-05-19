import random

tablero=[0,1,2,3,4,5,6,7,8]
m=[0,0,0,0,0,0,0,0,0]

print tablero



def pantalla():
	print tablero[0],"|",tablero[1],"|",tablero[2]
	print "----------"
	print tablero[3],"|",tablero[4],"|",tablero[5]
	print "----------"
	print tablero[6],"|",tablero[7],"|",tablero[8]

print pantalla()

def CPU():
        if tablero[0]=='O' and tablero[1]=='O' and tablero[2]=='O':
               return "Gana la CPU"
        elif tablero[3]=='O' and tablero[4]=='O' and tablero[5]=='O':
                return "Gana la CPU"
        elif tablero[6]=='O' and tablero[7]=='O' and tablero[8]=='O':
                return "Gana la CPU"
        #
        elif tablero[0]=='O' and tablero[4]=='O' and tablero[8]=='O':
                return "Gana la CPU"
        elif tablero[6]=='O' and tablero[4]=='O' and tablero[2]=='O':
                return "Gana la CPU"
        #
        elif tablero[0]=='O' and tablero[3]=='O' and tablero[6]=='O':
                return "Gana la CPU"
        elif tablero[1]=='O' and tablero[4]=='O' and tablero[7]=='O':
                return "Gana la CPU"
        elif tablero[2]=='O' and tablero[5]=='O' and tablero[8]=='O':
                return "Gana la CPU"
        #
        else:
                return "Gana el jugador"
        return "Empate"

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

def revi_evalua():
        for i in (0,1,2,3,4,5,6,7,8):
                if tablero[i]=='X':
                        m.pop(i)
                        m.insert(i,-1)
                elif tablero[i]=='O':
                        m.pop(i)
                        m.insert(i,1)
                else:
                        m.pop(i)
                        m.insert(i,0)
        return m

def base3(m):
                   print m,"m"
                   for i in range(len(m)):
                       if m[i]==-1:
                            m[i]=2
                   suma=0
                   pot=3**7
                   binaenvi=range(13*(len(m)/8))
                   j=0
                   gru=1
                   for i in range(len(m)):
                                  suma=suma+(m[i]*pot)
                                  pot=pot/3
                                  if (i+1)%8==0:
                                      print suma,"Decimal"
                                      for k in range(13):
                                          binaenvi[13*gru-k-1]=suma%2
                                          suma=suma/2
                                      gru=gru+1
                                      suma=0
                                      pot=3**7
                                  
                   return binaenvi
def inversabase3(bina13):
       
                   suma=0
                   pot=2**12
                   binaenvi=range(8*(len(bina13)/13))
                   j=0
                   gru=1
                   for i in range(len(bina13)):
                                  suma=suma+(bina13[i]*pot)
                                  pot=pot/2
                                  if (i+1)%13==0:
                                      print suma,"suma"
                                      for k in range(8):
                                          binaenvi[8*gru-k-1]=suma%3
                                          suma=suma/3
                                      gru=gru+1
                                      suma=0
                                      pot=2**12
                   for i in range(len(binaenvi)):
                           if binaenvi[i]==2:
                                   binaenvi[i]=-1
                   print binaenvi,"binaenvi base 3 inversa"
                   return binaenvi

while gana()==False:
    maquina = random.randint(0,8)
    while tablero[maquina]=='X' or tablero[maquina]=='O':
            maquina =random.randint(0,8)
    if tablero[maquina]!='X' and tablero[maquina]!='O':
            tablero[maquina]='O'
    pantalla()
    gana()
    revi_evalua()
    base3(m)
    
    
        
            
    usuario=int(raw_input("Eliga un lugar del 0 al 8: "))
    while tablero[usuario]=='X' or tablero[usuario]=='O':
        usuario=int(raw_input("Eliga un lugar del 0 al 8: "))
    if tablero[usuario]!='X' and tablero[usuario]!='O':
            tablero[usuario]='X'
    pantalla()
    gana()
    revi_evalua()
    base3(m)

    
    print"************************************"

        
if gana()==True:
        print CPU()
        
def estaocupado(posicion):
	for i in posicion:
		if posicion[i]!='X' or posicion[i]!='O':
			return False
	return True


def evaluacion(pos):
    posiblesjugadas=[]
    #filas
    for j in range(pos):
        posiblesjugadas.append(set((j)))
        print posiblejugadas

    #columnas 
    for j in range(3):
        for k in range(3):
            posiblesjugadas.append(set(([k][j])))
    #diagonales        
    for m in range(3):
        posiblesjugadas.append(set([m][m]))

    for m in range(3):
        posiblesjugadas.append(set([m][2-m]))

    for l in posiblesjugadas:
        if l==set(['X']):
            return "ganajugador1"
        elif l==set(['O']):
            return "cpu gana"
    return "Empate"

def buenajugada(pos):
	esbuena = False
	for i in pos:
		for j in pos:
			for a in pos:
				if pos[i]=="X" and pos[j]=="X" and pos[a]=="_":
					return a
					esbuena = True
					break
				if pos[a]=="X" and pos[j]=="X" and pos[i]=="_":
					return i
					esbuena = True
					break
				if pos[i]="X" and pos[a]=="X" and pos[j]=="_":
					return j
					esbuena = True
					break
	for i in pos:
		for j in pos:
			for a in pos:
				if pos[i]=="O" and pos[j]=="O" and pos[a]=="_":
					return a
					esbuena = True
					break
				if pos[a]=="O" and pos[j]=="O" and pos[i]=="_":
					return i
					esbuena = True
					break
				if pos[i]="O" and pos[a]=="O" and pos[j]=="_":
					return j
					esbuena = True
					break





