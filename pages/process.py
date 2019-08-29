import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Process

            For this project, I used all available data released through the City of Toronto's [Open Data site](https://open.toronto.ca/dataset/ttc-subway-delay-data/). The data is refreshed on a monthly basis, and the project utilizes nearly five years worth of data. I added weather data from [Weather Stats](https://www.weatherstats.ca/). 

            I developed a machine-learning model, Random Forest,to predict delay time by using the factors correlated with delay times. 




            """
        ),

    ],
)

layout = dbc.Row([column1])