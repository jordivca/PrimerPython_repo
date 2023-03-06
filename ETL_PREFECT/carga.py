from DB_credenciales import  coneccion_repo_preparacion
import pandas as pd
from prefect import flow, task

@task
def carga_datos(df):
    print("comienza la carga en covid19")
    conn = coneccion_repo_preparacion()
    df.to_sql(con=conn, index=False, name="covid19_tabla", if_exists='append')
    print("termina la carga de datos")
@task
def carga_resumen(df):
    print("comienza la carga en covid19")
    conn = coneccion_repo_preparacion()
    df.to_sql(con=conn, index=False, name="covid19_country", if_exists='append')
    print("termina la carga de datos")
