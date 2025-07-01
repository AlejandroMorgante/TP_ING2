from neo4j import GraphDatabase
import argparse

def explorar_neo4j():
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

    with driver.session() as session:
        print("Resumen de nodos:")
        result = session.run("MATCH (n) RETURN labels(n) AS tipo, count(*) AS cantidad")
        for row in result:
            print(f"{row['tipo']}: {row['cantidad']}")

        print("\nResumen de relaciones:")
        result = session.run("MATCH ()-[r]->() RETURN type(r) AS tipo, count(*) AS cantidad")
        for row in result:
            print(f"{row['tipo']}: {row['cantidad']}")

    driver.close()

#Caso de Uso 5 - Reservas realizadas en destinos tropicales y con más de 4 estrellas
def reservas_tropicales_cuatro_estrellas():
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))
    
    with driver.session() as session:
        
        print("\nReservas en destinos tropicales con más de 4 estrellas:")
        
        query = """
        MATCH (r:Reserva)-[:INCLUYE_HOTEL]->(h:Hotel)-[:UBICADO_EN]->(c:Ciudad)
        WHERE h.estrellas > 4 AND c.tropical = true
        RETURN r.id AS reserva_id, h.nombre AS hotel, h.estrellas AS estrellas, c.nombre AS ciudad;
        """
        result = session.run(query)
        
        for row in result:
            print(f"- Reserva {row['reserva_id']} | Hotel: {row['hotel']} ({row['estrellas']}) | Ciudad: {row['ciudad']}")
    
    driver.close()


if __name__ == "__main__":
    explorar_neo4j()