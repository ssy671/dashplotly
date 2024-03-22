import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import time
import random
# Dash 앱 초기화
app = dash.Dash(__nagit add .me__)

# 레이아웃 생성
app.layout = html.Div([
    # 그래프
    dcc.Graph(id='live-update-graph'),

    # Interval 컴포넌트: 10초마다 새로고침
    dcc.Interval(
        id='interval-component',
        interval=5*1000,  # 10초마다 새로고침 (단위: 밀리초)
        n_intervals=0
    )
])

# push test 잘되는거같구만
# push 확인!!
# 다시 시도!!!!
#반댜로 가즈베리에서 pc 로!!
# 잘되는거같긴한데 다시 연습!!
# 연습 add . - commit -m - push origin master

# 다시 역으로 테스트
###jjfjf

# 콜백 함수: 그래프 업데이트
@app.callback(
    Output('live-update-graph', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_graph_live(n):
    # 예시 데이터 생성
    data = {
        'x': [random.randint(1, 100) for _ in range(4)],
        'y': [random.randint(1, 100) for _ in range(4)],
        'type': 'line',
        'name': '데이터'
    }

    return {'data': [data], 'layout': {'title': '실시간 업데이트 그래프'}}

if __name__ == '__main__':
    app.run_server(debug=True)
