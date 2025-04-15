"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .link import Link, LinkTypedDict
from ragie.types import BaseModel
from typing import Any, Dict, Optional
from typing_extensions import NotRequired, TypedDict


class ScoredChunkTypedDict(TypedDict):
    text: str
    score: float
    id: str
    index: int
    document_id: str
    document_name: str
    document_metadata: Dict[str, Any]
    links: Dict[str, LinkTypedDict]
    metadata: NotRequired[Dict[str, Any]]


class ScoredChunk(BaseModel):
    text: str

    score: float

    id: str

    index: int

    document_id: str

    document_name: str

    document_metadata: Dict[str, Any]

    links: Dict[str, Link]

    metadata: Optional[Dict[str, Any]] = None
