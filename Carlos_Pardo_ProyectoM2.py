################################################## 

### Ejercicio 1. Longitud de una frase ###

#Se pide una palabra al usuario y se quitan los espacios en blanco
Palabra = input("Por favor introduce una Palabra entre 4 y 8 dígitos: ").strip()
#Se agrega un While por seguridad para que coloquen un dato válido
while not Palabra:
    Palabra = input("Por favor introduce una Palabra entre 4 y 8 dígitos: ").strip()
# se usa un condicional para verificar que la palabra dada por el usuario esté entre el rango de 4 a 8 caracteres y se imprime el mensaje correspondiente
if len(Palabra) < 4:
    print(f"Intenta de nuevo, La Palabra '{Palabra}' tiene {len(Palabra)} caracteres y debe ser mayor a 4 caracteres")
elif len(Palabra)>8:
    print(f"Intenta de nuevo, La Palabra '{Palabra}' tiene {len(Palabra)} caracteres y debe ser menor a 8 caracteres")
else :
    print(f"Muy bien, La Palabra '{Palabra}' tiene {len(Palabra)} caracteres")

################################################## 

### Ejercicio 2. Encuentra el cuadrante ###

#Se usa condicional while para garantizar que el dato que se pide sea el correcto
while True:
    #Se usa la función try: para revisar si el código a usar puede generar un error
    try:
        #Se pide el dato al usuario y se usa la función strip() para quitar espacios en blanco
        x = int (input ('Ingresa el valor de x: ').strip())
        #Condicional para validar que el dato en X no sea 0
        if x==0:
            print("Por favor, introduce un número Mayor a 0 pra el eje X.")
            continue
        #Se usa la función break para salir del bucle si se encuentra un valor válida
        break
    #Se usa la función except ValueError: para ejecutar algo si ocurre un error
    except ValueError:
        print("Por favor, introduce un número entero válido.")

#Se usa condicional while para garantizar que el dato que se pide sea el correcto
while True:
    #Se usa la función try: para revisar si el código a usar puede generar un error
    try:
        #Se pide el dato al usuario y se usa la función strip() para quitar espacios en blanco
        y = int (input ('Ingresa el valor de y: ').strip())
        #Condicional para validar que el dato en Y no sea 0
        if y==0:
            print("Por favor, introduce un número Mayor a 0 pra el eje Y.")
            continue
        #Se usa la función break para salir del bucle si se encuentra un valor válida
        break
    #Se usa la función except ValueError: para ejecutar algo si ocurre un error
    except ValueError:
        print("Por favor, introduce un número entero válido.")

#Se usa la función if como condicional para revisar a qué cuadrante pertenece el dato
#Cuadrante I: (X, Y): (+, +)
if x >=1 and y >=1:
    print(f"La cordenada {x}, {y} pertenece al cuadrante I.")
#Cuadrante II: (X, Y): (-, +)
elif x <=-1 and y >=1:
    print(f"La cordenada {x},{y} pertenece al cuadrante II.")
#Cuadrante III: (X, Y): (-, -)
elif x <=-1 and y <=-1:
    print(f"La cordenada {x},{y} pertenece al cuadrante III.")
#Cuadrante IV: (X, Y): (+, -)
elif x >=1 and y <=-1:
    print(f"La cordenada {x},{y} pertenece al cuadrante IV.")
#Esta función se usa en caso de no pertenecer a ningun cuadrante si no se tuviera la condición de que el valor de X o Y sea diferente a 0
else:
    print("La coordenada no pertenece a ningún cuadrante.")