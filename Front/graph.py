import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('testgraphvalues.csv')

pressure = go.Figure(go.Scatter(x=df['Time'], y=df['Value'], name='cmH2O',
                                marker=dict(color='#F0CF45')))
pressure.update_layout(title='Pressure',
                       plot_bgcolor='#000000',
                       showlegend=True)

oxygen = go.Figure(go.Scatter(x=df['Time'], y=df['Value'], name='l/min',
                              marker=dict(color='#15A71B')))
oxygen.update_layout(title='Oxygen',
                     plot_bgcolor='#000000',
                     showlegend=True)

volume = go.Figure(go.Scatter(x=df['Time'], y=df['Value'], name='mL',
                              marker=dict(color='#6A96DD')))
volume.update_layout(title='Volume',
                     plot_bgcolor='#000000',
                     showlegend=True)

app = dash.Dash(__name__)
app.layout = html.Div([
    html.Div([
        dcc.Graph(
            id='pressure',
            figure=pressure
        ),
    ]),
    html.Div([
        dcc.Graph(
            id='oxygen',
            figure=oxygen),
    ]),
    html.Div([
        dcc.Graph(
            id='volume',
            figure=volume),
    ]),
])


if __name__ == '__main__':
    app.run_server(debug=True)
