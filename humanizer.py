from transformers import pipeline
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import textstat

paraphraser = pipeline("text2text-generation", model="Vamsi/T5_Paraphrase_Paws")

def humanize_text(original):
    rewritten = paraphraser(original, max_length=150, num_return_sequences=1)[0]['generated_text']
    polished = str(TextBlob(rewritten).correct())
    vectorizer = TfidfVectorizer().fit_transform([original, polished])
    similarity = cosine_similarity(vectorizer[0:1], vectorizer[1:2])[0][0]
    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(polished)
    readability = textstat.flesch_reading_ease(polished)
    return polished, similarity, sentiment, readability
