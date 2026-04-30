from sklearn.feature_extraction.text import TfidfVectorizer

class Tagger:

    def extract_topics(self, text):

        if not text or len(text) < 50:
            return []

        vectorizer = TfidfVectorizer(
            stop_words='english',
            max_features=5,
            ngram_range=(1,2)   # 🔥 improvement
        )

        X = vectorizer.fit_transform([text])

        return vectorizer.get_feature_names_out().tolist()