from flask import Flask, render_template, request
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import os

# Initialize Flask app
app = Flask(__name__)

# Initialize Porter Stemmer
ps = PorterStemmer()

# Load the pickled model and vectorizer
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# Function to preprocess and transform the input text
import nltk
from nltk.corpus import stopwords
import string

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')


def transform_text(text):
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

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Predict route with error display
@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_sms = request.form['message']
        transformed_sms = transform_text(input_sms)
        vector_input = tfidf.transform([transformed_sms])
        result = model.predict(vector_input)[0]
        prediction = 'Spam' if result == 1 else 'Not Spam'
        return render_template('index.html', prediction=prediction)
    except Exception as e:
        return f"<h2>🔥 ERROR: {str(e)}</h2>"

# Run the Flask app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
