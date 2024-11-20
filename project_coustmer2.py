import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
import sqlite3

feedback_data = sqlite3.connect('CustomerFeedbackDB.db') 
feedback_data['Sentiment'] = feedback_data['Feedback_Text'].apply(lambda x: 1 if 'good' in x else 0)
X = feedback_data['Processed_Text']
y = feedback_data['Sentiment']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)
model = MultinomialNB()
model.fit(X_train_vec, y_train)
y_pred = model.predict(X_test_vec)
print(classification_report(y_test, y_pred))
