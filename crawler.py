import requests
from bs4 import BeautifulSoup

def get_news(keyword="교과서", max_pages=2):
    news_list = []
    for page in range(1, max_pages + 1):
        url = f"https://search.naver.com/search.naver?where=news&query={keyword}&start={page*10-9}"
        res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(res.text, "html.parser")
        links = soup.select("a.info")

        for link in links:
            if link.text == "언론사 선택":
                continue
            news_list.append({"title": link.text, "url": link["href"]})
    return news_list

def get_article_text(news_url):
    try:
        res = requests.get(news_url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")

        paragraphs = soup.select("article p")
        if not paragraphs:
            paragraphs = soup.select("div#dic_area")

        text = " ".join(p.get_text() for p in paragraphs)
        return text.strip()
    except:
        return ""