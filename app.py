
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Datos simulados
df_sample = pd.DataFrame({
    'MonthlyCharges': [29.85, 56.95, 53.85, 42.30, 70.70, 99.65, 89.10, 29.75, 105.65, 81.45],
    'TotalCharges': [29.85, 1889.5, 108.15, 1840.75, 151.65, 820.5, 1949.4, 301.9, 3046.05, 819.85],
    'Churn': ['No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes']
})

model_results = pd.DataFrame({
    'Modelo': ['Random Forest (Tuned)', 'Logistic Regression (L1)', 'Logistic Regression (L2)'],
    'Accuracy': [0.78, 0.73, 0.73],
    'Precision': [0.58, 0.50, 0.50],
    'Recall': [0.63, 0.76, 0.77],
    'F1-score': [0.61, 0.60, 0.60],
    'AUC': [0.83, 0.83, 0.83]
})

app = Dash(__name__)
app.title = "Dashboard Proyecto Churn"

app.layout = html.Div([
    html.H1("📊 Dashboard Final – Cancelación de Clientes en Telecom", style={'textAlign': 'center'}),

    dcc.Tabs([
        dcc.Tab(label='🔍 Exploración de Datos', children=[
            html.H2("Distribuciones de Variables"),
            dcc.Graph(figure=px.histogram(df_sample, x='MonthlyCharges', color='Churn',
                                           title="Distribución de MonthlyCharges por Churn")),
            dcc.Graph(figure=px.box(df_sample, x='Churn', y='TotalCharges', color='Churn',
                                    title="Boxplot de TotalCharges por Churn", points="all"))
        ]),

        dcc.Tab(label='📈 Resultados de Modelos', children=[
            html.H2("Comparación de Modelos Predictivos"),
            dcc.Graph(figure=px.bar(
                model_results.melt(id_vars='Modelo', value_vars=['Accuracy', 'Precision', 'Recall', 'F1-score']),
                x='variable', y='value', color='Modelo', barmode='group',
                title="Métricas Comparativas", labels={'value': 'Valor', 'variable': 'Métrica'}
            )),
            dcc.Graph(figure=px.bar(model_results, x='Modelo', y='AUC', color='Modelo',
                                    title="Área bajo la curva (AUC) por modelo"))
        ]),

        dcc.Tab(label='📝 Conclusiones', children=[
            html.H2("Conclusiones del Análisis"),
            html.Ul([
                html.Li("🔹 Cargos mensuales altos están relacionados con mayor tasa de cancelación."),
                html.Li("🔹 Random Forest logra mayor exactitud global."),
                html.Li("🔹 Las regresiones logísticas son útiles para interpretar los factores de cancelación."),
                html.Li("🔹 Se identifican segmentos de alto riesgo para campañas comerciales específicas.")
            ])
        ]),

        dcc.Tab(label='📢 Recomendaciones Comerciales', children=[
            html.H2("Acciones Sugeridas"),
            html.Ul([
                html.Li("🎯 Ofrecer descuentos o beneficios a clientes con contrato mensual."),
                html.Li("📞 Activar alertas tempranas para clientes con alto riesgo de cancelación."),
                html.Li("💡 Promover contratos anuales con incentivos para clientes nuevos."),
                html.Li("📊 Evaluar campañas de retención basadas en perfil de riesgo.")
            ])
        ])
    ]),

    html.Div("Desarrollado por Jose Vega • javega.qro@gmail.com",
             style={'textAlign': 'center', 'marginTop': 30, 'color': '#888'})
])

if __name__ == "__main__":
    app.run(debug=True)
