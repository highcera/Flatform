# import dash_app
# import dash_core_components as dcc
# import dash_html_components as html
# import plotly.express as px
# import pandas as pd

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash_app.Dash(__name__, external_stylesheets=external_stylesheets)

# df1 = pd.read_csv('result0219.csv')

# fig = px.bar(df1, x="지점", y="수량(int)", color="제품타입")

# app.layout = html.Div(children=[
#     html.H1(children='Dsah Board'),

#     html.Div(children='''
#         작업 대쉬 보드 
#     '''),

#     dcc.Graph(
#         id='example-graph',
#         figure=fig
#     )
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)

#!/usr/bin/python
# -*- coding: <encoding name> -*-


# import plotly.graph_objects as go
# fig = go.Figure()
# fig.add_trace(go.Bar(x=[1, 2, 3], y=[1, 3, 2]))
# fig.show()

# import plotly.express as px

# # 데이터 불러오기
# df = px.data.iris()

# # express를 활용한 scatter plot 생성
# fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
#                  title="Using The add_trace() method With A Plotly Express Figure")

# fig.add_trace(
#     go.Scatter(
#         x=[2, 4],
#         y=[4, 8],
#         mode="lines",
#         line=go.scatter.Line(color="gray"),
#         showlegend=False)
# )

# fig.show()

# from plotly.subplots import make_subplots

# # subplot 생성
# fig = make_subplots(rows=1, cols=2)

# # Trace 추가하기
# fig.add_scatter(y=[4, 2, 3.5], mode="markers",
#                 marker=dict(size=20, color="LightSeaGreen"),
#                 name="a", row=1, col=1)

# fig.add_bar(y=[2, 1, 3],
#             marker=dict(color="MediumPurple"),
#             name="b", row=1, col=1)

# fig.add_scatter(y=[2, 3.5, 4], mode="markers",
#                 marker=dict(size=20, color="MediumPurple"),
#                 name="c", row=1, col=2)

# fig.add_bar(y=[1, 3, 2],
#             marker=dict(color="LightSeaGreen"),
#             name="d", row=1, col=2)

# # 한번에 Bar plot 만 파란색으로 바꾸기
# fig.update_traces(marker=dict(color="RoyalBlue"),
#                   selector=dict(type="bar"))

# fig.show()

# # Seaborn 패키지 불러오기
# import plotly.express as px

# # 선거 데이터 불러오기
# election = px.data.election()
# print(election.head())

# import plotly.express as px

# #데이터 불러오기
# df = px.data.iris()

# #그래프 그리기
# fig = px.scatter(df, x="petal_length", y="petal_width")

# # 수직 사각 영 추가하기
# fig.add_vrect(x0=3, x1=5, line_width=0, fillcolor="green", opacity=0.2,
#               annotation_text="수직 영역", 
#               annotation_position="bottom right",
#               annotation_font_size=20,
#               annotation_font_color="green",
#               annotation_font_family="Times New Roman")

# # 수평 사각 영역 추가하기
# fig.add_hrect(y0=0.9, y1=1.5, line_width=0, fillcolor="red", opacity=0.2,
#               annotation_text="수 영역", 
#               annotation_position="top left",
#               annotation_font_size=20,
#               annotation_font_color="red",
#               annotation_font_family="Times New Roman")

# fig.show()

# import plotly.express as px

# # 주식 데이터 불러오기
# df = px.data.stocks(indexed=True)

# # 그래프 그리기
# fig = px.line(df)

# # 수평선 그리기
# fig.add_hline(y=1, line_dash="dot",
#               annotation_text="Jan 1, 2018 baseline", 
#               annotation_position="bottom right",
#               annotation_font_size=20,
#               annotation_font_color="blue"
#              )

# # 수직 영역 표시
# fig.add_vrect(x0="2018-09-24", x1="2018-12-18", 
#               annotation_text="decline", annotation_position="top left",
#               annotation=dict(font_size=20, font_family="Times New Roman"),
#               fillcolor="green", opacity=0.25, line_width=0)

# fig.show()


# # 

# import pandas as pd
# pd.options.plotting.backend = "plotly"

# import pandas as pd

# pd.options.plotting.backend = "plotly"

# df = pd.DataFrame(dict(a=[1,3,2], b=[3,2,1]))
# fig = df.plot()
# fig.show()

# import plotly.graph_objects as go
# import pandas as pd

# # 데이터 불러오기
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

# # Figure 생성
# fig = go.Figure()
# fig.add_trace(go.Candlestick(x=df['Date'],open=df['AAPL.Open'],high=df['AAPL.High'],low=df['AAPL.Low'],close=df['AAPL.Close']))

# fig.show()

# import chart_studio
# from chart_studio.plotly import plot, iplot
import plotly.graph_objects as go
import plotly.express as px

# chart_studio.tools.set_credentials_file(username='highcera', api_key='7gVlCpJzQShoh0EYUMed')


# Plotly 문법으로 그래프 생성하기
# fig = go.Figure(data=go.Bar(x=[1, 2, 3], y=[1, 3, 2]))
# fig.show()
# plot(fig, filename =  'FileName', auto_open=True)

# import plotly.express as px

# 주식 데이터 불러오기
df = px.data.stocks(indexed=True)

# 그래프 그리기
fig = px.line(df)

# 수평선 그리기
fig.add_hline(y=1, line_dash="dot",
              annotation_text="Jan 1, 2018 baseline", 
              annotation_position="bottom right",
              annotation_font_size=20,
              annotation_font_color="blue"
             )

# 수직 영역 표시
fig.add_vrect(x0="2018-09-24", x1="2018-12-18", 
              annotation_text="decline", annotation_position="top left",
              annotation=dict(font_size=20, font_family="Times New Roman"),
              fillcolor="green", opacity=0.25, line_width=0)

fig.show()

# plot(fig, filename =  'stock_plot', auto_open=True)