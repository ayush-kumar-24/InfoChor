from sklearn.feature_extraction.text import TfidfVectorizer


class Tagger:

    def extract_topics(self, text):

        vectorizer = TfidfVectorizer(
            stop_words="english",
            max_features=50,
            ngram_range=(1, 3)
        )

        X = vectorizer.fit_transform([text])

        feature_names = vectorizer.get_feature_names_out()
        scores = X.toarray()[0]

        ranked = sorted(
            zip(feature_names, scores),
            key=lambda x: x[1],
            reverse=True
        )

        topics = []

        # 🔥 domain keywords to BOOST
        important_phrases = [
            "artificial intelligence",
            "general intelligence",
            "artificial general intelligence",
            "machine intelligence",
            "ai systems"
        ]

        # 🔥 STEP 1 — capture important phrases first
        for phrase in important_phrases:
            if phrase in text.lower():
                topics.append(phrase)

            if len(topics) >= 3:
                break

        # 🔥 STEP 2 — fill remaining with TF-IDF
        for word, score in ranked:

            if len(word) < 4:
                continue

            if word in ["systems", "tasks", "ability", "capabilities"]:
                continue

            if any(word in existing or existing in word for existing in topics):
                continue

            topics.append(word)

            if len(topics) == 5:
                break

        return topics