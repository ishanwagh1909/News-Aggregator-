import streamlit as st
import requests
import spacy
from spacy.lang.en.stop_words import STOP_WORDS

# 🔑 Your NewsAPI key
API_KEY = "a41ef6c338fd406582fa328dcacf56da"
SEARCH_URL = "https://newsapi.org/v2/everything"

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# 🔍 Fetch news using keyword search
def search_news(query):
    params = {
        "apiKey": API_KEY,
        "q": query,
        "pageSize": 12,
        "sortBy": "publishedAt",
        "language": "en"
    }
    response = requests.get(SEARCH_URL, params=params)
    if response.status_code != 200:
        return []
    return response.json().get("articles", [])

# 🧠 NLP Processing
def preprocess_text(text):
    doc = nlp(text)
    tokens = [token.text for token in doc if token.text.lower() not in STOP_WORDS and token.is_alpha]
    pos_tags = [(token.text, token.pos_) for token in doc]
    noun_chunks = [chunk.text for chunk in doc.noun_chunks]
    return tokens, pos_tags, noun_chunks

# 🚀 Streamlit UI
def main():
    st.set_page_config(page_title="🔍 News Search + NLP", layout="wide")

    st.markdown("<h1 style='text-align: center; color: #3366cc;'>🔍 News Search + NLP</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:18px;'>Find the latest news articles by keyword — with NLP insights!</p>", unsafe_allow_html=True)

    query = st.text_input("Enter a topic to search for:", value="cryptocurrency", help="e.g., AI, sports, climate change, Bitcoin")

    if not query:
        st.info("Please enter a keyword to search.")
        return

    st.markdown("---")
    with st.spinner(f"Searching for news about '{query}'..."):
        articles = search_news(query)

    if not articles:
        st.warning("No news articles found or an error occurred.")
        return

    cols = st.columns(3)

    for idx, article in enumerate(articles):
        with cols[idx % 3]:
            title = article.get("title") or "Untitled"
            st.markdown("### " + title)

            if article.get("urlToImage"):
                st.image(article["urlToImage"], use_container_width=True)

            st.markdown(f"**Source:** {article['source']['name']}")
            if article.get("publishedAt"):
                st.markdown(f"🕒 Published: {article['publishedAt'][:10]}")
            st.markdown(f"[Read More ➡️]({article['url']})", unsafe_allow_html=True)

            # ✨ NLP Preview
            if article.get("description"):
                tokens, pos_tags, noun_chunks = preprocess_text(article["description"])
                with st.expander("🧠 NLP Insights"):
                    st.write("**Tokens (cleaned):**", tokens)
                    st.write("**POS Tags:**", pos_tags)
                    st.write("**Noun Phrases:**", noun_chunks)

            st.markdown("---")

if __name__ == "__main__":
    main()
