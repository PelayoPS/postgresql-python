import psycopg2


def setup(user1, password1):
    """
    Configura la conexión a la base de datos.

    Args:
        user1 (str): Nombre de usuario de la base de datos.
        password1 (str): Contraseña de la base de datos.

    Returns:
        tuple: Un par (bool, str) donde el primer elemento indica si la operación fue exitosa
               y el segundo elemento contiene un mensaje con el resultado de la operación.
    """
    # Comprueba si la base de datos ya existe
    try:
        conn = psycopg2.connect(f"dbname=productividad user={user1} password={password1}")
        return True, "Conexión a la base de datos establecida"
    except Exception:
        # si el error es que la base de datos no existe, la crea
        return True, crear_database(user1, password1)

def crear_database(user1, password1):
    """
    Crea la base de datos si no existe.
    Crea la tabla tareas si no existe.

    Args:
        user1 (str): Nombre de usuario de la base de datos.
        password1 (str): Contraseña de la base de datos.

    Returns:
        str: Mensaje indicando que la base de datos ha sido creada.

    """
    conn = psycopg2.connect(f"dbname=postgres user={user1} password={password1}")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("CREATE DATABASE productividad")
    cur.close()
    conn.close()
    conn = psycopg2.connect(f"dbname=productividad user={user1} password={password1}")
    cur = conn.cursor()
    # Crear la tabla inicial si no existe
    cur.execute("""
    CREATE TABLE IF NOT EXISTS tareas (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        tareas INT NOT NULL,
        tareas_completadas INT NOT NULL,
        dia DATE NOT NULL
    )
    """)
    cur.close()
    return "Base de datos creada"

