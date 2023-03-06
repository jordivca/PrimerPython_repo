
#Construccion de ETL
from sqlalchemy import create_engine

def coneccion_repo_preparacion():
    pword = "Luiggi12."
    name = "certus"
    host = 'DESKTOP-LPN6KNV\MSQL'
    database = 'ETL'
    # Carga desde SQL
    con = create_engine("mssql+pyodbc://" + name + ":" + pword + "@" + host +"/" + database + "?driver=ODBC+Driver+17+for+SQL+Server")
    return con
