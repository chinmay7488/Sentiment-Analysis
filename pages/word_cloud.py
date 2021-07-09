import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc


def create_cloud_page(Scrapedreviews,freq):
    layout=html.Div(children=[
        html.Div(className='cloud-page-bg',children=[
            html.Marquee(className='cloud-page-marquee',children=[
                html.H3(children=freq,className='cloud-page-h3')
            ])
        ]),
        html.Div(className='cloud-page-Div',children=[
            dcc.Dropdown(id='review-dropdown',options=[{'label':i, 'value':i} for i in Scrapedreviews],style={"width": "100%",'height':'70px'},multi=False,optionHeight = 100),
            html.Img(src='https://media.giphy.com/media/KGSxFwJJHQPsKzzFba/giphy.gif',width=300,height=300,className='cloud-page-img',id='review-dropdown-gif'),
            html.H4('Choose something',className='cloud-page-h4',id='review-type')
        ])
    ])


    return layout