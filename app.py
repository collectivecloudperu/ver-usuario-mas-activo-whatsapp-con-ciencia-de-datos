import re
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

# Archivo txt de WhatsApp
archivo_chat = 'Chat de WhatsApp con Nube Colectiva Devs.txt'

# Leer el archivo txt
with open(archivo_chat, encoding='utf-8') as file:
    lines = file.readlines()

pattern = re.compile(r'^(\d{1,2}/\d{1,2}/\d{2,4}) (\d{1,2}:\d{2})\s*[ap]\. ?m\.? - (.*?): (.+)$')

data = []
for line in lines:
    match = pattern.match(line.strip())
    if match:
        date, time, user, message = match.groups()
        data.append([date, time, user, message])

# Creamos el datafram con pandas
df = pd.DataFrame(data, columns=['Fecha', 'Hora', 'Usuario', 'Mensaje'])

# Eliminar el mensaje "Eliminaste este mensaje"
df = df[~df['Usuario'].str.contains('salió del grupo|solicitó unirse|se unió|Eliminaste|Creaste el grupo', case=False, na=False)]

# Contar mensajes de los usuarios
conteo = df['Usuario'].value_counts()

# Mostrar los 10 usuarios que más participaron
print(conteo.head(10))

# Gráfico de datos
plt.figure(figsize=(10,5))
sns.barplot(x=conteo.values[:10], y=conteo.index[:10], palette="mako")
plt.title("Usuarios que más participaron en el grupo de WhatsApp")
plt.xlabel("Cantidad de mensajes")
plt.ylabel("Usuario")
plt.tight_layout()
plt.show()
