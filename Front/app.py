import dash
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
app = dash.Dash()

app.layout = html.Div(
    children=[
        html.H1(children='Hello Dah'),

        html.Div(children='''
            Dash: A web application framework for Python. Also, Beth sucks!
        '''),

        dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'SF'}
                ],
                'layout': {
                    'title': 'Dash Data Visualization'
                }
            }
        ),
        html.Div(
            id="Graduated Bars",
            children=[
                daq.Slider(
                    id='O2 Concentration Slider',
                    min=20,
                    size=400,
                    max=100,
                    step=5,
                    handleLabel={"showCurrentValue": True, "label": "O2%"},
                    value=30,
                ),
                daq.Slider(
                    id='PEEP Slider',
                    min=0,
                    size=400,
                    max=50,
                    step=1,
                    handleLabel={"showCurrentValue": True, "label": "cmH2O"},
                    value=20,
                ),
                daq.Slider(
                    id='Resp Rate Slider',
                    min=6,
                    size=400,
                    max=40,
                    step=1,
                    handleLabel={"showCurrentValue": True, "label": "b/min"},
                    value=20,
                ),
                daq.Slider(
                    id='Tidal Volume Slider',
                    min=500,
                    size=400,
                    max=2000,
                    step=20,
                    handleLabel={"showCurrentValue": True, "label": "ml"},
                    value=1000,
                )
            ]
        )

    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
