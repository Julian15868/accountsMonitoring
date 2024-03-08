import subprocess
import sys

try:
    pairs = eval(sys.argv[1])
    print(pairs)
    for pair in pairs: print(pair)
except:
    #pairs = ["BTC/USDT"]
    # Desde cuenta de referencia:
    print("Entro aca al final")
    pairs = subprocess.run(['python', "/home/ubuntu/freqtrade8081/freqtrade/active_pairsNAME.py"], capture_output=True, text=True)
    pairs = pairs.stdout.strip().replace("[","").replace("]","").replace(" ","").split(',')
    print(pairs)

"""# Borramos cualquier tipo de bloqueo
subprocess.run(['python', "delete_locks.py"])"""

for pair in pairs:
    resultado_ejecucion = subprocess.run(['python', "scripts/rest_client.py", 'forcebuy',pair], capture_output=True, text=True)
