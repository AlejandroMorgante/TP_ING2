import os
import time

def ejecutar_sql():
    os.system("poetry run python review_sql.py")

def ejecutar_mongo():
    os.system("poetry run python review_mongo.py")

def ejecutar_neo4j():
    os.system("poetry run python review_neo4j.py")

def caso_uso_1():
    os.system("poetry run python -c \"from review_mongo import reservas_diarias_por_destino; reservas_diarias_por_destino()\"")

def caso_uso_2():
    os.system("poetry run python -c \"from review_mongo import tipos_alojamiento_mas_solicitados; tipos_alojamiento_mas_solicitados()\"")

def caso_uso_3():
    fecha = input("Ingresá la fecha desde la cual contar (formato yyyy-mm-dd): ")
    os.system(f'poetry run python -c "from review_mongo import contar_propiedades_desde_fecha; contar_propiedades_desde_fecha(\'{fecha}\')"')

def caso_uso_6():
    os.system("poetry run python -c \"from review_mongo import consulta_alojamientos_baratos_o_centrico; consulta_alojamientos_baratos_o_centrico()\"")

def mostrar_menu():
    while True:
        print("\n===== MENÚ DE CASOS DE USO =====")
        print("1. Ver datos en MySQL")
        print("2. Ver datos en MongoDB")
        print("3. Ver datos en Neo4j")
        print("4. CU1 - Cuántas reservas se realizan diariamente por destino")
        print("5. CU2 - Qué tipos de alojamientos son más solicitados por los usuarios")
        print("6. CU3 - Cuántas propiedades han sido agregadas recientemente a la plataforma")
        print("7. CU6 - ¿Qué tipos de alojamiento tienen precios por noche < 100 o están ubicados en zonas céntricas")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ejecutar_sql()
        elif opcion == "2":
            ejecutar_mongo()
        elif opcion == "3":
            ejecutar_neo4j()
        elif opcion == "4":
            caso_uso_1()
        elif opcion == "5":
            caso_uso_2()
        elif opcion == "6":
            caso_uso_3()
        elif opcion == "7":
            caso_uso_6()
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

        time.sleep(2)

if __name__ == "__main__":
    mostrar_menu()
