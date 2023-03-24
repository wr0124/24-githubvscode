from dash import Input, Output, callback
from Figures_Aliyasin import *

# version en cours

@callback(
    Output('page-1-display-value', 'children'),
    Input('page-1-dropdown', 'value'))
def display_value1(value):
    return f'You have selected {value}'


@callback(
    Output('page-2-display-value', 'children'),
    Input('page-2-dropdown', 'value'))
def display_value2(value):
    return f'You have selected {value}'


@callback(
    Output('page-3-display-value', 'figure'),
    Input('page-3-dropdown', 'value'))
def display_value3(value):
    return f'You have selected {value}'

@callback(
    Output('page-4-display-value', 'figure'),
    Input('page-4-dropdown', 'value'))
def display_value4(value):
    return f'You have selected {value}'

@callback(
    Output('graph-tx-incidence', 'figure'),
    Input('page-5-dropdown', 'value'))
def display_value4(value):
    return f'You have selected {value}'

@callback(
    Output("tab-content", "figure"),
    Input("tabs", "active_tab"),
)
def render_tab_content(active_tab):
    if active_tab == "creation":
        return fig6
    elif active_tab == "defaillance":
        return fig7