import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import pandas as pd
import plotly.express as px

def create_pie():
    df = pd.read_csv('Dataset/predictions.csv')
    values=df['predictions']
    names=df['status'].value_counts()
    pie1=px.pie(names=['Positive','Negative'], values=list(names), title='Scraped Reviews Pie Chart',template='presentation')
    
    pie1.update_traces(textposition='outside', textinfo='percent+label',
                            marker=dict(line=dict(color='#000000', width=4)),
                            pull=[0, 0.3], opacity=0.7, rotation=180)

    return pie1

def create_home_page():
    layout=html.Div(children=[
        html.Div(className='home-page-div',children=[
            html.H3('Determine whether review is positive, negative or neutral',className='home-page-heading'),
            html.H2('SENTIMENT ANALYSIS',className='home-page-h2'),
            html.Div(className='wrap',children=[
               html.A(href='/check_review',children=[ dbc.Button(className='start button',children='Start Now')])
            ])
        ]),
        html.Div(className='home-page-quote',children=[
            html.Img(src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTR_G2102GVD7LcU-5NUXWFJo3i8D1-uaZ6N59r0YcCozj7wTLuWYjqbzpiBih0CGi-m5Y&usqp=CAU',width=150,height=150),
            html.P(className='home-page-quote-p',children='“It’s not surprising, then, they get bitter, they cling to guns or religion or antipathy to people who aren’t like them or anti-immigrant sentiment or anti-trade sentiment as a way to explain their frustrations..”'),
            html.P(className='home-page-quote-pp',children='– Barack Obama')
        ]),
        html.Div(className='home-page-video',children=[
            html.Iframe(width=560, height=315, src='https://www.youtube.com/embed/O_B7XLfx0ic/?controls=1'),
            html.Div(className='home-page-video-sub',children=[
                html.H3('SENTIMENT ANALYSIS'),
               # html.Hr(style={'width':50,"color":'red'}),
                html.P('is contextual mining of text which identifies and extracts subjective information in source material, and helping a business to understand the social sentiment of their brand, product or service while monitoring online conversations. However, analysis of social media streams is usually restricted to just basic sentiment analysis and count based metrics. This is akin to just scratching the surface and missing out on those high value insights that are waiting to be discovered.'),
                html.A(href='https://towardsdatascience.com/sentiment-analysis-concept-analysis-and-applications-6c94d6f58c17',className='btn')
            ])
        ]),
        html.Div(className='home-page-graph-div',children=[
            dcc.Graph(id='pie-chart',figure=create_pie()),
            html.P(className='home-page-graph-p',children='I have extracted reviews from Etsy.com.'),
            html.A(href='/word_cloud',className='button-one', children='Try Now')
        ])

    ])


    return layout