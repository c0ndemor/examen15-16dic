import random

def filtra_ejercicios(lista, minutos):
    ejercicios_cortos = []
    for ejercicio in lista:
        if ejercicio["duracion"] <=minutos:
            ejercicios_cortos.append(ejercicio)
    return ejercicios_cortos


def duracion_ejercicios(lista):
    sumaminutos = 0
    for ejercicio in lista:
        sumaminutos += ejercicio["duracion"]
    return sumaminutos


def entrenamiento(lista, minutos):
    lista_aleatoria = []
    min = 0
    while min < minutos:
        ejercicio = random.choice(lista)
        if min + ejercicio["duracion"] <= minutos:
            lista_aleatoria.append(ejercicio)
            min += ejercicio["duracion"]
    return lista_aleatoria

#listaejercicios = [{"descripcion": "esta es la descripcion1", "denominacion": "esta es la denominacion1", "estrategias": ["estrategia 1.1", "estrategia 1.2"], "minutos": 10}, {"descripcion": "esta es la descripcion2", "denominacion": "esta es la denominacion2", "estrategias": ["estrategia 2.1", "estrategia 2.2"], "minutos": 20}]

if __name__ == "__main__":
    while True:
        try:
            orden = int(input("Qué quieres hacer? Para crear una lista, pulsa (1).\n Para ver la lista de ejercicios, pulsa (2).\n Para generar una lista de entrenamiento, pulsa (3).\n Para mostrar una lista de ejercicios de una duración menor o igual que la proporcionada, pulsa (4).\n Para terminar, pulsa (5). "))
            if orden <1 or orden >5:
                print("Debes introducir una orden válida, con los números del 1 al 5.")
            elif orden == 1:
                nuevoejercicio = input("Introduce aquí el nuevo ejercicio: ")
                lista = lista.append(nuevoejercicio)
            elif orden == 2:
                print(lista)
            elif orden == 3:
                duracion = int(input("¿De cuánto tiempo quieres tu rutina de ejercicios?"))
                if (duracion%10 ==0) and duracion >=10:
                    rutina = []
                    minu = 0
                    for ejercicio in lista:
                        while minu < duracion:
                            ejercicio = random.choice(lista)
                            if minu + ejercicio["duracion"] <= duracion:
                                rutina.append(ejercicio)
                                minu += ejercicio["duracion"]
                else:
                    print("Introduzca una duración válida, por favor.")
            elif orden == 4:
                print(filtra_ejercicios(lista, minutos))
            elif orden == 5:
                print("Se acabó. Gracias.")
                break
            
            
        except ValueError:
            print("Debes escribir una orden, con los números del 1 al 5. Gracias :)")    
    



    #print(filtra_ejercicios(listaejercicios, 10))
    #print(duracion_ejercicios(listaejercicios))
