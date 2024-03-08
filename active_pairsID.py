import subprocess
import json

resultado_ejecucion = subprocess.run(['python', "scripts/rest_client.py", 'status'], capture_output=True, text=True)

# Verificar si la ejecución fue exitosa
if resultado_ejecucion.returncode == 0:
    salida_del_script = json.loads(resultado_ejecucion.stdout.strip())
    pairs_on = []
    for id in salida_del_script:
        if id["is_open"]== True:
            pairs_on.append(id["trade_id"])
    print(pairs_on)
