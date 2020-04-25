import dash
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div(
    children=[
        html.Div(id='hidden-div', style={'display': 'none'}),
        html.H1(children='Hello World'),

        html.Div(children='''
            Dash: A web application framework for Python. Also, Beth sucks!
        '''),
        html.Div(
            id="Graduated Bars",
            children=[
                daq.Slider(
                    id='O2 Concentration Slider',
                    min=20,
                    size=400,
                    max=100,
                    step=5,
                    value=30,
                ),
                daq.Slider(
                    id='PEEP Slider',
                    min=0,
                    size=400,
                    max=50,
                    step=1,
                    value=20,
                ),
                daq.Slider(
                    id='Resp Rate Slider',
                    min=6,
                    size=400,
                    max=40,
                    step=1,
                    value=20,
                ),
                daq.Slider(
                    id='Tidal Volume Slider',
                    min=500,
                    size=400,
                    max=2000,
                    step=20,
                    value=1000,
                )
            ]
        )

    ]
)


@app.callback(
    Output('hidden-div', 'children'),
    [Input('O2 Concentration Slider', component_property='value'),
     Input('PEEP Slider', component_property='value'),
     Input('Resp Rate Slider', component_property='value'),
     Input('Tidal Volume Slider', component_property='value')])
def slider_update(O2Value, PeepSlider, RespRateSlider, TidalVolumeSlider):
    ctx = dash.callback_context
    if not ctx.triggered:
        return
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    values = {
        'O2 Concentration Slider': O2Value,
        'PEEP Slider': PeepSlider,
        'Resp Rate Slider': RespRateSlider,
        'Tidal Volume Slider': TidalVolumeSlider
    }
    print('Updated:', button_id)
    print('Value:', values[button_id])


if __name__ == '__main__':
    app.run_server(debug=True)
