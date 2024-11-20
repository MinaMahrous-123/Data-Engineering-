import mlflow
import mlflow.sklearn
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# تحميل البيانات
feedback_data = pd.read_csv('feedback_data.csv')

# تجهيز البيانات
X = feedback_data['Processed_Text']
y = feedback_data['Sentiment']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# بدء تتبع التجربة في MLflow
mlflow.start_run()

# تدريب النموذج
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# التنبؤ على بيانات الاختبار
y_pred = model.predict(X_test_vec)

# حساب الدقة
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# تسجيل النموذج والمعلمات في MLflow
mlflow.log_metric("accuracy", accuracy)
mlflow.sklearn.log_model(model, "model")

# إنهاء التجربة
mlflow.end_run()
