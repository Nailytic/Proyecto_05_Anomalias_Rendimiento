# 📄 Informe Técnico – Proyecto 05: Detección de Anomalías en Notas

## 🎯 Objetivo del Proyecto

Aplicar técnicas estadísticas para identificar valores atípicos en las calificaciones académicas de estudiantes, segmentadas por asignatura, grupo y centro educativo.

---

## 📊 Dataset

- 300 estudiantes
- 6 asignaturas
- Centros: 5
- Grupos: A y B
- Notas entre 0 y 10 con outliers simulados

---

## 🧠 Metodología

- Análisis por Asignatura
- Cálculo de IQR (Rango Intercuartílico)
- Detección de outliers:
  - Valores < Q1 - 1.5 × IQR
  - Valores > Q3 + 1.5 × IQR

---

## 📈 Resultados

- Visualización: Boxplot por asignatura
- Informe generado: `resumen_anomalias.pdf`
- Recuento de outliers por asignatura

---

## ✅ Conclusión

Este análisis permite detectar casos extremos en evaluaciones escolares, lo cual es útil para análisis de calidad, rendimiento académico, y posibles errores en la introducción de datos.

**Autora:** Naiara Rodríguez  
**Fecha:** Abril 2025  
**Licencia:** MIT
