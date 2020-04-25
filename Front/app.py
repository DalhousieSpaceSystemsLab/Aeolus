import dash
import dash_core_components as dcc
import dash_html_components as html
import datetime
import json
from random import randint

from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div(
    children=[
        html.Div(children=[
            html.Div(children=[
                html.Div(children=[
                    html.Div(html.Div(children=[html.Div('Graph 1')]),
                             style={"color": "white", "height": "33%"},
                             className='box'),
                    html.Div(html.Div(children=[html.Div('Graph 2')]),
                             style={"color": "white", "height": "33%"},
                             className='box'),
                    html.Div(html.Div(children=[html.Div('Graph 3')]),
                             style={"color": "white", "height": "33%"},
                             className='box'),
                ], className='graphs'),
                html.Div(children=[
                    html.Div(html.Div(children=[html.Div('O2 slider')]),
                             style={"color": "white"},
                             className='box'),
                    html.Div(html.Div(children=[html.Div('PEEP slider')]),
                             style={"color": "white"},
                             className='box'),
                    html.Div(html.Div(children=[html.Div('Resp Rate')]),
                             style={"color": "white"},
                             className='box'),
                    html.Div(html.Div(children=[html.Div('Tidal Vol Slider')]),
                             style={"color": "white"},
                             className='box'),
                ], className='sliders'),
            ], style={"width": "75%"}),
            html.Div(children=[
                html.Div(children=[
                    html.Div(
                        children=[html.Div('Volume Control'), html.Div(id='live-update-text', style={'fontSize': 10})]),
                    html.Img(src=app.get_asset_url('aeolus_logo.png'), style={"height": "40px", "width": "40px"})],
                    style={"color": "white"},
                    className='box'),
                html.Div(children=[
                    html.Div(children=[html.Div('Ppeak'), html.Div('cmH20', style={'fontSize': 10})]),
                    html.Div(id='ppeak', style={'fontSize': 20})],
                    style={"color": "yellow"},
                    className='box'),
                html.Div(children=[
                    html.Div(children=[html.Div('Pmean'), html.Div('cmH20', style={'fontSize': 10})]),
                    html.Div(id="pmean", style={'fontSize': 20})],
                    style={"color": "yellow"},
                    className='box'),
                html.Div(children=[
                    html.Div(children=[html.Div('Peep'), html.Div('cmH20', style={'fontSize': 10})]),
                    html.Div(id='peep', style={'fontSize': 20})],
                    style={"color": "yellow"},
                    className='box'),
                html.Div(children=[
                    html.Div(children=[html.Div('RR'), html.Div('b/min', style={'fontSize': 10})]),

                    html.Div(children=[html.Div(id='rr', style={'fontSize': 20, "marginRight": 20}),
                                       html.Div(children=[html.Div('35', style={'marginBottom': 10}), html.Div('5')])]
                             , style={'fontSize': 10, "display": "flex", "alignItems": "center"})],
                    style={"color": "green"},
                    className='box'),
                html.Div(children=[
                    html.Div(children=[html.Div('02 (%)'), html.Div('T/Ttot', style={'fontSize': 10})]),

                    html.Div(children=[html.Div(id='o2', style={'fontSize': 20, "marginRight": 20}),
                                       html.Div(children=[html.Div('65', style={'marginBottom': 10}), html.Div('55')])]
                             , style={'fontSize': 10, "display": "flex", "alignItems": "center"})],
                    style={"color": "green"},
                    className='box'),
                html.Div(children=[
                    html.Div(children=[html.Div('MVe (c)'), html.Div('l/min', style={'fontSize': 10})]),

                    html.Div(children=[html.Div(id='mve', style={'fontSize': 20, "marginRight": 20}),
                                       html.Div(
                                           children=[html.Div('20.0', style={'marginBottom': 10}), html.Div('3.0')])]
                             , style={'fontSize': 10, "display": "flex", "alignItems": "center"})],
                    style={"color": "cornflowerblue"},
                    className='box'),
                html.Div(children=[
                    html.Div(children=[html.Div('VTi'), html.Div('ml', style={'fontSize': 10})]),
                    html.Div(id='vti', style={'fontSize': 20})],
                    style={"color": "cornflowerblue"},
                    className='box'),
                html.Div(children=[
                    html.Div(children=[html.Div('VTe'), html.Div('ml', style={'fontSize': 10})]),
                    html.Div(id='vte', style={'fontSize': 20})],
                    style={"color": "cornflowerblue"},
                    className='box'),
            ], className='values'),
            dcc.Interval(
                id='interval-component',
                interval=1 * 300,  # in milliseconds
                n_intervals=0
            )
        ], style={"display": "flex"}),
        html.Div(children=[
            html.Div(html.Div(children=[html.Div('Additional Settings')]),
                     style={"color": "white", "width": "30%"},
                     className='box'),
            html.Div(html.Div(children=[html.Div('Patient')]),
                     style={"color": "white", "width": "20%"},
                     className='box'),
            html.Div(html.Div(children=[html.Div('I:E')]),
                     style={"color": "white", "width": "25%"},
                     className='box'),
            html.Div(html.Div(children=[html.Div('Additional Values')]),
                     style={"color": "white", "width": "25%"},
                     className='box'),
        ], className='settings'),
    ]
)


@app.callback(Output('live-update-text', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_date(n):
    return [html.P(datetime.datetime.now().strftime("%x %X"))]


@app.callback([
    Output('ppeak', 'children'),
    Output('pmean', 'children'),
    Output('peep', 'children'),
    Output('rr', 'children'),
    Output('o2', 'children'),
    Output('mve', 'children'),
    Output('vti', 'children'),
    Output('vte', 'children'),
], [Input('interval-component', 'n_intervals')])
def update_values(n):
    with open('assets/test.txt') as json_file:
        data = json.load(json_file)
        ppeak = [html.P(data["ppeak"])]
        pmean = [html.P(randint(0, 10))]
        peep = [html.P(data["peep"])]
        rr = [html.P(data["rr"])]
        o2 = [html.P(data["o2"])]
        mve = [html.P(data["mve"])]
        vti = [html.P(data["vti"])]
        vte = [html.P(data["vte"])]

    return ppeak, pmean, peep, rr, o2, mve, vti, vte


if __name__ == '__main__':
    app.run_server(debug=True)
