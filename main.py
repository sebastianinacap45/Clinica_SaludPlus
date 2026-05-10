from colorama import init, Fore, Style

from security.auth import (
    login,
    crear_admin
)

from services.seed_data import insertar_datos

from services.permiso_service import tiene_permiso

from services.doctor_service import (
    listar_doctores,
    agregar_doctor,
    actualizar_doctor,
    eliminar_doctor
)

from services.paciente_service import (
    listar_pacientes,
    agregar_paciente,
    actualizar_paciente,
    eliminar_paciente
)

from services.cita_service import (
    listar_citas,
    agregar_cita,
    actualizar_cita,
    eliminar_cita
)

from backup_restore import (
    realizar_backup,
    restaurar_backup
)


# INICIAR COLORAMA


init(autoreset=True)


# COLORES SUAVES


ADMIN_COLOR = Fore.LIGHTRED_EX
DOCTOR_COLOR = Fore.LIGHTCYAN_EX
SECRETARIA_COLOR = Fore.LIGHTGREEN_EX
SUPERVISOR_COLOR = Fore.LIGHTYELLOW_EX
RECEPCION_COLOR = Fore.LIGHTMAGENTA_EX
INFO_COLOR = Fore.LIGHTWHITE_EX
ERROR_COLOR = Fore.LIGHTRED_EX


# INICIO SISTEMA


crear_admin()

insertar_datos()

usuario = login()


# LOGIN EXITOSO


if usuario:

    rol_usuario = usuario["rol"]

    print(INFO_COLOR + f"\nROL ACTIVO: {rol_usuario.upper()}")

    
    # MENU PRINCIPAL
    

    while True:

        
        # MENU ADMIN
        

        if rol_usuario == "admin":

            print(ADMIN_COLOR + """

=========================== PANEL ADMINISTRADOR ===========================

[1] Listar Doctores   [2] Agregar Doctor   [3] Actualizar Doctor   [4] Eliminar Doctor

[5] Listar Pacientes  [6] Agregar Paciente [7] Actualizar Paciente [8] Eliminar Paciente

[9] Listar Citas      [10] Agregar Cita    [11] Actualizar Cita    [12] Eliminar Cita

[13] Realizar Backup  [14] Restaurar Backup  [15] Salir

========================================================================

""" + Style.RESET_ALL)

        
        # MENU DOCTOR
        

        elif rol_usuario == "doctor":

            print(DOCTOR_COLOR + """

=============================== PANEL DOCTOR ===============================

[5] Listar Pacientes

[9] Listar Citas

[15] Salir

===========================================================================

""" + Style.RESET_ALL)

        
        # MENU SECRETARIA
        

        elif rol_usuario == "secretaria":

            print(SECRETARIA_COLOR + """

============================= PANEL SECRETARIA =============================

[1] Listar Doctores

[5] Listar Pacientes   [6] Agregar Paciente   [7] Actualizar Paciente

[9] Listar Citas       [10] Agregar Cita      [11] Actualizar Cita

[15] Salir

===========================================================================

""" + Style.RESET_ALL)

        
        # MENU SUPERVISOR
        

        elif rol_usuario == "supervisor":

            print(SUPERVISOR_COLOR + """

============================= PANEL SUPERVISOR =============================

[1] Listar Doctores

[5] Listar Pacientes

[9] Listar Citas

[15] Salir

===========================================================================

""" + Style.RESET_ALL)

        
        # MENU RECEPCION
        

        elif rol_usuario == "recepcion":

            print(RECEPCION_COLOR + """

============================= PANEL RECEPCION ==============================

[1] Listar Doctores

[5] Listar Pacientes   [6] Agregar Paciente

[9] Listar Citas       [10] Agregar Cita

[15] Salir

===========================================================================

""" + Style.RESET_ALL)

        opcion = input(INFO_COLOR + "Seleccione opcion: ")

        
        # VALIDACION DE PERMISOS
        

        if not tiene_permiso(rol_usuario, opcion):

            print(ERROR_COLOR + "No tiene permisos para esta opcion")

            continue

        
        # DOCTORES
        

        if opcion == "1":

            listar_doctores()

        elif opcion == "2":

            agregar_doctor()

        elif opcion == "3":

            actualizar_doctor()

        elif opcion == "4":

            eliminar_doctor()

        
        # PACIENTES
        

        elif opcion == "5":

            listar_pacientes()

        elif opcion == "6":

            agregar_paciente()

        elif opcion == "7":

            actualizar_paciente()

        elif opcion == "8":

            eliminar_paciente()

        
        # CITAS
        

        elif opcion == "9":

            listar_citas()

        elif opcion == "10":

            agregar_cita()

        elif opcion == "11":

            actualizar_cita()

        elif opcion == "12":

            eliminar_cita()

        
        # BACKUP
        

        elif opcion == "13":

            realizar_backup()

        elif opcion == "14":

            restaurar_backup()

        
        # SALIR
        

        elif opcion == "15":

            print(INFO_COLOR + "Saliendo del sistema")

            break

        else:

            print(ERROR_COLOR + "Opcion invalida")