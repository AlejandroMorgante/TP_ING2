from pymongo import MongoClient
from datetime import datetime, timedelta
import argparse

def caso_1():
    client = MongoClient("mongodb://localhost:27017")
    db = client["test"]
    pipeline = [
        {"$group": {
            "_id": {"fecha": "$fecha_creacion", "destino": "$vuelo.destino"},
            "total": {"$sum": 1}
        }},
        {"$sort": {"_id.fecha": 1}}
    ]
    print("\nReservas diarias por destino:")
    for doc in db.reservas.aggregate(pipeline):
        print(f"{doc['_id']['fecha']} - {doc['_id']['destino']}: {doc['total']}")
    client.close()

def caso_2():
    client = MongoClient("mongodb://localhost:27017")
    db = client["test"]
    pipeline = [
        {"$project": {
            "tipo_habitacion": {
                "$ifNull": ["$paquete.hotel.tipo_habitacion", "$hotel.tipo_habitacion"]
            }}},
        {"$group": {
            "_id": "$tipo_habitacion",
            "total": {"$sum": 1}}},
        {"$sort": {"total": -1}}
    ]
    print("\nTipos de alojamiento más solicitados:")
    for doc in db.reservas.aggregate(pipeline):
        print(f"{doc['_id']}: {doc['total']}")
    client.close()

def caso_3():
    client = MongoClient("mongodb://localhost:27017")
    db = client["test"]
    hace_30_dias = datetime.utcnow() - timedelta(days=30)
    resultados = db.propiedades.find({"fecha_agregado": {"$gte": hace_30_dias}})
    print("\nPropiedades agregadas recientemente:")
    for doc in resultados:
        print(f"{doc.get('nombre', 'Sin nombre')} - {doc.get('fecha_agregado')}")
    client.close()

def caso_4():
    client = MongoClient("mongodb://localhost:27017")
    db = client["test"]
    pipeline = [
        {"$group": {"_id": "$hotel.zona", "total": {"$sum": 1}}},
        {"$sort": {"total": -1}}
    ]
    print("\nÁreas más demandadas:")
    for doc in db.reservas.aggregate(pipeline):
        print(f"{doc['_id']}: {doc['total']}")
    client.close()

def caso_6():
    client = MongoClient("mongodb://localhost:27017")
    db = client["test"]
    filtro = {
        "$or": [
            {"precio": {"$lt": 100}},
            {"zona": "centro"}
        ]
    }
    print("\nAlojamientos < $100 o en zona céntrica:")
    for doc in db.propiedades.find(filtro):
        print(f"{doc.get('nombre')} - ${doc.get('precio')} - Zona: {doc.get('zona')}")
    client.close()

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
