from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

from pokeapidash.utils.helpers import get_pokemon_by_region, get_status, get_front_img, get_back_img
from pokeapidash.view.content import content
from pokeapidash.view.sidebar import sidebar

app = Dash(name='Pokeapi', external_stylesheets=[dbc.themes.CERULEAN, dbc.icons.BOOTSTRAP])

app.layout = html.Div([sidebar, content])


@app.callback(
        Output('pokemon_dropdown', 'options'),
        [Input('region_dropdown', 'value')]
)
def update_dropdown(generation):
    return get_pokemon_by_region(generation)


@app.callback(
        Output('front-sprite', 'src'),
        [Input('pokemon_dropdown', 'value')]
)
def update_dropdown(pokemon):
    return get_front_img(pokemon)

@app.callback(
        Output('back-sprite', 'src'),
        [Input('pokemon_dropdown', 'value')]
)
def update_dropdown(pokemon):
    return get_back_img(pokemon)
@app.callback(
        [Output('Card_hp', 'children'),
         Output('Card_attack', 'children'),
         Output('Card_defense', 'children'),
         Output('Card_special-attack', 'children'),
         Output('Card_special-defense', 'children'),
         Output('Card_speed', 'children'),
         Output('Card_height', 'children'),
         Output('Card_weight', 'children')],
        [Input('pokemon_dropdown', 'value')])
def update_card_attack(pokemon):
    return get_status(pokemon)[0][0], get_status(pokemon)[0][1], \
           get_status(pokemon)[0][2], get_status(pokemon)[0][3], \
           get_status(pokemon)[0][4], get_status(pokemon)[0][5], \
           get_status(pokemon)[0][6], get_status(pokemon)[0][7]


if __name__ == '__main__':
    app.run_server(port=8000, debug=True)
