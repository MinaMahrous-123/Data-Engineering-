import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import sqlite3

feedback_data = sqlite3.connect('CustomerFeedbackDB.db') 
feedback_data['Feedback_Text'] = feedback_data['Feedback_Text'].str.lower()
feedback_data['Feedback_Text'] = feedback_data['Feedback_Text'].str.replace('[^\w\s]', '')
nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def process_text(text):
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if not word in stop_words]
    return " ".join(filtered_text)

feedback_data['Processed_Text'] = feedback_data['Feedback_Text'].apply(process_text)
print(feedback_data.head())











