import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc


def create_check_review_page():
    layout = html.Div(className='review-check-page',children=[
        html.Div(className='review-check-page-div',children=[
            dbc.Textarea(placeholder='Enter your review...', required=True,className='check-review-enter-name',id='textarea-check-review'),
            dbc.Button(type='submit',children='Check Review',className='check-review-submit-btn',id='check-review-btn',n_clicks=0),
            html.Img(src='https://media.giphy.com/media/KGSxFwJJHQPsKzzFba/giphy.gif',width=300,height=300,className='check-review-img',id='check-review-gif'),
            html.H4('Enter something',className='check-review-h4',id='check-review-h4')
        ])
    ])


    return layout