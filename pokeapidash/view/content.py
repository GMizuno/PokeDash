import dash_bootstrap_components as dbc
from dash import Dash, html

from pokeapidash.asset.style import CONTENT_STYLE
from pokeapidash.view.cards import card_template
from pokeapidash.view.image import image_front, image_back

cards = dbc.Row(
        [
            dbc.Col(card_template('hp', 'hp', 'primary'), width="auto"),
            dbc.Col(card_template('attack', 'attack', 'primary'), width="auto"),
            dbc.Col(card_template('defense', 'defense', 'primary'), width="auto"),
            dbc.Col(card_template('speed', 'speed', 'primary'), width="auto"),
        ]
)

cards2 = dbc.Row(
        [
            dbc.Col(card_template('special-attack', 'special-attack', 'success'), width="auto"),
            dbc.Col(card_template('special-defense', 'special-defense', 'success'), width="auto"),
            dbc.Col(card_template('height', 'height', "secondary"), width="auto"),
            dbc.Col(card_template('weight', 'weight', "secondary"), width="auto"),
        ]
)

imgs = dbc.Row(
        [
            dbc.Col(image_front(), width="auto"),
            dbc.Col(width="auto"),
            dbc.Col(image_back(), width="auto")
        ]
)

content = html.Div(
        [imgs,
         html.Hr(),
         cards,
         html.Br(),
         cards2],
        id="page-content",
        style=CONTENT_STYLE
)
