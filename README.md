_**Monitoreo:**_

(Hay que modificar los archivos que paso aca abajo, para que anden en la nueva infraestructura, paths... etc)

_**Son 5 los archivos, se ubican en la carpeta principal (en donde esta config.json):**_
- **delete_locks.py**: Borra todos los locks activos (si hay señales de compra activas, las comprara inmediatamente).
- **buy_pairs.py**: Compra las cryptos de la cuenta de referencia.
- **sell_pairs.py**: Vende todas las cryptos abiertas.
- **active_pairsID.py**: Muestra el id de los trades activos (funcion necesaria para sell-pairs y delete_locks)
- **active_pairsNAME.py**: Muestra el nombre de los pares que estan activos (sirve para buy_pairs, este archivo va solamente en la cuenta de referencia)

_**Obs:**_
- En todas las cuentas estarian unicamente los primeros 4 archivos.
- active_pairsNAME.py tiene que estar en la/s cuenta de referencia, esta funcion es para ver los pares activos.
- buy_pairs se relaciona con active_pairsName, ya si se abre una cuenta nueva y se ejecuta buy_pairs,
se fija primero que pares esta activo de la cuenta de referencia con active_pairsName y los compra.

___
_**Futuro config:**_
Cree una carpeta para dejar el futuro config, como deberia de ser con las pocas modificaciones que se le hicieron (max_open_trades en 7, stake_amount (para que compre solo si tiene USDT > 100),el whitelist de las 7, force_entry en true)
*obs:*
Quizas tambien hay que tener en cuenta la salida de la crypto ya que si baja lentamente (es decir que no lo capte el atr) a una cantidad que no se puede vender, se va a poder solo resolver eliminando el trade. De todas formas con el config asi seria muy poco probable que sucediera dado los 100 usdt como tope inferior y la volatilidad de las cryptos, pero es para tener en cuenta.


___

**Datasets**:
Se dejaron los datasets que tenemos hasta ahora:
Cryptos10Factor2(Primer-dataset):
 - Es el primer dataset
 - Tiene como moneda de intercambio USD
 - Factor 2 y las 10 cryptos: BTC, ETH, MATIC, DOGE, SOL, BNB, ADA, XRP, LTC, TRX
Cryptos6Factor2:
 - Es el segundo dataset
 - Tiene como moneda de intercambio BTC
 - Factor 2 y las 6 cryptos: ETH, MATIC, DOGE, SOL, BNB, ADA

___

Si se quiere editar la presentacion, esta en canvas:

https://www.canva.com/design/DAF9Qhq-KeY/U3Un2fNOQu1V8trkCmghmw/edit?utm_content=DAF9Qhq-KeY&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

___

Aca dejo el colab, no era la idea porque no esta ordenado para el uso de todos y quizas no es entendible:

https://colab.research.google.com/drive/1iVpHvBOQHZNjWLuKuQTXbLLSp0kLc3sl?usp=sharing
