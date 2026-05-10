
def tiene_permiso(rol, opcion):

    permisos = {

        "admin": [

            "1", "2", "3", "4",
            "5", "6", "7", "8",
            "9", "10", "11", "12",
            "13", "14", "15"
        ],

        "secretaria": [

            "1",
            "5", "6", "7", "8",
            "9", "10", "11", "12",
            "15"
        ],

        "doctor": [

            "5",
            "9",
            "15"
        ],

        "supervisor": [

            "1",
            "5",
            "9",
            "15"
        ],

        "recepcion": [

            "1",
            "5",
            "6",
            "9",
            "10",
            "15"
        ]
    }

    return opcion in permisos.get(rol, [])