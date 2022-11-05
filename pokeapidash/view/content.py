import dash_bootstrap_components as dbc
from dash import Dash, html

from pokeapidash.asset.style import CONTENT_STYLE
from pokeapidash.view.cards import card1

content = html.Div(
        dbc.Row(
                html.Div([dbc.Col([card1], md=4)], id='card1')
        ),
        dbc.Row(
                html.Div([dbc.Col([card1], md=4)], id='card2')
        ),
        id="page-content",
        style=CONTENT_STYLE
)
