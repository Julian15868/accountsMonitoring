**Son 5 los archivos, se ubican en la carpeta principal (en donde esta config.json):**
- **delete_locks.py**: Borra todos los locks activos (si hay señales de compra activas, las comprara inmediatamente).
- **buy_pairs.py**: Compra las cryptos de la cuenta de referencia.
- **sell_pairs.py**: Vende todas las cryptos abiertas.
- **active_pairsID.py**: Muestra el id de los trades activos (funcion necesaria para sell-pairs y delete_locks)
- **active_pairsNAME.py**: Muestra el nombre de los pares que estan activos (sirve para buy_pairs, este archivo va solamente en la cuenta de referencia)

**Obs:**
- En todas las cuentas estarian unicamente los primeros 4 archivos.
- active_pairsNAME.py tiene que estar en la/s cuenta de referencia, esta funcion es para ver los pares activos.
- buy_pairs se relaciona con active_pairsName, ya si se abre una cuenta nueva y se ejecuta buy_pairs,
se fija primero que pares esta activo de la cuenta de referencia con active_pairsName y los compra.
