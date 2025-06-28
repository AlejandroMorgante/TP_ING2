


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

if __name__ == "__main__":
    explorar_mongo()