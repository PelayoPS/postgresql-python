import src.data.database_setup as database_setup
import src.log.logger as logger
import src.data.export_database as export_database
import tkinter as tk
from src.interface.gui_manager import LoginWindow, App

def main():
    """
    Función principal de la aplicación.

    Configura el logger, solicita las credenciales de la base de datos al usuario,
    configura la base de datos y exporta las tablas a archivos CSV.
    """
    my_logger = logger.log_setup()
    # Cargar el módulo de la interfaz gráfica
    my_logger.info("Cargando interfaz gráfica...")
    root = tk.Tk()
    login_window = LoginWindow(root, my_logger, on_login_success)
    root.mainloop()

def on_login_success(user, password, my_logger, self):
    """Si las credenciales son correctas, se inicia la aplicación.

    Args:
        user (_type_): usuario de la base de datos.
        password (_type_): contraseña de la base de datos.
        my_logger (_type_): logger de la aplicación.
    """
    
    result, message = database_setup.setup(user, password)
    if not result:
        my_logger.error(message)
        return
    self.root.destroy()
    my_logger.info(message)
    app = App(tk.Tk(), my_logger)
    app.create_widgets()
    app.root.mainloop()
    # Después de que la interfaz gráfica se cierre, podemos guardar los datos en la base de datos usando una lista

    # Exportar tablas a CSV
    my_logger.info("Exportando tablas a CSV...")
    result, message = export_database.export_all_tables_to_csv(user, password)
    if not result:
        my_logger.error(message)
        return

    my_logger.info(message)
    my_logger.info("Proceso finalizado correctamente")

if __name__ == "__main__":
    main()
