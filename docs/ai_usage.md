Herramienta: Codex, modelo identificado por el entorno como GPT-6; no se dispone de un identificador de compilación más preciso. Fecha de trabajo: 2026-11-05. Nivel propuesto: Ámbar (asistencia con código y pruebas); el equipo debe completar y aprobar su Declaración de Transparencia Tecnológica conforme a las indicaciones del curso.

Prompt: se conserva íntegro en docs/user_request.txt. Salidas relevantes: implementación inicial de referencia, suite QA, pipeline experimental, interfaz, documentación y propuesta de argumento de correctitud. No se atribuyen contribuciones a estudiantes ni se presenta la demostración como aprobada por ellos.

Afirmación verificable de IA: «El ejemplo produce 6 y ambos motores respetan el mismo desempate». Se verifica con casos parametrizados, 500 arreglos aleatorios y un oráculo exhaustivo independiente para 1092 arreglos pequeños; el resultado se consulta en el JSON QA real. También se verifica por inspección que fuerza bruta usa suma acumulada en dos bucles. El equipo debe reproducir la verificación y registrar responsable y fecha.

Descartado durante el diseño: inicializar el máximo en cero (falla para todos negativos), recalcular sumas en cada intervalo (introduce costo cúbico), tiempos ficticios, atribuciones simuladas y uso de la web como sustituto del PDF. No se afirma haber medido cobertura.

Pendiente: cada integrante debe entender y defender su parte, rehacer o validar la demostración de forma independiente y redactar la conclusión crítica. El PDF de asignación prohíbe delegar demostración, conclusión o juicio crítico; la propuesta asistida es solo material de trabajo y no constituye evidencia de autoría o comprensión del equipo.
