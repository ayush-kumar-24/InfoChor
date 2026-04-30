class TrustEngine:

    def compute(self, doc, processed):

        # 🔹 1. Source Score
        source_map = {
            "pubmed": 1.0,
            "youtube": 0.7,
            "blog": 0.6
        }
        source_score = source_map.get(doc["source"], 0.5)

        # 🔹 2. Content Length Score
        length = len(processed["clean_content"])
        length_score = min(length / 2000, 1)

        # 🔹 3. Structure Score (based on sentence count)
        sentences = processed["clean_content"].split(".")
        structure_score = min(len(sentences) / 20, 1)

        # 🔹 4. Language Score
        language_score = 1.0 if processed["language"] == "en" else 0.5

        # 🔹 5. Metadata Score
        metadata_score = 0

        if doc.get("author"):
            metadata_score += 0.5
        if doc.get("publish_date"):
            metadata_score += 0.5

        # 🔹 Final weighted score
        final_score = (
            0.25 * source_score +
            0.25 * length_score +
            0.2 * structure_score +
            0.15 * language_score +
            0.15 * metadata_score
        )

        return round(final_score, 2)