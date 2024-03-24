import pandas as pd
import numpy as np
import plotly.graph_objs as go
from dash import Dash, dcc, html

# 시뮬레이션을 위한 가상의 데이터 생성
np.random.seed(42)  # 결과의 일관성을 위한 난수 시드 설정
data = {
    "Date": pd.date_range(start="2023-01-01", periods=100),
    "Value": np.random.rand(100).cumsum()  # 누적 합을 사용하여 가상의 시계열 데이터 생성
}
df = pd.DataFrame(data)

# 예측값 계산 및 실제 값과 비교하여 색상 결정
colors = ['blue'] * (len(df) - 2) + ['blue', 'blue']  # 마지막 두 포인트는 비교 대상이 아니므로 기본 색상을 설정

for i in range(len(df) - 2):
    # 포인트 i와 i+1 사이의 기울기 계산
    slope = (df['Value'].iloc[i+1] - df['Value'].iloc[i]) / (df.index[i+1] - df.index[i])
    # 포인트 i+2에 대한 예측값 계산
    predicted_value = df['Value'].iloc[i+1] + slope
    # 실제 값이 예측값보다 크면 색상을 빨간색으로 설정
    if df['Value'].iloc[i+2] > predicted_value:
        colors[i+2] = 'red'

# Dash 애플리케이션 초기화
app = Dash(__name__)

# 앱 레이아웃 설정
app.layout = html.Div(children=[
    dcc.Graph(
        id='time-series-plot',
        figure={
            'data': [
                go.Scatter(
                    x=df['Date'],
                    y=df['Value'],
                    mode='markers+lines',
                    marker=dict(color=colors),
                    name='Values'
                )
            ],
            'layout': go.Layout(
                title='Time Series Analysis with Linear Prediction Highlighting',
                xaxis={'title': 'Date'},
                yaxis={'title': 'Value'}
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
