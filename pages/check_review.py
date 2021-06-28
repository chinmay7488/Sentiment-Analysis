import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

def create_checkreview_page():
    layout=html.Div(className='elementor-section-wrap',children=[
    html.Section(className='elementor-section elementor-top-section elementor-element elementor-element-33a79095 elementor-section-boxed elementor-section-height-default elementor-section-height-default',children=[
    html.Div(className='elementor-background-overlay'),
    html.Div(className='elementor-container elementor-column-gap-default',children=[
        html.Div(className='elementor-column elementor-col-33 elementor-top-column elementor-element elementor-element-b7194dc',children=[
        html.Div(className='elementor-widget-wrap')
        ]),
        html.Div(className='elementor-column elementor-col-33 elementor-top-column elementor-element elementor-element-3706530d',children=[
        html.Div(className='elementor-widget-wrap elementor-element-populated',children=[
        html.Div(className='elementor-element elementor-element-49369b2 elementor-widget elementor-widget-wpforms',children=[
        html.Div(className='elementor-widget-container',children=[
        html.Div(className='wpforms-container ',id='wpforms-680',children=[
        html.Form(className='wpforms-validate wpforms-form',id='wpforms-form-680',children=[
        html.Div(className='wpforms-field-container',children=[
        html.Div(className='wpforms-field wpforms-field-text',id='wpforms-680-field_1-container',children=[
            dcc.Textarea(id='textarea-check-review',placeholder='Enter the Review here...',style = {'width':'300%', 'height':50})
        ])
        ]),
        html.Div(className='wpforms-submit-container',children=[
            #dbc.Button(id='check-review-button',children='Check Review',n_clicks=0)
        ])
        ])
        ])
        ])
        ]),
        html.Div(className='elementor-element elementor-element-b4375f9 elementor-widget elementor-widget-image',children=[
        html.Div(className='elementor-widget-container',children=[
            html.Img(src='https://media.giphy.com/media/4Zt2BAmW8NNBe/giphy.gif',width=325,height=217,className='attachment-medium_large size-medium_large',id='gif')
        ])
        ]),
        html.Div(className='elementor-element elementor-element-d727274 elementor-widget elementor-widget-text-editor',children=[
        html.Div(className='elementor-widget-container',children=[
            html.H4(className='elementor-widget-container',id='h4',children='')
        ])
        ])
        ])
        ]),
        html.Div(className='elementor-column elementor-col-33 elementor-top-column elementor-element elementor-element-4788e5dc',children=[
            html.Div(className='elementor-widget-wrap')
        ])
    ])
    ])
    ])


    return layout
