import os
import json

from bson import json_util

from database.connection import get_db

db = get_db()

COLLECTIONS = [
    "doctores",
    "pacientes",
    "citas",
    "usuarios"
]


def realizar_backup():

    if not os.path.exists("backups"):

        os.makedirs("backups")

    for collection_name in COLLECTIONS:

        datos = list(
            db[collection_name].find()
        )

        with open(
            f"backups/{collection_name}.json",
            "w",
            encoding="utf-8"
        ) as archivo:

            json.dump(
                datos,
                archivo,
                indent=4,
                default=json_util.default
            )

    print("Backup realizado correctamente")


def restaurar_backup():

    for collection_name in COLLECTIONS:

        ruta = f"backups/{collection_name}.json"

        if os.path.exists(ruta):

            with open(
                ruta,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(
                    archivo,
                    object_hook=json_util.object_hook
                )

            db[collection_name].delete_many({})

            if datos:

                db[collection_name].insert_many(datos)

    print("Restauracion completada")