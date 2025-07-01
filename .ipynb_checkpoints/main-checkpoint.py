import os

def ejecutar_sql():
    os.system("poetry run python review_sql.py")

def ejecutar_mongo():
    os.system("poetry run python review_mongo.py")

def ejecutar_neo4j():
    os.system("poetry run python review_neo4j.py")


def caso_uso_3():
    fecha = input("Ingresá la fecha desde la cual contar (formato yyyy-mm-dd): ")
    os.system(f'poetry run python -c "from review_mongo import contar_propiedades_desde_fecha; contar_propiedades_desde_fecha(\'{fecha}\')"')

def mostrar_menu():
    while True:
        print("\n===== MENÚ DE CASOS DE USO =====")
        print("1. Ver datos en MySQL")
        print("2. Ver datos en MongoDB")
        print("3. Ver datos en Neo4j")
        print("4. Caso de uso 3 - Cuántas propiedades han sido agregadas recientemente a la plataforma")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ejecutar_sql()
        elif opcion == "2":
            ejecutar_mongo()
        elif opcion == "3":
            ejecutar_neo4j()
        elif opcion == "4":
            caso_uso_3()
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    mostrar_menu()
