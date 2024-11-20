import psycopg2
import csv
import os

def export_all_tables_to_csv(user, password):
    """
    Exporta todas las tablas de la base de datos a archivos CSV.

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
            cur.execute(f"SELECT * FROM {table_name}")
            rows = cur.fetchall()
            colnames = [desc[0] for desc in cur.description]

            output_file = os.path.join(output_dir, f"{table_name}.csv")
            with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(colnames)
                csvwriter.writerows(rows)
            return (f"Tabla {table_name} exportada a {output_file} correctamente.")

        # Cerrar el cursor y la conexión
        cur.close()
        conn.close()
        return True, "Tablas exportadas correctamente"
    except Exception as e:
        return False, (f"Error al exportar las tablas a CSV: {e}")
    

