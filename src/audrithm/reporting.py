"""Texto académico editable; la aprobación humana está pendiente."""
from .experiment import ROOT

SECTIONS = [
    ("Especificación del problema", "specification.md"),
    ("Demostración de correctitud", "correctness.md"),
    ("Análisis de costo", "complexity.md"),
    ("Implementación y pruebas", "validation.md"),
    ("Experimento reproducible", "experiment.md"),
    ("Contraste entre teoría y evidencia", "analysis.md"),
    ("Uso y verificación de IA", "ai_usage.md"),
    ("Reproducibilidad", "reproducibility.md"),
]

def report_markdown():
    parts = ["# Equipo 5 · Bitácora 1\n\nBORRADOR ASISTIDO POR IA. Pendiente de revisión y aprobación del equipo.\n"]
    for i, (title, filename) in enumerate(SECTIONS, 1):
        parts.append(f"## {i}. {title}\n\n" + (ROOT / "docs" / filename).read_text(encoding="utf-8"))
    return "\n\n".join(parts)
