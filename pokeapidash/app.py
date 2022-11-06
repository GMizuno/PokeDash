from dash import Dash, html, Input, Output
import dash_bootstrap_components as dbc

from pokeapidash.assets.radar import create_radar
from pokeapidash.utils.helpers import get_pokemon_by_region, get_status, get_front_img, get_back_img, \
    get_status_by_type, get_data_for_radar
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
    result = get_status(pokemon)
    return result[0][0], result[0][1], \
           result[0][2], result[0][3], \
           result[0][4], result[0][5], \
           result[0][6], result[0][7]

@app.callback(
    Output('radar', 'figure'),
    [Input('pokemon_dropdown', 'value')])
def uptade_radar(pokemon):
    return create_radar(get_data_for_radar(pokemon))


if __name__ == '__main__':
    app.run_server(port=8000, debug=True)
