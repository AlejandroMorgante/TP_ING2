# init_sql.py

import pymysql

DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "root",
    "database": "tpdb"
}

def ejecutar_init_sql():
    with open("init/mysql/init.sql", "r", encoding="utf-8") as f:
        script = f.read()

    conn = pymysql.connect(**DB_CONFIG)
    conn.autocommit(True)

    with conn.cursor() as cursor:
        for statement in script.split(";"):
            stmt = statement.strip()
            if stmt:
                try:
                    cursor.execute(stmt)
                except pymysql.err.ProgrammingError as e:
                    print(f"Error en sentencia:\n{stmt}\n→ {e}")
    conn.close()
    print("Script SQL ejecutado correctamente.")

if __name__ == "__main__":
    ejecutar_init_sql()
