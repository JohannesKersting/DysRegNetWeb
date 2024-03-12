import dash_bootstrap_components as dbc
from dash import dcc
from dash import html

import parameters
from popovers import info_button, heading_with_info


def get_settings():
    settings = [
        dbc.Card(
            dbc.CardBody([
                heading_with_info('Display options', 'display_options_info'),
                html.Label('Minimum dysregulation fraction:'),
                dcc.Slider(
                    id='min_fraction_slider',
                    min=0,
                    max=1,
                    step=0.01,
                    value=0,
                    tooltip={"placement": "bottom", "always_visible": True},
                ),
                html.Label('Maximum regulations displayed:'),
                dcc.Slider(
                    id='max_regulations_slider',
                    min=0,
                    max=parameters.max_regulations,
                    step=1,
                    value=parameters.max_regulations,
                    tooltip={"placement": "bottom", "always_visible": True},

                ),
                html.Label('Scale node size by:'),
                dcc.Dropdown(
                    options=[
                        {'label': 'Mutation', 'value': 'mu'},
                        {'label': 'Methylation', 'value': 'me'},
                    ],
                    multi=False,
                    id='diameter_type'
                ),
                html.Label('Display nodes:'),
                dcc.Dropdown(
                    options=[
                        {'label': 'Targets', 'value': 't'},
                        {'label': 'Sources', 'value': 's'},
                        {'label': 'All', 'value': 'a'}
                    ],
                    value="a",
                    multi=False,
                    id='display_nodes'
                ),
            ]),

        ),

        dbc.Card(
            dbc.CardBody([
                heading_with_info('Compare options', 'compare_options_info'),
                html.Label('Compare to cancer type:'),
                dbc.Spinner(
                    dcc.Dropdown(
                        multi=False,
                        id='compare_cancer',
                    ),
                    color="primary",
                ),
                html.Br(),
                dbc.Switch(
                    id="compare_switch",
                    label="Display dysregulation difference",
                    value=True,
                ),
            ]),
            className="mt-3"
        ),

        dbc.Card(
            dbc.CardBody([
                heading_with_info('Downloads', 'downloads_info'),
                html.Div(
                    [
                        dbc.Button(children=[html.I(className="fa fa-download mr-1"), " Download queried graph (.csv)"],
                            id="btn_download_graph_full", outline=True, color="primary",
                            style={'textAlign': 'left'}, size="sm"),
                        dbc.Button(
                            children=[html.I(className="fa fa-download mr-1"), " Download displayed graph (.csv)"],
                            id="btn_download_graph_displayed", outline=True, color="primary",
                            style={'textAlign': 'left'}, size="sm"),
                        dbc.Button(children=[html.I(className="fa fa-download mr-1"), " Download graph image (.png)"],
                            id="btn_download_graph_png", outline=True, color="primary",
                            style={'textAlign': 'left'}, size="sm"),
                    ],
                    className="d-grid gap-2",
                ),
            ]),
            className="mt-3 mb-3"
        ),
        dbc.Card(
            dbc.CardBody([
                heading_with_info('Drug repurposing', 'repurposing_info'),
                html.Div(
                    [
                        dbc.Button(children=[html.I(className="fa fa-external-link mr-1"), " Drugst.One"],
                                   id="btn_export_drugstone", outline=True, color="primary",
                                   style={'textAlign': 'left'}, size="sm"),
                    ],
                    className="d-grid gap-2",
                ),
            ]),
            className="mt-3 mb-3"
        ),

        dcc.Download(id="download_graph_full"),
        dcc.Download(id="download_graph_displayed"),
        dcc.Store(id='store_drugstone_link', storage_type='memory'),
    ]
    return settings
