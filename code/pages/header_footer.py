import dash
import dash_html_components as html
import dash_core_components as dbc

def create_header():
    header_layout=html.Div(className='hfeed site', id='page',children=[
    html.Header(className='header',id='masthead', children=[
    html.Div(className='header-div', children=[
    html.Div(className='header-div2',children=[    
    html.A(href='',className='active',children='Home'),
    html.A(href='',children='Review Check'),
    html.A(href='project.py',children='Word Cloud'),
    html.A(href='contact.py',children='Contact Me')
    ])
    ])
    ])
    ])
 
    return header_layout

def create_footer():
    footer_layout=html.Footer(className='site-footer', id='colophon', children=[
    html.Div(className='site-primary-footer-wrap ast-builder-grid-row-container site-footer-focus-item ast-builder-grid-row-full ast-builder-grid-row-tablet-full ast-builder-grid-row-mobile-full ast-footer-row-stack ast-footer-row-tablet-stack ast-footer-row-mobile-stack',children=[
    html.Div(className='ast-builder-grid-row-container-inner',children=[
    html.Div(className='ast-builder-footer-grid-columns site-primary-footer-inner-wrap ast-builder-grid-row',children=[
    html.Div(className='site-footer-primary-section-1 site-footer-section site-footer-section-1',children=[
    html.Div(className='footer-widget-area widget-area site-footer-focus-item ast-footer-html-1',children=[
    html.Div(className='ast-header-html inner-link-style-',children=[
    html.Div(className='ast-builder-html-element',children=[
        html.P(children='Phone: +91-9589445122 | Email: chinmayjainst8314@gmail.com')
    ])
    ])
    ]),
    html.Div(className='ast-builder-layout-element ast-flex site-footer-focus-item ast-footer-copyright',children=[
    html.Div(className='ast-footer-copyright',children=[
        html.P(children='Copyright © 2021 Sentiment Analysis')
        ])
    ])  
    ])
    ])
    ])    
    ])    
    ])

    return footer_layout