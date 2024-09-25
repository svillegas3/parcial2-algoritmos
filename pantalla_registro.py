#pantalla_registro.py
import os

from termcolor import colored
from usuario import Usuario

os.system('color')

def mostrar_pantalla_registro():
    if not os.path.exists("usuarios.txt"):
        with open("usuarios.txt", "w") as archivo:
            pass
    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        print(colored("Bienvenido a Biblot", "green"))
        print(colored("-------------------", "green"))
        print(colored("Seleccione una opción: ", "yellow"))
        print(colored("1. Registrarse", "yellow"))
        print(colored("2. Iniciar sesión", "yellow"))
        print(colored("3. Salir", "yellow"), colored("(!)", "red"))
        opcion = input(colored("Opción: ", "yellow"))
        os.system('cls' if os.name == 'nt' else 'clear')

        match opcion:
            case "1":
                registrarse()
            case "2":
                u, c, t, l, a, h = iniciar_sesion()
                usuario = Usuario(u, c, t, l, a, h)
                return usuario
            case "3":
                exit()
            case _:
                print(colored("Bienvenido a Biblot", "green"))
                print(colored("-------------------", "green"))
                print(colored("Error: Por favor, ingrese solo una de las opciones del menú", "red"))
                input(colored("Presione ENTER para continuar...", "red"))
                os.system('cls' if os.name == 'nt' else 'clear')

def registrarse():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored("Bienvenido a Biblot", "green"))
        print(colored(" --> REGISTRO DE CUENTAS: TIPO DE USUARIO", "green"))
        print(colored("-----------------------------------------", "green"))
        print(colored("Seleccione el tipo de usuario que más lo identifica: ", "yellow"))
        print(colored("1. Estudiante", "yellow"))
        print(colored("2. Investigador", "yellow"))
        print(colored("3. Lector habitual", "yellow"))
        print(colored("4. Lector historia", "yellow"))
        print(colored(" <-- Escriba 'B' para volver al menú principal", "green"))
        opcion = input(colored("Opción: ", "yellow"))
        os.system('cls' if os.name == 'nt' else 'clear')

        if opcion == "B":
            return

        match opcion:
            case "1":
                tipo_usuario = "lector_estudiante"
            case "2":
                tipo_usuario = "lector_investigador"
            case "3":
                tipo_usuario = "lector_habitual"
            case "4":
                tipo_usuario = "lector_historia"
            case _:
                print(colored("Bienvenido a Biblot", "green"))
                print(colored(" --> REGISTRO DE CUENTAS: TIPO DE USUARIO", "green"))
                print(colored("-----------------------------------------", "green"))
                print(colored("Error: Por favor, ingrese solo una de las opciones del menú", "red"))
                input(colored("Presione ENTER para continuar...", "red"))
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
        break

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored("Bienvenido a Biblot", "green"))
        print(colored(" --> REGISTRO DE CUENTAS: USUARIO", "green"))
        print(colored("---------------------------------", "green"))
        print(colored("Ingrese un usuario tal que: ", "yellow"))
        print(colored("\t-Los unicos caracteres permitidos son números y letras minúsculas", "yellow"))
        print(colored("\t-No debe contener espacios", "yellow"))
        print(colored("\t-Tiene que tener entre 6 y 20 caracteres", "yellow"))
        print(colored("\t-Debe contener mínimo 3 letras", "yellow"))
        print(colored(" <-- Escriba 'B' para volver al menú principal", "green"))
        usuario = input(colored("Usuario: ", "yellow"))
        os.system('cls' if os.name == 'nt' else 'clear')

        if usuario == "B":
            return

        if ' ' in usuario:
            print(colored("Bienvenido a Biblot", "green"))
            print(colored(" --> REGISTRO DE CUENTAS: USUARIO", "green"))
            print(colored("---------------------------------", "green"))
            print(colored("Error: El usuario no debe contener espacios", "red"))
            input(colored("Presione ENTER para continuar...", "red"))
            continue

        if not all(char.islower() or char.isdigit() for char in usuario):
            print(colored("Bienvenido a Biblot", "green"))
            print(colored(" --> REGISTRO DE CUENTAS: USUARIO", "green"))
            print(colored("---------------------------------", "green"))
            print(colored("Error: El usuario solo puede contener letras minúsculas y números", "red"))
            input(colored("Presione ENTER para continuar...", "red"))
            continue

        letras = [char for char in usuario if char.isalpha()]
        if len(letras) < 3:
            print(colored("Bienvenido a Biblot", "green"))
            print(colored(" --> REGISTRO DE CUENTAS: USUARIO", "green"))
            print(colored("---------------------------------", "green"))
            print(colored("Error: El usuario debe contener al menos 3 letras", "red"))
            input(colored("Presione ENTER para continuar...", "red"))
            continue

        if len(usuario) not in range(6, 21):
            print(colored("Bienvenido a Biblot", "green"))
            print(colored(" --> REGISTRO DE CUENTAS: USUARIO", "green"))
            print(colored("---------------------------------", "green"))
            print(colored("Error: El usuario debe tener entre 6 y 20 caracteres", "red"))
            input(colored("Presione ENTER para continuar...", "red"))
            continue
        
        romper = True
        with open("usuarios.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                u, *_ = linea.strip().split("|")
                if usuario == u:
                    print(colored("Bienvenido a Biblot", "green"))
                    print(colored(" --> REGISTRO DE CUENTAS: USUARIO", "green"))
                    print(colored("---------------------------------", "green"))
                    print(colored("Error: El usuario ya existe. Por favor, elija otro", "red"))
                    input(colored("Presione ENTER para continuar...", "red"))
                    romper = False
                    break
            if romper is False:
                continue
            else:
                break

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored("Bienvenido a Biblot", "green"))
        print(colored(" --> REGISTRO DE CUENTAS: CONTRASEÑA", "green"))
        print(colored("------------------------------------", "green"))
        print(colored("Ingrese una contraseña tal que: ", "yellow"))
        print(colored("\t-Los únicos caracteres permitidos son números y letras", "yellow"))
        print(colored("\t-No debe contener espacios", "yellow"))
        print(colored("\t-Debe tener mínimo 8 caracteres", "yellow"))
        print(colored(" <-- Escriba 'B' para volver al menú principal", "green"))
        contraseña = input(colored("Contraseña: ", "yellow"))
        os.system('cls' if os.name == 'nt' else 'clear')

        if contraseña == "B":
            return

        if ' ' in contraseña:
            print(colored("Bienvenido a Biblot", "green"))
            print(colored(" --> REGISTRO DE CUENTAS: CONTRASEÑA", "green"))
            print(colored("------------------------------------", "green"))
            print(colored("Error: La contraseña no debe contener espacios", "red"))
            input(colored("Presione ENTER para continuar...", "red"))
            continue

        if not contraseña.isalnum():
            print(colored("Bienvenido a Biblot", "green"))
            print(colored(" --> REGISTRO DE CUENTAS: CONTRASEÑA", "green"))
            print(colored("------------------------------------", "green"))
            print(colored("Error: La contraseña solo puede contener letras y números", "red"))
            input(colored("Presione ENTER para continuar...", "red"))
            continue

        if len(contraseña) < 8:
            print(colored("Bienvenido a Biblot", "green"))
            print(colored(" --> REGISTRO DE CUENTAS: CONTRASEÑA", "green"))
            print(colored("------------------------------------", "green"))
            print(colored("Error: La contraseña debe tener al menos 8 caracteres", "red"))
            input(colored("Presione ENTER para continuar...", "red"))
            continue

        with open("usuarios.txt", "a", encoding="utf-8") as archivo:
                archivo.write(f"{usuario}|{contraseña}|{tipo_usuario}|None|None|None|None\n")

        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored("Bienvenido a Biblot", "green"))
        print(colored(" --> REGISTRO DE CUENTAS: CUENTA CREADA EXITOSAMENTE", "green"))
        print(colored("----------------------------------------------------", "green"))
        print(colored("Su cuenta ha sido creada exitosamente", "green"))
        input(colored("Presione ENTER para continuar...", "green"))
        os.system('cls' if os.name == 'nt' else 'clear')
        return

def iniciar_sesion():
    while True:
        print(colored("Bienvenido a Biblot", "green"))
        print(colored(" --> INICIO DE SESIÓN: INGRESAR USUARIO", "green"))
        print(colored("---------------------------------------", "green"))
        print(colored(" <-- Escriba 'B' para volver al menú principal", "green"))
        usuario = input(colored("Usuario: ", "yellow"))
        if usuario == "B":
            mostrar_pantalla_registro()
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored("Bienvenido a Biblot", "green"))
        print(colored(" --> INICIO DE SESIÓN: INGRESAR CONTRASEÑA", "green"))
        print(colored("---------------------------------------", "green"))
        print(colored(" <-- Escriba 'B' para volver al menú principal", "green"))
        contraseña = input(colored("Contraseña: ", "yellow"))
        if contraseña == "B":
            mostrar_pantalla_registro()
        
        with open("usuarios.txt", "r", encoding="utf-8") as archivo:
            usuarios = archivo.readlines()

        for linea in usuarios:
            u, c, t, l, a, h, _ = linea.strip().split("|", 7)
            temp_l = l
            temp_a = a
            temp_h = h
            if temp_l == "None":
                l = None
            if temp_a == "None":
                a = None
            if temp_h == "None":
                h = None

            if usuario == u and contraseña == c:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(colored("Bienvenido a Biblot", "green"))
                print(colored(" --> INICIO DE SESIÓN: INICIO EXITOSO", "green"))
                print(colored("---------------------------------------", "green"))
                print(colored("Inicio de sesión exitoso", "green"))
                input(colored("Presiona ENTER para continuar...", "green"))
                
                return u, c, t, l, a, h
            
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored("Bienvenido a Biblot", "green"))
        print(colored(" --> INICIO DE SESIÓN: DATOS INCORRECTOS", "green"))
        print(colored("---------------------------------------", "green"))
        print(colored("Error: Usuario o contraseña incorrectos", "red"))
        input(colored("Presione ENTER para continuar...", "red"))
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    mostrar_pantalla_registro()