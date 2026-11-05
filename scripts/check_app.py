"""Verificación funcional de las seis vistas usando Streamlit AppTest."""
from pathlib import Path
from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parents[1]
app = AppTest.from_file(str(ROOT / "app.py"), default_timeout=30).run()
assert not app.exception, app.exception
for view in ["Inicio","Algoritmos","Pruebas QA","Experimentos","Resultados","Reporte"]:
    app.sidebar.radio[0].set_value(view).run()
    assert not app.exception, (view, app.exception)
    if view == "Algoritmos":
        next(b for b in app.button if b.label == "Ejecutar análisis").click().run()
        assert not app.exception, app.exception
        assert any(m.value == "6" for m in app.metric)
        assert any("Equivalencia confirmada" in s.value for s in app.success)
    print(f"OK: {view}")
