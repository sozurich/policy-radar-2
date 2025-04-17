from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text):
    if not text or len(text) < 100:
        return "본문이 부족하거나 요약 불가"
    try:
        result = summarizer(text[:1000], max_length=100, min_length=30, do_sample=False)
        return result[0]['summary_text']
    except:
        return "요약 실패"