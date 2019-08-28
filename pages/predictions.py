import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load

from app import app

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
            max=2018, 
            step=1, 
            value=2014, 
            marks={n: str(n) for n in range(2014,2019,1)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Delay Codes'), 
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
    [Input('year', 'value'), Input('Code', 'value')],
)

def predict(year, Code):
    df = pd.DataFrame(
        columns=['year', 'Code'],
        data=[[year, Code]]
    )
    y_pred = pipeline.predict(df)[0]
    return f'{y_pred:.0f} minutes'