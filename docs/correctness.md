**Material de trabajo asistido por IA. El equipo debe reconstruir, comprender y verificar este argumento independientemente antes de entregarlo.**

Definamos E(i) como la mejor suma de un intervalo no vacío que termina exactamente en i, y G(i) como la mejor suma de cualquier intervalo contenido en A[0:i+1]. La relación a revisar es E(0)=G(0)=A[0], E(i)=max(A[i], E(i-1)+A[i]) y G(i)=max(G(i-1), E(i)).

**Invariante formal.** Tras procesar i (0 <= i < n): current = E(i) = max_{0 <= l <= i} Σ_{k=l}^{i} A[k], y left es el menor l que alcanza E(i). Además best = G(i) = max_{0 <= l <= r <= i} Σ_{k=l}^{r} A[k], y (start,end) es el par lexicográficamente mínimo que alcanza G(i). Antes de la iteración siguiente estos predicados se mantienen sobre el prefijo ya procesado.

**Inicialización.** Antes del segundo elemento, current y best valen A[0]. El único intervalo es [0,0], de modo que ambos predicados se cumplen incluso para A[0] negativo.

**Mantenimiento.** Todo intervalo que termina en i es el singleton [i,i] o extiende algún intervalo terminado en i-1. Entre las extensiones, basta extender el mejor: sumar A[i] conserva su orden. Si current anterior es negativo conviene reiniciar; si es cero se extiende para conservar el inicio menor. Así current representa E(i), con el inicio más temprano. Todo óptimo global anterior permanece en el prefijo o termina en i. Comparar best con current establece G(i), resolviendo empates por (inicio,fin). La comparación explícita preserva también el fin más temprano para el mismo inicio.

**Terminación.** El índice avanza de 1 a n-1, con variante n-i que disminuye y está acotada inferiormente. Al salir, best representa G(n-1); los índices y la tupla devuelta satisfacen la postcondición. Para n=1 el ciclo no se ejecuta y la inicialización basta.

**Fuerza bruta.** Para un inicio fijo l, después de agregar A[r], current es la suma A[l:r+1]. Los dos bucles visitan cada par 0 <= l <= r < n. best conserva el mayor intervalo visitado; como los pares se recorren en orden lexicográfico y solo se actualiza ante mejora estricta, se respeta el mismo desempate. Ambos rangos son finitos.
