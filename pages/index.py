import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has 
twelve columns.

There are three main layout components in dash-bootstrap-components: Container, 
Row, and Col.

The layout of your app should be built as a series of rows of columns.

We set md=4 indicating that on a 'medium' sized or larger screen each column 
should take up a third of the width. Since we don't specify behaviour on 
smaller size screens Bootstrap will allow the rows to wrap so as not to squash 
the content.
"""

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## How Long Is My Delay?

            Subway delays are a near daily occurence in Toronto. This is in part due to an aging infrastructure and [delayed critical signal upgrades](https://www.thestar.com/news/gta/2019/04/04/key-subway-project-has-been-delayed-years-and-has-gone-way-over-budget.html) even as the number of commuters continues to increase. Others blame factors such as inclement weather (particularly in the winter) causing equipment to fail and poor management. 

            This app allows commuters to predict the length of delay and plan their routes for an improved commuting journey. It is also useful for train infrastructure enthusiasts to explore what factors actually drive train delays in one of North American's largest cities.

            """
        ),
        dcc.Link(dbc.Button('Calculate My Delay', color='primary'), href='/predictions')
    ],
    md=6,
)


column2 = dbc.Col(
    [
        html.Img(src='assets/delay.png', className='img-fluid'),
    ],
    md=6,
)

layout = dbc.Row([column1, column2])


