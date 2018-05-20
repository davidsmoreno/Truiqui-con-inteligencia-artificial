import random


tablero=[0,1,2,3,4,5,6,7,8]
m=[0,0,0,0,0,0,0,0,0]
foo = [1,3,5,7]
random = random.choice(foo)


print tablero



def pantalla():
	print tablero[0],"|",tablero[1],"|",tablero[2]
	print "----------"
	print tablero[3],"|",tablero[4],"|",tablero[5]
	print "----------"
	print tablero[6],"|",tablero[7],"|",tablero[8]

print pantalla()

def buenajugada(pos):
	esbuena = False
	for i in pos:
		for j in pos:
			for a in pos:
				if pos[i]==1 and pos[j]==1 and pos[a]==0:
					return a
					esbuena = True
					break
				if pos[a]==1 and pos[j]==1 and pos[i]==0:
					return i
					esbuena = True
					break
				if pos[i]==1 and pos[a]==1 and pos[j]==0:
					return j
					esbuena = True
					break
	for i in pos:
		for j in pos:
			for a in pos:
				if pos[i]==-1 and pos[j]==-1 and pos[a]==0:
					return a
					esbuena = True
					break
				if pos[a]==-1 and pos[j]==-1 and pos[i]==0:
					return i
					esbuena = True
					break
				if pos[i]==-1 and pos[a]==-1 and pos[j]==0:
					return j
					esbuena = True
					break
				
	if pos[0]==pos[8]==-1 or pos[2]==pos[6]==-1:
                while pos[random]==-1 or pos[random]==1:
                        random= random.choice(foo)
                return random
                esbuena=True

        if pos[4]==-1:
                randomp = random.choice([0,2,6,8])
                while pos[randomp]==-1 or pos[randomp]==1:
                        randomp = random.choice([0,2,6,8])
                return randomp
                esbuena=True
                
	return esbuena

#Funcion que permite saber quien gano
def CPU():
        if tablero[0]=='X' and tablero[1]=='X' and tablero[2]=='X':
               return "Gana la CPU"
        elif tablero[3]=='X' and tablero[4]=='X' and tablero[5]=='X':
                return "Gana la CPU"
        elif tablero[6]=='X' and tablero[7]=='X' and tablero[8]=='X':
                return "Gana la CPU"
        #
        elif tablero[0]=='X' and tablero[4]=='X' and tablero[8]=='X':
                return "Gana la CPU"
        elif tablero[6]=='X' and tablero[4]=='X' and tablero[2]=='X':
                return "Gana la CPU"
        #
        elif tablero[0]=='X' and tablero[3]=='X' and tablero[6]=='X':
                return "Gana la CPU"
        elif tablero[1]=='X' and tablero[4]=='X' and tablero[7]=='X':
                return "Gana la CPU"
        elif tablero[2]=='X' and tablero[5]=='X' and tablero[8]=='X':
                return "Gana la CPU"
        #
        else:
                return "Gana el jugador"

#Funcion que evalua si alguien completo 3 casillas
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

#Revisa si hay empate
def paraempate(pos):
        contador=0
        for i in pos:
            if pos[i]==1 or pos[i]==-1:
                    contador +=1
                    
        while contador<8:
                return False
                contador=0
        if contador==8:
                return True
                
#Creacion de la lista que permite saber las posiciones
def revi_evalua():
        for i in (0,1,2,3,4,5,6,7,8):
                if tablero[i]=='O':
                        m.pop(i)
                        m.insert(i,-1)
                elif tablero[i]=='X':
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
#TURNO
def jugada_x(pos):
        contador=0
        for i in pos:
                if pos[i]==1:
                        contador+=1
                elif pos[i]==-1:
                        contador+=1

        if contador%2==0:
                return True
        else:
                return False

def quienmueve(algo):
        if algo==True:
                print "Turno de la maquina"
        else:
                print "Turno del jugador"
                        
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




#Ejecucuion
while gana()==False or paraempate(m)==False:
    maquina = random.randint(0,8)
    while tablero[maquina]=='X' or tablero[maquina]=='O':
            if buenajugada(m)==True:
                    tablero[buenajugada(tablero)]='X'
            else:
                    maquina =random.randint(0,8)
    if tablero[maquina]!='X' and tablero[maquina]!='O':
            tablero[maquina]='X'
    pantalla()
    if gana()==True or paraempate(m)==True:
            break
    revi_evalua()
    quienmueve(jugada_x(m))
    base3(m)
    paraempate(m)
    buenajugada(m)
    
        
            
    usuario=int(raw_input("Eliga un lugar del 0 al 8: "))
    while tablero[usuario]=='X' or tablero[usuario]=='O':
        usuario=int(raw_input("Eliga un lugar del 0 al 8: "))
    if tablero[usuario]!='X' and tablero[usuario]!='O':
            tablero[usuario]='O'
    pantalla()
    gana()
    if gana()==True:
            break
    revi_evalua()
    quienmueve(jugada_x(m))
    base3(m)
    paraempate(m)
    buenajugada(m)

    
    print"************************************"

#DICE EL GANADOR       
if gana()==True:
        print CPU()
#Empate
if paraempate(m)==True:
        print "Empate"












