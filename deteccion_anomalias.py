import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Cargar datos
df = pd.read_csv("data/notas_estudiantes.csv")

# Crear boxplot por asignatura
plt.figure(figsize=(10, 6))
sns.boxplot(x="Asignatura", y="Nota", data=df)
plt.title("Distribución de Notas por Asignatura")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/boxplot_anomalias.png")
plt.close()

# Calcular estadísticos y detectar outliers
resumen = []
for asignatura in df["Asignatura"].unique():
    notas = df[df["Asignatura"] == asignatura]["Nota"]
    q1 = notas.quantile(0.25)
    q3 = notas.quantile(0.75)
    iqr = q3 - q1
    outliers = df[(df["Asignatura"] == asignatura) & 
                  ((df["Nota"] < q1 - 1.5 * iqr) | (df["Nota"] > q3 + 1.5 * iqr))]
    resumen.append({
        "Asignatura": asignatura,
        "Media": round(notas.mean(), 2),
        "Outliers": len(outliers)
    })

# Guardar resumen en PDF
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, "Informe de Análisis de Anomalías en Notas", ln=True, align="C")
pdf.ln(10)

for r in resumen:
    pdf.cell(200, 10, f"{r['Asignatura']}: media {r['Media']}, outliers detectados: {r['Outliers']}", ln=True)

pdf.output("output/resumen_anomalias.pdf")

print("Análisis completado. Informe PDF generado.")
