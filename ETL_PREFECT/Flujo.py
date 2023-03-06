from prefect import flow
from transformacion import  transform
from carga import  carga_datos,carga_resumen
@flow
def flujo_final():
    df, res_df =transform()
    carga_datos(df)
    carga_resumen(res_df)

