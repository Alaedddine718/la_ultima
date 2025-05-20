from src.config import cargar_config

def crear_nft_repo():
    config = cargar_config()
    tipo = config.get("base_datos")

    if tipo == "mongo":
        from src.repositories.mongo.nft_repo_mongo import NFTRepositoryMongo
        return NFTRepositoryMongo(config["mongo_uri"])

    elif tipo == "firebase":
        from src.repositories.firebase.nft_repo import NFTRepositoryFirebase
        return NFTRepositoryFirebase(config["firebase_key"])

    elif tipo == "neo4j":
        from src.repositories.neo4j.nft_repo import NFTRepositoryNeo4j
        return NFTRepositoryNeo4j(
            config["neo4j_uri"],
            config["neo4j_user"],
            config["neo4j_password"]
        )

    else:
        raise Exception("Tipo de base de datos no soportado: " + tipo)

