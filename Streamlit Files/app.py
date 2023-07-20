import streamlit as st
import nltk
import pickle
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')

ps = PorterStemmer()

def preprocess_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    
    text = y[:]
    y.clear()
    
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
            
    text = y[:]
    y.clear()
    
    for i in text:
        y.append(ps.stem(i))
        
    return " ".join(y)

tfidf = pickle.load(open("tfidf.pkl","rb"))
model = pickle.load(open("model.pkl", "rb"))

st.title("Email/SMS Spam Classifier")
st.write("This app predicts whether an email or SMS is Spam or Not Spam.")
st.write("Made By Aditya Goyal.")

input_msg = st.text_area("Enter the message")

if st.button("Predict"):
    data_new = preprocess_text(input_msg)

    tfidf_data = tfidf.transform([data_new])

    result = model.predict(tfidf_data)[0]

    if result == 1:
        st.header("It's Spam")
        st.markdown("**Please be cautious with this message.**")
    else:
        st.header("Not Spam")
        st.markdown("**This message appears to be safe.**")