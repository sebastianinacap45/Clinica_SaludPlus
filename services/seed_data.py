from database.connection import get_db
from security.auth import hash_password

db = get_db()


def insertar_datos():

    
    # DOCTORES
    

    doctores_existentes = db.doctores.count_documents({})

    if doctores_existentes == 0:

        db.doctores.insert_many([

            {
                "nombre": "Dr. Carlos Perez",
                "especialidad": "Cardiologia",
                "telefono": "+56911111111"
            },

            {
                "nombre": "Dra. Ana Lopez",
                "especialidad": "Pediatria",
                "telefono": "+56922222222"
            },

            {
                "nombre": "Dr. Felipe Rojas",
                "especialidad": "Neurologia",
                "telefono": "+56933333333"
            },

            {
                "nombre": "Dra. Camila Torres",
                "especialidad": "Dermatologia",
                "telefono": "+56944444444"
            },

            {
                "nombre": "Dr. Diego Soto",
                "especialidad": "Traumatologia",
                "telefono": "+56955555555"
            }
        ])

        print("Doctores insertados")


    
    # PACIENTES
    

    pacientes_existentes = db.pacientes.count_documents({})

    if pacientes_existentes == 0:

        db.pacientes.insert_many([

            {
                "nombre": "Juan Gonzalez",
                "rut": "11.111.111-1",
                "edad": 30,
                "diagnostico": "Hipertension"
            },

            {
                "nombre": "Maria Fernandez",
                "rut": "22.222.222-2",
                "edad": 25,
                "diagnostico": "Diabetes"
            },

            {
                "nombre": "Pedro Ramirez",
                "rut": "33.333.333-3",
                "edad": 40,
                "diagnostico": "Migraña"
            },

            {
                "nombre": "Sofia Morales",
                "rut": "44.444.444-4",
                "edad": 35,
                "diagnostico": "Dermatitis"
            },

            {
                "nombre": "Lucas Herrera",
                "rut": "55.555.555-5",
                "edad": 50,
                "diagnostico": "Artritis"
            }
        ])

        print("Pacientes insertados")


    
    # CITAS
    

    citas_existentes = db.citas.count_documents({})

    if citas_existentes == 0:

        db.citas.insert_many([

            {
                "paciente": "Juan Gonzalez",
                "doctor": "Dr. Carlos Perez",
                "fecha": "2026-05-10",
                "hora": "09:00"
            },

            {
                "paciente": "Maria Fernandez",
                "doctor": "Dra. Ana Lopez",
                "fecha": "2026-05-11",
                "hora": "10:00"
            },

            {
                "paciente": "Pedro Ramirez",
                "doctor": "Dr. Felipe Rojas",
                "fecha": "2026-05-12",
                "hora": "11:00"
            },

            {
                "paciente": "Sofia Morales",
                "doctor": "Dra. Camila Torres",
                "fecha": "2026-05-13",
                "hora": "12:00"
            },

            {
                "paciente": "Lucas Herrera",
                "doctor": "Dr. Diego Soto",
                "fecha": "2026-05-14",
                "hora": "13:00"
            }
        ])

        print("Citas insertadas")


    
    # USUARIOS
    

    usuarios = [

        {
            "nombre": "Administrador",
            "case": "ADMIN001",
            "password": hash_password("admin123"),
            "rol": "admin"
        },

        {
            "nombre": "Secretaria",
            "case": "SECRE001",
            "password": hash_password("secret123"),
            "rol": "secretaria"
        },

        {
            "nombre": "Doctor",
            "case": "DOC001",
            "password": hash_password("doctor123"),
            "rol": "doctor"
        },

        {
            "nombre": "Supervisor",
            "case": "SUPER001",
            "password": hash_password("super123"),
            "rol": "supervisor"
        },

        {
            "nombre": "Recepcion",
            "case": "RECEP001",
            "password": hash_password("recep123"),
            "rol": "recepcion"
        }
    ]

    for usuario in usuarios:

        existe = db.usuarios.find_one({
            "case": usuario["case"]
        })

        if not existe:

            db.usuarios.insert_one(usuario)

            print(f"Usuario {usuario['case']} insertado")

    print("Datos insertados correctamente")