from fastapi import FastAPI

app= FastAPI()

@app.get('/inicio')
def ruta_prueba():
    return "Hola Canijos"

@app.get('/lista')
def ruta_prueba():
    return "lista"