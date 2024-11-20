import tkinter as tk
from tkinter import ttk

class DataDialog:
    """Clase que representa un diálogo para mostrar los datos de las tablas."""
    def __init__(self, parent, tablas):
        """Constructor de la clase DataDialog.

        Args:
            parent (_type_): ventana padre.
            tablas (list): lista de tablas a mostrar.
        """
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Datos Guardados")
        self.tablas = tablas
        self.create_widgets()

    def create_widgets(self):
        """Crea los widgets del diálogo."""
        # Crear un Treeview para mostrar los datos
        self.tree = ttk.Treeview(self.dialog, columns=("Usuario", "Tareas", "Tareas Completadas", "Día"), show="headings")
        self.tree.heading("Usuario", text="Usuario")
        self.tree.heading("Tareas", text="Tareas")
        self.tree.heading("Tareas Completadas", text="Tareas Completadas")
        self.tree.heading("Día", text="Día")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Insertar los datos en el Treeview
        for tabla in self.tablas:
            self.tree.insert("", tk.END, values=(tabla.usuario, tabla.tareas, tabla.tareas_completadas, tabla.dia))

        # Botón para cerrar el diálogo
        self.close_button = tk.Button(self.dialog, text="Cerrar", command=self.dialog.destroy)
        self.close_button.pack(pady=10)
