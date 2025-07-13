import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Datos de ejemplo (fijos)
df_sample = pd.DataFrame({
    'MonthlyCharges': [29.85, 56.95, 53.85, 42.30, 70.70, 99.65, 89.10, 29.75, 105.65, 81.45],
    'TotalCharges': [29.85, 1889.5, 108.15, 1840.75, 151.65, 820.5, 1949.4, 301.9, 3046.05, 819.85],
    'Churn': ['No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes']
})

model_results_fixed = pd.DataFrame({
    'Modelo': ['Random Forest (Tuned)', 'Logistic Regression (L1)', 'Logistic Regression (L2)'],
    'Accuracy': [0.78, 0.73, 0.73],
    'Precision': [0.58, 0.50, 0.50],
    'Recall': [0.63, 0.76, 0.77],
    'F1-score': [0.61, 0.60, 0.60],
    'AUC': [0.83, 0.83, 0.83]
})

# Crear aplicación
app = Dash(__name__)
app.title = "Demo Dashboard Churn"

# Diseño del layout
app.layout = html.Div([
    html.H1("📊 Dashboard – Análisis de Cancelación de Clientes", style={'textAlign': 'center'}),

    html.H2("🔍 Análisis Exploratorio"),
    dcc.Graph(figure=px.histogram(df_sample, x='MonthlyCharges', color='Churn',
                                   title="Distribución de MonthlyCharges por Churn")),

    dcc.Graph(figure=px.box(df_sample, x='Churn', y='TotalCharges', color='Churn',
                            title="Distribución de TotalCharges por Churn", points="all")),

    dcc.Graph(figure=px.histogram(df_sample, x='Churn', title="Conteo de clientes con o sin cancelación")),

    html.H2("📈 Comparación de Modelos"),
    dcc.Graph(figure=px.bar(
        model_results_fixed.melt(id_vars='Modelo', value_vars=['Accuracy', 'Precision', 'Recall', 'F1-score']),
        x='variable', y='value', color='Modelo', barmode='group',
        title="Métricas comparativas de modelos", labels={'value': 'Valor', 'variable': 'Métrica'}
    )),

    dcc.Graph(figure=px.bar(model_results_fixed, x='Modelo', y='AUC', color='Modelo',
                            title="Comparación de AUC por Modelo")),

    html.H2("📝 Conclusiones"),
    html.Ul([
        html.Li("🔹 Los cargos mensuales altos están asociados a una mayor tasa de cancelación."),
        html.Li("🔹 Random Forest muestra buen rendimiento general."),
        html.Li("🔹 Los modelos de regresión tienen mejor capacidad de detección de clientes en riesgo."),
        html.Li("🔹 El análisis de características guía las estrategias de retención.")
    ]),

    html.Div("Demo desarrollada por Jose Vega • javega.qro@gmail.com",
             style={'textAlign': 'center', 'marginTop': 30, 'color': '#888'})
])

# Punto de entrada
if __name__ == "__main__":
    app.run(debug=True)
