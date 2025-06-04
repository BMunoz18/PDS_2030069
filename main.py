def main():
    Actividad = input("Seleccion de actividad a visualizar:  ")

    if Actividad == "U1_Act1":
        from src.u1act1 import signals
        signals()
    elif Actividad == "U1_Act2":
        from src.u1act2 import signals
        signals()
    else:
        print("Esta tarea aun no existe")

if __name__ == "__main__":
    main()
