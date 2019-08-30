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

            1. Train delay data is extremely skewed, with 70.5% of observations at 0 minutes. The longest delay is 999 minutes. The use of minutes, instead of seconds, suggests that more precise, and thus more usefully predictive data, has been lost due to collection methods.

            """
        ),
        html.Div([
            html.Img(src='assets/skew.png', className='img-fluid'),
        ]),
        dcc.Markdown(
            """

            2. Surprisingly, and contrary to academic literature and domain knowledge, bad weather is weakly correlated with delays. Bad weather is thought to cause equipment failures or causing operating speeds to be reduced, thus increasing delay times. This counter-intuitive observation has also been seen in at least [one other study](https://academic.oup.com/tse/advance-article/doi/10.1093/tse/tdy001/5306170).

            """
        ),
        html.Div([
            html.Img(src='assets/heatmap.png', className='img-fluid'),
        ]),
         dcc.Markdown(
            """

            3. Almost a third of all delays can be attributed to operator speed management. Passenger-activated false alarms come in as the next most important reason behind delays.
            """
        ),  
         dcc.Markdown(
            """

            4. The variable `Gap` is overwhelmingly key to predicting delays. It is potentially a source of leakage, but included in this model pending a more suitable substitute engineered feature. It has been shown in ML models done elsewhere that capturing the "ripple effect" of a delay on the system is an important predictor of future delays. Hence, a more sophisticated model would capture the real-time, dynamic information that `Gap` provides about the probability of future delays in the subway system.

            """
        ),
        html.Div([
            html.Img(src='assets/importances.png', className='img-fluid'),
        ]),
         dcc.Markdown(
            """

            5. The last stops of the subway lines saw the most number of delays. Kipling, Kennedy, and Finch top the list. 

            """
        ),
         dcc.Markdown(
            """

            6. PDP
            """
        ),
        html.Div([
            html.Img(src='assets/pdp.png', className='img-fluid'),
        ]),
         dcc.Markdown(
            """

            7. Shapley
            """
        ),
        html.Div([
            html.Img(src='assets/pdp.png', className='img-fluid'),
        ]),

    ],
    md=12,
)

layout = dbc.Row([column1])


