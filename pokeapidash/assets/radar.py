import plotly.graph_objects as go

from pokeapidash.utils.helpers import get_status, get_status_by_type, get_data_for_radar

categories = ['hp', 'attack', 'defense', 'special_attack', 'special_defense',
              'speed', 'height', 'weight']


def create_radar(r: list , theta: list = [categories, categories], names: list = ['Pokemon', 'Type']):
    fig = go.Figure()

    for plots in zip(r, theta, names):
        fig.add_trace(go.Scatterpolar(
                r=list(plots[0][0]),
                theta=plots[1],
                fill='toself',
                name=plots[2]
        ))

    fig.update_layout(
            polar=dict(
                    radialaxis=dict(
                            visible=True
                    )),
            showlegend=False
    )

    return fig

