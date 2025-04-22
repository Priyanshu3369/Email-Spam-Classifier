# 📧 Email Spam Classifier

An intelligent web app built using Flask that detects whether an input email message is **Spam** or **Not Spam** using Machine Learning (NLP + TF-IDF + ML Model).

---

## 🚀 Quick Setup Guide

### 📌 Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/email-spam-classifier.git
cd email-spam-classifier

🧰 Step 2: Install Dependencies

Install all the necessary Python libraries using the `requirements.txt` file:

```bash
pip install -r requirements.txt


📂 Step 3: Download or Train Model

✅ Option 1: Using Pre-trained Model
Download the following files and place them in the root project directory:

- `model.pkl`  
- `vectorizer.pkl`

---

#### 🛠️ Option 2: Train Your Own Model
Use any spam classification dataset (e.g., **Enron Dataset**), then follow these steps:

**Preprocessing Includes:**
- Tokenization  
- Stopword Removal  
- Stemming  

**Train a model** (e.g., Logistic Regression or Naive Bayes) using scikit-learn.  
After training, save your model and vectorizer like this:

```python
import pickle

# Save the model and vectorizer
pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(tfidf_vectorizer, open('vectorizer.pkl', 'wb'))


▶️ Step 4: Run the Flask App
bash
Copy
Edit
python app.py
By default, the app runs on:

cpp
Copy
Edit
http://127.0.0.1:5000/


🌐 Step 5: Access the App
Open your browser.

Go to:

cpp
Copy
Edit
http://127.0.0.1:5000/
Paste an email message into the textbox.

Click Check for Spam.

View the prediction displayed at the top as a beautiful heading 🎯


🌓 Step 6: Toggle Dark Mode
Click the 🌙 icon to switch between Light and Dark themes.


🛠 Troubleshooting
Missing model.pkl or vectorizer.pkl?
Make sure they exist in the project root.

Dependencies not installed?
Re-run: pip install -r requirements.txt


🪪 License
Licensed under the MIT License. See LICENSE file for details.


🤝 Contributing
Pull requests are welcome! Feel free to fork the project and submit improvements.


🌟 Don't forget to leave a ⭐ on GitHub if this helped you!