import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

class Visual:
    
    def __init__(self, data):
        self.data = data

    def create_heatmap(self):
        # Asegurarse de que las columnas sean numéricas
        self.data['Tareas Pendientes'] = pd.to_numeric(self.data['Tareas Pendientes'], errors='coerce')
        self.data['Tareas Realizadas'] = pd.to_numeric(self.data['Tareas Realizadas'], errors='coerce')

        # Calcular eficiencia como porcentaje
        self.data['Eficiencia'] = (self.data['Tareas Realizadas'] / self.data['Tareas Pendientes']) * 100

        # Crear el heatmap
        heatmap_data = self.data.pivot(index="Nombre", columns="Día", values="Eficiencia")

        plt.figure(figsize=(10, 6))
        sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap='coolwarm',  # Formato a un decimal
                    cbar_kws={"label": "Eficiencia (%)"}, square=True, linewidths=0.5, linecolor='black')

        plt.title('Eficiencia de Tareas por Usuario y Día', fontsize=16)
        plt.xlabel('Día de la Semana', fontsize=12)
        plt.ylabel('Nombre del Usuario', fontsize=12)
        plt.xticks(rotation=45)
        plt.yticks(rotation=0)
        plt.tight_layout()
        plt.show()

    def create_bar_chart(self):
        # Asegurarse de que las columnas sean numéricas
        self.data['Tareas Pendientes'] = pd.to_numeric(self.data['Tareas Pendientes'], errors='coerce')
        self.data['Tareas Realizadas'] = pd.to_numeric(self.data['Tareas Realizadas'], errors='coerce')

        # Calcular eficiencia como porcentaje
        self.data['Eficiencia'] = (self.data['Tareas Realizadas'] / self.data['Tareas Pendientes']) * 100

        # Definir colores para cada día de la semana
        day_colors = {
            'Lunes': 'lighblue',
            'Martes': 'lighgreen',
            'Miercoles': 'lighcoral',
            'Jueves': 'lighgoldenrodyellow',
            'Viernes': 'lighpink'
        }

        # Crear una paleta de colores para los usuarios
        user_palette = sns.color_palette("husl", len(self.data['Nombre'].unique()))
        user_colors = dict(zip(self.data['Nombre'].unique(), user_palette))

        # Crear un gráfico de barras para tareas pendientes
        plt.figure(figsize=(12, 6))
        sns.barplot(x='Día', y='Tareas Pendientes', hue='Nombre', data=self.data, palette=user_colors, alpha=0.6)
        plt.title('Tareas Pendientes por Usuario y Día', fontsize=16)
        plt.xlabel('Día de la Semana', fontsize=12)
        plt.ylabel('Número de Tareas Pendientes', fontsize=12)
        plt.xticks(rotation=45)
        plt.legend(title='Usuarios', loc='upper right')
        plt.tight_layout()
        plt.show()

        # Crear un segundo gráfico de barras para tareas realizadas
        plt.figure(figsize=(12, 6))
        sns.barplot(x='Día', y='Tareas Realizadas', hue='Nombre', data=self.data, palette=user_colors, alpha=0.6)
        plt.title('Tareas Realizadas por Usuario y Día', fontsize=16)
        plt.xlabel('Día de la Semana', fontsize=12)
        plt.ylabel('Número de Tareas Realizadas', fontsize=12)
        plt.xticks(rotation=45)
        plt.legend(title='Usuarios', loc='upper right')
        plt.tight_layout()
        plt.show()

        # Crear un tercer gráfico de barras para eficiencia
        plt.figure(figsize=(12, 6))
        sns.barplot(x='Día', y='Eficiencia', hue='Nombre', data=self.data, palette=user_colors, alpha=0.6)
        plt.title('Eficiencia por Usuario y Día', fontsize=16)
        plt.xlabel('Día de la Semana', fontsize=12)
        plt.ylabel('Eficiencia (%)', fontsize=12)
        plt.xticks(rotation=45)
        plt.legend(title='Usuarios', loc='upper right')
        plt.tight_layout()
        plt.show()

# Ruta al archivo CSV
file_path = os.path.join('datos_ejemplo.csv')

# Cargar los datos sin cabecera
try:
    # Especificar el delimitador como punto y coma y sin cabecera
    data = pd.read_csv(file_path, delimiter=';', header=None)

    # Asignar nombres a las columnas
    data.columns = ['Nombre', 'Tareas Pendientes', 'Tareas Realizadas', 'Día']

    # Imprimir los nombres de las columnas
    print("Nombres de las columnas:", data.columns.tolist())
    
    # Crear una instancia de la clase Visual
    visual = Visual(data)
    visual.create_heatmap()  # Crear el heatmap
    visual.create_bar_chart()  # Crear el gráfico de barras

except FileNotFoundError:
    print(f"Error: El archivo {file_path} no se encontró.")
except Exception as e:
    print(f"Ocurrió un error: {e}")