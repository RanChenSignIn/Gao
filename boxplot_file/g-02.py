import plotly.plotly as py
import matplotlib.pyplot as plt
import plotly.graph_objs as go
py.sign_in(username='cr187',api_key='18790656980')
# 注意：这里是plotly网站的用户名和密码
# import plotly
# py.sign_in(username='DemoAccount', api_key='lr1c37zw81')
x = ['day 1', 'day 1', 'day 1', 'day 1', 'day 1', 'day 1',
     'day 2', 'day 2', 'day 2', 'day 2', 'day 2', 'day 2']
trace0 = go.Box(
    y=[0.2, 0.2, 0.6, 1.0, 0.5, 0.4, 0.2, 0.7, 0.9, 0.1, 0.5, 0.3],
    x=x,
    name='kale',
    marker=dict(
        color='#3D9970'
    )
)
trace1 = go.Box(
    y=[0.6, 0.7, 0.3, 0.6, 0.0, 0.5, 0.7, 0.9, 0.5, 0.8, 0.7, 0.2],
    x=x,
    name='radishes',
    marker=dict(
        color='#FF4136'
    )
)
trace2 = go.Box(
    y=[0.1, 0.3, 0.1, 0.9, 0.6, 0.6, 0.9, 1.0, 0.3, 0.6, 0.8, 0.5],
    x=x,
    name='carrots',
    marker=dict(
        color='#FF851B'
    )
)
data = [trace0, trace1, trace2]
layout = go.Layout(
    yaxis=dict(
        title='normalized moisture',
        zeroline=False
    ),
    boxmode='group'
)
fig = go.Figure(data=data, layout=layout)
plt.show(fig)
#py.iplot(fig)

"""

"""

