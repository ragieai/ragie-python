"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .documentchunk import DocumentChunk, DocumentChunkTypedDict
from .pagination import Pagination, PaginationTypedDict
from ragie.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class DocumentChunkListTypedDict(TypedDict):
    pagination: PaginationTypedDict
    chunks: List[DocumentChunkTypedDict]


class DocumentChunkList(BaseModel):
    pagination: Pagination

    chunks: List[DocumentChunk]
