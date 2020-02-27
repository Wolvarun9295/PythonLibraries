import plotly.graph_objs as go
import pandas as pd

data = pd.read_csv('/home/bridgelabz/Desktop/2014_usa_states.csv')

fig = go.Figure(data=go.Scatter(
    x=data['Postal'],
    y=data['Population'],
    mode='markers',
    marker_color=data['Population'],
    text=data['State'])
)

fig.update_layout(title='Population of USA')
fig.show()
