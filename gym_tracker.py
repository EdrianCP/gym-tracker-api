import json
import os


ARCHIVO_DATOS = "mis_entrenamientos.json"
historial_entrenamientos = []
contador_id = 1

def cargar_datos():
    global historial_entrenamientos, contador_id
    
    if os.path.exists(ARCHIVO_DATOS):
        with open(ARCHIVO_DATOS, "r") as archivo:
            historial_entrenamientos = json.load(archivo)
            
            if len(historial_entrenamientos) > 0:
                contador_id = historial_entrenamientos[-1]["id"] + 1

def guardar_datos():
    
    with open(ARCHIVO_DATOS, "w") as archivo:
        json.dump(historial_entrenamientos, archivo, indent=4)



def registrar_dia(tipo_rutina, ejercicio, peso):
    global contador_id
    nuevo_registro = {"id": contador_id, "rutina": tipo_rutina, "ejercicio": ejercicio, "peso_maximo": peso}
    historial_entrenamientos.append(nuevo_registro)
    print(f"✅ Guardado: ID {contador_id} | {tipo_rutina} - {ejercicio}")
    contador_id += 1
<<<<<<< HEAD
    guardar_datos() 
=======
    guardar_datos()

>>>>>>> 558c4cdc562aaf4fb3017ba8f8fa1c0782ecdb92
def ver_historial():
    print("\n--- MI HISTORIAL ACTUAL ---")
    if len(historial_entrenamientos) == 0:
        print("Aún no hay registros. ¡Ve a entrenar!")
    for registro in historial_entrenamientos:
         print(f"[{registro['id']}] {registro['rutina']} | {registro['ejercicio']} | {registro['peso_maximo']}kg")
    print("---------------------------\n")

def actualizar_peso(id_buscar, nuevo_peso):
    for registro in historial_entrenamientos:
        if registro["id"] == id_buscar:
            registro["peso_maximo"] = nuevo_peso
            print(f"🔄 ¡Actualizado! El ID {id_buscar} ahora tiene {nuevo_peso}kg.")
            guardar_datos()
            return
    print("❌ Error: No se encontró ese ID.")

def borrar_registro(id_buscar):
    for registro in historial_entrenamientos:
        if registro["id"] == id_buscar:
            historial_entrenamientos.remove(registro)
            print(f"🗑️ El ID {id_buscar} ha sido eliminado.")
            guardar_datos() 
            return
    print("❌ Error: No se encontró ese ID.")



def iniciar_sistema():
    cargar_datos() 
    print("🏋️‍♂️ Bienvenido a tu Gym Tracker 🏋️‍♂️")
    
    while True: 
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar nuevo entrenamiento")
        print("2. Ver mi historial")
        print("3. Actualizar un peso máximo")
        print("4. Borrar un registro")
        print("5. Salir")
        
        opcion = input("Elige una opción (1-5): ") 
        
        if opcion == '1':
            rutina = input("¿Qué rutina hiciste? (Push/Pull/Legs): ")
            ejercicio = input("¿Cuál fue el ejercicio principal?: ")
            peso = input("¿Cuánto peso levantaste? (kg): ")
            registrar_dia(rutina, ejercicio, peso)
        elif opcion == '2':
            ver_historial()
        elif opcion == '3':
            id_editar = int(input("Ingresa el ID del registro que quieres editar: "))
            nuevo_peso = input("¿Cuál es el nuevo peso máximo? (kg): ")
            actualizar_peso(id_editar, nuevo_peso)
        elif opcion == '4':
            id_borrar = int(input("Ingresa el ID del registro que quieres borrar: "))
            borrar_registro(id_borrar)
        elif opcion == '5':
            print("¡Buen entrenamiento! Cerrando sistema...")
            break
        else:
            print("❌ Opción no válida, intenta de nuevo.")

iniciar_sistema()
