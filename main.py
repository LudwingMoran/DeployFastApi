from fastapi import FastAPI

app= FastAPI()

@app.get('/inicio')
def ruta_prueba():
    return "Hola Canijos"