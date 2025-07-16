Here's an updated version of the README that includes information about setting up a **virtual environment** and other necessary details for your **News Aggregator web app**:

---

# 🔍 News Aggregator with Keyword Search

This is a simple and beautiful **News Aggregator web app** built using Streamlit and NewsAPI.   
It allows users to search the latest news articles by any keyword — such as "AI", "cryptocurrency", "sports", or any trending topic worldwide.

---

## ✨ Features

- 🔍 Keyword-based news search (no fixed categories)
- 📰 Fetches latest news using NewsAPI's `everything` endpoint
- 🌍 Global news in English
- 🧱 Responsive 3-column layout
- 🖼️ Article images, publish date, source, and direct links
- ⚡ Fast and lightweight UI powered by Streamlit

---

## 🚀 Demo

![screenshot](image.png)

---

### **Add your NewsAPI key:**

   - Sign up at [NewsAPI](https://newsapi.org/) to get your API key.
   - Open `app.py` and replace the placeholder value of `API_KEY` with your actual API key:
     ```python
     API_KEY = 'your_api_key_here'
     ```

### **Run the app:**

   Once the setup is complete, start the app by running:
   ```bash
   streamlit run app.py
   ```

---

---

## Author

Made with ❤️ by Ishan Wagh
---

