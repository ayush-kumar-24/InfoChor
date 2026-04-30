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