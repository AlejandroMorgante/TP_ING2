import pymysql
import argparse

def conectar():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="tpdb",
        port=3306
    )

def caso_1():
    conn = conectar()
    with conn.cursor() as cursor:
        print("\nReservas diarias por destino:")
        cursor.execute("""
            SELECT fecha_creacion, destino, COUNT(*)
            FROM reservas
            GROUP BY fecha_creacion, destino
            ORDER BY fecha_creacion;
        """)
        for row in cursor.fetchall():
            print(row)
    conn.close()

def caso_2():
    conn = conectar()
    with conn.cursor() as cursor:
        print("\nTipos de alojamiento más solicitados:")
        cursor.execute("""
            SELECT tipo_habitacion, COUNT(*)
            FROM reservas
            GROUP BY tipo_habitacion
            ORDER BY COUNT(*) DESC;
        """)
        for row in cursor.fetchall():
            print(row)
    conn.close()

def caso_3():
    conn = conectar()
    with conn.cursor() as cursor:
        print("\nPropiedades agregadas recientemente:")
        cursor.execute("""
            SELECT nombre, fecha_agregado
            FROM propiedades
            WHERE fecha_agregado >= DATE_SUB(NOW(), INTERVAL 30 DAY);
        """)
        for row in cursor.fetchall():
            print(row)
    conn.close()

def caso_4():
    conn = conectar()
    with conn.cursor() as cursor:
        print("\nÁreas más demandadas:")
        cursor.execute("""
            SELECT zona, COUNT(*)
            FROM reservas
            GROUP BY zona
            ORDER BY COUNT(*) DESC;
        """)
        for row in cursor.fetchall():
            print(row)
    conn.close()

def caso_6():
    conn = conectar()
    with conn.cursor() as cursor:
        print("\nAlojamientos < $100 o en zona céntrica:")
        cursor.execute("""
            SELECT nombre, precio, zona
            FROM propiedades
            WHERE precio < 100 OR zona = 'centro';
        """)
        for row in cursor.fetchall():
            print(row)
    conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--caso", type=str)
    args = parser.parse_args()

    if args.caso == "1":
        caso_1()
    elif args.caso == "2":
        caso_2()
    elif args.caso == "3":
        caso_3()
    elif args.caso == "4":
        caso_4()
    elif args.caso == "6":
        caso_6()
    else:
        print("Caso no reconocido.")
