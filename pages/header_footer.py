import dash
import dash_html_components as html
import dash_core_components as dbc

def create_header():
    header_layout=html.Div(className='topnav',children=[
        html.A(className='active',href='/home',children='Home'),
        html.A(href='/about',children='About'),
        html.A(href='/check_review',children='Check Review'),
        html.A(href='/word_cloud',children='Word Cloud'),
        html.A(href='/contact_me',children='Contact Me'),
    ])
    return header_layout

def create_footer():
    footer_layout=html.Div(className='footer',children=[
        html.P(className='footer-p',children='Phone: +91-9589445122 | Email: chinmayjainst8314@gmail.com'),
        html.P(children='Copyright © 2021 Sentiment Analysis')
    ])

    return footer_layout