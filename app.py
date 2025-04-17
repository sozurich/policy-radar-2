import streamlit as st
from crawler import get_news, get_article_text
from detector import detect_policy_news
from summarizer import summarize_text

st.title("📰 교과서 정책 뉴스 요약")

with st.spinner("뉴스 수집 중..."):
    news_list = get_news()
    filtered = detect_policy_news(news_list)

st.success(f"정책 관련 뉴스 {len(filtered)}건")

for news in filtered:
    st.subheader(news['title'])
    st.markdown(f"[기사 링크]({news['url']})")

    article = get_article_text(news['url'])
    summary = summarize_text(article)

    st.markdown("✅ **요약문:**")
    st.info(summary)
    st.markdown("---")