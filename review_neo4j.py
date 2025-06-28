

from neo4j import GraphDatabase

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

if __name__ == "__main__":
    explorar_neo4j()