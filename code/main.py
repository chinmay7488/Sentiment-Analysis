import dash
import dash_html_components as html
import dash_core_components as dbc
from dash.dependencies import Input, Output
from pages import header_footer,contact,check_review as check,home,word_cloud
import pandas as pd
import plotly.express as px
import pickle
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

app =dash.Dash(__name__)

def load_model():
    global scrappedReviews
    scrappedReviews = pd.read_csv('ScrapedReviews.csv')
  
    global pickle_model
    file = open("models/model_pickle.pkl", 'rb') 
    pickle_model = pickle.load(file)

    global vocab
    file = open("models/vocab_pickle.pkl", 'rb') 
    vocab = pickle.load(file)
    


def check_review(reviewText):
    transformer = TfidfTransformer()
    loaded_vec = CountVectorizer(decode_error="replace",vocabulary=vocab)
    vectorised_review = transformer.fit_transform(loaded_vec.fit_transform([reviewText]))
    
    return pickle_model.predict(vectorised_review)

def get_top_n_words():
        
    vec = CountVectorizer().fit(scrappedReviews['Review'])
    bag_of_words = vec.transform(scrappedReviews['Review'])
    sum_words = bag_of_words.sum(axis=0) 
    words_freq = [(word) for word, idx in vec.vocabulary_.items() if word not in stopwords.words('english')]
    words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True) 
    
    return words_freq[:21]


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/home':
        return home.create_home_page()
    if pathname == '/check_review':
        return check.create_checkreview_page()
    if pathname == '/contact_me':
        return contact.create_contact_page()
    if pathname == '/word_cloud':
        return word_cloud.create_project_page(scrappedReviews.sample(n=100)['Review'])
    else:
        return "404 Page Error! Please choose a link"

@app.callback(
    [Output('review-type',  'children' ),
    Output('review-dropdown-gif','src')
    ],
    [
    Input('review-dropdown', 'value')
    ]
    )
def update_app_ui2(review_text):
    if review_text==None:
        result=''
        src='https://media.giphy.com/media/4Zt2BAmW8NNBe/giphy.gif'
        return result,src
    response = check_review(review_text)
    print('response = ', response)

    if (response[0] == 0):
        result = 'Negative Review'
        src='https://media.giphy.com/media/gGn9eq3prU6m4/giphy.gif'
    elif  (response[0] == 1):
        result = 'Positive Review'
        src='https://media.giphy.com/media/11sBLVxNs7v6WA/giphy.gif'
    else:
        result = 'Unknown'
        src='https://media.giphy.com/media/4Zt2BAmW8NNBe/giphy.gif'
        
    return result,src

def main():
    load_model()
    app.title='Sentiment Analysis'
    header =header_footer.create_header()
    footer=header_footer.create_footer()
    app.layout=html.Div(children=[
        dbc.Location(id='url',refresh=False),
        header,
        html.Div(id='page-content',children=[]),
        footer
    ])
    app.run_server()


if __name__=='__main__':
    main()