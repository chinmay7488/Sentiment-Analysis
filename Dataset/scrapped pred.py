import pickle
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer


    
df =  pd.read_csv('ScrapedReviews.csv')



# df.isnull().any(axis = 0)

# #handle the missing data
# df.dropna(inplace =  True)

# #leaving the reviews with rating 3 and collect reviews with
# #rating 1, 2, 4 and 5 onyl


file = open("model_pickle.pkl", 'rb') 
pickle_model = pickle.load(file)
    
file = open("vocab_pickle.pkl", 'rb') 
vocab = pickle.load(file)

features = df.iloc[:,-1]


transformer = TfidfTransformer()
loaded_vec = CountVectorizer(decode_error="replace",vocabulary=vocab)
vectorised_review = transformer.fit_transform(loaded_vec.fit_transform(features))
    

predictions = pickle_model.predict(vectorised_review)

predDf = pd.DataFrame(predictions)
predDf['status'] = np.where(predDf[0] == 1, 'Positive', 'Negative')
predDf = predDf.rename(columns={0:'predictions'})


predDf.to_csv('predictions.csv',index=False)
