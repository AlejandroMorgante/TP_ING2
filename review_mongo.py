from pymongo import MongoClient

def explorar_mongo():
    client = MongoClient("mongodb://localhost:27017")
    db = client["test"] 

    print("Colecciones en MongoDB:")
    for collection_name in db.list_collection_names():
        print(f"- {collection_name}")

        print("  Documentos:")
        for doc in db[collection_name].find().limit(5):
            print(f"    {doc}")

    client.close()

def consulta_alojamientos_baratos_o_centrico():
    client = MongoClient("mongodb://localhost:27017")
    db = client["test"]

    print("\nConsulta: Tipos de alojamiento con precio < 100 o en zona céntrica")

    # Suponiendo que los alojamientos están en la colección "alojamientos"
    resultados = db.alojamientos.find({
        "$or": [
            {"precio_por_noche": {"$lt": 100}},
            {"zona": "centrica"}
        ]
    })

    for doc in resultados:
        tipo = doc.get("tipo", "Desconocido")
        precio = doc.get("precio_por_noche", "N/A")
        zona = doc.get("zona", "N/A")
        print(f"- Tipo: {tipo} | Precio: {precio} | Zona: {zona}")

    client.close()

if __name__ == "__main__":
    explorar_mongo()
    consulta_alojamientos_baratos_o_centrico()
