import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
from detail import detail
from display_info import display_info
from plots import blank_fig

tab_info = html.Div([display_info])

tab_mutation = html.Div(
        dcc.Graph(
            id='mutation_plot',
            config={'modeBarButtonsToRemove': ['lasso2d', 'select2d']},
            figure=blank_fig(),
    )
)

tab_methylation = html.Div([
    dbc.Spinner([
        dbc.Row(
            dcc.Graph(
                id='methylation_plot',
                figure=blank_fig(),
                style={'height': '500px'},
                responsive=True,
            ),
        ),
        dbc.Row(
            html.Div(
                dbc.Button(
                    "Load methylation heatmap",
                    outline=True,
                    color="primary",
                    className="me-1",
                    id="refresh_methylation_button",
                    n_clicks=0
                ),
                className="d-grid gap-2 mx-auto"
            )
        )
    ], color="primary"),
])

tab_dysregulation = html.Div([
    dbc.Spinner([
        dbc.Row(
            dcc.Graph(
                id='dysregulation_plot',
                figure=blank_fig(),
                style={'height': '500px'},
                responsive=True,
            ),
        ),
        dbc.Row(
            html.Div(
                dbc.Button(
                    "Load dysregulation heatmap",
                    outline=True,
                    color="primary",
                    className="me-1",
                    id="refresh_dysregulation_button",
                    n_clicks=0
                ),
                className="d-grid gap-2 mx-auto"
            )
        )
    ], color="danger"),
])


tabs = html.Div([
    dbc.Tabs(id="tabs", active_tab='tab_info', children=[
        dbc.Tab(tab_info, label='Display info', tab_id='tab_info'),
        dbc.Tab(tab_mutation, label='Mutation', tab_id='tab_mutation'),
        dbc.Tab(tab_methylation, label='Methylation', tab_id='tab_methylation'),
        dbc.Tab(tab_dysregulation, label='Dysregulation', tab_id='tab_dysregulation'),
    ]),
    html.Div(id='tab-content', style={'marginBottom': '10px'})
])
