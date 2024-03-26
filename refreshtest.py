import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

import time
import random

import pandas as pd


# Dash 앱 초기화555
app = dash.Dash(__name__)

# 데이터 read
df = pd.read_csv('./onlinefoods.csv')
print(df.head())

# 레이아웃 생성
app.layout = html.Div([
        html.Div([
        # 그래프
        dcc.Graph(id='live-update-graph',),

        # Interval 컴포넌트: 10초마다 새로고침
        dcc.Interval(
            id='interval-component',
            interval=1*1000,  # 5초마다 새로고침 (단위: 밀리초)
            n_intervals=0
        )
    ]),
    html.Div([
        dcc.Graph(id = 'graph2'),

        dcc.Interval(
            id='interval-component',
            interval=1*1000,  # 5초마다 새로고침 (단위: 밀리초)
            n_intervals=0
        )
    ])
], style={'display': 'flex'})


# 콜백 함수: 그래프 업데이트
@app.callback(
    Output('live-update-graph', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_graph_live(n):
    x_data = df['Family size'].to_list()
    y_data = df['longitude'].to_list()

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_data, y=y_data, mode='markers'))

    fig.update_layout(title='sctter related foods',
                      width = 500,
                      height= 500,
                      xaxis={'title': 'X Axis'},  # X축 제목
                    yaxis={'title': 'Y Axis'},)  # Y축 제목)

    return fig

@app.callback(
    Output('graph2', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_graph_live(n):
    x_data = df['latitude'].to_list()
    y_data = df['longitude'].to_list()

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_data, y=y_data, mode='markers'))

    fig.update_layout(title='sctter related foods',
                      width = 500,
                      height= 500,
                      xaxis={'title': 'X Axis'},  # X축 제목
                    yaxis={'title': 'Y Axis'},)  # Y축 제목)

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
