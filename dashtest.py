import dash
from dash import dcc, html, Input, Output
import plotly.graph_objs as go
from datetime import datetime, timedelta
import pandas as pd
import base64

# 예시 데이터 생성
start_date = datetime(2024, 1, 1)
date_list = [start_date + timedelta(days=x) for x in range(100)]
data = pd.DataFrame({'Date': date_list, 'Value': range(100)})

# 이미지 decoding
with open("simple1.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()

# Dash 앱 초기화
app = dash.Dash(__name__)

# 레이아웃 생성
app.layout = html.Div([
    # 그림 및 그래프 컨테이너
    html.Div([
        # 그림
        html.Div([
            html.Img(src='data:image/png;base64,{}'.format(encoded_string), style={'width': '15%'})
        ], className='three columns'),

        # 그래프
        html.Div([
            dcc.Graph(id='time-series-graph',)
        ], className='six columns'),

        # 컨텍스트
        html.Div([
            html.P("여기에 컨텍스트를 추가하세요.")
        ], className='three columns')
    ], className='row'),

])

# 콜백 함수: 최근 30일치 데이터 필터링
@app.callback(
    Output('hidden-div', 'children'),
    [Input('filter-button', 'n_clicks')]
)
def filter_data(n_clicks):
    if n_clicks is None:
        return data.to_json(date_format='iso', orient='split')
    else:
        thirty_days_ago = datetime.now() - timedelta(days=30)
        filtered_data = data[data['Date'] >= thirty_days_ago]
        return filtered_data.to_json(date_format='iso', orient='split')

# 콜백 함수: 그래프 업데이트
@app.callback(
    Output('time-series-graph', 'figure'),
    [Input('hidden-div', 'children')]
)
def update_graph(jsonified_data):
    data = pd.read_json(jsonified_data, orient='split')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Value'], mode='lines'))
    fig.update_layout(title='최근 30일 데이터', xaxis_title='날짜', yaxis_title='값')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
