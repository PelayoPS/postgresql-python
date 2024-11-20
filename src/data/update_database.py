# modifica los datos dentro de la base de datos usando la estructura de la clase Tabla
import psycopg2

class database_manager:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def update_to_table(self, table_name, column_name, value, condition):
        """
        Actualiza un valor en una tabla de la base de datos.

        Args:
            table_name (str): Nombre de la tabla a actualizar.
            column_name (str): Nombre de la columna a actualizar.
            value (_type_): Nuevo valor de la columna.
            condition (str): Condición para seleccionar las filas a actualizar.

        Returns:
            tuple: Un par (bool, str) donde el primer elemento indica si la operación fue exitosa
                   y el segundo elemento contiene un mensaje con el resultado de la operación.
        """
        try:
            # Conectar a la base de datos
            conn = psycopg2.connect(f"dbname=productividad user={self.user} password={self.password}")
            cur = conn.cursor()

            # Actualizar el valor en la tabla
            cur.execute(f"UPDATE {table_name} SET {column_name} = %s WHERE {condition}", (value,))

            # Confirmar la transacción
            conn.commit()

            # Cerrar el cursor y la conexión
            cur.close()
            conn.close()
            return True, f"Valor actualizado correctamente en la tabla {table_name}"
        except Exception as e:
            return False, f"Error al actualizar el valor en la tabla {table_name}: {e}"
        
    def delete_from_table(self, table_name, condition):
        """
        Elimina filas de una tabla de la base de datos.

        Args:
            table_name (str): Nombre de la tabla a actualizar.
            condition (str): Condición para seleccionar las filas a eliminar.

        Returns:
            tuple: Un par (bool, str) donde el primer elemento indica si la operación fue exitosa
                   y el segundo elemento contiene un mensaje con el resultado de la operación.
        """
        try:
            # Conectar a la base de datos
            conn = psycopg2.connect(f"dbname=productividad user={self.user} password={self.password}")
            cur = conn.cursor()

            # Eliminar las filas de la tabla
            cur.execute(f"DELETE FROM {table_name} WHERE {condition}")

            # Confirmar la transacción
            conn.commit()

            # Cerrar el cursor y la conexión
            cur.close()
            conn.close()
            return True, f"Filas eliminadas correctamente de la tabla {table_name}"
        except Exception as e:
            return False, f"Error al eliminar filas de la tabla {table_name}: {e}"
        
    def insert_into_table(self, table_name, values):
        """
        Inserta una fila en una tabla de la base de datos.

        Args:
            table_name (str): Nombre de la tabla a actualizar.
            values (list): Valores de las columnas de la fila a insertar.

        Returns:
            tuple: Un par (bool, str) donde el primer elemento indica si la operación fue exitosa
                   y el segundo elemento contiene un mensaje con el resultado de la operación.
        """
        try:
            # Conectar a la base de datos
            conn = psycopg2.connect(f"dbname=productividad user={self.user} password={self.password}")
            cur = conn.cursor()

            # Insertar la fila en la tabla
            cur.execute(f"INSERT INTO {table_name} VALUES (%s)", (values,))

            # Confirmar la transacción
            conn.commit()

            # Cerrar el cursor y la conexión
            cur.close()
            conn.close()
            return True, f"Fila insertada correctamente en la tabla {table_name}"
        except Exception as e:
            return False, f"Error al insertar la fila en la tabla {table_name}: {e}"
        
    def create_table(self):
        """
        Crea una tabla en la base de datos si no existe.

        Returns:
            tuple: Un par (bool, str) donde el primer elemento indica si la operación fue exitosa
                   y el segundo elemento contiene un mensaje con el resultado de la operación.
        """
        try:
            # Conectar a la base de datos
            conn = psycopg2.connect(f"dbname=productividad user={self.user} password={self.password}")
            cur = conn.cursor()

            # Crear la tabla si no existe
            cur.execute("CREATE TABLE IF NOT EXISTS tareas (usuario TEXT, tareas TEXT, tareas_completadas TEXT, dia TEXT)")

            # Confirmar la transacción
            conn.commit()

            # Cerrar el cursor y la conexión
            cur.close()
            conn.close()
            return True, "Tabla creada correctamente"
        
        except Exception as e:
            return False, f"Error al crear la tabla: {e}"
        




