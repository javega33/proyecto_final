import dash
from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from sklearn.metrics import roc_curve, auc

# Simulación de resultados finales (sustituye por tus resultados reales)
models_tuned_results = pd.DataFrame({
    'Modelo': ['Random Forest (Tuned)', 'Logistic Regression (L1)', 'Logistic Regression (L2)'],
    'Accuracy': [0.780, 0.731, 0.732],
    'Precision': [0.578, 0.496, 0.497],
    'Recall': [0.636, 0.765, 0.767],
    'F1-score': [0.606, 0.601, 0.604],
    'AUC': [0.826, 0.829, 0.829]
})

# Crear gráfico de barras comparativo
metrics = ['Accuracy', 'Precision', 'Recall', 'F1-score']
df_melted = models_tuned_results.melt(id_vars='Modelo', value_vars=metrics, var_name='Métrica', value_name='Valor')
fig_metrics = px.bar(df_melted, x='Métrica', y='Valor', color='Modelo', barmode='group',
                     title="Comparación de Métricas por Modelo", range_y=[0,1])

# Gráfico AUC
fig_auc = px.bar(models_tuned_results, x='Modelo', y='AUC', title='AUC por Modelo', range_y=[0,1])

# Curva ROC simulada (sustituye por tus valores reales)
fpr_rf = [0.0, 0.1, 0.3, 1.0]
tpr_rf = [0.0, 0.6, 0.8, 1.0]
roc_auc_rf = 0.826

fig_roc = go.Figure()
fig_roc.add_trace(go.Scatter(x=fpr_rf, y=tpr_rf, mode='lines', name=f'Random Forest (AUC={roc_auc_rf:.3f})'))
fig_roc.add_trace(go.Scatter(x=[0,1], y=[0,1], mode='lines', line=dict(dash='dash'), name='Random'))
fig_roc.update_layout(title='Curva ROC – Random Forest (Tuned)',
                      xaxis_title='False Positive Rate', yaxis_title='True Positive Rate')

# Inicializar app Dash
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Dashboard de Modelos Predictivos – Churn Telecom'),

    html.Div(children='Comparación de métricas de modelos entrenados.'),

    dcc.Graph(
        id='metrics-graph',
        figure=fig_metrics
    ),

    dcc.Graph(
        id='auc-graph',
        figure=fig_auc
    ),

    dcc.Graph(
        id='roc-graph',
        figure=fig_roc
    )
])

if __name__ == '__main__':
    app.run(debug=True)