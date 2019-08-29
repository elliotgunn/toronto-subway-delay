import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load

from app import app

import dash_daq as daq


pipeline = load('assets/pipeline.joblib')
print(type(pipeline))
print('Hello World')

column1 = dbc.Col(
    [
        dcc.Markdown('## Predictions', className='mb-5'), 
        dcc.Markdown('#### Year'), 
        dcc.Slider(
            id='year', 
            min=2014, 
            max=2019, 
            step=1, 
            value=2014, 
            marks={n: str(n) for n in range(2014,2020,1)}, 
            className='mb-5', 
        ), 
        
        dcc.Markdown('#### Top 5 Delay Codes'), 
        dcc.Dropdown(
            id='Code', 
            options = [
                {'label': 'Misc. Speed Control', 'value': 'MUSC'}, 
                {'label': 'Operator Overspeeding', 'value': 'TUSC'}, 
                {'label': 'Passenger Assistance Alarm Activated (No Trouble Found)', 'value': 'MUPAA'}, 
                {'label': 'Injured or ill Customer', 'value': 'MUIS'}, 
                {'label': 'Misc. General Delays', 'value': 'MUGD'}, 
            ], 
            value = 'MUSC', 
            className='mb-5', 
        ), 

        dcc.Markdown('#### Day of Week'), 
        dcc.Dropdown(
            id='Day', 
            options = [
                {'label': 'Monday', 'value': 'Monday'}, 
                {'label': 'Tuesday', 'value': 'Tuesday'},
                {'label': 'Wednesday', 'value': 'Wednesday'},
                {'label': 'Thursday', 'value': 'Thursday'},
                {'label': 'Friday', 'value': 'Friday'},
                {'label': 'Saturday', 'value': 'Saturday'},
                {'label': 'Sunday', 'value': 'Sunday'},   
            ], 
            value = 'Monday', 
            className='mb-5', 
        ), 

        dcc.Markdown('#### Hour of Day'), 
        daq.NumericInput(
            id='hour',
            max=23,
            value=8,
            min=0,
            className='mb-5',
        ),
        
        dcc.Markdown('#### Top 10 Stations/Lines'), 
        dcc.Dropdown(
            id='Station', 
            options = [
                {'label': 'KIPLING STATION', 'value': 'KIPLING STATION'},
                {'label': 'KENNEDY BD STATION', 'value': 'KENNEDY BD STATION'},
                {'label': 'YONGE UNIVERSITY LINE', 'value': 'YONGE UNIVERSITY LINE'},
                {'label': 'FINCH STATION', 'value': 'FINCH STATION'},
                {'label': 'SHEPPARD WEST STATION', 'value': 'SHEPPARD WEST STATION'},
                {'label': 'WARDEN STATION', 'value': 'WARDEN STATION'},
                {'label': 'WILSON STATION', 'value': 'WILSON STATION'},
                {'label': 'ISLINGTON STATION', 'value': 'ISLINGTON STATION'},
                {'label': 'KEELE STATION', 'value': 'KEELE STATION'},
                {'label': 'VICTORIA PARK STATION', 'value': 'VICTORIA PARK STATION'},

            ],
            value = 'KEELE STATION', 
            className='mb-5',
        ), 

        dcc.Markdown('#### Direction'), 
        dcc.Dropdown(
            id='Bound', 
            options = [
                {'label': 'North', 'value': 'N'},
                {'label': 'South', 'value': 'S'},
                {'label': 'West', 'value': 'W'},
                {'label': 'East', 'value': 'E'},
                {'label': 'Not Recorded', 'value': 'R'},

            ],
            value = 'W', 
            className='mb-5', 
        ), 

        dcc.Markdown('#### Gap'), 
        daq.NumericInput(
            id='Gap',
            max=999,
            value=8,
            min=0,
            className='mb-5',
        ),

    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.H2('Expected Delay', className='mb-5'), 
        html.Div(id='prediction-content', className='lead')
    ]
)

layout = dbc.Row([column1, column2])

import pandas as pd

@app.callback(
    Output('prediction-content', 'children'),
    [Input('year', 'value'), Input('Code', 'value'), Input('Day', 'value'), Input('hour', 'value'), Input('Station', 'value'), Input('Bound', 'value'), Input('Gap', 'value')],
)

def predict(year, Code, Day, hour, Station, Bound, Gap):
    df = pd.DataFrame(
        columns=['year', 'Code', 'Day', 'hour', 'Station', 'Bound', 'Gap'],
        data=[[year, Code, Day, hour, Station, Bound, Gap]]
    )
    y_pred = pipeline.predict(df)[0]
    return f'The estimated TTC delay is {y_pred:.0f} minutes.'