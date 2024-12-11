import src.log.logger as logger
from src.interface.web_login import app

def main():
    """
    Función principal de la aplicación.

    Configura el logger y lanza la aplicación web.
    """
    my_logger = logger.log_setup()
    my_logger.info("Iniciando aplicación web...")
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == "__main__":
    main()
