turistas = {
    "001": ["John Doe", "Estados Unidos", "12-01-2024"],
    "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
    "012": ["Julian Martinez", "Argentina", "19-09-2023"],
    "014": ["Agustin Morales", "Argentina", "28-03-2024"],
    "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
    "006": ["Maria Lopez", "Mexico", "08-12-2023"],
    "007": ["Joao Silva", "Brasil", "20-06-2024"],
    "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
    "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
    "008": ["Ana Santos", "Brasil", "03-10-2023"],
    "010": ["Martin Fernandez", "Argentina", "13-03-2023"],
    "011": ["Sofia Gomez", "Argentina", "07-04-2024"],
     }

'''
Recibe como argumento un país (string), luego compara con los paises de
los turistas del diccionario, si coincide entonces agrega EL NOMBRE a la
lista nombres_turistas.
Si nombres_turistas no está vacío (longitud es mayor a 0), imprime la lista
'''
def turistas_por_pais(pais):
    nombres_turistas = []

    for clave in turistas:
        # lower() para comparar los 2 paises con minúsculas, 
        # independientemente si tienen mayúsculas o no
        if turistas[clave][1].lower() == pais.lower():
            nombres_turistas.append(turistas[clave][0])
    
    if len(nombres_turistas) > 0:
        print(nombres_turistas)
    else:
        print("No se encontraron turistas con ese país")


'''
Recibe como argumento un mes (int) del 1 al 12.
Luego imprime el porcentaje de turistas con el mes ingresado (del total del diccionario)
'''
def turistas_por_mes(mes):
    total = len(turistas)
    turistas_mes = 0

    for clave in turistas:
        # Crea una lista de un texto separandolo por "-"
        # por ejemplo, "13-03-2023" se convertira en:
        # ["13", "03", "2023"]
        fecha = turistas[clave][2].split("-")

        # el mes que está en fecha es un string, por lo que necesita convertir a int.
        # Al convertir a int, los "0" del mes en fecha serán quitados (02, 05, etc...)
        if int(fecha[1]) == mes:
            turistas_mes += 1
    
    porcentaje = round((turistas_mes * 100) / total, 2)

    print(f"El número de turistas equivale al {porcentaje} % del total.")


'''
Elimina un turista por nombre
No recibe ningún argumento
'''
def eliminar_turista():
    nombre_turista = input("Ingrese nombre del turista a eliminar: ")

    turista_a_eliminar = "" # Se reemplaza con la clave del usuario encontrado

    for clave in turistas:
        # Se compara con lower() para que ambos strings estén en minúsculas
        if turistas[clave][0].lower() == nombre_turista.lower():
            turista_a_eliminar = clave
    
    if len(turista_a_eliminar) > 0:
        del turistas[turista_a_eliminar]
        
        print("Turista eliminado con exito.")
    else:
        print("Turista no encontrado. No se pudo eliminar")

while True:
    print('''
       *** MENU PRINCIPAL ***
       1.- Turistas por país.
       2.- Turista por mes.
       3.- Eliminar turista.
       4.- Salir
       ''')
    
    opcion = 0

    try:
        opcion = int(input("ingrese opción: "))
    except ValueError as error:
        print("Opción inválida")
    
    # Salir
    if opcion == 4:
        print("Has salido del programa...")
        break

    #Turistas por país
    elif opcion == 1:
        pais_usuario = input("Ingrese un país: ")

        turistas_por_pais(pais_usuario)

    # Turista por mes
    elif opcion == 2:
        mes_usuario = 0
        try:
            mes_usuario = int(input("Ingrese un mes (1-12): "))
        except ValueError as error:
            print("Ingrese un número válido")

        while True:
            if mes_usuario >= 1 and mes_usuario <= 12:
                break
            else:
                print("Debe ingresar un valor entre 1 y 12. Inténtelo nuevamente.")
                mes_usuario = int(input("Ingrese un mes (1-12): "))
        
        turistas_por_mes(mes_usuario)

    # Eliminar turista
    elif opcion == 3:
        eliminar_turista()
        
    else:
        print("Por favor, ingrese una opción válida")

