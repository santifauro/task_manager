import json
import os
from datetime import datetime


def cargar_tareas():
    if not os.path.exists("tasks.json"):
        return []

    with open("tasks.json", "r", encoding="utf-8") as archivo:
        try:
            return json.load(archivo)
        except json.JSONDecodeError:
            return []

def guardar_tareas(tareas):
    with open("tasks.json", "w", encoding="utf-8") as archivo:
        json.dump(tareas, archivo, indent=4, ensure_ascii=False)


def show_tasks(tareas):
    if not tareas:
        print("\nNo hay tareas.\n")
        return

    print("\nLista de tareas:")
    for i, tarea in enumerate(tareas):
        estado = "✔" if tarea["completada"] else " "
        print(f'{i+1}. [{estado}] {tarea["descripcion"]} ({tarea["fecha"]})')
    print()


def add_task(tareas):
    descripcion = input("Nueva tarea: ")

    nueva_tarea = {
        "descripcion": descripcion,
        "completada": False,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    tareas.append(nueva_tarea)
    guardar_tareas(tareas)

    print("Tarea agregada.\n")


def complete_task(tareas):
    show_tasks(tareas)

    try:
        index = int(input("Número de tarea completada: ")) - 1

        if 0 <= index < len(tareas):
            tareas[index]["completada"] = True
            guardar_tareas(tareas)
            print("Tarea completada.\n")
        else:
            print("Número fuera de rango.\n")

    except ValueError:
        print("Ingresá un número válido.\n")


def delete_task(tareas):
    if not tareas:
        print("\nNo hay tareas para eliminar.\n")
        return

    show_tasks(tareas)

    try:
        index = int(input("Número de tarea a eliminar: ")) - 1

        if 0 <= index < len(tareas):
            tarea = tareas[index]
            confirm = input(
                f"¿Eliminar '{tarea['descripcion']}'? (s/n): "
            ).lower()

            if confirm == "s":
                tareas.pop(index)
                guardar_tareas(tareas)
                print("Tarea eliminada.\n")
            else:
                print("Operación cancelada.\n")
        else:
            print("Número fuera de rango.\n")

    except ValueError:
        print("Ingresá un número válido.\n")


def main():
    tareas = cargar_tareas()

    while True:
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            show_tasks(tareas)
        elif opcion == "2":
            add_task(tareas)
        elif opcion == "3":
            complete_task(tareas)
        elif opcion == "4":
            delete_task(tareas)
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.\n")


if __name__ == "__main__":
    main()
