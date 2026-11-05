Ejecutar `python -m pytest tests -q` o `python run_pipeline.py --qa-only`. La evidencia medida está en results/qa_results.json con fecha UTC, commit si existe, hash del código fuente y salida capturada; no se afirma cobertura.

La suite contempla positivos, negativos, mixtos, ceros, singleton positivo y negativo, vacíos, repetidos, óptimos al inicio/final/centro y empates. Verifica suma, índices, salida y ausencia de mutación. Se comparan 500 entradas aleatorias de semilla 20261105 y los 1092 arreglos de longitudes 1 a 6 sobre {-1,0,1}, estos últimos también contra un oráculo independiente basado en sumas directas. La traza se contrasta con prefijos y sufijos calculados directamente.

El número de casos parametrizados Pytest difiere del número de arreglos explorados dentro de las pruebas diferenciales. La interfaz ejecuta exclusivamente la suite fija con un timeout de 45 segundos y no acepta código ni comandos externos.
