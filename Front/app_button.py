import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_daq as daq
from dash.dependencies import Input, Output



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    daq.LEDDisplay(
        id='num-display',
        label="Default",
        value=0
    ),
    html.Button('-', id='decrement-button'),
    html.Button('+', id='increment-button'),
])


@app.callback(
    Output('num-display', 'value'),
    [Input('decrement-button', 'n_clicks'),
     Input('increment-button', 'n_clicks')],
    [dash.dependencies.State('num-display', 'value')])
def handle_button_press(n_click1, n_click2, value):
    ctx = dash.callback_context

    if not ctx.triggered:
        button_id = ''
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if (button_id == "decrement-button"):
        value -= 1
    elif (button_id == "increment-button"):
        value += 1
    return value

if __name__ == '__main__':
    app.run_server(debug=True)