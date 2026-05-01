InfoChor
Multi-Source Data Ingestion & Trust Scoring Pipeline

Overview
InfoChor is a modular pipeline designed to ingest, process, and evaluate unstructured content from multiple sources such as blogs and YouTube.
The system transforms raw data into structured, machine-consumable output while assigning a trust score based on explainable signals.
This project demonstrates system design thinking for real-world AI pipelines, particularly for use cases like retrieval-augmented generation (RAG), knowledge engines, and trust-aware search systems.

Why This System Matters
Most AI systems consume unstructured internet data without evaluating reliability.
This leads to:


low-quality context in retrieval systems


unreliable outputs in AI assistants


lack of trust signals in content pipelines


InfoChor introduces a trust-aware ingestion layer that ensures:


higher quality inputs for AI systems


structured and consistent data transformation


explainable reliability scoring


This system is designed as a foundational layer for trust-aware AI applications, not just a scraping utility.

System Workflow
Input URL   |   v[Source Detection]   |---- Blog   |---- YouTube   |   v[Scraper Layer]   |---- Blog Scraper (HTML Parsing)   |---- YouTube Scraper (Transcript / Metadata Fallback)   |   v[Validation Layer]   |---- Source-aware content validation   |---- Failure handling   |   v[Processing Layer]   |---- Text Cleaning   |---- Noise Removal   |   v[Semantic Layer]   |---- Topic Extraction (TF-IDF + Heuristics)   |---- Content Chunking   |   v[Trust Engine]   |---- Source Credibility   |---- Content Depth   |---- Structure Quality   |---- Language Signal   |   v[Output Layer]   |---- Structured JSON   |---- Explainable Score Breakdown

Key Features
Multi-Source Ingestion


Blog scraping using HTML parsing


YouTube ingestion via transcript API


Metadata fallback when transcripts are unavailable



Adaptive Validation


Source-aware validation logic


Prevents pipeline failure due to variable data formats



Content Processing


Removal of UI noise and irrelevant text


Sentence-level filtering


Clean normalization of extracted content



Semantic Extraction


TF-IDF based topic extraction


Phrase prioritization and redundancy removal


Content chunking for downstream AI systems



Explainable Trust Scoring
The trust score is computed using multiple weighted signals:
SignalDescriptionSourceCredibility of originLengthDepth of contentStructureContent organization via chunksLanguageBasic readability signal
The system outputs:


final trust score


score breakdown for transparency



Robust Failure Handling


Graceful handling of missing transcripts


Fallback strategies for incomplete data


Structured failure responses



Example Output
{  "status": "success",  "document": {    "title": "...",    "source": "youtube",    "word_count": 39  },  "insights": {    "topics": [...],    "trust_score": 0.49,    "score_breakdown": {      "source": 0.6,      "length": 0.3,      "language": 0.7,      "structure": 0.4    }  },  "content": {    "preview": "...",    "chunks": [...]  }}

Design Decisions
Rule-Based Trust Engine
Chosen for:


interpretability


deterministic behavior


ease of debugging


Future direction includes ML-based scoring.

Hybrid Topic Extraction


TF-IDF for statistical relevance


Heuristic filtering for semantic quality


Ensures meaningful topics and avoids redundancy.

Source-Aware Validation
Different content sources require different validation thresholds.
Example:


Blogs → long-form validation


YouTube fallback → short-form validation



Fallback Strategy
The system assumes imperfect data conditions.
If primary extraction fails:


fallback mechanisms are triggered


pipeline continues execution


structured output is still generated



Folder Structure
src/ ├── scrapers/ │    ├── blog.py │    ├── youtube.py │ ├── processing/ │    ├── cleaner.py │    ├── tagging.py │ ├── chunking/ │    ├── chunker.py │ ├── scoring/ │    ├── trust_engine.py │ ├── pipeline/ │    ├── orchestrator.py │ ├── utils/ │    ├── file_handler.py │ ├── models/ │    ├── schemas.py

How to Run
Install dependencies
pip install -r requirements.txt

Run the pipeline
python main.py

Test Inputs
Blog:
https://example.com/blog
YouTube:
https://www.youtube.com/watch?v=...

Assignment Coverage
This system fulfills the assignment requirements:


Structured Data Ingestion
Multi-source scraping (blogs + YouTube)


Metadata Extraction
Title, content, and semantic topics


Reliability Scoring
Explainable trust scoring engine


Real-World Robustness
Handles missing data with fallback strategies



Example Use Case
Input:


Blog article or YouTube video


Output:


Extracted topics


Trust score with explanation


Structured content chunks


Enables:


RAG pipelines


AI assistants


knowledge engines



Current Limitations


YouTube transcripts are not always available


Topic extraction is heuristic-based


Trust scoring is rule-based



Future Improvements


ML-based trust scoring


Embedding-based topic extraction


API layer (FastAPI)


UI dashboard (Streamlit)


Real-time ingestion



Positioning
InfoChor is not just a scraper.
It is a trust-aware data ingestion system designed for AI pipelines.

Author
Ayush Kumar

License
MIT License