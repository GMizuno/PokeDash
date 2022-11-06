import dash_bootstrap_components as dbc
from dash import html

from pokeapidash.assets.style import CONTENT_STYLE
from pokeapidash.view.cards import card_template
from pokeapidash.view.image import image_front, image_back
from pokeapidash.view.radar import radar_plot

cards = dbc.Row(
        [
            dbc.Col(card_template('hp', 'hp', 'primary'), md=3),
            dbc.Col(card_template('attack', 'attack', 'primary'), md=3),
            dbc.Col(card_template('defense', 'defense', 'primary'), md=3),
            dbc.Col(card_template('speed', 'speed', 'primary'), md=3),
        ]
)

cards2 = dbc.Row(
        [
            dbc.Col(card_template('special-attack', 'special-attack', 'success'), md=3),
            dbc.Col(card_template('special-defense', 'special-defense', 'success'), md=3),
            dbc.Col(card_template('height', 'height', "secondary"), md=3),
            dbc.Col(card_template('weight', 'weight', "secondary"), md=3),
        ]
)

imgs = dbc.Row(
        [
            dbc.Col(image_front(), md=3),
            dbc.Col(radar_plot(), md=6),
            dbc.Col(image_back(), md=3)
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
