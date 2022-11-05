from dash import html
import dash_bootstrap_components as dbc


def image_front(url: str | None = None):
    return dbc.CardGroup(
            [
                dbc.CardBody(
                        [
                            html.H4(className="card-title", style={'alling':'center'})
                        ]
                ),
                dbc.CardImg(id='front-sprite', src=url, top=True),
            ],
            style={"width":"18rem"}
    )


def image_back(url: str | None = None):
    return dbc.CardGroup(
            [
                dbc.CardBody(
                        [
                            html.H4(className="card-title", style={'alling':'center'})
                        ]
                ),
                dbc.CardImg(id='back-sprite', src=url, top=True),
            ],
            style={"width":"18rem"}
    )
