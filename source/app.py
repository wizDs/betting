import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from BetVsOneself import BetVsOneself
from typing import List

class Callback:

    def __init__(self, excess_return: float, implied_prob: List[float]):

        returns_rounded       = self.floatToPct(excess_return)
        implied_prob_rounded = [self.floatToPct(p) for p in implied_prob]

        
        self.implied_prob1 = 'Implicit probability outcome 1: {}%'.format(implied_prob_rounded[0])
        self.implied_prob2 = 'Implicit probability outcome 2: {}%'.format(implied_prob_rounded[1])

        if excess_return > 0:
            self.excess_return = 'Return: {}%'.format(returns_rounded)
        else:
            self.excess_return = 'Cost: {}%'.format(returns_rounded)



    def floatToPct(self, x: float) -> float:
        return "{:.2f}".format(x * 100)


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div(["Odds outcome 1: ", dcc.Input(id='b1', value=8, type='number',    min=0, max=1000, step=0.01)]),
    html.Div(["Odds outcome 2: ", dcc.Input(id='b2', value=1.04, type='number', min=0, max=1000, step=0.01)]),
    html.Br(),
    html.Div(id='excess_return'),
    html.Div(id='implied1'),
    html.Div(id='implied2'),
    html.Br(),
])


@app.callback(
    Output(component_id='excess_return', component_property='children'),
    Output(component_id='implied1', component_property='children'),
    Output(component_id='implied2', component_property='children'),
    Input(component_id='b1', component_property='value'),
    Input(component_id='b2', component_property='value'),
)
def update_output_div(*args):
    betVsOneself = BetVsOneself(*args)

    infos = Callback(betVsOneself.excess_return, betVsOneself.implied_prob)

    return infos.excess_return, infos.implied_prob1, infos.implied_prob2

if __name__ == '__main__':
    app.run_server(debug=True)