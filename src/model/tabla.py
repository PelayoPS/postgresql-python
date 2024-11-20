class Tabla:
    """Clase que representa una tabla de la base de datos.
    """
    def __init__(self, usuario, tareas, tareas_completadas, dia):
        """Constructor de la clase Tabla.

        Args:
            usuario (_type_): usuario del que se guardan las tareas.
            tareas (_type_): tareas pendientes del usuario.
            tareas_completadas (_type_): tareas completadas del usuario.
            dia (_type_): día en el que se registran las tareas.
        """
        self.usuario = usuario
        self.tareas = tareas
        self.tareas_completadas = tareas_completadas
        self.dia = dia

    def __repr__(self):
        """Representación de la clase Tabla.

        Returns:
            _type_: representación de la clase Tabla en forma de cadena.
        """
        return f"Tabla(usuario='{self.usuario}', tareas={self.tareas}, tareas_completadas={self.tareas_completadas}, dia='{self.dia}')"
    
    

