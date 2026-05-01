# InfoChor
## Multi-Source Data Ingestion & Trust Scoring Pipeline

---

## Overview

InfoChor is a modular pipeline designed to ingest, process, and evaluate unstructured content from multiple sources such as blogs and YouTube.

The system transforms raw data into structured, machine-consumable output while assigning a trust score based on explainable signals.

This project demonstrates system design thinking for real-world AI pipelines, particularly for use cases like:
- Retrieval-Augmented Generation (RAG)
- Knowledge engines
- Trust-aware search systems

---

## Why This System Matters

Most AI systems consume unstructured internet data without evaluating reliability.

This leads to:
- Low-quality context in retrieval systems  
- Unreliable outputs in AI assistants  
- Lack of trust signals in content pipelines  

InfoChor introduces a trust-aware ingestion layer that ensures:
- Higher quality inputs for AI systems  
- Structured and consistent data transformation  
- Explainable reliability scoring  

This system is designed as a foundational layer for trust-aware AI applications, not just a scraping utility.

---

## System Workflow
Input URL
↓
Source Detection
├── Blog
└── YouTube
↓
Scraper Layer
├── Blog Scraper (HTML Parsing)
└── YouTube Scraper (Transcript / Metadata Fallback)
↓
Validation Layer
├── Source-aware validation
└── Failure handling
↓
Processing Layer
├── Text Cleaning
└── Noise Removal
↓
Semantic Layer
├── Topic Extraction
└── Content Chunking
↓
Trust Engine
├── Source Credibility
├── Content Depth
├── Structure Quality
└── Language Signal
↓
Output Layer
├── Structured JSON
└── Explainable Score Breakdown
---## Key Features### Multi-Source Ingestion- Blog scraping using HTML parsing  - YouTube ingestion via transcript API  - Metadata fallback when transcripts are unavailable  ### Adaptive Validation- Source-aware validation logic  - Handles variable content formats across sources  ### Content Processing- Removes UI noise and irrelevant text  - Normalizes and cleans extracted content  ### Semantic Extraction- TF-IDF based topic extraction  - Phrase prioritization and filtering  - Content chunking for AI pipelines  ### Explainable Trust Scoring| Signal | Description ||------|------------|| Source | Credibility of origin || Length | Depth of content || Structure | Organization via chunks || Language | Basic readability signal |---### Robust Failure Handling- Graceful handling of missing transcripts  - Fallback strategies for incomplete data  - Structured failure responses  ---## Example Output```json{  "status": "success",  "document": {    "title": "...",    "source": "youtube",    "word_count": 39  },  "insights": {    "topics": [...],    "trust_score": 0.49,    "score_breakdown": {      "source": 0.6,      "length": 0.3,      "language": 0.7,      "structure": 0.4    }  },  "content": {    "preview": "...",    "chunks": [...]  }}

Design Decisions
Rule-Based Trust Engine


Interpretable


Deterministic


Easy to debug


Hybrid Topic Extraction


TF-IDF for relevance


Heuristics for quality filtering


Source-Aware Validation


Blogs → long-form validation


YouTube → short-form fallback validation


Fallback Strategy


Attempts primary extraction


Falls back to metadata


Ensures pipeline continuity



Folder Structure
src/ ├── scrapers/ │    ├── blog.py │    ├── youtube.py │ ├── processing/ │    ├── cleaner.py │    ├── tagging.py │ ├── chunking/ │    ├── chunker.py │ ├── scoring/ │    ├── trust_engine.py │ ├── pipeline/ │    ├── orchestrator.py │ ├── utils/ │    ├── file_handler.py │ ├── models/ │    ├── schemas.py

How to Run
Install dependencies
pip install -r requirements.txt
Run the pipeline
python main.py

Assignment Coverage


Structured Data Ingestion → Multi-source support


Metadata Extraction → Title, content, topics


Reliability Scoring → Explainable trust engine


Robustness → Handles missing/partial data



Positioning
InfoChor is not just a scraper.
It is a trust-aware data ingestion system designed for AI pipelines.

Author
Ayush Kumar

License
MIT License
