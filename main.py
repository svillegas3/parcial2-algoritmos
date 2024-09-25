#main.py
import os

from pantalla_registro import mostrar_pantalla_registro
from pantalla_principal import mostrar_pantalla_principal
from usuario import Usuario
from libros import Libro

os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        if os.path.exists("flag.txt"):
            with open("flag.txt", "r") as archivo:
                u, c, t, l, a, h, key = archivo.readlines()[0].strip().split("|", 6)
                temp_l = l
                temp_a = a
                temp_h = h
                if temp_l == "None":
                    l = None
                if temp_a == "None":
                    a = None
                if temp_h == "None":
                    h = None
                if key == "None":
                    pass
                else:
                    for libro in Libro.libros:
                        if libro.id == int(key):
                            l = libro
                            break
            usuario = Usuario(u, c, t, l, a, h)
            mostrar_pantalla_principal(usuario)
            main()
        else:
            usuario = mostrar_pantalla_registro()
            with open("usuarios.txt", "r") as archivo:
                temp = None
                lineas = archivo.readlines()
                for linea in lineas:
                    if linea.startswith(usuario.usuario + '|'):
                        temp = linea
                        break
                u, c, t, l, a, h, key = linea.strip().split("|", 6)
                if key == "None":
                    pass
                else:
                    for libro in Libro.libros:
                        if libro.id == int(key):
                            usuario.libro_actual = libro
                            break
            mostrar_pantalla_principal(usuario)
main()