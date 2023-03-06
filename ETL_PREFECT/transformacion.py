from DB_credenciales import  coneccion_repo_preparacion
import pandas as pd
def transform():
    print("Comienza la transformacion")

    conn = coneccion_repo_preparacion()

    sql ="select * from covid19"
    df = pd.read_sql(sql , con = conn)

    #eliminar duplicados
    new_df = df.drop_duplicates()
    new_df = new_df.drop_duplicates(df.columns[~df.columns.isin(['index'])], keep='first')
    new_df.columns
    #eliminar columnas =
    new_df = new_df.drop(columns =[
       'Lat', 'Long_', 'Combined_Key', 'Case_Fatality_Ratio'])
    #eliminar las filas que tienen vlores nulos o ceros en las columnas confirmadas o muertes o recuperados o activados

    new_df = new_df.dropna(subset = ['Confirmed', 'Deaths', 'Recovered', 'Active'])
    new_df = new_df.drop(new_df[new_df['Confirmed'] == 0].index)

    #agrupar por paises
    res_df = df.groupby(['Country_Region'],as_index= False)['Confirmed', 'Deaths', 'Recovered', 'Active'].sum()

    print("Termina la transformacion")

    return new_df, res_df

