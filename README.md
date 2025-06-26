# 📊 Proyecto Final Data Scientist – Telecom

## 🎯 Objetivo del Proyecto

El objetivo de este proyecto es predecir la cancelación de clientes mediante el análisis de los datos proporcionados por la compañía Telecom. A partir de los resultados, se podrán identificar usuarios con alto riesgo de abandono y ofrecerles promociones o paquetes personalizados para mejorar la retención.

## 🗂️ Fuentes de Datos

El análisis se basa en la integración de los siguientes archivos:

- `contract.csv`: información contractual del cliente.
- `personal.csv`: datos personales del cliente.
- `internet.csv`: detalles sobre los servicios de internet contratados.
- `phone.csv`: servicios de telefonía y llamadas.

Todos los archivos están relacionados mediante el campo `customerID`.

## 🛠️ Plan de Trabajo

1. Crear proyecto en Github
* Creación de Readme para presentación del proyecto.
* Manejo de control de versiones.

2. Carga y consolidación de datos
* Cargar los archivos: contract.csv, personal.csv, internet.csv, phone.csv.
* Unirlos utilizando customerID como clave principal.
* Verificar dimensiones, columnas y tipos de datos.

3. Importación de bibliotecas
* Importar librerías necesarias como pandas, numpy, matplotlib, seaborn, sklearn, etc.

4. Análisis exploratorio de datos (EDA)
* Revisión general del conjunto de datos.
* Detección y tratamiento de valores nulos.
* Análisis univariado (distribución de variables).
* Análisis bivariado con la variable objetivo.

Visualizaciones clave: - Barras, histogramas, mapas de calor, boxplots. - Análisis de correlaciones.

5. Preprocesamiento de datos
* Codificación de variables categóricas (LabelEncoder, OneHotEncoder).
* Conversión de tipos de datos.
* Imputación de valores faltantes si aplica.
* Normalización de variables numéricas.
* División de datos en conjunto de entrenamiento y prueba.

6. Balanceo de clases
* Verificar si la variable objetivo está desbalanceada.
* Aplicar técnicas de balanceo:
  - Submuestreo de la clase mayoritaria.
  - Sobremuestreo.

7. Entrenamiento de modelos predictivos
* Probar varios algoritmos:
  - Regresión Logística
  - Árboles de Decisión
  - Random Forest
  - Gradient Boosting (XGBoost, LightGBM, CatBoost)
* Ajuste de hiperparámetros.

8. Evaluación de modelos
* Métricas de evaluación:
  - Accuracy, Precision, Recall, F1-score
* Matriz de confusión
* Curva ROC y AUC
* Comparación de modelos para elegir el mejor.

9. Interpretación y explicación del modelo
* Feature importance: ¿Qué factores influyen más en la cancelación?
* Perfil típico de cliente propenso a cancelar.

10. Propuesta de acciones comerciales
* Diseño de estrategias de retención basadas en los insights:
* Segmentos con mayor riesgo
* Ofertas específicas para cada tipo de cliente (desarrollar promociones).
* Automatización de alertas para clientes en riesgo.

11. Conclusiones y recomendaciones
* Resumen de hallazgos clave.
* Modelo elegido y su rendimiento.
* Recomendaciones prácticas para el negocio.

## ✅ Seguimiento de Avances

El proyecto incluye una tabla de control.

![alt text](https://github.com/javega33/proyecto_final/blob/docs/crono.png?raw=true)
<img src="https://github.com/javega33/proyecto_final/blob/docs/crono.png" height="35" width="35">

### Leyenda de Estado

- ⬜ Pendiente
- 🟡 En proceso
- ✅ Completado
