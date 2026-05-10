from bson.objectid import ObjectId

from database.connection import get_db

db = get_db()

citas = db["citas"]


def listar_citas():

    print("\n===== CITAS =====")

    for cita in citas.find():

        print(f"ID: {cita['_id']}")
        print(f"Paciente: {cita['paciente']}")
        print(f"Doctor: {cita['doctor']}")
        print(f"Fecha: {cita['fecha']}")
        print(f"Hora: {cita['hora']}")
        print("--------------------------")


def agregar_cita():

    paciente = input("Paciente: ")

    doctor = input("Doctor: ")

    fecha = input("Fecha: ")

    hora = input("Hora: ")

    citas.insert_one({

        "paciente": paciente,

        "doctor": doctor,

        "fecha": fecha,

        "hora": hora
    })

    print("Cita registrada")


def actualizar_cita():

    listar_citas()

    cita_id = input("Ingrese ID de la cita: ")

    paciente = input("Nuevo paciente: ")

    doctor = input("Nuevo doctor: ")

    fecha = input("Nueva fecha: ")

    hora = input("Nueva hora: ")

    citas.update_one(

        {"_id": ObjectId(cita_id)},

        {
            "$set": {

                "paciente": paciente,

                "doctor": doctor,

                "fecha": fecha,

                "hora": hora
            }
        }
    )

    print("Cita actualizada")


def eliminar_cita():

    listar_citas()

    cita_id = input("Ingrese ID de la cita: ")

    citas.delete_one({
        "_id": ObjectId(cita_id)
    })

    print("Cita eliminada")