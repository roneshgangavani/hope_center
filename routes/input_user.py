import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
from application import app
import plotly.express as px
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import dash_table
from dash.dependencies import Input, Output
from datetime import datetime, timedelta, date
import boto3

from dash_table.Format import Format

from util.dash_layout import external_stylesheets, update_fig
import pandas as pd
import psycopg2
# from config.flask_config import DatabaseConfig
import numpy as np
from datetime import date
from datetime import datetime
from dateutil import relativedelta
import pandas as pd
pd.options.display.float_format = '{:.2f}'.format
home_url = "/covid_requirments/user_post/"
from csv import writer
covid_help = dash.Dash(__name__,
                          server=app,
                          url_base_pathname=home_url,
                          external_stylesheets=external_stylesheets)

df=pd.read_csv('data/state.csv')
print(df)
covid_help.layout = html.Div(
    [
    html.H3(["Ask Help here"
             ], className="text-center"),
    html.Div([
        html.Label("Select State :"),
        dcc.Dropdown(
                 id='demo-dropdown',
                 options=[{
                     'label': str(i).replace("_", " "), 'value': i} for i in df['state'].unique()],
                 value='Type here')
    ],
    style={'width': '30%', 'display': 'inline-block', 'marginTop': 5, 'marginBottom': 15}),
    html.Div([
        html.Label("Select District  :"),
        dcc.Dropdown(id='demo-dropdown_dis',
                 options=[{
                     'label': str(i).replace("_", " "), 'value': i} for i in df['district'].unique()],
                 value='Type here')
    ],
    style={'width': '30%', 'display': 'inline-block', 'marginTop': 5, 'marginBottom': 15}),   
    html.Div([
        html.Label("Type of Help:"),
        dcc.Dropdown(id='demo-dropdown_tpye',
                 options=[
                         {
                             'label': 'Hospital Beds',
                             'value': 'Hospital Beds'
                         }, {
                             'label': 'Blood Group',
                             'value': 'Blood Group'
                         }],
                     value='Select')
    ],
    style={'width': '30%', 'display': 'inline-block', 'marginTop': 5, 'marginBottom': 15}),
    html.Div([
        html.Label("Contact Details:"),
    dcc.Input(
            id="contact",
            type="number",
            placeholder="contanct no.",
        )
         ],
    style={'width': '30%', 'display': 'inline-block', 'marginTop': 5, 'marginBottom': 15}),
    html.Div([
        html.Label("Your Message:"),
    dcc.Textarea(
        id='textarea-example',
        value='',
    ),
      ],
    style={'width': '30%', 'display': 'inline-block', 'marginTop': 5, 'marginBottom': 15}),
    html.Button('Submit', id='button'),
    html.Div(id='dd-output-container'),
])
@covid_help.callback(
    dash.dependencies.Output('dd-output-container', 'children'),
    [dash.dependencies.Input('demo-dropdown', 'value'),
    dash.dependencies.Input('demo-dropdown_dis', 'value'),
    dash.dependencies.Input('demo-dropdown_tpye', 'value'),
     dash.dependencies.Input('contact', 'value'),
     dash.dependencies.Input('textarea-example', 'value'),
     dash.dependencies.Input('button', 'n_clicks')]
)
def update_output_once(state,district,type_help,contact,msg,n_clicks):
    file = open('data/user_ask_help.csv','a')
    write = writer(file)
    if n_clicks != None:
        if state != None and district != None and type_help != None and contact != None:
            write.writerow([state,district,type_help,contact,msg])
            return html.Div(
                html.H3(["Successfully Recorded"
                ], className="text-center"),

            )
        else:
            return html.Div(
                html.H3(["Not Recorded"
                ], className="text-center"),

            )
    
