#iniciar el servidor
prefect orion start
#iniciar el agente
prefect agent start -q test

#poner el produccion
prefect deployment build Flujo.py:flujo_final -n proceso
prefect deployment apply flujo_final-deployment.yaml   


