# Variable generales
from abc import abstractclassmethod
errores=0
aciertos=0
intentos=0
barritas=""
palabra=""
respuesta=[]
usadas=[]
vacio=[]
excepciones=[ " " ,".",",",":",";","?","¿","¡","!","#","@","+", "(",")","[","]","{","}","-","€","$","=","*","'","<",">"]
guiones_a = ""
guiones = guiones_a
reintento=""
juegoTerminado= False
# variables para el muñeco
palo = " |"
base = ("_"+ "|" + "_")
pasarela1 = "  _"
pasarela2 = "_"
cuerda = "   |"
pierna_i = "  /"
pierna_d = " \ "
brazo_i = "  \O"
brazo_d = "/"
cabeza = "   O"

# Funcion para dibujar el muñeco
def muñeco(errores):
    if errores==0:
        print (pasarela1+pasarela2+pasarela2)
        print (palo+cuerda)
        print (palo)
        print (palo)
        print (palo)
        print (base)
    if errores==1:
        print (pasarela1+pasarela2+pasarela2)
        print (palo+cuerda)
        print (palo+cabeza)
        print (palo)
        print (palo)
        print (base)
    elif errores==2:  
        print (pasarela1+pasarela2+pasarela2)
        print (palo+cuerda)
        print (palo + cabeza)
        print (palo+cuerda)
        print (palo)
        print (base)
    elif errores==3:    
        print (pasarela1+pasarela2+pasarela2)
        print (palo+cuerda)
        print (palo+cabeza)
        print (palo+cuerda)
        print (palo+pierna_i)
        print (base)
    elif errores==4:    
        print (pasarela1+pasarela2+pasarela2)
        print (palo+cuerda)
        print (palo+cabeza)
        print (palo+cuerda)
        print (palo+pierna_i+pierna_d)
        print (base)
    elif errores==5:
        print (pasarela1+pasarela2+pasarela2)
        print (palo+cuerda)
        print (palo+brazo_i) 
        print (palo+cuerda)
        print (palo+pierna_i+pierna_d)
        print (base)
    elif errores==6:
        print (pasarela1+pasarela2+pasarela2)
        print (palo+cuerda)
        print (palo+brazo_i+brazo_d) 
        print (palo+cuerda)
        print (palo+pierna_i+pierna_d)
        print (base)

# Cambiamos las palabras que nos den a las barritas o por las excepciones
def cambio(p):
    global barritas , palabra , barritas_a
    barritas_a = barritas
    for i in p: # solicitar es la palabra que nos a dado el usuario para adivinar
        if i not in excepciones : # Le diremos que si esta en excepciones que nos devuelva las excepciones y no las cambie por "_"
            barritas_a = barritas_a + "_"
        else:
            barritas_a=barritas_a+i
    print("Palabra: " + barritas_a)

# Funcion principal del juego donde almacenaremos todo lo necesario para poder crear el juego
def game():
    global excepciones , palabra , barritas , barritas_a, reintento, errores
    errores=0
    aciertos=0
    usadas=[]

    # Mensajes de bienvenida:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") # Para que se "limpie" la cmd al poner la palabra para adivinar
    print("-Bienvenido al juego del ahorcado")
    print('---')
    print("- La palabra para adivinar nos la da una persona al azar, es decir tenemos que poner la palabra manualmente")
    print("- El objetivo del juego es adivinar la palabra secreta letra por letra")
    print("- Tienes un total de 6 vidas, pierdes una vida cada que te equivocas, si te quedas sin vidas pierdes")
    print("---")
    palabra=input("Dame tu palabra para adivinar: ") # Se encuentra la palabra que nos den para adivinar
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") # Para que se "limpie" la cmd al poner la palabra para adivinar

    # Empezamos el bucle pricipal del juego
    while errores<=6:
        # Le pedimos la letra
        respuesta=input("-Letra de la palabra a adivinar: ")
        print("---------------------")
        if respuesta not in palabra:
                    if len(respuesta)>1: # Cuando tengamos mas de una letra que no nos cuente los fallos y nos de otro intento
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") # Para que se "limpie" la cmd al poner la palabra para adivinar
                        print("-Solo puedes poner una letra\n-Prueba otra vez")
                    elif respuesta in excepciones or respuesta in usadas:
                        print("-Esa letra ya la has usado")
                    else:
                        errores=errores+1
                        muñeco(errores)
                        cambio(p = palabra)
                        print("Esa letra no es correcta")
        # Printeamos el muñeco
        if respuesta in palabra:
            muñeco(errores)
        # Le diremos que cuando llegue a un maximo de 6 errores que ha perdido y nos de todo el dibujo del ahorcado
        if errores==6:
            print(f"-¡Has perdido!")
            print(f"Fallos: {errores}/6")
            # Cuando pierda le diremos que si quiere volver a jugar que pulse uno sino que pulse otra telca
            reintento=input("-Si quieres volver a jugar pulse 1, sino quieres volver a jugar pulsa cualquier otra tecla: ")
            if reintento=="1":
                # Que nos devuelta la funcion de game()
                return game(), cambio()
            else:
                print("-¡Hasta la proxima!")
                break
        # Le obligamos a que no pueda darnos mas de una sola letra
        if respuesta in palabra:
            if len(respuesta)>1: # Cuando tengamos mas de una letra que no nos cuente los fallos y nos de otro intento
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") # Para que se "limpie" la cmd al poner la palabra para adivinar
                print("-Solo puedes poner una letra\n-Prueba otra vez")
            elif respuesta in excepciones or respuesta in usadas:
                print("-Esa letra ya la has usado")
                cambio(p=palabra)
            else:
                aciertos+=1
                excepciones[len(excepciones):]= respuesta
                cambio(p=palabra) 
                print("Esa letra si es correcta")
        # Con este if le diremos que siempre que nos de una respuesta nos devuelva los fallos y las letras usadas
        if respuesta:
            usadas+=respuesta
            print(f"Fallos: {errores}/6") 
            print(f"Letras usadas: {usadas}")
        # Con este if podemos reinicar el juego y decir si has ganado
        if palabra == barritas_a:
            print("¡Has ganado!")
            respuesta=input("Si quieres volver a jugar pulse 1, si no quieres volver a jugar pulsa cualquier otra tecla: ")
            # En caso de que nos de vuelva un 1 reiniciamos el juego
            if respuesta=="1":

                return game()
            # Si no le diremos adios y cerraremos el juego
            else:
                print("¡Hasta la proxima!")
                break
game()