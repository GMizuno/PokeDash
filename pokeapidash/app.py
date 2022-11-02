from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

from pokeapidash.utils.helpers import get_generation, get_region

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Pokeapi", className="display-4"),
        html.Hr(),
        html.P(
            "Pokemon Generation", className="lead"
        ),
        dbc.Nav(
            [
                dcc.Dropdown(get_generation(), 'all', id='demo-dropdown'),
                dcc.Dropdown(get_region(), 'all', id='demo-dropdown')
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app = Dash(name='Pokeapi', external_stylesheets=[dbc.themes.CERULEAN])

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


if __name__ == '__main__':
    app.run_server(port=8000, debug=True)
