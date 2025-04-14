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

## 🛠️ Setup Instructions

1. **Clone the repo:**

   git clone https://github.com/ishanwagh1909/News-Aggregator-.git
   cd news-aggregator

2. **Install dependencies:**

   pip install -r requirements.txt

3. **Add your NewsAPI key:**

   Open `app.py` and replace the placeholder value of `API_KEY` with your actual API key from https://newsapi.org.

4. **Run the app:**

   streamlit run main.py

---

## 📦 Requirements

See `requirements.txt`

---

## 📌 Notes

- The app uses the `everything` endpoint to search for articles using keywords.
- Currently, it fetches English-language articles and shows the latest results.
- You can customize filters like date range, language, or sources in the code.

---

## 📄 License

MIT License — free to use and modify.

---

## 💡 Author

Made with ❤️ by Ishan Wagh
