"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from ragie.types import BaseModel
from typing import Any, Dict, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class RetrieveParamsTypedDict(TypedDict):
    query: str
    r"""The query to search with when retrieving document chunks."""
    top_k: NotRequired[int]
    r"""The maximum number of chunks to return. Defaults to 8."""
    filter_: NotRequired[Dict[str, Any]]
    r"""The metadata search filter on documents. Returns chunks only from documents which match the filter. The following filter operators are supported: $eq - Equal to (number, string, boolean), $ne - Not equal to (number, string, boolean), $gt - Greater than (number), $gte - Greater than or equal to (number), $lt - Less than (number), $lte - Less than or equal to (number), $in - In array (string or number), $nin - Not in array (string or number). The operators can be combined with AND and OR. Read [Metadata & Filters guide](https://docs.ragie.ai/docs/metadata-filters) for more details and examples."""
    rerank: NotRequired[bool]
    r"""Reranks the chunks for semantic relevancy post cosine similarity. Will be slower but returns a subset of highly relevant chunks. Best for reducing hallucinations and improving accuracy for LLM generation."""
    max_chunks_per_document: NotRequired[int]
    r"""Maximum number of chunks to retrieve per document. Use this to increase the number of documents the final chunks are retreived from. This feature is in beta and may change in the future."""
    

class RetrieveParams(BaseModel):
    query: str
    r"""The query to search with when retrieving document chunks."""
    top_k: Optional[int] = 8
    r"""The maximum number of chunks to return. Defaults to 8."""
    filter_: Annotated[Optional[Dict[str, Any]], pydantic.Field(alias="filter")] = None
    r"""The metadata search filter on documents. Returns chunks only from documents which match the filter. The following filter operators are supported: $eq - Equal to (number, string, boolean), $ne - Not equal to (number, string, boolean), $gt - Greater than (number), $gte - Greater than or equal to (number), $lt - Less than (number), $lte - Less than or equal to (number), $in - In array (string or number), $nin - Not in array (string or number). The operators can be combined with AND and OR. Read [Metadata & Filters guide](https://docs.ragie.ai/docs/metadata-filters) for more details and examples."""
    rerank: Optional[bool] = False
    r"""Reranks the chunks for semantic relevancy post cosine similarity. Will be slower but returns a subset of highly relevant chunks. Best for reducing hallucinations and improving accuracy for LLM generation."""
    max_chunks_per_document: Optional[int] = None
    r"""Maximum number of chunks to retrieve per document. Use this to increase the number of documents the final chunks are retreived from. This feature is in beta and may change in the future."""
    