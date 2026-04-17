from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI(
    title="Gym Tracker API",
    description="My first backend API to track Push/Pull/Legs workouts",
    version="1.0.0"
)

DATA_FILE = "mis_entrenamientos.json"


class Workout(BaseModel):
    rutina: str
    ejercicio: str
    peso_maximo: float

@app.get("/")
def home():
    return {"message": "Welcome to the Gym Tracker API. Server is running!"}


@app.get("/workouts")
def get_all_workouts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            return {"status": "success", "total_records": len(data), "data": data}
    return {"status": "success", "total_records": 0, "data": []}


@app.post("/workouts")
def create_workout(workout: Workout):
    
    data = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            
    
    nuevo_id = 1 if len(data) == 0 else data[-1]["id"] + 1
    
    
    nuevo_registro = {
        "id": nuevo_id,
        "rutina": workout.rutina,
        "ejercicio": workout.ejercicio,
        "peso_maximo": workout.peso_maximo
    }
    
    
    data.append(nuevo_registro)
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
        
    return {"status": "success", "message": "Workout added perfectly!", "record": nuevo_registro}

@app.delete("/workouts/{workout_id}")
def delete_workout(workout_id: int):
    
    with open("mis_entrenamientos.json", "r") as file:
        import json
        entrenamientos = json.load(file)
    
    
    entrenamiento_a_borrar = None
    for ent in entrenamientos:
        if ent["id"] == workout_id:
            entrenamiento_a_borrar = ent
            break
            
    
    if entrenamiento_a_borrar is None:
        raise HTTPException(status_code=404, detail=f"El entrenamiento con ID {workout_id} no existe.")
        
    
    entrenamientos.remove(entrenamiento_a_borrar)
    
    
    with open("mis_entrenamientos.json", "w") as file:
        json.dump(entrenamientos, file, indent=4)
        
    return {"status": "success", "message": f"Entrenamiento {workout_id} borrado permanentemente."}
@app.put("/workouts/{workout_id}")
def update_workout(workout_id: int, workout_actualizado: Workout):
    
    with open("mis_entrenamientos.json", "r") as file:
        import json
        entrenamientos = json.load(file)
    
    
    entrenamiento_a_editar = None
    for ent in entrenamientos:
        if ent["id"] == workout_id:
            entrenamiento_a_editar = ent
            break
            
    
    if entrenamiento_a_editar is None:
        raise HTTPException(status_code=404, detail=f"El entrenamiento con ID {workout_id} no existe.")
        
    
    entrenamiento_a_editar["rutina"] = workout_actualizado.rutina
    entrenamiento_a_editar["ejercicio"] = workout_actualizado.ejercicio
    entrenamiento_a_editar["peso_maximo"] = workout_actualizado.peso_maximo
    
    
    with open("mis_entrenamientos.json", "w") as file:
        json.dump(entrenamientos, file, indent=4)
        
    return {"status": "success", "message": f"Entrenamiento {workout_id} actualizado con éxito.", "record": entrenamiento_a_editar}