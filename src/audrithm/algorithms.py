"""Subarreglo no vacío óptimo. Responsable académico propuesto: integrante 1.

Contrato: secuencia no vacía de int de Python, sin bool; no se modifica.
Desempate: menor inicio y, luego, menor fin (ambos inclusivos, base cero).
Kadane usa Θ(n) tiempo y O(1) auxiliar; brute_force Θ(n²) y O(1).
Se excluye de memoria auxiliar la tupla de salida. Modelo RAM de enteros
acotados: los enteros arbitrariamente grandes añaden costo por bits.
"""
from dataclasses import dataclass
from collections.abc import Sequence


@dataclass(frozen=True)
class Result:
    total: int
    start: int
    end: int
    subarray: tuple[int, ...]


def _validate(arr):
    if not isinstance(arr, Sequence) or isinstance(arr, (str, bytes)):
        raise TypeError("Se requiere una secuencia de enteros.")
    if len(arr) == 0:
        raise ValueError("El arreglo debe contener al menos un entero.")
    if any(type(x) is not int for x in arr):
        raise TypeError("Solo se admiten enteros de Python, sin booleanos.")


def kadane(arr: Sequence[int]) -> Result:
    """Mejor sufijo en i y mejor global hasta i; ver docs/correctness.md."""
    _validate(arr)
    current = best = arr[0]
    left = start = end = 0
    for i in range(1, len(arr)):
        # En empate se extiende, preservando el inicio más temprano.
        if current < 0:
            current, left = arr[i], i
        else:
            current += arr[i]
        if current > best or (current == best and (left, i) < (start, end)):
            best, start, end = current, left, i
    return Result(best, start, end, tuple(arr[start:end + 1]))


def brute_force(arr: Sequence[int]) -> Result:
    """Enumera n(n+1)/2 intervalos con suma acumulada, sin recalcular sumas."""
    _validate(arr)
    best, start, end = arr[0], 0, 0
    for left in range(len(arr)):
        current = 0
        for right in range(left, len(arr)):
            current += arr[right]
            if current > best:
                best, start, end = current, left, right
    return Result(best, start, end, tuple(arr[start:end + 1]))


def max_sum(arr):
    return kadane(arr).total


def kadane_trace(arr):
    """Traza educativa independiente del intervalo de medición."""
    _validate(arr)
    current = best = arr[0]
    rows = [{"Índice": 0, "Elemento": arr[0], "Mejor terminado": current, "Mejor global": best}]
    for i in range(1, len(arr)):
        current = max(arr[i], current + arr[i])
        best = max(best, current)
        rows.append({"Índice": i, "Elemento": arr[i], "Mejor terminado": current, "Mejor global": best})
    return rows
