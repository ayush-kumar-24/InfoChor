import requests
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi
from src.models.schemas import RawDocument


class YouTubeScraper:

    def fetch(self, url: str) -> RawDocument:

        video_id = self.extract_video_id(url)

        # 🔥 STEP 1 — TRY TRANSCRIPT
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            content = " ".join([t["text"] for t in transcript])

            if content.strip():
                return RawDocument(
                    source="youtube",
                    url=url,
                    title="YouTube Video",
                    author=None,
                    content=content,
                    metadata={"type": "transcript"}
                )

        except:
            pass

        # 🔥 STEP 2 — FALLBACK (SCRAPE TITLE + DESCRIPTION)
        try:
            headers = {
                "User-Agent": "Mozilla/5.0"
            }

            res = requests.get(url, headers=headers)
            soup = BeautifulSoup(res.text, "html.parser")

            title = soup.title.string if soup.title else "YouTube Video"

            # Try meta description
            description_tag = soup.find("meta", {"name": "description"})
            description = description_tag["content"] if description_tag else ""

            content = title + " " + description

            return RawDocument(
                source="youtube",
                url=url,
                title=title,
                author=None,
                content=content,
                metadata={"type": "metadata_fallback"}
            )

        except Exception as e:
            return RawDocument(
                source="youtube",
                url=url,
                title=None,
                author=None,
                content="",
                metadata={"error": str(e)}
            )

    def extract_video_id(self, url: str):
        if "v=" in url:
            return url.split("v=")[-1].split("&")[0]
        elif "youtu.be/" in url:
            return url.split("youtu.be/")[-1]
        else:
            raise ValueError("Invalid YouTube URL")