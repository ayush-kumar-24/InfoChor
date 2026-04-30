print("🔥 NEW BLOG SCRAPER RUNNING")
import requests
from bs4 import BeautifulSoup
from src.models.schemas import RawDocument


class BlogScraper:

    def fetch(self, url: str) -> RawDocument:

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
        }

        try:
            res = requests.get(url, headers=headers, timeout=15)
            res.raise_for_status()
        except Exception as e:
            return RawDocument(
                source="blog",
                url=url,
                title=None,
                author=None,
                content="",
                metadata={"error": str(e)}
            )

        # 🔥 DEBUG (keep temporarily)
        print("STATUS:", res.status_code)
        print("HTML LENGTH:", len(res.text))
        print("HTML PREVIEW:", res.text[:300])

        soup = BeautifulSoup(res.text, "html.parser")

        title = soup.title.string.strip() if soup.title else None
        
        # extract ALL visible text
        content = soup.get_text(separator=" ")


        # 🔹 cleanup
        content = " ".join(content.split())
        
        print("HTML LENGTH:", len(res.text))
        print("EXTRACTED CONTENT LENGTH:", len(content))

        return RawDocument(
            source="blog",
            url=url,
            title=title,
            author=None,
            content=content,
            metadata={}
        )