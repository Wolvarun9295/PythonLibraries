import plotly.graph_objs as go
import numpy as np
from plotly.offline import *

N = 1000
randomX = np.random.randn(N)
randomY = np.random.randn(N)

trace = go.Scatter(
    x=randomX,
    y=randomY,
    mode='markers'
)

data = [trace]

offline.plot(data, filename='1000Scatter')
