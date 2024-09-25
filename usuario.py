#usuario.py
class Usuario:

    def __init__(self, usuario, contraseña, tipo_usuario, libro_actual, ultimo_actor_leido, historial):
        self.usuario = usuario
        self.contraseña = contraseña
        self.tipo_usuario = tipo_usuario
        self.libro_actual = libro_actual
        self.ultimo_autor_leido = ultimo_actor_leido
        self.historial = historial