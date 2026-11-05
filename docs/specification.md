Se recibe una secuencia A de n enteros de Python, n >= 1. Se devuelve una estructura inmutable con suma, inicio i, fin j y subarreglo A[i:j+1], tal que 0 <= i <= j < n y su suma es máxima entre todos los intervalos contiguos no vacíos.

Desempate lexicográfico por (i,j): menor inicio y luego menor fin. No se modifica la entrada. Una entrada vacía produce ValueError; tipos no enteros, incluidos booleanos, producen TypeError. Todos negativos devuelve el mayor elemento, con el primer índice si se repite. Ejemplo: [-2,1,-3,4,-1,2,1,-5,4] produce suma 6, índices [3,6], subarreglo [4,-1,2,1].
