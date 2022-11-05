from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

from pokeapidash.asset.style import FONT_AWESOME
from pokeapidash.utils.helpers import get_pokemon_by_region
from pokeapidash.view.content import content
from pokeapidash.view.sidebar import sidebar

app = Dash(name='Pokeapi', external_stylesheets=[dbc.themes.CERULEAN, FONT_AWESOME])

app.layout = html.Div([sidebar, content])


@app.callback(
        Output('pokemon_dropdown', 'options'),
        [Input('region_dropdown', 'value')])
def update_dropdown(generation):
    return get_pokemon_by_region(generation)


if __name__ == '__main__':
    app.run_server(port=8000, debug=True)
