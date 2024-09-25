#pantalla_principal.py
import os
import ast

from libros import Libro
from termcolor import colored
from pantalla_registro import mostrar_pantalla_registro

os.system('color')

with open("libros.txt", "r", encoding="utf-8") as archivo:
    libros = archivo.readlines()
for linea in libros:
    t, c, f, a= linea.split(",", 3)
    libro = Libro(t, c, f, a)


def mostrar_pantalla_principal(usuario):

    if os.path.exists("flag.txt"):
        os.remove("flag.txt")
    if not os.path.exists("flag.txt"):
        with open("flag.txt", "w", encoding="utf-8") as archivo:
            if usuario.libro_actual is None:
                if usuario.ultimo_autor_leido is None:
                    archivo.write(f"{usuario.usuario}|{usuario.contraseña}|{usuario.tipo_usuario}|{usuario.libro_actual}|None|{usuario.historial}|None")
                else:
                    archivo.write(f"{usuario.usuario}|{usuario.contraseña}|{usuario.tipo_usuario}|{usuario.libro_actual}|{usuario.ultimo_autor_leido.strip()}|{usuario.historial}|None")
            else:
                archivo.write(f"{usuario.usuario}|{usuario.contraseña}|{usuario.tipo_usuario}|{usuario.libro_actual}|{usuario.ultimo_autor_leido.strip()}|{usuario.historial}|{usuario.libro_actual.id}")

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored("Bienvenido,", "green"), colored(usuario.usuario, "cyan"))
        if usuario.libro_actual == None:
            print(colored(f"Estado: En este momento, a usted no se le ha sido prestado ningún libro\n", "green"))
        else:
            print(colored(f"Estado: En este momento, a usted se le ha sido prestado:", "green"), colored(f"{usuario.libro_actual.titulo}", "red"), colored(", de", "green"), colored(f"{usuario.ultimo_autor_leido}", "red"))
        print(colored("¿Qué desea hacer?", "yellow"))
        print(colored("1. Ver mi historial de lectura", "yellow"))
        print(colored("2. Buscar y pedir libros", "yellow"))
        print(colored("3. Devolver libro", "yellow"))
        print(colored("4. Cerrar sesión", "yellow"))
        print(colored("5. Salir y guardar sesión", "yellow"))
        print(colored("6. Salir y cerrar sesión", "yellow"))
        opcion = input(colored("Opción: ", "yellow"))

        match opcion:
            case "1":
                ver_historial(usuario)
            case "2":
                buscar_libros(usuario)
            case "3":
                temp = usuario.historial
                if temp is None and usuario.libro_actual is not None:
                    usuario.historial = []
                if temp is not None:
                    print(usuario.historial)
                    usuario.historial = ast.literal_eval(str(usuario.historial))
                if usuario.libro_actual is None:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(colored("Bienvenido,", "green"), colored(usuario.usuario, "cyan"))
                    print(colored("Error: Usted no tiene ningún pendiente", "red"))
                    input(colored("Presiona ENTER para continuar...", "red"))
                    mostrar_pantalla_principal(usuario)
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    usuario.historial.append(usuario.libro_actual.id)
                    print(colored("Bienvenido,", "green"), colored(usuario.usuario, "cyan"))
                    print(colored("El libro ha sido devuelto exitosamente", "green"))
                    input(colored("Presiona ENTER para continuar...", "green"))
                usuario.libro_actual = None
                os.system('cls' if os.name == 'nt' else 'clear')
                mostrar_pantalla_principal(usuario)
            case "4":
                reemplazar_linea_usuario_con_flag("usuarios.txt", "flag.txt", usuario.usuario)
                if os.path.exists("flag.txt"):
                    os.remove("flag.txt")
                    return
            case "5":
                exit()
            case "6":
                reemplazar_linea_usuario_con_flag("usuarios.txt", "flag.txt", usuario.usuario)
                if os.path.exists("flag.txt"):
                    os.remove("flag.txt")
                exit()
            case _:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(colored("Bienvenido,", "green"), colored(usuario.usuario, "cyan"))
                print(colored("Error: Por favor, ingrese solo una de las opciones del menú", "red"))
                input(colored("Presiona ENTER para continuar...", "red"))

def buscar_libros(usuario):
    while True:
        if usuario.libro_actual is not None:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(colored("Bienvenido,", "green"), colored(usuario.usuario, "cyan"))
            print(colored("Error: Por favor, devuelva el libro actual antes de pedir otro", "red"))
            input(colored("Presiona ENTER para continuar...", "red"))
            mostrar_pantalla_principal(usuario)
        break

    libros_target = []
    libros_adicionales = []

    match usuario.tipo_usuario:
        case "lector_estudiante":
            for libro in Libro.libros:
                if libro.categoria in ["Educacion", "Tecnologia"]:
                    libros_target.append(libro)
                else:
                    libros_adicionales.append(libro)

            if usuario.ultimo_autor_leido:
                libros_ultimo_autor = [libro for libro in libros_target if libro.autor == usuario.ultimo_autor_leido]
                libros_otro_autor = [libro for libro in libros_target if libro.autor != usuario.ultimo_autor_leido]
            else:
                libros_ultimo_autor = []
                libros_otro_autor = libros_target

            libros_ultimo_autor.sort(key=lambda x: x.fecha, reverse=True)
            libros_otro_autor.sort(key=lambda x: x.fecha, reverse=True)

            libros_recomendados = libros_ultimo_autor + libros_otro_autor
            libros_recomendados += libros_adicionales
            mostrar_libros_paginados(libros_recomendados, usuario)

        case "lector_historia":
            libros_target = []
            libros_adicionales = []
            for libro in Libro.libros:
                if libro.categoria in ["Historia", "Humanidades"]:
                    libros_target.append(libro)
                else:
                    libros_adicionales.append(libro)

            if usuario.ultimo_autor_leido:
                libros_ultimo_autor = [libro for libro in libros_target if libro.autor == usuario.ultimo_autor_leido]
                libros_otro_autor = [libro for libro in libros_target if libro.autor != usuario.ultimo_autor_leido]
            else:
                libros_ultimo_autor = []
                libros_otro_autor = libros_target

            libros_ultimo_autor.sort(key=lambda x: x.fecha)
            libros_otro_autor.sort(key=lambda x: x.fecha)

            libros_recomendados = libros_ultimo_autor + libros_otro_autor + libros_adicionales
            mostrar_libros_paginados(libros_recomendados, usuario)

        case "lector_investigador":
            libros_target = []
            libros_adicionales = []
            for libro in Libro.libros:
                if libro.categoria in ["Divulgacion", "Tecnologia"]:
                    libros_target.append(libro)
                else:
                    libros_adicionales.append(libro)

            libros_target.sort(key=lambda x: x.fecha, reverse=True)

            libros_recomendados = libros_target + libros_adicionales
            mostrar_libros_paginados(libros_recomendados, usuario)

        case "lector_habitual":
            libros_target = []
            libros_adicionales = []
            for libro in Libro.libros:
                if libro.categoria in ["Literatura", "Tecnologia", "Historia", "Humanidades", "Cocina"]:
                    libros_target.append(libro)
                else:
                    libros_adicionales.append(libro)

            if usuario.ultimo_autor_leido:
                libros_ultimo_autor = [libro for libro in libros_target if libro.autor == usuario.ultimo_autor_leido]
                libros_otro_autor = [libro for libro in libros_target if libro.autor != usuario.ultimo_autor_leido]
            else:
                libros_ultimo_autor = []
                libros_otro_autor = libros_target

            libros_ultimo_autor.sort(key=lambda x: x.fecha, reverse=True)
            libros_otro_autor.sort(key=lambda x: x.fecha, reverse=True)

            libros_recomendados = libros_ultimo_autor + libros_otro_autor + libros_adicionales
            mostrar_libros_paginados(libros_recomendados, usuario)

def mostrar_libros_paginados(libros, usuario):
    os.system('cls' if os.name == 'nt' else 'clear')
    index = 0
    while index < len(libros):
        print(colored("Bienvenido,", "green"), colored(usuario.usuario, "cyan"))
        for libro in libros[0:index + 10]:
            print(colored(f'Id: {libro.id}, Título: {libro.titulo}, Categoría: {libro.categoria}, Fecha de Publicación: {libro.fecha}, Autor: {libro.autor}', "yellow"), end="")
        index += 10
        if index < len(libros):
          
            print(colored(" <-- Escriba 'B' para volver al menú principal", "green"))
            print(colored("(!)", "red"), colored("Use el comando --pedir 'id_libro' para reservar el libro", "green"))
            opcion = input(colored("¿Desea cargar más libros? (B/--y/--n/--pedir 'id_libro'): ", "yellow"))
            os.system('cls' if os.name == 'nt' else 'clear')
            if opcion == '--y':
                continue
            elif opcion == "--n":
                break
            elif opcion == "B":
                mostrar_pantalla_principal(usuario)
            else:
                try:
                    comando, numero = opcion.split(" ")
                    numero = int(numero)
                except ValueError:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(colored("Bienvenido,", "green"), colored(usuario.usuario, "cyan"))
                    print(colored("Error: Comando inválido", "red"))
                    print(colored("Lista de comandos:", "red"))
                    print(colored("\tB", "red"))
                    print(colored("\t--y", "red"))
                    print(colored("\t--n", "red"))
                    print(colored("\t--pedir 'id_libro'", "red"))
                    input(colored("Presiona ENTER para continuar...", "red"))
                    mostrar_pantalla_principal(usuario)

                if numero < 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(colored("Bienvenido,", "green"), colored(usuario.usuario, "cyan"))
                    print(colored("Error: Libro no encontrado", "red"))
                    input(colored("Presiona ENTER para continuar...", "red"))
                    mostrar_pantalla_principal(usuario)

            if comando == "--pedir" and numero <= Libro.id:
                for libro in Libro.libros:
                    if libro.id == numero:
                        usuario.libro_actual = libro
                        usuario.ultimo_autor_leido = usuario.libro_actual.autor
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(colored("Bienvenido,", "green"), colored(usuario.usuario, "cyan"))
                        print(colored("El libro ha sido reservado", "green"))
                        input(colored("Presiona ENTER para continuar...", "green"))
                        mostrar_pantalla_principal(usuario)
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(colored("Bienvenido,", "green"), colored(usuario.usuario, "cyan"))
                print(colored("Error: Libro no encontrado", "red"))
                input(colored("Presiona ENTER para continuar...", "red"))
                mostrar_pantalla_principal(usuario)
        else:
            print( colored("\n\t(!)", "red"), colored("Parece que has llegado al final", "green"))
            input(colored("¿Qué desea hacer? (B/--pedir 'id_libro'): ", "yellow"))

def reemplazar_linea_usuario_con_flag(archivo_usuarios, archivo_flag, usuario):
    with open(archivo_flag, 'r', encoding='utf-8') as f_flag:
        nueva_linea = f_flag.readline().strip()

    with open(archivo_usuarios, 'r', encoding='utf-8') as f_usuarios:
        lineas = f_usuarios.readlines()

    with open(archivo_usuarios, 'w', encoding='utf-8') as f_usuarios:
        for linea in lineas:
            if linea.startswith(usuario + '|'):
                f_usuarios.write(nueva_linea + '\n')
            else:
                f_usuarios.write(linea)

def ver_historial(usuario):
    if usuario.historial == None:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored("Bienvenido,", "green"), colored(usuario.usuario, "cyan"))
        print(colored("HISTORIAL (De más reciente a más antiguo): ", "green"))
        print(colored("-----------------------------------------", "green"))
        print(colored("(!)", "red"), colored("Usted no ha leído otros libros", "yellow"))
        print(colored("-----------------------------------------", "green"))
        input(colored("Presione ENTER para continuar...", "green"))
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored("Bienvenido,", "green"), colored(usuario.usuario, "cyan"))
        print(colored("HISTORIAL (De más reciente a más antiguo): ", "green"))
        print(colored("-----------------------------------------", "green"))

        lista_temp =  [int(num) for num in list(ast.literal_eval(usuario.historial))]
        lista_temp2 = []
        for num in lista_temp:
            for libro in Libro.libros:
                if libro.id == num:
                    lista_temp2.append(f"{libro.titulo}, de {libro.autor.strip()}")
        lista_temp2 = lista_temp2[::-1]
        for linea in lista_temp2:
            print(colored(linea, "yellow"))
        print(colored("-----------------------------------------", "green"))
        input(colored("Presione ENTER para continuar...", "green"))

if __name__ == "__main__":
    mostrar_pantalla_principal()