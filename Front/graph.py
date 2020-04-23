import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('testgraphvalues.csv')

fig = go.Figure(go.Scatter(x=df['Time'], y=df['Value'], name='cmH2O'))

fig.update_layout(title='Pressure',
                  plot_bgcolor='rgb(230, 230,230)',
                  showlegend=True)

fig.show()

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False)