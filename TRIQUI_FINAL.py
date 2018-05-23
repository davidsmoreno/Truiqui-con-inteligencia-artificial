import random
#el jugador p lo vamos a denotar como el jugador persona y lo iniciamos en el espacio vacio
jugadorp=''
#el jugador maquina igual
jugadorm=''
#creamos un caracter vacio
vacio=''
#y una lista vacia de 9 digitos ya que vamos de 0 a 8
m=['','','','','','','','','']


#esta funcion le pregunta al usuario si quiere ser x o O y decimos que si el jugarpersona elige ser x entonces jugador maquina tiene que valer O y al reves
def elegir_X_o_O(jugadorp,jugadorm):
	jugadorp=raw_input("¿Quiere ser X o O?: ")
	while jugadorp not in ('X','O'):
		print ("elija otra vez...")
		jugadorp=raw_input("¿Quiere ser X o O?: ")
	if jugadorp=='X':
		print "Es su turno..."
		jugadorm='O'
	else:
		print "Es el turno de la maquina..."
		jugadorm='X'
	return jugadorm,jugadorp
#creamos una funcion tambien preguntandole al usuario si quiere comezar,a lo que responde Si o No (la primera en mayuscula) si responde que si entonces retornamos un 1 y si juega de segundo returna un 0
def quienvaprimero():
	turno=None
	while turno not in ('Si','No'):
		turno=raw_input("¿Quiere comenzar en primer lugar?: ")
		if turno=='Si':
			return 1
		elif turno=='No':
			return 0
		else:
			print "Es invalido..."


#crea el tablero 
def dibujartablero(tablero):
    
    print tablero[0]  ,"|",tablero[1],"|",tablero[2]
    print "----------"
    print tablero[3]  ,"|",tablero[4],"|",tablero[5]
    print "----------"
    print tablero[6]  ,"|",tablero[7],"|",tablero[8]


#esta funcion mira si el jugador persona va de primero recibe el jugador p el jugadorm y la lista vacia,while gana is None porque la funcion gana retorna 1 si el jugadorp gana,0 si el jugador maquina gana y 'empate' si ninguno gana,mientras gana es vacio,agregamos una jugada y llamamos el tablero y agregamos la jugada en la lista vacia,llamamos la funcion gana y si gana es 1 que diga que gano y sino perdio si no retorna es empate.
def jugador_p1(jugadorp, jugadorm, m):
    while gana(jugadorp, jugadorm, m) is None:
        jugada = jugadorp_mueve(jugadorp,m)
        m[int(jugada)] = jugadorp
        dibujartablero(m)
        if gana(jugadorp, jugadorm, m) != None:
            break
        else:
            pass
        print "bueno"
        jugada = jugadorm_mueve(jugadorp,jugadorm,m)
        print jugada
        m[int(jugada)] = jugadorm
        dibujartablero(m)
    q = gana(jugadorp, jugadorm, m)
    if q == 1:
        print "¡Ganaste!"
    elif q == 0:
        print "Perdiste :("
    else:
        print "Es empate..."
#la funcion si maquina va de primeras 
def jugador_m1(jugadorp,jugarorm,m):
    while not gana(jugadorp,jugarorm,m):
        print "Hola"
        jugada =jugadorm_mueve(jugadorp,jugarorm,m)
        print jugada
        m[jugada] = jugadorm
        dibujartablero(m)
        if gana(jugadorp,jugarorm,m) != None:
            break
        else:
            pass
        jugada = jugadorp_mueve(jugadorp,m)
        m[int(jugada)] = jugadorp
        dibujartablero(m)
    q = gana(jugadorp, jugadorm, m)
    if q == 1:
        print "¡Ganaste!"
    elif q == 0:
        print "Perdiste :("
    else:
        print "Es empate..."




# la funcion gana mira las posibles victorias y si encuentra que en esas posiciones hay algo mira la posicion 0 y si ve que es la letra de la persona que la puso ahi por ejemplo si jugadorp elige ser x  entonces retorna 1 y si es maquina retorna 0 y si ve que que no hay 3 en linea y ya estan ocupados todos entonces es empate
def gana(jugadorp,jugadorm,m):
	mdeganar=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
	for i in mdeganar:
		if m[i[0]]==m[i[1]]==m[i[2]] !=vacio:
			ganador=m[i[0]]
			if ganador==jugadorp:
				return 1
			elif ganador==jugadorm:
				return 0
			if vacio not in m:
				return 'Empate'
	if vacio not in m:
		return 'Empate'
	return None




		
#pedimos la posicion de donde quiere jugar y mientras ese lugar en la lista sea diferente de vacio que vuelva a pedir la posicion y si es vacio que retorne la posicion.
def jugadorp_mueve(jugadorp,m):
	a=raw_input("¿Donde quiere mover? (0 al 8): ")
	while True:
		a=raw_input("Elija del 0 al 8: ")
		if m[int(a)]!=vacio:
			a=raw_input("Elija del 0 al 8: ")
		else:
			return int(a)
#si maquina mueve elegimos las mejores jugadas inicales que son las esquinas y el centro creamos una lista vacia que le vamos agregando elementos de las posibles jugadas que puede hacer y despues hacemos un ciclo en las jugadas posibles si la funcion gana ==0 entonces la maquina gana y que me retorne las jugadas en las que gana,vaciamos la lista para que lo vuelva a hacer, y ahora miramos si el adversario puede ganar en 1 ,y si nosotros no podemos ganar en uno entonces devolvemos las jugadas en donde gana el adversario y las ponemos ahi,sino elegimos entre las mejores jugadas y hacemos un random entre esos numeros.

def jugadorm_mueve(jugadorp,jugadorm,m):
	mejoresj=[4,0,2,6,8]
	lista=[]
	for i in range(9):
		if m[i]==vacio:
			lista.append(i)
	for i in lista:
		m[i]=jugadorm
		if gana(jugadorp,jugadorm,m)== 0:
			return i
		m[i]=vacio
	for i in lista:
		m[i]=jugadorp
		if gana(jugadorp,jugadorm,m)== 1:
			return i
		m[i]=vacio

	return int(lista[random.randrange(len(lista))])
#en esta funcion llamamos las funciones, entonces llamamos a a que va a ser igual a al que eligio la x e O miramos quien va primero si va primero entonces b==1,llamamos al tablero y la funcion en la cual va primero el jugador para que ponga la jugada y la dibuje en el terminal sino juega la maquina y hace lo mismo con la funcion maquina va primero else que no haga nada y llamamos el main.

			
def ejecutable(jugadorp,jugadorm,m):

	a=elegir_X_o_O(jugadorp,jugadorm)
	jugadorp=a[0]
	jugadorm=a[1]
	b=quienvaprimero()
	if b==1:
		print "Vas de primero..."
		dibujartablero(m)
		jugador_p1(jugadorp,jugadorm,m)
	elif b==0:
		print "La maquina va primero..."
		dibujartablero(m)
		jugador_m1(jugadorp,jugadorm,m)
	else:
		pass
		
ejecutable(jugadorp,jugadorm,m)
