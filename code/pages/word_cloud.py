import dash
import dash_html_components as html
import dash_core_components as dbc

def create_project_page(Scrapedreviews):
    layout=html.Div(className='elementor-section-wrap',children=[
    html.Section(className='elementor-section elementor-section-image elementor-top-section elementor-element elementor-element-7ac9ca5 elementor-section-boxed elementor-section-height-default elementor-section-height-default',children=[
        html.Div(className='elementor-background-overlay'),
    html.Div(className='elementor-container elementor-column-gap-default',children=[
    html.Div(className='elementor-column elementor-col-33 elementor-top-column elementor-element elementor-element-fc40e94',children=[
        html.Div(className='elementor-widget-wrap')
    ]), 
    html.Div(className='elementor-column elementor-col-33 elementor-top-column elementor-element elementor-element-90988fe',children=[
        html.Div(className='elementor-widget-wrap elementor-element-populated',children=[
        html.Div(className='elementor-element elementor-element-4a1c612 elementor-widget elementor-widget-heading',children=[
        html.Div(className='elementor-widget-container-h1',children=[
        html.Marquee(children=[
            html.H1(className='elementor-heading elementor-size-default',children='Hello')
        ])  
        ])
        ])
        ])
    ]),
    html.Div(className='elementor-column elementor-col-33 elementor-top-column elementor-element elementor-element-919f5c1',children=[
        html.Div(className='elementor-widget-wrap')
    ])
    ])
    ]),
    html.Section(className='elementor-section elementor-top-section elementor-element elementor-element-03eac35 elementor-section-boxed elementor-section-height-default elementor-section-height-default',children=[
    html.Div(className='elementor-container elementor-column-gap-default',children=[
    html.Div(className='elementor-widget-wrap elementor-element-populated',children=[
    html.Div(className='elementor-widget-container',children=[
    html.Form(className='wpforms-validate wpforms-form',id='wpforms-form-598',children=[
    html.Div(className='wpforms-field-container',children=[
        html.Div(className='wpforms-field wpforms-field-select wpforms-field-select-style-classic',id='wpforms-598-field_1-container',children=[
        dbc.Dropdown(id='review-dropdown',options=[{'label':i, 'value':i} for i in Scrapedreviews],style={"width": "100%"},multi=False,optionHeight = 100),
    ])
    ])
    ])
    ])
    ]),
    html.Section(className='elementor-section elementor-inner-section elementor-element elementor-element-2d93010 elementor-section-boxed elementor-section-height-default elementor-section-height-default',children=[
    html.Div(className='elementor-container elementor-column-gap-default',children=[
    html.Div(className='elementor-column elementor-col-100 elementor-inner-column elementor-element elementor-element-a3374a1',children=[
    html.Div(className='elementor-widget-wrap elementor-element-populated',children=[
    html.Div(className='elementor-element elementor-element-14f7fa4 elementor-widget elementor-widget-image',children=[
    html.Div(className='elementor-widget-container',children=[
        html.Figure(className='wp-caption',children=[
            html.Img(src='https://media.giphy.com/media/4Zt2BAmW8NNBe/giphy.gif',width=325,height=217,id='review-dropdown-gif'),
            html.H4(id='review-type',children=[html.Strong(children='')])
        ])
    ])
    ])
    ])
    ])
    ])
    ])
    ])
    ])
    ])
    
    return layout


    