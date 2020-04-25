import dash
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html


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
                daq.GraduatedBar(
                    id='O2 Concentration Slider',
                    min=20,
                    max=100,
                    step=5,
                    value=30,
                ),
                daq.GraduatedBar(
                    id='PEEP Slider',
                    min=0,
                    max=50,
                    step=1,
                    value=20,
                ),
                daq.GraduatedBar(
                    id='Resp Rate Slider',
                    min=6,
                    max=40,
                    step=1,
                    value=20,
                ),
                daq.GraduatedBar(
                    id='Tidal Volume Slider',
                    min=500,
                    max=2000,
                    step=20,
                    value=1000,
                )
            ]
        )

    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
