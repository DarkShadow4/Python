import plotly
plotly.tools.set_credentials_file(username='DarkShadow', api_key='K0G7wWqtw1MahIt8mGmp')
plotly.tools.set_config_file(world_readable=True, sharing='public')
import plotly.plotly as py
from plotly.graph_objs import *
import plotly.graph_objs as go
# table = go.Table(header = dict(values=['A', 'B']), cells=dict(values=[[100, 90, 80, 90], [95, 85, 75, 95]]))
# data = [table]
trace0 = Scatter3d(
    x=[1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2],
    y=[1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2],
    z=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230]
)
trace1 = Scatter3d(
    x=[2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1],
    y=[2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1],
    z=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230]
)
data = Data([trace0, trace1])
py.iplot(data, filename='table1')
