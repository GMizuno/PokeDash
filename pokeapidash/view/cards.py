from dash import html
import dash_bootstrap_components as dbc

from pokeapidash.asset.style import CARD_ICON


def card_template(card_id: str, name: str, color: str):
    return dbc.CardGroup(
            [
                dbc.Card(
                        dbc.CardBody(
                                [
                                    html.H5(id=f"Card_{card_id}", style={"width":"10rem", "margin":"auto"}),
                                    html.P(children=f"{name.capitalize()}", id=f"{name}", style={"margin":"auto"}),
                                ]
                        ),
                ),
                dbc.Card(
                        html.Div(style=CARD_ICON),
                        className=f"bg-{color}",
                        style={"maxWidth":50},
                ),
            ]
    )
