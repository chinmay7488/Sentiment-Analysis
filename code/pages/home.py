import dash
import dash_html_components as html
import dash_core_components as dbc
import plotly.express as px
from dash.dependencies import Input, Output
# import pandas as pd
# df=pd.Dataframe()

def create_home_page():
    layout=html.Div(className='elementor-section-wrap',children=[
    html.Section(className='elementor-section elementor-top-section elementor-element elementor-element-c50838b elementor-section-boxed elementor-section-height-default elementor-section-height-default',children=[
    html.Div(className='elementor-background-overlay'),
    html.Div(className='elementor-container elementor-column-gap-default',children=[
    html.Div(className='elementor-column elementor-col-33 elementor-top-column elementor-element elementor-element-2f84d6d',children=[
        html.Div(className='elementor-widget-wrap')
    ]),
    html.Div(className='elementor-column elementor-col-33 elementor-top-column elementor-element elementor-element-55b0429',children=[
    html.Div(className='elementor-widget-wrap elementor-element-populated',children=[
    html.Div(className='elementor-element elementor-element-3428592 elementor-widget elementor-widget-heading',children=[
    html.Div(className='elementor-widget-container',children=[
        html.H4(className='elementor-heading-title elementor-size-default',children='Determine whether review is positive, negative or neutral.')
        ])
    ]),
    html.Div(className='elementor-element elementor-element-92570e2 elementor-widget-divider--view-line elementor-widget elementor-widget-divider',children=[
    html.Div(className='elementor-widget-container',children=[
    html.Div(className='elementor-divider',children=[html.Span(className='elementor-divider-separator')])

    ])
    ]),
    html.Div(className='elementor-element elementor-element-453e782 elementor-widget elementor-widget-heading animated fadeIn',children=[
    html.Div(className='elementor-widget-container',children=[
        html.H1(className='elementor-heading-title elementor-size-xxl',children='Sentiment   Analysis')
    ])
    ]),
    html.Div(className='elementor-element elementor-element-6d0d9cb elementor-align-center elementor-widget elementor-widget-button',children=[
    html.Div(className='elementor-widget-container',children=[
    html.Div(className='elementor-button-wrapper',children=[
    html.A(className='elementor-button-link elementor-button elementor-size-sm elementor-animation-pulse-grow',href='',children=[
    html.Span(className='elementor-button-content-wrapper',children=[
    html.Span(className='elementor-button-text',children='Start Now')
    ])
    ])
    ])
    ])
    ])
    ])
    ]),
    html.Div(className='elementor-column elementor-col-33 elementor-top-column elementor-element elementor-element-79b148e',children=[
        html.Div(className='elementor-widget-wrap')
    ])
    ])
    ]),
    html.Section(className='elementor-section elementor-top-section elementor-element elementor-element-5c31627 elementor-section-boxed elementor-section-height-default elementor-section-height-default',children=[
    html.Div(className='elementor-container elementor-column-gap-default',children=[
    html.Div(className='elementor-column elementor-col-33 elementor-top-column elementor-element elementor-element-32f335d',children=[
    html.Div(className='elementor-widget-wrap elementor-element-populated',children=[
    html.Div(className='elementor-element elementor-element-afcd584 elementor-widget elementor-widget-image',children=[
    html.Div(className='elementor-widget-container',children=[
    html.Img(className='attachment-large size-large',height=154,width=200)
    ])
    ])
    ])
    ]),
    html.Div(className='elementor-column elementor-col-33 elementor-top-column elementor-element elementor-element-a107e3a',children=[
    html.Div(className='elementor-widget-wrap elementor-element-populated',children=[
    html.Div(className='elementor-background-overlay'),
    html.Div(className='elementor-element elementor-element-26eb166 elementor-widget elementor-widget-text-editor',children=[
    html.Div(className='elementor-widget-container',children=[
        html.P('“It’s not surprising, then, they get bitter, they cling to guns or religion or antipathy to people who aren’t like them or anti-immigrant sentiment or anti-trade sentiment as a way to explain their frustrations..”')
    ])
    ]),
    html.Div(className='elementor-element elementor-element-95e575c elementor-widget elementor-widget-text-editor',children=[
    html.Div(className='elementor-widget-container',children=[
        html.P('– Barack Obama')
    ])
    ])
    ])
    ]),
    html.Div(className='elementor-column elementor-col-33 elementor-top-column elementor-element elementor-element-33bc69a',children=[
    html.Div(className='elementor-widget-wrap')
    ])
    ])
    ]),
    html.Section(className='elementor-section elementor-top-section elementor-element elementor-element-51af88c elementor-section-boxed elementor-section-height-default elementor-section-height-default',children=[
    html.Div(className='elementor-background-overlay'),
    html.Div(className='elementor-container elementor-column-gap-default',children=[
    html.Div(className='elementor-column elementor-col-50 elementor-top-column elementor-element elementor-element-b0bec06',children=[
    html.Div(className='elementor-widget-wrap elementor-element-populated',children=[
    html.Div(className='elementor-element elementor-element-8b3c2a9 elementor-aspect-ratio-32 elementor-widget elementor-widget-video',children=[
    html.Div(className='elementor-widget-container',children=[
    html.Div(className='elementor-wrapper elementor-fit-aspect-ratio elementor-open-inline',children=[
    html.Iframe(className='elementor-video',width=560, height=315, src='https://www.youtube.com/embed/O_B7XLfx0ic/?controls=1')
    ])
    ])
    ])
    ])
    ])
    ]),
    html.Div(className='elementor-column elementor-col-50 elementor-top-column elementor-element elementor-element-a9a69dd',children=[
    html.Div(className='elementor-widget-wrap elementor-element-populated',children=[
    html.Div(className='elementor-element elementor-element-903dcf2 elementor-widget elementor-widget-heading',children=[
    html.Div(className='elementor-widget-container',children=[
        html.H2(className='elementor-heading-title elementor-size-default',children='Sentiment analysis')
    ])
    ]),
    html.Div(className='elementor-element elementor-element-1694eb3 elementor-widget-divider--view-line elementor-widget elementor-widget-divider',children=[
    html.Div(className='elementor-widget-container',children=[
    html.Div(className='elementor-divider',children=[
        html.Span(className='elementor-divider-separator')
    ])
    ])
    ]),
    html.Div(className='elementor-element elementor-element-c07d6ad elementor-widget elementor-widget-text-editor',children=[
    html.Div(className='elementor-widget-container',children=[
        html.P(' is contextual mining of text which identifies and extracts subjective information in source material, and helping a business to understand the social sentiment of their brand, product or service while monitoring online conversations. However, analysis of social media streams is usually restricted to just basic sentiment analysis and count based metrics. This is akin to just scratching the surface and missing out on those high value insights that are waiting to be discovered.')
    ])
    ]),
    html.Div(className='elementor-element elementor-element-3ab74e6 elementor-align-left elementor-mobile-align-center elementor-widget elementor-widget-button',children=[
    html.Div(className='elementor-widget-container',children=[
    html.Div(className='elementor-button-wrapper',children=[
    html.A(href='https://towardsdatascience.com/sentiment-analysis-concept-analysis-and-applications-6c94d6f58c17',className='elementor-button-link elementor-button elementor-size-sm elementor-animation-pulse-shrink',role='button',children=[
    html.Span(className='elementor-button-content-wrapper',children=[
    html.Span(className='elementor-button-icon elementor-align-icon-right',children=[
        html.I(className='fas fa-long-arrow-alt-right')
    ]),
    html.Span(className='elementor-button-text',children='Learn More')
    ])
    ])
    ])
    ])
    ])
    ])
    ])
    ]),
    html.Section(children=[
    dbc.Graph(id='pie-chart'),
    html.Div(className='elementor-column elementor-col-50 elementor-inner-column elementor-element elementor-element-2203917',children=[
    html.Div(className='elementor-widget-wrap elementor-element-populated',children=[
    html.Div(className='elementor-element elementor-element-9bb6e78 elementor-widget elementor-widget-text-editor',children=[
    html.Div(className='elementor-widget-container',children=[
        html.P('I have extracted reviews from Etsy.com .')
    ])
    ])
    ])    
    ]),
    html.Div(className='elementor-element elementor-element-bb759e4 elementor-align-center elementor-widget elementor-widget-button',children=[
    html.Div(className='elementor-widget-container',children=[
    html.Div(className='elementor-button-wrapper',children=[
    html.A(className='elementor-button-link elementor-button elementor-size-sm elementor-animation-bounce-out',href='',children=[
        html.Span(className='elementor-button-content-wrapper',children=[
            html.Span(className='elementor-button-text',children='Try Now')
        ])
    ])
    ])
    ])
    ])    
    ])
    ])

    return layout
# @app.callback(
#     Output("pie-chart", "figure"), 
#     [Input("names", "value"), 
#      Input("values", "value")])
# def generate_chart(names, values):
#     fig = px.pie(df, values=values, names=names, title='Scraped Reviews Pie Chart')
#     return fig