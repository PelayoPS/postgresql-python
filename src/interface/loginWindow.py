import tkinter as tk
import psycopg2

class LoginWindow:
    """Clase que representa la ventana de inicio de sesión.
    """
    def __init__(self, root, logger, on_login_success):
        """Constructor de la clase LoginWindow.

        Args:
            root (_type_): root de la ventana.
            logger (_type_): logger de la aplicación.
            on_login_success (_type_): función que se ejecutará cuando el usuario inicie sesión correctamente.
        """
        self.root = root
        self.logger = logger
        self.on_login_success = on_login_success
        self.root.title("Inicio de Sesión")

       # Crear los widgets
        tk.Label(root, text="Usuario:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.NSEW)
        self.usuario_entry = tk.Entry(root)
        self.usuario_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.NSEW)

        tk.Label(root, text="Contraseña:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.NSEW)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.NSEW)

        # Campo de mensaje de error
        self.error_label = tk.Label(self.root, text="", fg="red")
        self.error_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky=tk.EW)

        self.submit_button = tk.Button(root, text="Enviar", command=self.submit)
        self.submit_button.grid(row=3, column=0, columnspan=2, pady=10, sticky=tk.EW)

        # Configurar el comportamiento de las columnas
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=3)
        
        # Establecer tamaño mínimo de la ventana
        self.root.minsize(300, 200)
        
        # Centrar la ventana
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

    def submit(self):
        """Función que se ejecuta al hacer click en el botón de enviar. Comprueba que los campos no estén vacíos y llama a la función on_login_success si no lo están.
        """
        user = self.usuario_entry.get()
        password = self.password_entry.get()
        if not user or not password:
            error_msg = "Todos los campos son necesarios."
            self.error_label.config(text=error_msg)
            self.logger.error(error_msg)
            return
        else:
            try:
                self.on_login_success(user, password, self.logger, self)
            except psycopg2.Error as e:
                error_msg = "Credenciales incorrectas."
                self.error_label.config(text=error_msg)
                self.logger.error(error_msg)
            return

