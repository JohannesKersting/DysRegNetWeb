import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import parameters


def get_settings(cancer_ids):
    settings = [
        dbc.Card(
            dbc.CardBody([
                html.H5('Display options'),
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
                html.H5('Compare options'),
                html.Label('Compare to cancer type:'),
                dcc.Dropdown(
                    options=[{'label': cancer_id, 'value': cancer_id} for cancer_id in cancer_ids],
                    multi=False,
                    id='compare_cancer'
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
                html.H5('Downloads'),
                html.Div(
                    [
                        dbc.Button(children=[html.I(className="fa fa-download mr-1"), " Download full graph (.csv)"],
                                   id="btn_download_graph_full", outline=True, color="primary",
                                   className="me-1", style={'textAlign': 'left'}, size="sm"),
                        dbc.Button(
                            children=[html.I(className="fa fa-download mr-1"), " Download displayed graph (.csv)"],
                            id="btn_download_graph_displayed", outline=True, color="primary",
                            className="me-1", style={'textAlign': 'left'}, size="sm"),
                        dbc.Button(children=[html.I(className="fa fa-download mr-1"), " Download graph image (.png)"],
                                   id="btn_download_graph_png", outline=True, color="primary",
                                   className="me-1", style={'textAlign': 'left'}, size="sm"),
                    ],
                    className="d-grid gap-2",
                ),
            ]),
            className="mt-3 mb-3"
        ),

        dcc.Download(id="download_graph_full"),
        dcc.Download(id="download_graph_displayed"),
    ]
    return settings