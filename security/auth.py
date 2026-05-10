import bcrypt

from database.connection import get_db

db = get_db()

usuarios = db["usuarios"]


def hash_password(password):

    return bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )


def verify_password(password, hashed):

    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed
    )


def crear_admin():

    existe = usuarios.find_one({
        "case": "ADMIN001"
    })

    if not existe:

        usuarios.insert_one({

            "nombre": "Administrador",

            "case": "ADMIN001",

            "password": hash_password("admin123"),

            "rol": "admin"
        })

        print("Administrador creado")


def login():

    print("\n===== LOGIN =====")

    case = input("Ingrese CASE: ")

    password = input("Ingrese contraseña: ")

    usuario = usuarios.find_one({
        "case": case
    })

    if usuario:

        if verify_password(password, usuario["password"]):

            print(f"\nBienvenido {usuario['nombre']}")

            return usuario

    print("Credenciales incorrectas")

    return None