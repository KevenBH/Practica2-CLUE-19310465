#ALTA DE CARTAS
cartas = {
    "profesores":[
                "Prof. Maurinhio",
                "Prof. Lizarrinhia",
                "Prof. Victorinhio",
                "Prof. Lazzinhio",
                "Prof. Pelanhio",
                "Prof. Ricardinhio"],
    "armas":[
           "Regla T",
           "Banana",
           "Marcador",
           "Lapiz HB ",
           "Biblia"],
    "lugares":[
                  "Tiendita del L",
                  "Salon 205-L",
                  "Bibloioteca",
                  "Auditorio",
                  "Direccion"]
}

import random
import os
import time
borrarPantalla = lambda: os.system ("cls")

#SELECCION DE LA VICTIMA
victima = random.choice(cartas["profesores"])

#Dialogo
borrarPantalla()
print("BIENVENIDO A CLUE ft Ceti\n\n¿Quién es el Homicida?")
input("\n\nPress Enter to continue...")
borrarPantalla()
print("REGLAS DEL JUEGO\n\nPara encontrar al culpable, se te otorgara hacer 5 preguntas, entre las cuales estan los Profesores, Armas y Lugares.")
input("\n\nPress Enter to continue...")
borrarPantalla()
print("REGLAS DEL JUEGO\n\nPodrás corroborar tus preguntas por las camaras de seguridad que se encuentrar por la institucion y dar con el mata cristianos")
input("\n\nPress Enter to continue...")
borrarPantalla()
print("REGLAS DEL JUEGO\n\nUna vez terminadas tus 5 questions de generar pistas, podrás hacer una acusación sobre cual profesor fue, con qué objeto mató a la victima y en lugar fue ejecutado")
input("\n\nPress Enter to continue...")
borrarPantalla()
print("¡QUE INICIE EL JUEGO!")
input("\n\nPress Enter to continue...")
borrarPantalla()
print("\n-¡OOHHHH NOOOOO! Encontraron al petateado de " + victima)
time.sleep(2)
print("\n-¡Quién jue el malandro que hizo esto?!")
input("\n\nPress Enter to continue...")
borrarPantalla()

#elimina a la victima de la lista personajes
cartas["profesores"].remove(victima)

#SELECCION DEL HOMICIDIO
#Culpable, arma y habitacion
homicidio = [random.choice(cartas["profesores"]),random.choice(cartas["armas"]), random.choice(cartas["lugares"])]

#GENERACION DE PISTAS PARA CREAR LAS HISTORIAS
random.shuffle(cartas["profesores"])
lista_Historias = []                              

for i in range(5):
  p = cartas["profesores"][i]
  a = cartas["armas"][i]
  h = cartas["lugares"][i]
  lista_Historias.append((p,a,h))

#SELECCION PARA MOSTRAR HISTORIAS
print("ENCONTREMOS PISTAS...")

#ciclo para 5 preguntas
for p in range(5):
  #Menú 1
  print("\nSelecciona una opcion para hacer una pregunta:\n1 Profesor \n2 Arma\n3 Lugar")
  opcion = int(input())

  #Opciones
  if opcion == 1:
    #Menu 2 
    print("\nSelecciona el personaje por el que quieres preguntar:")
    for i in range(len(cartas["profesores"])):
      print(i+1, cartas["profesores"][i])
    op2 = int(input())

    #busca la pista dentro de la lista de lista_Historias y poder mostrar la historia
    eleccion = cartas["profesores"][op2-1]

    for j in range(len(lista_Historias)):
      if eleccion in lista_Historias[j]:
        historia= lista_Historias[j]
        borrarPantalla()
        print("\n\n",historia[0],"dice que estuvo en", historia[2], "y que vio el objeto", historia[1])
        time.sleep(3)

    #busca las listas en homicidio para mostrar si hay o no registro 
    print("\n\n")
    for x in range(3):
      frase = ""
      if historia[x] not in homicidio[x]:
        frase += "Hay registro de " + historia[x]
        print(frase)
      else:
        frase += "No se encontro registro de " + historia[x]
        print(frase)
    input("\n\nPress Enter to continue...")
    borrarPantalla()


  if opcion == 2:
    print("\nSelecciona el arma por la que quieres preguntar:")
    for i in range(len(cartas["armas"])):
      print(i+1, cartas["armas"][i])
    op2 = int(input())

    eleccion = cartas["armas"][op2-1]

    for j in range(len(lista_Historias)):
      if eleccion in lista_Historias[j]:
        historia= lista_Historias[j]
        borrarPantalla()
        print("\n", historia[0],"dice que estuvo en", historia[2], "y que vio el objeto", historia[1])
        time.sleep(3)

    print("\n\n")
    for x in range(3):
      frase = ""
      if historia[x] not in homicidio[x]:
        frase += "Hay registro de " + historia[x]
        print(frase)
      else:
        frase += "No se encontro registro de " + historia[x]
        print(frase)      
    input("\n\nPress Enter to continue...")
    borrarPantalla()


  if opcion == 3:
    print("\nSelecciona el lugar por la que quieres preguntar:")
    for i in range(len(cartas["lugares"])):
      print(i+1, cartas["lugares"][i])
    op2 = int(input())  

    eleccion = cartas["lugares"][op2-1] 

    for j in range(len(lista_Historias)):
      if eleccion in lista_Historias[j]:
        historia= lista_Historias[j]
        borrarPantalla()
        print("\n", historia[0],"dice que estuvo en", historia[2], "y que vio el objeto", historia[1])
        time.sleep(3)

    print("\n\n")
    for x in range(3):
      frase = ""
      if historia[x] not in homicidio[x]:
        frase += "Hay registro de " + historia[x]
        print(frase)
      else:
        frase += "No se encontro registro de " + historia[x]
        print(frase)      
    input("\n\nPress Enter to continue...")
    borrarPantalla()       

#SUPOSICIÓN
print("ES MOMENTO DE HACER UNA ACUSACIÓN.\nRecuerda que debes escoger un profesor, un arma y un lugar con las pistas que haz recolectado hasta ahora\n")
time.sleep(3)
print("\nSelecciona al Profe:")
for i in range(len(cartas["profesores"])):
  print(i+1, cartas["profesores"][i])
culp = int(input())
culpable = cartas["profesores"][culp-1]    

print("\nSelecciona el arma homicida:")
for i in range(len(cartas["armas"])):
  print(i+1, cartas["armas"][i])
ah = int(input())
arm_hom = cartas["armas"][ah-1]  

print("\nSelecciona el lugar:")
for i in range(len(cartas["lugares"])):
  print(i+1, cartas["lugares"][i])
ha = int(input())  
habit = cartas["lugares"][ha-1]   

suposicion = [culpable,arm_hom,habit]


#RESULTADOS
borrarPantalla()
print("¿WHAT IS THE IMPOSTOR?")
time.sleep(3)
print("Los resultados de tu acusación son los siguientes...\n\n")
time.sleep(3)
for x in range(3):
  frase2 = ""
  if suposicion[x] not in homicidio[x]:
    frase2 += suposicion[x] + ": No es correcta"
    print(frase2)
  else:
    frase2 += suposicion[x] + ": Es correcta"
    print(frase2)  

time.sleep(3)
print("\n\nEl culpable a sido",homicidio[0],"con", homicidio[1], "en",homicidio[2])  