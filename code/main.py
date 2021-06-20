import dash
import dash_html_components as html
import dash_core_components as dbc
from dash.dependencies import Input, Output
from pages import home  as check
from pages import header_footer as h


app =dash.Dash(__name__)
header =h.create_header()
contact_page=check.create_home_page()
footer=h.create_footer()
app.layout=html.Div([
    header,
    contact_page,
    footer
])


if __name__=='__main__':
    app.run_server()