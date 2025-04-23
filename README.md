
# 📧 Email Spam Classifier

An intelligent web app built with **Flask** that detects whether an input email message is **Spam** or **Not Spam** using **Machine Learning** (NLP + TF-IDF + ML Model).

---

## 🚀 Quick Setup Guide

### 📌 Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/email-spam-classifier.git
cd email-spam-classifier
```

---

### 🧰 Step 2: Install Dependencies

Install all the necessary Python libraries using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

### 📂 Step 3: Download or Train Model

#### ✅ Option 1: Using Pre-trained Model

Download the following files and place them in the project root directory:

- `model.pkl`
- `vectorizer.pkl`

#### 🛠️ Option 2: Train Your Own Model

Use any spam classification dataset (e.g., **Enron Dataset**), then follow these steps:

**Preprocessing Includes:**
- Tokenization  
- Stopword Removal  
- Stemming  

**Train a model** (e.g., Logistic Regression or Naive Bayes) using `scikit-learn`.

After training, save your model and vectorizer:

```python
import pickle

# Save the model and vectorizer
pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(tfidf_vectorizer, open('vectorizer.pkl', 'wb'))
```

---

### ▶️ Step 4: Run the Flask App

```bash
python app.py
```

By default, the app runs on:

```
[http://127.0.0.1:5000/](https://email-spam-classifier-0ar4.onrender.com/predict)
```

---

### 🌐 Step 5: Access the App

1. Open your browser and go to: [Live Demo](https://email-spam-classifier-0ar4.onrender.com/predict)
2. Paste an email message into the textbox.
3. Click **Check for Spam**.
4. View the prediction displayed at the top as a beautiful heading 🎯

---

### 🌓 Step 6: Toggle Dark Mode

Click the 🌙 icon to switch between Light and Dark themes.

---

## 🛠 Troubleshooting

- **Missing `model.pkl` or `vectorizer.pkl`?**  
  Make sure they exist in the project root directory.

- **Dependencies not installed?**  
  Re-run:  
  ```bash
  pip install -r requirements.txt
  ```

---

## 🪪 License

Licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Pull requests are welcome! Feel free to fork the project and submit improvements.

---

## 🌟 Support

If you found this helpful, don’t forget to ⭐ the repo on GitHub!
