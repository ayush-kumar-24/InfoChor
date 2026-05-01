class TrustEngine:

    def compute(self, metadata, processed):

        breakdown = {}

        # 🔹 1. Source credibility
        source = metadata.get("source")

        if source == "pubmed":
            source_score = 0.9
        elif source == "youtube":
            source_score = 0.6
        elif source == "blog":
            source_score = 0.5
        else:
            source_score = 0.4

        breakdown["source"] = source_score

        # 🔹 2. Content length quality
        text = processed.get("clean_content", "")
        word_count = len(text.split())

        if word_count > 1000:
            length_score = 0.9
        elif word_count > 500:
            length_score = 0.75
        elif word_count > 200:
            length_score = 0.6
        else:
            length_score = 0.3

        breakdown["length"] = length_score

        # 🔹 3. Language quality
        if text and text[0].isupper():
            language_score = 0.7
        else:
            language_score = 0.5

        breakdown["language"] = language_score

        # 🔹 4. Structure quality (chunks)
        chunks = processed.get("chunks", [])

        if len(chunks) > 5:
            structure_score = 0.8
        elif len(chunks) > 2:
            structure_score = 0.6
        else:
            structure_score = 0.4

        breakdown["structure"] = structure_score

        # 🔥 FINAL WEIGHTED SCORE
        final_score = (
            breakdown["source"] * 0.3 +
            breakdown["length"] * 0.25 +
            breakdown["language"] * 0.2 +
            breakdown["structure"] * 0.25
        )

        return round(final_score, 2), breakdown