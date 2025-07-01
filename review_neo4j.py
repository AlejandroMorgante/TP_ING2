from neo4j import GraphDatabase
import argparse

def caso_5():
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))
    with driver.session() as session:
        print("\nReservas en destinos tropicales con más de 4 estrellas:")
        query = """
        MATCH (r:Reserva)-[:INCLUYE_HOTEL]->(h:Hotel)-[:UBICADO_EN]->(c:Ciudad)
        WHERE h.estrellas > 4 AND c.tropical = true
        RETURN h.nombre AS hotel, count(DISTINCT r) AS reservas
        ORDER BY reservas DESC
        """
        result = session.run(query)
        for row in result:
            print(f"{row['hotel']}: {row['reservas']} reservas")
    driver.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--caso", type=str)
    args = parser.parse_args()

    if args.caso == "5":
        caso_5()
    else:
        print("Caso no reconocido.")
