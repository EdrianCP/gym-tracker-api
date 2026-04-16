from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

app = FastAPI(
    title="Gym Tracker API",
    description="My first backend API to track Push/Pull/Legs workouts",
    version="1.0.0"
)

DATA_FILE = "mis_entrenamientos.json"

# --- NUEVO: Definimos la estructura exacta que esperamos recibir ---
class Workout(BaseModel):
    rutina: str
    ejercicio: str
    peso_maximo: float

# Ruta 1: Bienvenida (GET)
@app.get("/")
def home():
    return {"message": "Welcome to the Gym Tracker API. Server is running!"}

# Ruta 2: Leer historial (GET)
@app.get("/workouts")
def get_all_workouts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            return {"status": "success", "total_records": len(data), "data": data}
    return {"status": "success", "total_records": 0, "data": []}

# --- NUEVO: Ruta 3: Crear un nuevo registro (POST) ---
@app.post("/workouts")
def create_workout(workout: Workout):
    # 1. Cargamos los datos que ya existen
    data = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            
    # 2. Calculamos el nuevo ID automático
    nuevo_id = 1 if len(data) == 0 else data[-1]["id"] + 1
    
    # 3. Creamos el nuevo registro usando los datos que llegaron de la web
    nuevo_registro = {
        "id": nuevo_id,
        "rutina": workout.rutina,
        "ejercicio": workout.ejercicio,
        "peso_maximo": workout.peso_maximo
    }
    
    # 4. Lo guardamos en el archivo JSON
    data.append(nuevo_registro)
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
        
    return {"status": "success", "message": "Workout added perfectly!", "record": nuevo_registro}