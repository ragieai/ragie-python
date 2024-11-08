"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from ragie.types import BaseModel
from typing import Dict, List, Optional, Union
from typing_extensions import NotRequired, TypedDict


class PartitionStrategy(str, Enum):
    HI_RES = "hi_res"
    FAST = "fast"


ConnectionBaseMetadataTypedDict = Union[str, int, bool, List[str]]


ConnectionBaseMetadata = Union[str, int, bool, List[str]]


class ConnectionBaseTypedDict(TypedDict):
    partition_strategy: PartitionStrategy
    metadata: NotRequired[Dict[str, ConnectionBaseMetadataTypedDict]]
    r"""Metadata for the document. Keys must be strings. Values may be strings, numbers, booleans, or lists of strings. Numbers may be integers or floating point and will be converted to 64 bit floating point. 1000 total values are allowed. Each item in an array counts towards the total. The following keys are reserved for internal use: `document_id`, `document_type`, `document_source`, `document_name`, `document_uploaded_at`."""


class ConnectionBase(BaseModel):
    partition_strategy: PartitionStrategy

    metadata: Optional[Dict[str, ConnectionBaseMetadata]] = None
    r"""Metadata for the document. Keys must be strings. Values may be strings, numbers, booleans, or lists of strings. Numbers may be integers or floating point and will be converted to 64 bit floating point. 1000 total values are allowed. Each item in an array counts towards the total. The following keys are reserved for internal use: `document_id`, `document_type`, `document_source`, `document_name`, `document_uploaded_at`."""