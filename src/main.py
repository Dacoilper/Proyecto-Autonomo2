def mostrar_menu():
    print("\n--- Gestor de Tareas ---")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Buscar tarea")
    print("0. Salir")
    
def agregar_tarea(tareas):
    """
    Agrega una tarea a la lista con validación:
    - No permite texto vacío.
    """
    while True:
        texto = input("Ingrese la descripción de la tarea: ").strip()

        if texto == "":
            print("Error: la tarea no puede estar vacía. Intente nuevamente.")
        else:
            nueva_tarea = {"texto": texto, "completada": False}
            tareas.append(nueva_tarea)
            print("Tarea agregada correctamente.")
            break
        
def listar_tareas(tareas):
    """
    Muestra todas las tareas con su estado.
    Usa un bucle for para recorrer la lista.
    """
    if len(tareas) == 0:
        print("No hay tareas registradas.")
        return

    print("\n--- Lista de tareas ---")
    for i, tarea in enumerate(tareas, start=1):
        estado = "✓" if tarea["completada"] else " "
        print(f"{i}. [{estado}] {tarea['texto']}")

def buscar_tarea(tareas):
    """
    Busca tareas que contengan una palabra o frase.
    - Recorre la lista con for
    - Cuenta coincidencias para mostrar 'no encontrado' si aplica
    """
    if len(tareas) == 0:
        print("No hay tareas para buscar.")
        return

    clave = input("Ingrese palabra o frase a buscar: ").strip().lower()
    if clave == "":
        print("Error: la búsqueda no puede estar vacía.")
        return

    coincidencias = 0
    print("\n--- Resultados de búsqueda ---")
    for i, tarea in enumerate(tareas, start=1):
        if clave in tarea["texto"].lower():
            estado = "✓" if tarea["completada"] else " "
            print(f"{i}. [{estado}] {tarea['texto']}")
            coincidencias += 1

    if coincidencias == 0:
        print("No se encontraron tareas con esa palabra o frase.")

def marcar_completada(tareas):
    """
    Marca una tarea como completada.
    - Valida que existan tareas
    - Valida que el índice sea un número y esté en rango
    """
    if len(tareas) == 0:
        print("No hay tareas para marcar como completadas.")
        return

    listar_tareas(tareas)

    while True:
        entrada = input("Ingrese el número de la tarea a completar (o 0 para cancelar): ").strip()

        if entrada == "0":
            print("Operación cancelada.")
            return

        if not entrada.isdigit():
            print("Error: debe ingresar un número válido.")
            continue

        indice = int(entrada)
        if indice < 1 or indice > len(tareas):
            print("Error: número fuera de rango. Intente nuevamente.")
            continue

        tarea = tareas[indice - 1]
        if tarea["completada"]:
            print("Esa tarea ya está marcada como completada.")
        else:
            tarea["completada"] = True
            print("Tarea marcada como completada.")

        break




def main():
    tareas = []  # Lista donde se almacenan las tareas

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            listar_tareas(tareas)
        elif opcion == "3":
            marcar_completada(tareas)
        elif opcion == "4":
            pass
        elif opcion == "5":
            buscar_tarea(tareas)
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
