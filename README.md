# InfoChor
## Multi-Source Data Ingestion & Trust Scoring Pipeline

---

## Overview

InfoChor is a modular pipeline that ingests unstructured content from blogs and YouTube, processes it into structured data, and assigns a reliability score using explainable signals.

It is designed as a preprocessing layer for AI systems that depend on high-quality, trustworthy input data.

---

## Why This System Matters

Most AI systems consume internet data without evaluating its reliability.

This leads to:

- Poor-quality context in retrieval systems  
- Unreliable outputs in AI assistants  
- No trust signal in data pipelines  

InfoChor solves this by introducing:

- Structured content ingestion  
- Consistent data transformation  
- Explainable trust scoring  

This makes it useful as a **trust-aware input layer for AI pipelines**.

---

## System Workflow
Input URL
↓
Source Detection (Blog / YouTube)
↓
Scraper Layer
↓
Validation Layer
↓
Processing Layer
↓
Semantic Layer
↓
Trust Engine
↓
Structured Output


---

## Key Features

### Multi-Source Ingestion
- Blog scraping using HTML parsing  
- YouTube ingestion via transcript API  
- Metadata fallback when transcripts are unavailable  

### Adaptive Validation
- Source-aware validation logic  
- Different thresholds for blogs and YouTube  

### Content Processing
- Removes UI noise and irrelevant text  
- Normalizes extracted content  

### Semantic Extraction
- TF-IDF based topic extraction  
- Filters redundant or weak terms  
- Splits content into chunks  

### Explainable Trust Scoring

- Source credibility  
- Content length  
- Structure quality  
- Language signal  

Each score includes a **breakdown for transparency**.

### Robust Failure Handling
- Handles missing transcripts  
- Uses fallback strategies  
- Returns structured failure responses  

---

## Example Output

```json
{
  "status": "success",
  "document": {
    "title": "...",
    "source": "youtube",
    "word_count": 39
  },
  "insights": {
    "topics": [...],
    "trust_score": 0.49
  },
  "content": {
    "preview": "...",
    "chunks": [...]
  }
}
Design Decisions
Trust Engine
Rule-based for interpretability
Deterministic behavior
Easy to debug
Topic Extraction
TF-IDF for relevance
Heuristics for filtering
Validation Strategy
Blogs → long-form validation
YouTube → short-form fallback validation
Fallback Strategy
Try primary extraction
Fall back to metadata
Ensure pipeline continuity
Folder Structure
src/
 ├── scrapers/
 ├── processing/
 ├── chunking/
 ├── scoring/
 ├── pipeline/
 ├── utils/
 ├── models/
How to Run

Install dependencies:

pip install -r requirements.txt

Run the pipeline:

python main.py
Assignment Coverage
Structured Data Ingestion → Multi-source support
Metadata Extraction → Title, content, topics
Reliability Scoring → Explainable trust engine
Robustness → Handles missing or partial data
Positioning

InfoChor is not just a scraper.

It is a trust-aware data ingestion system designed for AI pipelines.

Author

Ayush Kumar

License

MIT License


---

# 🧠 WHAT I FIXED

- Proper headings (`##`, `###`)
- Bullet points everywhere needed
- Removed clutter text
- Fixed broken workflow block
- Clean, readable sections
- No garbage formatting

---

# 🚀 NEXT STEP

Now:

```bash
git add README.md
git commit -m "Fix README formatting and clarity"
git push