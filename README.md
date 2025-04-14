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

## 🛠️ Setup Instructions

Follow these steps to get your environment set up for the app:

### 1. **Clone the repository:**
   ```bash
   git clone https://github.com/ishanwagh1909/News-Aggregator-.git
   cd news-aggregator
   ```

### 2. **Create and activate a virtual environment (optional but recommended):**

   For **Windows**:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   For **macOS/Linux**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   This will create a virtual environment that isolates dependencies for this project.

### 3. **Install dependencies:**

   Make sure your virtual environment is active, then run:
   ```bash
   pip install -r requirements.txt
   ```

   This will install all the necessary dependencies, including Streamlit and the NewsAPI package.

### 4. **Add your NewsAPI key:**

   - Sign up at [NewsAPI](https://newsapi.org/) to get your API key.
   - Open `app.py` and replace the placeholder value of `API_KEY` with your actual API key:
     ```python
     API_KEY = 'your_api_key_here'
     ```

### 5. **Run the app:**

   Once the setup is complete, start the app by running:
   ```bash
   streamlit run app.py
   ```

   The app should open in your web browser, and you can begin searching for the latest news articles!

---

## 📦 Requirements

The app requires the following Python packages:

- `streamlit`
- `requests`
- `pandas`

These dependencies are listed in `requirements.txt`, which you can install via:

```bash
pip install -r requirements.txt
```

---

## 📌 Notes

- The app uses the `everything` endpoint of the NewsAPI to search for articles using keywords.
- Currently, it fetches English-language articles and shows the latest results.
- You can customize filters like date range, language, or sources in the code by modifying the `NewsAPI` query parameters.

---

## 📄 License

MIT License — free to use and modify.

---

## 💡 Author

Made with ❤️ by Ishan Wagh

---

