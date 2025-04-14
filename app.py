import streamlit as st
import requests

# 🔑 Your NewsAPI key
API_KEY = "a41ef6c338fd406582fa328dcacf56da"
SEARCH_URL = "https://newsapi.org/v2/everything"

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

# 🚀 Streamlit UI
def main():
    st.set_page_config(page_title="🔍 News Search", layout="wide")

    st.markdown("<h1 style='text-align: center; color: #3366cc;'>🔍 News Search</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:18px;'>Find the latest news articles by keyword</p>", unsafe_allow_html=True)

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
            st.markdown("### " + (article.get("title") or "Untitled"))

            if article.get("urlToImage"):
                st.image(article["urlToImage"], use_container_width=True)

            st.markdown(f"**Source:** {article['source']['name']}")
            if article.get("publishedAt"):
                st.markdown(f"🕒 Published: {article['publishedAt'][:10]}")
            st.markdown(f"[Read More ➡️]({article['url']})", unsafe_allow_html=True)
            st.markdown("---")

if __name__ == "__main__":
    main()
