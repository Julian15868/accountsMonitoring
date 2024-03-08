import subprocess
import sys

#pairs = ["BTC/USDT"] # Poner los pares a vender, o directamente ver los pares activos:
try:
    pairs = eval(sys.argv[1])
    print(pairs)
    for pair in pairs: print(pair)
except:
    pairs = (subprocess.run(['python', "active_pairsID.py"], capture_output=True, text=True))
    pairs = pairs.stdout.strip().replace("[","").replace("]","").replace(" ","").split(',')
    print(pairs)
    
for pair in pairs:
    resultado_ejecucion = subprocess.run(['python', "scripts/rest_client.py", 'forceexit',pair], capture_output=True, text=True)


pairs = (subprocess.run(['python', "active_pairsID.py"], capture_output=True, text=True))
pairs = pairs.stdout.strip().replace("[","").replace("]","").replace(" ","").split(',')
if str(pairs) == "['']":
    print("Se vendieron todos los pares")