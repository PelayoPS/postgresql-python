class Usuario:
    """Clase que representa a un usuario de la aplicación.
    """
    def __init__(self, nombre, tareas=0, tareas_completadas=0):
        """Constructor de la clase Usuario.

        Args:
            nombre (_type_): nombre del usuario.
            tareas (int, optional): número de tareas pendientes del usuario. Por defecto 0.
            tareas_completadas (int, optional): número de tareas completadas del usuario. Por defecto 0.
        """
        self._nombre = nombre
        self._tareas = tareas
        self._tareas_completadas = tareas_completadas

    # Getters
    @property
    def nombre(self):
        """Getter del nombre del usuario.

        Returns:
            _type_: nombre del usuario.
        """
        return self._nombre

    @property
    def tareas(self):
        """Getter del número de tareas pendientes del usuario.

        Returns:
            _type_: número de tareas pendientes del usuario.
        """
        return self._tareas

    @property
    def tareas_completadas(self):
        """Getter del número de tareas completadas del usuario.

        Returns:
            _type_: número de tareas completadas del usuario.
        """
        return self._tareas_completadas

    @property
    def eficiencia(self):
        """Getter de la eficiencia del usuario.

        Returns:
            _type_: eficiencia del usuario.
        """
        return self._eficiencia

    # Setters
    @nombre.setter
    def nombre(self, nombre):
        """Setter del nombre del usuario.

        Args:
            nombre (_type_): nombre del usuario.
        """
        self._nombre = nombre

    @tareas.setter
    def tareas(self, tareas):
        """Setter del número de tareas pendientes del usuario.

        Args:
            tareas (_type_): número de tareas pendientes del usuario.
        """
        self._tareas = tareas

    @tareas_completadas.setter
    def tareas_completadas(self, tareas_completadas):
        """Setter del número de tareas completadas del usuario.

        Args:
            tareas_completadas (_type_): número de tareas completadas del usuario.
        """
        self._tareas_completadas = tareas_completadas

    def calcular_eficiencia(self):
        """Calcula la eficiencia del usuario.
        """
        if self._tareas == 0:
            self._eficiencia = 0
        else:
            self._eficiencia = self._tareas_completadas / self._tareas

    def __repr__(self):
        """Representación de la clase Usuario.

        Returns:
            _type_: representación de la clase Usuario en forma de cadena.
        """
        return f"Usuario(nombre='{self._nombre}', tareas={self._tareas}, tareas_completadas={self._tareas_completadas}, eficiencia={self._eficiencia})"
