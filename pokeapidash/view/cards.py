from dash import html
import dash_bootstrap_components as dbc

from pokeapidash.asset.style import CARD_ICON, FONT_AWESOME

card1 = dbc.CardGroup(
        [
            dbc.Card(
                    dbc.CardBody(
                            [
                                html.H5("Card 1", className="card-title", style={"margin":"auto"}),
                                html.P("This card has some text content", className="card-text",
                                       style={"margin":"auto"}),
                            ]
                    ),
            ),
            dbc.Card(
                    html.Div(className="fa fa-list", style=CARD_ICON),
                    className="bg-primary",
                    style={"maxWidth":1000},
            ),
        ],
        className="card_1",
)
