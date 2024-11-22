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

# Extrae las fechas de los commits
dates = [commit['commit']['author']['date'] for commit in commits]

# Convierte las fechas a un DataFrame de pandas
df = pd.DataFrame(dates, columns=['date'])
df['date'] = pd.to_datetime(df['date'])

# Cuenta los commits por día
commits_per_day = df.groupby(df['date'].dt.date).size()

# Elimina el archivo de la gráfica de commits si existe
if os.path.exists('commit_graph.png'):
    os.remove('commit_graph.png')

# Grafica los datos
plt.figure(figsize=(12, 6))
commits_per_day.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Commits por día', fontsize=16)
plt.xlabel('Fecha', fontsize=14)
plt.ylabel('Número de commits', fontsize=14)
plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas de fecha 45 grados y alinearlas a la derecha
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('commit_graph.png')