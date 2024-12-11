import psycopg2
import csv
import os

table_name = 'tareas'

def export_all_tables_to_csv(user, password):
    """
    Exporta todas las tablas de la base de datos a archivos CSV.
    !TODO usar para exportar las tablas de la base de datos a CSV.

    Args:
        user (str): Nombre de usuario de la base de datos.
        password (str): Contraseña de la base de datos.

    Returns:
        tuple: Un par (bool, str) donde el primer elemento indica si la operación fue exitosa
               y el segundo elemento contiene un mensaje con el resultado de la operación.
    """
    try:
        # Conectar a la base de datos
        conn = psycopg2.connect(f"dbname=productividad user={user} password={password}")
        cur = conn.cursor()
        
        # Obtener los nombres de las tablas
        cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
        tables = cur.fetchall()


        # Crear el directorio de salida si no existe
        output_dir = 'src/data/database'
        os.makedirs(output_dir, exist_ok=True)
        
        # Exportar cada tabla a un archivo CSV
        for table in tables:
            table_name = table[0]
            # Query para obtener los datos de la tabla llamada "tareas"
            
            cur.execute(f"SELECT * FROM {table_name}")
            data = cur.fetchall()
            # Crea una lista con
            # formato: Nombre;Tareas;Tareas_Completadas;Dia
            data = [f"{row[0]}" for row in data]
            # Cambio de formato de (Pelayo,12,12,Lunes) a Pelayo;12;12;Lunes
            data = [row.replace('(','') for row in data]
            data = [row.replace(')','') for row in data]
            data = [row.replace(',',';') for row in data]

            # Crea un archivo CSV con el nombre de la tabla
            with open(f"{output_dir}/{table_name}.csv", "w") as file:
                file.write("\n".join(data))
        # Cerrar el cursor y la conexión
        cur.close()
        conn.close()
        return True, "Tablas exportadas correctamente"
    except Exception as e:
        return False, (f"Error al exportar las tablas a CSV: {e}")