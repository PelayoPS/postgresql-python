import requests
import pandas as pd
import matplotlib.pyplot as plt
import os

# Reemplaza con tu propio repositorio
repo_owner = 'PelayoPS'
repo_name = 'postgresql-python'

# URL de la API de GitHub para obtener los commits
url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/commits'

# Realiza la solicitud a la API
response = requests.get(url)
commits = response.json()

# Extrae las fechas y los autores de los commits
data = [(commit['commit']['author']['date'], commit['commit']['author']['name']) for commit in commits]

# Convierte los datos a un DataFrame de pandas
df = pd.DataFrame(data, columns=['date', 'author'])
df['date'] = pd.to_datetime(df['date']).dt.date

# Cuenta los commits por día y por autor
commits_per_day_author = df.groupby(['date', 'author']).size().unstack(fill_value=0)

# Elimina el archivo de la gráfica de commits si existe
if os.path.exists('commit_graph.png'):
    os.remove('commit_graph.png')

# Grafica los datos
plt.figure(figsize=(12, 6))
commits_per_day_author.plot(kind='area', stacked=True, linewidth=2)  # Aumenta el grosor de la línea
plt.title('Commits por día y autor', fontsize=16)
plt.xlabel('Fecha', fontsize=14)
plt.ylabel('Número de commits', fontsize=14)
plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas de fecha 45 grados y alinearlas a la derecha
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%d/%m/%Y'))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('commit_graph.png')
plt.show()