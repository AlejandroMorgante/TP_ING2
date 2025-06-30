import os

def ejecutar_sql():
    os.system("poetry run python review_sql.py")

def ejecutar_mongo():
    os.system("poetry run python review_mongo.py")

def ejecutar_neo4j():
    os.system("poetry run python review_neo4j.py")

def mostrar_menu():
    while True:
        print("\n===== MENÚ DE CASOS DE USO =====")
        print("1. Ver datos en MySQL")
        print("2. Ver datos en MongoDB")
        print("3. Ver datos en Neo4j")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ejecutar_sql()
        elif opcion == "2":
            ejecutar_mongo()
        elif opcion == "3":
            ejecutar_neo4j()
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    mostrar_menu()
