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
        pass

    # Turista por mes
    elif opcion == 2:
        pass

    # Eliminar turista
    elif opcion == 3:
        pass
    else:
        print("Por favor, ingrese una opción válida")

