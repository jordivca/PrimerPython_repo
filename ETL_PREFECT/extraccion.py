import requests
import tqdm
from DB_credenciales import  coneccion_repo_preparacion
import pandas as pd
def extract_covid19():
    # CONSTANTES
    OWNER = 'CSSEGISandData'
    REPO = 'COVID-19'
    PATH = 'csse_covid_19_data/csse_covid_19_daily_reports'
    URL = f'https://api.github.com/repos/{OWNER}/{REPO}/contents/{PATH}'

    download_urls = []
    response = requests.get(URL)
    conn = coneccion_repo_preparacion()
    print("Coneccion exitosa")
    i = 0
    for data in tqdm.tqdm(response.json()):
        if data['name'].endswith('.csv'):
            file_path = data['download_url']
            dat = pd.read_csv(file_path)
            # escribir datos a sqlite
            if i == 0:  # si es la primera entrada y el nombre de la tabla ya existe, entonces remplazar
                dat.to_sql( con=conn, index=False,name="covid19", if_exists='replace')
            else:  # de lo contrario añadir a la tabla existente
                dat.to_sql( con=conn, index=False,name="covid19", if_exists='append')
            i = i+1
        if i==10:
            break
    print("extraccion y guardado en DB exitosa")

extract_covid19()