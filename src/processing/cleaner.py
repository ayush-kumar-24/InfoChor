import re
from langdetect import detect

class Processor:

    def clean(self, raw_doc):

        text = raw_doc.content

        # 🔹 Remove extra spaces
        text = re.sub(r'\s+', ' ', text)

        # 🔹 Remove UI junk words
        junk_patterns = [
            r"Sign up",
            r"Sign in",
            r"Newsletter",
            r"Privacy",
            r"Terms",
            r"Help",
            r"Press"
        ]

        for pattern in junk_patterns:
            text = re.sub(pattern, "", text, flags=re.IGNORECASE)

        # 🔹 Remove very short sentences
        sentences = text.split(".")
        sentences = [s.strip() for s in sentences if len(s.strip()) > 40]

        clean_text = ". ".join(sentences)

        # 🔹 Language detection
        try:
            lang = detect(clean_text)
        except:
            lang = "unknown"

        return {
            "clean_content": clean_text,
            "language": lang
        }

import re


class Processor:

    def clean(self, raw):
        text = raw.content

        # 🔥 Remove ONLY obvious UI junk
        junk_patterns = [
            r"Sign up", r"Sign in", r"Get app", r"Write", r"Search",
            r"Sitemap", r"Mastodon",
            r"Open in app"
        ]

        for pattern in junk_patterns:
            text = re.sub(pattern, "", text, flags=re.IGNORECASE)

        # 🔥 Remove excessive metadata (light version)
        text = re.sub(r"\d+ min read", "", text)

        # 🔥 LIGHT sentence filtering (not aggressive)
        sentences = re.split(r'[.!?]', text)

        cleaned_sentences = [
            s.strip() for s in sentences
            if len(s.strip()) > 25   # 🔥 lowered threshold
        ]

        # fallback (IMPORTANT)
        if len(cleaned_sentences) < 5:
            cleaned_text = text   # don’t destroy data
        else:
            cleaned_text = ". ".join(cleaned_sentences)

        # 🔹 final cleanup
        cleaned_text = " ".join(cleaned_text.split())

        return {
            "clean_content": cleaned_text,
            "language": "en"
        }