import subprocess
import json

resultado_ejecucion = subprocess.run(['python', "/home/ubuntu/freqtrade8081/freqtrade/scripts/rest_client.py", 'status',"-c","/home/ubuntu/freqtrade8081/freqtrade/config.json"], capture_output=True, text=True)

# Verificar si la ejecución fue exitosa
if resultado_ejecucion.returncode == 0:
    salida_del_script = json.loads(resultado_ejecucion.stdout.strip())
    pairs_on = []
    for id in salida_del_script:
        if id["is_open"]== True:
            pairs_on.append(id["pair"])
    print(pairs_on)
