import os

def ejecutar_mongo(caso):
    os.system(f"C:\\Users\\d78650\\AppData\\Local\\Programs\\Python\\Python313\\python.exe review_mongo.py --caso {caso}")

def ejecutar_sql(caso):
    os.system(f"C:\\Users\\d78650\\AppData\\Local\\Programs\\Python\\Python313\\python.exe review_sql.py --caso {caso}")

def ejecutar_neo4j(caso):
    os.system(f"C:\\Users\\d78650\\AppData\\Local\\Programs\\Python\\Python313\\python.exe review_neo4j.py --caso {caso}")


def mostrar_menu():
    while True:
        print("\n===== MENÚ DE CASOS DE USO =====")
        print("1. Caso 1 - Reservas diarias por destino (MongoDB)")
        print("2. Caso 2 - Tipos de alojamiento más solicitados (MongoDB)")
        print("3. Caso 3 - Propiedades agregadas recientemente (MongoDB)")
        print("4. Caso 4 - Áreas más demandadas en un país (MongoDB)")
        print("5. Caso 5 - Reservas en destinos tropicales con +4 estrellas (Neo4j)")
        print("6. Caso 6 - Alojamientos < $100 o en zonas céntricas (MongoDB)")
        print("7. Caso 1 SQL Server")
        print("8. Caso 2 SQL Server")
        print("9. Caso 3 SQL Server")
        print("10. Caso 4 SQL Server")
        print("11. Caso 6 SQL Server")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ejecutar_mongo("1")
        elif opcion == "2":
            ejecutar_mongo("2")
        elif opcion == "3":
            ejecutar_mongo("3")
        elif opcion == "4":
            ejecutar_mongo("4")
        elif opcion == "5":
            ejecutar_neo4j("5")
        elif opcion == "6":
            ejecutar_mongo("6")
        elif opcion == "7":
            ejecutar_sql("1")
        elif opcion == "8":
            ejecutar_sql("2")
        elif opcion == "9":
            ejecutar_sql("3")
        elif opcion == "10":
            ejecutar_sql("4")
        elif opcion == "11":
            ejecutar_sql("6")
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    mostrar_menu()
