from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

with open("init/neo4j/init.cypher", "r", encoding="utf-8") as file:
    cypher_script = file.read()

# Ejecutar los comandos
def run_script(tx, script):
    for statement in script.split(";"):
        stmt = statement.strip()
        if stmt:
            tx.run(stmt)

with driver.session() as session:
    session.execute_write(run_script, cypher_script)

driver.close()
print("Script Cypher ejecutado correctamente.")