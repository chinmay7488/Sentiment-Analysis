import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

def create_contact_page():
    layout = html.Div(children=[
        html.Div(className='contact-page-bg',
            children=[
                html.H1("Contact Me",id='contact_h1')]
            ),
       html.Div(className='contact-page-div',children=[
            html.H3("WE'RE READY, LET'S TALK."),

            dbc.Input(type='text',placeholder='Your Name',size="52"),
            html.Br(),
            dbc.Input(type='mail',placeholder='Email',size="52"),
            html.Br(),
            dbc.Textarea(placeholder='Your Message',className='contact-page-textarea'),
            html.Br(),
            dbc.Button(type='Submit',children='Send Message',className='contact-btn')
        ])    
    ])

    return layout