import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc




def create_about_page():
    layout=html.Div(children=[
        html.Div(className='about-page-bg',children=[
            html.H1('WHO AM I ?',className='about-page-h1')
        ]),
        html.Div(className='about-second-div',children=[
            html.P(className='about-page-p-intro',children="Hi Everyone, I am Chinmay Jain from Bhopal, India. I am a final year undergraduate pursuing B.Tech. in Computer Science in LNCT, Bhopal."),
            html.Img(className='about-page-img',src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-hZ2e029xLPG-7Sg_91-9Op5LlF6W8ZANlQ&usqp=CAU')
        ]),
        html.Div(className='about-third-div',children=[
            html.H2('Professional Skillset'),
            html.Ul(children=[
                html.Li('Python'),
                html.Li('Machine Learning'),
                html.Li('Deep Learning'),
                html.Li('MySQL'),
                html.Li('Java'),
                html.Li('Java'),
                ]),
        ])
    ])


    return layout
