import tkinter as tk
from tkinter import ttk
from src.model.tabla import Tabla
from src.interface.data_dialog import DataDialog

class App:
    """Clase que representa la ventana principal de la aplicación.
    """
    # lista de tablas
    tablas = []
    def __init__(self, root, logger):
        """Constructor de la clase App.

        Args:
            root (_type_): root de la ventana.
            logger (_type_): logger de la aplicación.
        """
        self.root = root
        self.logger = logger
        self.root.title("Gestión Empresarial")
        
        # Establecer tamaño mínimo de la ventana
        self.root.minsize(300,200)
        
        self.create_widgets()
        self.center_window()

    def center_window(self):
        """Centra la ventana en la pantalla.
        """
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        self.root.minsize(width, height)

    def create_widgets(self):
        """Crea los widgets de la ventana.
        """
        # Limpiar la ventana
        for widget in self.root.winfo_children():
            widget.destroy()

        # Campo de usuario
        tk.Label(self.root, text="Usuario:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.NSEW)
        self.usuario_entry = tk.Entry(self.root)
        self.usuario_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.NSEW)

        # Campo de tareas sólo puede ser números
        tk.Label(self.root, text="Tareas:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.NSEW)
        self.tareas_entry = tk.Entry(self.root, validate="key", validatecommand=(self.root.register(self.validate_numeric), '%P'))
        self.tareas_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.NSEW)

        # Campo de tareas completadas sólo puede ser números
        tk.Label(self.root, text="Tareas Completadas:").grid(row=2, column=0, padx=10, pady=10, sticky=tk.NSEW)
        self.tareas_completadas_entry = tk.Entry(self.root, validate="key", validatecommand=(self.root.register(self.validate_numeric), '%P'))
        self.tareas_completadas_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.NSEW)

        # Combobox de días de la semana sin posibilidad de introducir texto
        tk.Label(self.root, text="Día:").grid(row=3, column=0, padx=10, pady=10, sticky=tk.NSEW)
        self.dia_combobox = ttk.Combobox(self.root, values=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"], state="readonly")
        self.dia_combobox.grid(row=3, column=1, padx=10, pady=10, sticky=tk.NSEW)

        # Campo de mensaje de error
        self.error_label = tk.Label(self.root, text="", fg="red")
        self.error_label.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

        # Botón de enviar
        self.submit_button = tk.Button(self.root, text="Enviar", command=self.submit)
        self.submit_button.grid(row=5, column=0, columnspan=1, pady=10, sticky=tk.NSEW)

        # Botón de ver datos
        self.ver_datos_button = tk.Button(self.root, text="Ver Datos", command=self.ver_datos)
        self.ver_datos_button.grid(row=5, column=1, columnspan=1, pady=10, sticky=tk.NSEW)
        

        # Configurar el comportamiento de las columnas
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=3)

    def validate_numeric(self, value_if_allowed):
        """Valida que el valor ingresado sea numérico."""
        return bool(value_if_allowed.isdigit() or value_if_allowed == "")

    def submit(self):
        """Función que se ejecuta al hacer click en el botón de enviar. Comprueba que los campos no estén vacíos y guarda los datos en la base de datos.
        """
        # Obtener los datos de los campos
        usuario = self.usuario_entry.get()
        tareas = self.tareas_entry.get()
        tareas_completadas = self.tareas_completadas_entry.get()
        dia = self.dia_combobox.get()

        # Comprobar que los campos no estén vacíos y mandar un mensaje de error si lo están
        if not usuario or not tareas or not tareas_completadas or not dia:
            error_msg = "Todos los campos son necesarios."
            self.error_label.config(text=error_msg)
            self.logger.error(error_msg)
            self.adjust_window_size()
            return

        # Mensaje de éxito
        self.error_label.config(text="")
        print(f"Usuario: {usuario}, Tareas: {tareas}, Tareas Completadas: {tareas_completadas}, Día: {dia}")
        self.logger.info(f"Datos guardados: Usuario: {usuario}, Tareas: {tareas}, Tareas Completadas: {tareas_completadas}, Día: {dia}")
        # muestra un mensaje de que los datos se han guardado correctamente usando error_label con color verde
        self.error_label.config(text="Datos guardados correctamente", fg="green")
        self.guardar_datos(usuario, tareas, tareas_completadas, dia)

    def adjust_window_size(self):
        """Ajusta el tamaño de la ventana para acomodar el mensaje de error."""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        self.root.geometry(f'{width}x{height}')

    def guardar_datos(self, usuario, tareas, tareas_completadas, dia):
        """Guarda los datos en la base de datos.

        Args:
            usuario (_type_): usuario del que se han introducido los datos.
            tareas (_type_): tareas que se han introducido.
            tareas_completadas (_type_): tareas completadas que se han introducido.
            dia (_type_): día de la semana que se ha introducido.
        """
        tabla = Tabla(usuario, tareas, tareas_completadas, dia)
        self.tablas.append(tabla)
        # TODO subir a base de datos y no sólo en local

    def ver_datos(self):
        """Muestra los datos guardados en la base de datos."""
        DataDialog(self.root, self.tablas)


