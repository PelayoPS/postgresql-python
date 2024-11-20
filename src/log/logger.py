import logging
import os

def log_setup():
    """
    Configura el logger para la aplicación.

    Crea un logger con dos handlers:
    - Un handler para guardar los logs en un archivo.
    - Un handler para mostrar los logs en la consola con colores.

    Returns:
        logging.Logger: El logger configurado.
    """
    # Configuración del logger
    logger = logging.getLogger('mi_logger')
    # Nivel de los mensajes que se van a mostrar
    logger.setLevel(logging.DEBUG)

    # Crear el directorio de logs si no existe
    log_dir = os.path.join(os.path.dirname(__file__), 'logs')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    

    # Formato del logger
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Handler para guardar en archivo
    log_file = os.path.join(log_dir, 'logfile.log')
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    # Asignar el formato al handler
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Handler para mostrar en consola con colores
    class ColorHandler(logging.StreamHandler):
        """
        Handler personalizado para mostrar logs en la consola con colores.
        """
        COLORS = {
            'DEBUG': '\033[94m',  # Azul
            'INFO': '\033[92m',   # Verde
            'WARNING': '\033[93m', # Amarillo
            'ERROR': '\033[91m',  # Rojo
            'CRITICAL': '\033[95m' # Magenta
        }

        def emit(self, record):
            try:
                message = self.format(record)
                color = self.COLORS.get(record.levelname, '\033[0m')
                self.stream.write(color + message + '\033[0m' + self.terminator)
                self.flush()
            except Exception:
                self.handleError(record)

    console_handler = ColorHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger