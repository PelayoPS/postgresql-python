import tkinter as tk
from src.interface.LoginWindow import LoginWindow
from src.interface.App import App

class GUI:
    """Clase que gestiona las ventanas de la aplicación."""
    def __init__(self, logger):
        """Constructor de la clase GUI.

        Args:
            logger (_type_): logger de la aplicación.
        """
        self.logger = logger
        self.root = tk.Tk()
        self.login_window = LoginWindow(self.root, self.logger, self.on_login_success)

    def on_login_success(self, user, password, logger, login_window):
        """Método que se ejecuta cuando el usuario inicia sesión correctamente.

        Args:
            user (_type_): usuario de la base de datos.
            password (_type_): contraseña de la base de datos.
            logger (_type_): logger de la aplicación.
            login_window (_type_): instancia de la ventana de inicio de sesión.
        """
        self.logger.info("Inicio de sesión exitoso")
        login_window.root.destroy()
        self.root = tk.Tk()
        self.app = App(self.root, self.logger)
        self.app.create_widgets()
        self.root.mainloop()