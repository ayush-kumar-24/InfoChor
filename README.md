InfoChor

Multi-Source Data Ingestion & Trust Scoring Pipeline

Overview

InfoChor is a modular data pipeline designed to ingest, process, and evaluate unstructured content from multiple sources such as blogs and YouTube.

The system transforms raw content into structured, machine-consumable data while assigning a trust score based on explainable signals.

This project is built to demonstrate real-world system design thinking for AI pipelines, particularly in contexts like retrieval-augmented generation (RAG), knowledge engines, and trust-aware search systems.

Problem Statement

Most AI systems consume data from the internet without evaluating its reliability or structure.

This leads to:

Low-quality context in RAG systems
Unreliable outputs in AI assistants
Lack of trust signals in content pipelines

InfoChor addresses this by introducing a trust-aware ingestion layer.

System Architecture
Input (URL)
   |
   v
[Scraper Layer]
   |---- Blog Scraper
   |---- YouTube Scraper (Transcript / Fallback)
   |
   v
[Processing Layer]
   |---- Text Cleaning
   |---- Content Validation
   |
   v
[Semantic Layer]
   |---- Topic Extraction (TF-IDF + Heuristics)
   |---- Content Chunking
   |
   v
[Trust Engine]
   |---- Source Credibility
   |---- Content Depth
   |---- Structure Quality
   |---- Language Signal
   |
   v
[Output Layer]
   |---- Structured JSON
   |---- Explainable Score Breakdown
Key Features
1. Multi-Source Ingestion
Blog scraping using HTML parsing
YouTube ingestion via transcript API
Metadata fallback when transcripts are unavailable
2. Adaptive Validation
Different validation thresholds for different sources
Prevents pipeline failure due to source variability
3. Content Processing
Noise removal (UI elements, metadata junk)
Sentence-level filtering
Clean text normalization
4. Semantic Understanding
TF-IDF based topic extraction
Phrase prioritization and redundancy removal
Content chunking for downstream AI usage
5. Explainable Trust Scoring

Score is computed using weighted signals:

Signal	Description
Source	Credibility of origin (blog, YouTube, etc.)
Length	Depth of content
Structure	Chunk distribution
Language	Basic readability signal

Outputs include both:

Final score
Score breakdown (transparent logic)
6. Robust Failure Handling
Graceful handling of missing transcripts
Structured failure responses
No pipeline crashes
Example Output
{
  "status": "success",
  "document": {
    "title": "...",
    "source": "youtube",
    "word_count": 39
  },
  "insights": {
    "topics": [...],
    "trust_score": 0.49,
    "score_breakdown": {
      "source": 0.6,
      "length": 0.3,
      "language": 0.7,
      "structure": 0.4
    }
  },
  "content": {
    "preview": "...",
    "chunks": [...]
  }
}
Design Decisions
Rule-Based Trust Engine

Chosen for:

Interpretability
Deterministic behavior
Easy debugging

Future scope includes ML-based scoring.

Hybrid Topic Extraction
TF-IDF for statistical relevance
Heuristic filtering for semantic quality

Avoids:

generic keywords
duplicated concepts
Source-Aware Validation

Different content sources require different validation logic.

Example:

Blog → long-form content
YouTube fallback → short metadata
Fallback Strategy

System does not assume ideal data conditions.

Instead:

Attempts primary extraction
Falls back to alternative signals
Continues pipeline execution
Folder Structure
src/
 ├── scrapers/
 │    ├── blog.py
 │    ├── youtube.py
 │
 ├── processing/
 │    ├── cleaner.py
 │    ├── tagging.py
 │
 ├── chunking/
 │    ├── chunker.py
 │
 ├── scoring/
 │    ├── trust_engine.py
 │
 ├── pipeline/
 │    ├── orchestrator.py
 │
 ├── utils/
 │    ├── file_handler.py
 │
 ├── models/
 │    ├── schemas.py
How to Run
1. Install dependencies
pip install -r requirements.txt
2. Run pipeline
python main.py
3. Test with inputs

Blog:

https://example.com/blog-article

YouTube:

https://www.youtube.com/watch?v=...
Current Limitations
YouTube transcripts are not always available
Topic extraction is heuristic-based, not semantic embeddings
Trust score is rule-based (not learned)
Future Improvements
ML-based trust scoring
Embedding-based topic extraction
API layer (FastAPI)
UI dashboard (Streamlit)
Integration with RAG pipelines
Real-time ingestion
Positioning

InfoChor is not just a scraper.

It is a trust-aware data ingestion system designed for AI pipelines.

It can act as:

Pre-processing layer for LLM systems
Content reliability filter
Knowledge base builder
Author

Ayush Kumar
Founder-minded builder focused on AI systems and real-world problem solving

License

MIT License