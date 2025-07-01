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

def tipos_alojamiento_mas_solicitados():
    client = MongoClient("mongodb://localhost:27017")
    db = client["test"]

    print("\nTipos de alojamiento más solicitados:")

    pipeline = [
        {
            "$project": {
                "tipo_habitacion": {
                    "$ifNull": ["$paquete.hotel.tipo_habitacion", "$hotel.tipo_habitacion"]
                }
            }
        },
        {
            "$group": {
                "_id": "$tipo_habitacion",
                "total": { "$sum": 1 }
            }
        },
        { "$sort": { "total": -1 } }
    ]

    resultados = db.reservas.aggregate(pipeline)

    for doc in resultados:
        tipo = doc["_id"]
        total = doc["total"]
        print(f"- {tipo}: {total} reservas")


    client.close()


def contar_propiedades_desde_fecha(fecha_str):
    from datetime import datetime
    import pytz

    try:
        fecha_iso = datetime.strptime(fecha_str, "%Y-%m-%d").replace(tzinfo=pytz.UTC)
    except ValueError:
        print("Formato de fecha inválido. Usá 'yyyy-mm-dd'.")
        return

    client = MongoClient("mongodb://localhost:27017")
    db = client["test"]

    count = db.propiedades.count_documents({
        "fechaAlta": { "$gte": fecha_iso }
    })

    print(f"\nCantidad de propiedades con fechaAlta desde {fecha_str}: {count}")

    client.close()

if __name__ == "__main__":
    explorar_mongo()
    consulta_alojamientos_baratos_o_centrico()
    contar_propiedades_desde_fecha("2025-06-01")
