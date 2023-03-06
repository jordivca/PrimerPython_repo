# crearemos una funcion para leer solo algunas columnas

def leer_csv(path="", column_name=[], sep=';'):
    if len(column_name) == 0:

        df = pd.read_csv(path, sep=';')

    else:

        df = pd.read_csv(path, usecols=column_name, sep=';')

    return df





# Importando las librerias
import pandas as pd
import glob
import os
# Seteamos el directorio a buscar los archivos
path = r'D:\ANALYTIC_PYTHON\EntornoPython\ETL DATASET\World Cup\Raw'
#cambiamos el path
os.chdir(path)
# vamos  a buscar todos los archivos que son csv
files = glob.glob('*.csv')
print(files)

import shutil

# Creamos una lista en blanco para cargar los datasets
li = []
# Realizaremos un loop sobre cada archivo, lo leeremos y lo juntaremos.

path_salida = 'D:/ANALYTIC_PYTHON/EntornoPython/ETL DATASET/World Cup/Procesado/'

for f in files:
    # Leemos el archivo
    temp_df = leer_csv(f, sep=';')
    # agregamos a la lista los dataframes
    li.append(temp_df)

    # Moviendo archivos a la capa de Procesado
    shutil.move(f, path_salida + f)

    print(f'Dataframe creado exitosamente para {f} con un tamañao {temp_df.shape}')

# Uniremos todos los dataframe en uno
df = pd.concat(li, axis=0)
print(df.shape)
df.head()



path_final = 'D:/ANALYTIC_PYTHON/EntornoPython/ETL DATASET/World Cup/Consolidado/'

df.to_csv(path_final+"MergeFinal.csv",index=False)