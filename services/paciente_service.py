from bson.objectid import ObjectId

from database.connection import get_db

db = get_db()

pacientes = db["pacientes"]


def listar_pacientes():

    print("\n===== PACIENTES =====")

    for paciente in pacientes.find():

        print(f"ID: {paciente['_id']}")
        print(f"Nombre: {paciente['nombre']}")
        print(f"Rut: {paciente['rut']}")
        print(f"Edad: {paciente['edad']}")
        print(f"Diagnostico: {paciente['diagnostico']}")
        print("--------------------------")


def agregar_paciente():

    nombre = input("Nombre: ")

    rut = input("Rut: ")

    edad = int(input("Edad: "))

    diagnostico = input("Diagnostico: ")

    pacientes.insert_one({

        "nombre": nombre,

        "rut": rut,

        "edad": edad,

        "diagnostico": diagnostico
    })

    print("Paciente agregado")


def actualizar_paciente():

    listar_pacientes()

    paciente_id = input("Ingrese ID del paciente: ")

    nombre = input("Nuevo nombre: ")

    rut = input("Nuevo rut: ")

    edad = int(input("Nueva edad: "))

    diagnostico = input("Nuevo diagnostico: ")

    pacientes.update_one(

        {"_id": ObjectId(paciente_id)},

        {
            "$set": {

                "nombre": nombre,

                "rut": rut,

                "edad": edad,

                "diagnostico": diagnostico
            }
        }
    )

    print("Paciente actualizado")


def eliminar_paciente():

    listar_pacientes()

    paciente_id = input("Ingrese ID del paciente: ")

    pacientes.delete_one({
        "_id": ObjectId(paciente_id)
    })

    print("Paciente eliminado")