from pydantic import BaseModel, Field
from typing import List, Optional, Dict


# 🔹 Raw Data (directly from scraper)
class RawDocument(BaseModel):
    source: str
    url: Optional[str] = None
    title: Optional[str] = None
    author: Optional[str] = None
    publish_date: Optional[str] = None

    content: str

    metadata: Dict = Field(default_factory=dict)


# 🔹 After processing & enrichment
class ProcessedDocument(BaseModel):
    source: str
    url: Optional[str]
    title: Optional[str]
    author: Optional[str]
    publish_date: Optional[str]

    clean_content: str
    language: Optional[str]
    region: Optional[str]

    topics: List[str] = []

    metadata: Dict = Field(default_factory=dict)


# 🔹 Final output
class ScoredDocument(BaseModel):
    source: str
    url: Optional[str]
    title: Optional[str]
    author: Optional[str]

    topics: List[str]
    chunks: List[str]

    trust_score: float

    metadata: Dict = Field(default_factory=dict)