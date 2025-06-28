

import pymysql

def explorar_mysql():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="tpdb",
        port=3306
    )

    with conn.cursor() as cursor:
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        print("Tablas en MySQL:", tables)

        for (table_name,) in tables:
            print(f"\nContenido de {table_name}:")
            cursor.execute(f"SELECT * FROM {table_name} LIMIT 5;")
            for row in cursor.fetchall():
                print(row)

    conn.close()

if __name__ == "__main__":
    explorar_mysql()