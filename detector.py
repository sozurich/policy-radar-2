def detect_policy_news(news_list):
    keywords = ["검정기준", "디지털교과서", "공청회", "교과서 선정", "발행사"]
    filtered = []
    for news in news_list:
        if any(k in news['title'] for k in keywords):
            filtered.append(news)
    return filtered