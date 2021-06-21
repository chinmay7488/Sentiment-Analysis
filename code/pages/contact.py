import dash
import dash_html_components as html
import dash_core_components as dbc


def create_contact_page():
    layout=html.Div(className='elementor-section-wrap',children=[
    html.Section(className='elementor-section-contact-page-1',children=[
    html.Div(className='elementor-background'),
    html.Div(className='elementor-container elementor-column-gap-default',children=[
    html.Div(className='elementor-column elementor-col-33 elementor-top-column elementor-element elementor-element-5b80d24',children=[
    html.Div(className='elementor-widget-wrap')
    ]),
    html.Div(className='elementor-column elementor-col-33 elementor-top-column elementor-element elementor-element-24c9f1f',children=[
    html.Div(className='elementor-widget-wrap elementor-element-populated',children=[
    html.Div(className='elementor-element elementor-element-a5e247a elementor-widget elementor-widget-heading',children=[
    html.Div(className='elementor-widget-container',children=[
        html.H1(className='heading elementor-size-default',children='Contact Me')
    ])
    ])
    ])
    ]),
    html.Div(className='elementor-column elementor-col-33 elementor-top-column elementor-element elementor-element-9a08ab1',children=[
        html.Div(className='elementor-widget-wrap')
    ])
    ])
    ]),
    html.Section(className='elementor-section elementor-top-section elementor-element elementor-element-34cbd81 elementor-section-boxed elementor-section-height-default elementor-section-height-default',children=[
    html.Div(className='elementor-container elementor-column-gap-default',children=[
    html.Div(className='elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-1dfb88a',children=[
    html.Div(className='elementor-widget-wrap elementor-element-populated',children=[
    html.Section(className='elementor-section elementor-inner-section elementor-element elementor-element-8672813 elementor-section-boxed elementor-section-height-default elementor-section-height-default',children=[
    html.Div(className='elementor-container elementor-column-gap-default',children=[
    html.Div(className='elementor-column elementor-col-50 elementor-inner-column elementor-element elementor-element-21ad806',children=[
    html.Div(className='elementor-widget-wrap elementor-element-populated',children=[
    html.Div(className='elementor-background-overlay'),
    html.Div(className='elementor-element elementor-element-74c0dbc elementor-widget elementor-widget-heading',children=[
    html.Div(className='elementor-widget-container',children=[
    html.H2(className='heading-title elementor-size-default',children="We're Ready, Let's Talk.")
    ])
    ]),
    html.Div(className='elementor-element elementor-element-bef937d elementor-widget elementor-widget-shortcode',children=[
    html.Div(className='elementor-widget-container',children=[
    html.Div(className='elementor-shortcode',children=[
    html.Div(className='wpforms-container ',id='wpforms-5',children=[
    html.Form(id='wpforms-form-5',className='wpforms-validate wpforms-form',children=[
    html.Div(className='wpforms-field-container',children=[
    html.Div(id='wpforms-5-field_0-container',className='wpforms-field wpforms-field-name',children=[
    dbc.Input(className='wpforms-field-large wpforms-field-required',id='wpforms-5-field_0',type='text',placeholder='Your Name')
    ]),
    html.Div(id='wpforms-5-field_1-container',className='wpforms-field wpforms-field-email',children=[
        dbc.Input(id='wpforms-5-field_1',type='text',placeholder='Email Address')
    ]),
    html.Div(className='wpforms-5-field_2-container',children=[
        dbc.Textarea(id='wpforms-5-field_2',placeholder='Message')
    ])
    ]),
    html.Div(className='wpforms-submit-container',children=[
        html.Button(id='submit',type='submit',children='Send Message')
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
    ])
    ])
    ])
    ])
    ])
    return layout