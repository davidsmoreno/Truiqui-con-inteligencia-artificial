import random


tablero=[0,1,2,3,4,5,6,7,8]
m=[0,0,0,0,0,0,0,0,0]
lol=random.choice([1,3,5,7])
olo = random.choice([0,2,6,8])




print tablero



def pantalla():
	print tablero[0],"|",tablero[1],"|",tablero[2]
	print "----------"
	print tablero[3],"|",tablero[4],"|",tablero[5]
	print "----------"
	print tablero[6],"|",tablero[7],"|",tablero[8]

print pantalla()

def buenajugada(pos,jugada_x,m):
	jugadaganadora=True;
	if jugada_x=="turno maquina":
		if jugadaganadora==True:
		
			for i in range(7):
				if (i==0 and i+2==2) or (i==3 and i+2==5) or (i==6 and i+2==8):
					if pos[i]==1 and pos[i+2]==1 and pos[i+1]==0:		
						pos.pop(i+1)
						pos.insert(i+1,'X')
						jugadaganadora=True
			for j in range(5):
				if (j==0 and j+3==3) or (j==1 and j+3==4) or (j==2 and j+3==5):
					if m[j]==1 and m[j+3]==1 and m[j+6]==0:		
						pos.pop(j+6)
						pos.insert(j+6,'X')
						jugadaganadora=True
			for j in [0,2]:
				if (j==0 and j+4==4):
					if pos[j]==1 and pos[j+4]==1 and pos[j+8]==0:
						pos.pop(j+8)
						pos.insert(j+8,1)
						jugadaganadora=True
				if pos[j]==1 and pos[j+2]==1 and pos[j+6]==0:
						pos.pop(j+4)
						pos.insert(j+4,'X')
						jugadaganadora=True

	if (pos[0]==-1 and pos[8]==-1) or (pos[2]==-1 and pos[6]==-1): 
		while pos[lol]==1 or pos[lol]==-1:
      			lol = random.choice([1,3,5,7])
                return lol
                return "nokas"

        if pos[4]==-1:
		while pos[olo]==1 or pos[olo]==-1:
			olo = random.choice([0,2,6,8]) 
                return olo
                return "nokas"
	if base3(m)==306:
		pos[0]='X'
	if base3(m)==1106 or base3(m)==5691 or base3(m)==4240:
		pos[8]='X'
        if base3(m)==4064:
		pos[4]='X'

	for i in range(len(pos)):
		for j in range(len(pos)):
			for a in range(len(pos)):
				if pos[i]==1 and pos[j]==1 and pos[a]==0:
					return a
					return "nokas"
					
				elif pos[a]==1 and pos[j]==1 and pos[i]==0:
					return i
					return "nokas"
					
				elif pos[i]==1 and pos[a]==1 and pos[j]==0:
					return j
					return "nokas"
					
	for i in range(len(pos)):
		for j in range(len(pos)):
			for a in range(len(pos)):
				if pos[i]==-1 and pos[j]==-1 and pos[a]==0:
					return a
					return "nokas"
					
				elif pos[a]==-1 and pos[j]==-1 and pos[i]==0:
					return i
					return "nokas"
					
				elif pos[i]==-1 and pos[a]==-1 and pos[j]==0:
					return j
					return "nokas"

					
				
	
          

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
def is_full(pos):
	for row in range(len(pos)):
		if pos[row]==0 :
			return False
	return True

                
#Creacion de la lista que permite saber las posiciones
def revi_evalua(m):
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
                                      return suma,"Decimal"
                                      for k in range(13):
                                          binaenvi[13*gru-k-1]=suma%2
                                          suma=suma/2
                                      gru=gru+1
                                      suma=0
                                      pot=3**7
                                  
                   return binaenvi
#TURNO
def jugada_x(pos):
	z = True
        c=0
	j=0
        for i in range(len(pos)):
                if pos[i]==1:
                        c=c+1
			z=True
                elif pos[i]==-1:
                        j=j+1
			z=False

        if c==j:
		return "turno maquina"
	else:
		return "turno jugador"
                        
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
while gana()==False:
    buenajugada(tablero,jugada_x(m),m)
    maquina = random.randint(0,8)
    while tablero[maquina]=='X' or tablero[maquina]=='O':
            if buenajugada(tablero,jugada_x(m),m)=="nokas":
                    tablero[buenajugada(tablero)]='X'
            else:
                    maquina =random.randint(0,8)
    if tablero[maquina]!='X' and tablero[maquina]!='O':
            tablero[maquina]='X'
    pantalla()
    if gana()==True or is_full(m)==True:
            break
    print revi_evalua(m)
    print base3(m)
    is_full(m)
    if is_full(m)==True:
	break
    buenajugada(tablero,jugada_x(m),m)
    jugada_x(m)
    print buenajugada(tablero,jugada_x(m),m)
    
        
            
    usuario=int(raw_input("Eliga un lugar del 0 al 8: "))
    while tablero[usuario]=='X' or tablero[usuario]=='O':
        usuario=int(raw_input("Eliga un lugar del 0 al 8: "))
    if tablero[usuario]!='X' and tablero[usuario]!='O':
            tablero[usuario]='O'
    pantalla()
    gana()
    if gana()==True:
            break
    print revi_evalua(m)
    print base3(m)
    is_full(m)
    if is_full(m)==True:
	break
    buenajugada(tablero,jugada_x(m),m)

    
    print"************************************"
    jugada_x(m)
    print buenajugada(tablero,jugada_x(m),m)

#DICE EL GANADOR       
if gana()==True:
        print CPU()
#Empate
if is_full(m)==True:
	print "Empate"


