"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ragie.types import BaseModel
from typing import Dict, List, Optional, TypedDict, Union
from typing_extensions import NotRequired


CreateDocumentRawParamsMetadataTypedDict = Union[str, int, bool, List[str]]


CreateDocumentRawParamsMetadata = Union[str, int, bool, List[str]]


class TwoTypedDict(TypedDict):
    pass
    

class Two(BaseModel):
    pass
    

DataTypedDict = Union[TwoTypedDict, str]
r"""Document data in a text or JSON format."""


Data = Union[Two, str]
r"""Document data in a text or JSON format."""


class CreateDocumentRawParamsTypedDict(TypedDict):
    data: DataTypedDict
    r"""Document data in a text or JSON format."""
    metadata: NotRequired[Dict[str, CreateDocumentRawParamsMetadataTypedDict]]
    r"""Metadata for the document. Keys must be strings. Values may be strings, numbers, booleans, or lists of strings. Numbers may be integers or floating point and will be converted to 64 bit floating point. 1000 total values are allowed. Each item in an array counts towards the total. The following keys are reserved for internal use: `document_id`, `document_type`, `document_source`, `document_name`, `document_uploaded_at`."""
    

class CreateDocumentRawParams(BaseModel):
    data: Data
    r"""Document data in a text or JSON format."""
    metadata: Optional[Dict[str, CreateDocumentRawParamsMetadata]] = None
    r"""Metadata for the document. Keys must be strings. Values may be strings, numbers, booleans, or lists of strings. Numbers may be integers or floating point and will be converted to 64 bit floating point. 1000 total values are allowed. Each item in an array counts towards the total. The following keys are reserved for internal use: `document_id`, `document_type`, `document_source`, `document_name`, `document_uploaded_at`."""
    