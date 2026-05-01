from src.scrapers.blog import BlogScraper
from src.scrapers.youtube import YouTubeScraper
from src.processing.cleaner import Processor
from src.processing.tagging import Tagger
from src.chunking.chunker import Chunker
from src.scoring.trust_engine import TrustEngine
from src.utils.file_handler import FileHandler


class Pipeline:

    def run(self, url):

        # 🔥 STEP 0 — SELECT SCRAPER (CRITICAL FIX)
        if "youtube.com" in url or "youtu.be" in url:
            scraper = YouTubeScraper()
            print("🎥 USING YOUTUBE SCRAPER")
        else:
            scraper = BlogScraper()
            print("📝 USING BLOG SCRAPER")

        processor = Processor()
        tagger = Tagger()
        chunker = Chunker()
        scorer = TrustEngine()
        file_handler = FileHandler()

        # 🔹 Step 1: Fetch
        raw = scraper.fetch(url)

        print("RAW CONTENT LENGTH:", len(raw.content))
        print("RAW CONTENT SAMPLE:", raw.content[:200])

        if not raw.content or len(raw.content.strip()) < 30:
            return self._fail(file_handler, url, "Content too small")

        word_count = len(raw.content.split())

       # 🔥 SOURCE-AWARE VALIDATION
        if raw.source == "youtube":
                if word_count < 30:
                     return self._fail(file_handler, url, "Too little content (YouTube)")
        else:
            if word_count < 100:
                return self._fail(file_handler, url, "Too little content")

        # 🔹 Step 2: Process
        processed = processor.clean(raw)

        print("\n--- BEFORE CLEANING ---")
        print(raw.content[:300])

        print("\n--- AFTER CLEANING ---")
        print(processed["clean_content"][:300])

        if not processed["clean_content"] or len(processed["clean_content"]) < 50:
            return self._fail(file_handler, url, "Content too small after cleaning")

        # 🔹 Step 3: Tagging
        topics = tagger.extract_topics(processed["clean_content"])

        # 🔹 Step 4: Chunking
        chunks = chunker.split(processed["clean_content"])
        processed["chunks"] = chunks

        # 🔹 Step 5: Scoring
        score, breakdown = scorer.compute(
            {
                "source": raw.source,
                "author": raw.author,
                "publish_date": raw.publish_date
            },
            processed
        )

        # 🔥 FINAL OUTPUT (WOW FORMAT)
        result = {
            "status": "success",

            "document": {
                "title": raw.title,
                "source": raw.source,
                "word_count": word_count
            },

            "insights": {
                "topics": topics,
                "trust_score": score,
                "score_breakdown": breakdown
            },

            "content": {
                "preview": processed["clean_content"][:300],
                "chunks": chunks[:2]
            }
        }

        file_handler.save(result)

        return result

    def _fail(self, file_handler, url, reason):
        failure_data = {
            "status": "failed",
            "reason": reason,
            "url": url
        }

        file_handler.save_failed(failure_data)
        return failure_data