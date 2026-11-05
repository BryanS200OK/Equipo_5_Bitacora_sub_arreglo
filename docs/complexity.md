Modelo RAM con enteros de tamaño acotado y operaciones aritméticas de costo constante. Los enteros Python de precisión arbitraria añaden costo dependiente del número de bits, por lo que las cotas en n requieren este supuesto.

Kadane: la operación dominante del núcleo es la actualización del mejor sufijo, exactamente K(n)=sumatoria de 1 para i=1,...,n-1 = n-1. Para n>=2, n/2 <= n-1 <= n: constantes explícitas c_inferior=1/2, c_superior=1 y n0=2 para este conteo. La validación hace n comprobaciones y la copia de salida hasta n elementos. El tiempo total permanece Θ(n), pero las constantes anteriores se refieren al conteo dominante, no a nanosegundos ni a todas las instrucciones Python.

Fuerza bruta: la operación dominante es current += A[r], exactamente B(n)=sumatoria de (n-l), l=0,...,n-1 = n(n+1)/2. Para n>=1, n²/2 <= B(n) <= n²: c_inferior=1/2, c_superior=1, n0=1. La inicialización, validación y copia final no cambian Θ(n²).

Mejor y peor caso: Θ(n) para Kadane y Θ(n²) para fuerza bruta; no hay salida anticipada y las cantidades de iteraciones no dependen de los valores. Para el caso promedio, bajo cualquier distribución de valores acotados condicionada a una longitud fija n y el mismo modelo RAM, esos conteos exactos son constantes respecto a la entrada; su esperanza es K(n) o B(n). Esto no predice un tiempo promedio exacto, pues cambian ramas, tamaño de enteros, caché y entorno.

Memoria auxiliar O(1) para ambos motores, excluyendo la salida de k elementos (O(k)). La traza educativa sí usa O(n) adicional y no interviene en el cronometraje. El experimento almacena entradas y resultados fuera del intervalo medido.
