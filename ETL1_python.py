# Importando las librerias
import pandas as pd
import glob
import os
# Seteamos el directorio a buscar los archivos
#D:\ANALYTIC_PYTHON\EntornoPython\ETL DATASET\World Cup
path = r'D:\ANALYTIC_PYTHON\EntornoPython\ETL DATASET\World Cup\Raw'
#cambiamos el path
os.chdir(path)
#
files = glob.glob( '*.csv')
print(files)




# Creamos una lista en blanco para cargar los datasets
li = []
# Realizaremos un loop sobre cada archivo, lo leeremos y lo juntaremos.

for f in files:
    # Leemos el archivo
    temp_df = pd.read_csv(f ,sep=';')
    # agregamos a la lista los dataframes
    li.append(temp_df)
    print(f'Dataframe creado exitosamente para {f} con un tamañao {temp_df.shape}')

# Uniremos todos los dataframe en uno
df = pd.concat(li, axis=0)
print(df.shape)
df.head()
df.to_csv(r'D:\ANALYTIC_PYTHON\EntornoPython\ETL DATASET\World Cup\Consolidado\Merge1.csv')