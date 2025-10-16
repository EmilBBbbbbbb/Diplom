import plotly.graph_objects as go
from db.core import table_to_df, engine
import pandas as pd


df = table_to_df(table_name='sliver')

fig = go.Figure(data=[go.Candlestick(x=df['date'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])])

fig.show()