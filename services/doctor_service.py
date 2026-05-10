from bson.objectid import ObjectId

from database.connection import get_db

db = get_db()

doctores = db["doctores"]


def listar_doctores():

    print("\n===== DOCTORES =====")

    for doctor in doctores.find():

        print(f"ID: {doctor['_id']}")
        print(f"Nombre: {doctor['nombre']}")
        print(f"Especialidad: {doctor['especialidad']}")
        print(f"Telefono: {doctor['telefono']}")
        print("--------------------------")


def agregar_doctor():

    nombre = input("Nombre: ")

    especialidad = input("Especialidad: ")

    telefono = input("Telefono: ")

    doctores.insert_one({

        "nombre": nombre,

        "especialidad": especialidad,

        "telefono": telefono
    })

    print("Doctor agregado correctamente")


def actualizar_doctor():

    listar_doctores()

    doctor_id = input("Ingrese ID del doctor: ")

    nombre = input("Nuevo nombre: ")

    especialidad = input("Nueva especialidad: ")

    telefono = input("Nuevo telefono: ")

    doctores.update_one(

        {"_id": ObjectId(doctor_id)},

        {
            "$set": {

                "nombre": nombre,

                "especialidad": especialidad,

                "telefono": telefono
            }
        }
    )

    print("Doctor actualizado")


def eliminar_doctor():

    listar_doctores()

    doctor_id = input("Ingrese ID del doctor a eliminar: ")

    doctores.delete_one({
        "_id": ObjectId(doctor_id)
    })

    print("Doctor eliminado")