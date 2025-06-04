def main():
    Actividad = input("Seleccion de actividad a visualizar (Ejemplo u1_a1):  ")

    if Actividad == "u1_a1":
        from src.u1act1 import signals
        signals()
    elif Actividad == "u1_a2":
        from src.u1act2 import signals
        signals()
    else:
        print("Esta tarea aun no existe")

if __name__ == "__main__":
    main()
    
