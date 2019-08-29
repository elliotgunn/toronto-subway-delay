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
        
            ## Insights

            1. Train delay data is extremely skewed, mostly 0, raising questions about data collection methods.

            2. Surprisingly, and contrary to academic literature and domain knowledge, bad weather is weakly correlated with delays.

            html.Img(src='assets/2_heatmap.png', className='img-fluid')


            3. Almost a third of all delays can be attributed to operator speed management. Passenger-activated false alarms come in as the next most important reason behind delays.

            4. [Feature importances chart] The variable `Min Gap` is overwhelmingly key to predicting delays. It is potentially a source of leakage, but included in this model pending a more suitable substitute engineered feature. It has been shown in ML models done elsewhere that capturing the "ripple effect" of a delay on the system is an important predictor of future delays.

            5. 

            6. 

            7. PDP

            8. A good prediction: Shapley values

            9. A bad prediction:
            Shapley values


            """
        ),
    ],
    md=4,
)


column2 = dbc.Col(
    [
        
    ]
)

layout = dbc.Row([column1, column2])