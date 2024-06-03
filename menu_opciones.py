from usuarioDAO import UsuarioDAO
from usuario import Usuario
from logger_base import log

opcion = None
while opcion != 5:
    try:
        print("Elija una opcion (1-5):")
        print("1 - Listar usuarios")
        print("2 - Agregar usuario")
        print("3 - Modificar usuario")
        print("4 - Eliminar usuario")
        print("5 - Salir")
        opcion = int(input("Escribe tu opcion entre 1 y 5: "))

        if opcion == 1:
            usuarios = UsuarioDAO.seleccionar()
            for usuario in usuarios:
                log.info(usuario)

        elif opcion == 2:
            username_usuario = input("escribe tu username: ")
            password_usuario = input("escribe tu password: ")
            usuario1 = Usuario(username=username_usuario, password=password_usuario)
            usuarios_insertados = UsuarioDAO.insertar(usuario1)
            log.info(f'Usuarios insertados {usuarios_insertados}')


        elif opcion == 3:
            id_usuario = input("escribe el id del usuario a modificar: ")
            username_usuario = input("escribe el username: ")
            password_usuario = input("escribe el password: ")
            usuario2 = Usuario(id_usuario, username_usuario, password_usuario)
            usuarios_actualizados = UsuarioDAO.actualizar(usuario2)
            log.info(f'Usuarios actualizados: {usuarios_actualizados}')

        elif opcion == 4:
            id_usuario = int(input("escribe el id del usuario a eliminar: "))
            usuario3 = Usuario(id_usuario=id_usuario)
            usuarios_eliminados = UsuarioDAO.eliminar(usuario3)
            log.info(f'Usuarios eliminados: {usuarios_eliminados}')

        elif opcion == 5:
            print("Salimos del programa")
            exit()

        else:
            print("Opcion erronea, elegir una opcion entre 1 y 5")


    except Exception as e:
        print(f'Error {e}, escriba una opcion valida')
        opcion = None

else:
    print("Salimos del programa")
