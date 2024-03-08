import subprocess
import json
resultado_ejecucion = subprocess.run(['python', "scripts/rest_client.py", 'locks'], capture_output=True, text=True)

# Verificar si la ejecución fue exitosa
if resultado_ejecucion.returncode == 0:
    resultados = json.loads(resultado_ejecucion.stdout.strip())
    locks = []
    # Vemos los bloqueados
    for id in range(int(resultados["lock_count"])):
        locks.append(resultados["locks"][id]["id"])
    #print(locks)
    for lock in locks:
        subprocess.run(['python', "scripts/rest_client.py", "delete_lock",str(lock)], capture_output=True, text=True)
    print("Pares desbloqueados")
else:
    print("No se pudo realizar la tarea.")