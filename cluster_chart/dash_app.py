import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import os
from dotenv import load_dotenv 
load_dotenv()

# Загрузка данных для графиков
elbow_data = pd.read_csv('data/elbow_data.csv')
cluster_data = pd.read_csv('data/clustered_messages.csv')
tsne_data = pd.read_csv('data/tsne_data.csv')
time_data = pd.read_csv('data/output.csv')  # Загрузка данных средних метрик

# Агрегация данных по кластеру и подсчет количества сообщений в каждом кластере
cluster_counts = cluster_data['cluster'].value_counts().reset_index()
cluster_counts.columns = ['cluster', 'count']

# Фигуры с использованием Plotly Express
fig_elbow = px.line(elbow_data, x='Clusters', y='Inertia', title='Elbow Method For Optimal k', markers=True)
fig_clusters = px.bar(cluster_counts, x='cluster', y='count', title='Frequency of Messages by Cluster')
fig_tsne = px.scatter(tsne_data, x='t-SNE Feature 1', y='t-SNE Feature 2', color='cluster', title='t-SNE Visualization of Message Embeddings')
fig_avg_duration = px.bar(time_data, x='ClusterIndex', y='AvgDuration', title='Average Duration by Cluster')
fig_avg_reaction = px.bar(time_data, x='ClusterIndex', y='AvgReaction', title='Average Reaction by Cluster')
fig_median_duration = px.bar(time_data, x='ClusterIndex', y='MedianDuration', title='Histogram of Median Durations by Cluster')
fig_median_reaction = px.bar(time_data, x='ClusterIndex', y='MedianReaction', title='Histogram of Median Reactions by Cluster')

graph_style = {
    'width': '30%',        
    'display': 'inline-block',
    'padding': '0 20px'
}

# Инициализация Dash приложения
dash_app = dash.Dash(__name__)

# Определение макета приложения
dash_app.layout = html.Div(children=[
    html.H1(children='Data Visualization Dashboard'),
    
    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
    dcc.Interval(
        id='interval-component',
        interval=1*300000,  # in milliseconds
        n_intervals=0
    ),

    dcc.Graph(
        id='elbow-method-graph',
        figure=fig_elbow,
        style=graph_style
    ),
    
    dcc.Graph(
        id='cluster-frequency-graph',
        figure=fig_clusters,
        style=graph_style
    ),
    
    dcc.Graph(
        id='tsne-visualization-graph',
        figure=fig_tsne,
        style=graph_style
    ),
    
    dcc.Graph(
        id='average-duration-graph',
        figure=fig_avg_duration,
        style=graph_style
    ),

    dcc.Graph(
        id='average-reaction-graph',
        figure=fig_avg_reaction,
        style=graph_style
    ),

    dcc.Graph(
        id='median-duration-histogram',
        figure=fig_median_duration,
        style=graph_style
    ),

    dcc.Graph(
        id='median-reaction-histogram',
        figure=fig_median_reaction,
        style=graph_style
    )
])

# Запуск сервера
if __name__ == '__main__':
    dash_app.run_server(host=os.getenv('PY_CHART_HOST'), debug=True, port=int(os.getenv('PY_CHART_PORT')))
