import dash_bootstrap_components as dbc
from dash import html, dcc

from pokeapidash.asset.style import SIDEBAR_STYLE
from pokeapidash.utils.helpers import get_generation, get_region, get_pokemon_by_region

sidebar = html.Div(
        [
            html.H2("PokeApi", className="display-4"),
            html.Hr(),
            html.P(
                    "Pokemon Generation", className="lead"
            ),
            dbc.Nav(
                    [
                        dcc.Dropdown(options=get_region(), id='region_dropdown'),
                        html.Hr(),
                        html.P("Pokemon", className="lead"),
                        dcc.Dropdown(options=get_pokemon_by_region(), id='pokemon_dropdown'),
                        html.Br(),
                        dbc.Button("Refresh Report", className="refresh"),
                    ],
                    vertical=True,
                    pills=True,
            )
        ],
        style=SIDEBAR_STYLE,
)
