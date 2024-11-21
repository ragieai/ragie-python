"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from pydantic import model_serializer
from ragie.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from typing import Dict, List, Optional, Union
from typing_extensions import NotRequired, TypedDict


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
    name: NotRequired[str]
    r"""An optional name for the document. If set, the document will have this name. Otherwise it will default to the current timestamp."""
    metadata: NotRequired[Dict[str, CreateDocumentRawParamsMetadataTypedDict]]
    r"""Metadata for the document. Keys must be strings. Values may be strings, numbers, booleans, or lists of strings. Numbers may be integers or floating point and will be converted to 64 bit floating point. 1000 total values are allowed. Each item in an array counts towards the total. The following keys are reserved for internal use: `document_id`, `document_type`, `document_source`, `document_name`, `document_uploaded_at`."""
    external_id: NotRequired[Nullable[str]]
    r"""An optional identifier for the document. A common value might be an id in an external system or the URL where the source file may be found."""
    partition: NotRequired[str]
    r"""An optional partition identifier. Documents can be scoped to a partition. Partitions must be lowercase alphanumeric and may only include the special characters `_` and `-`.  A partition is created any time a document is created or moved to a new partition."""


class CreateDocumentRawParams(BaseModel):
    data: Data
    r"""Document data in a text or JSON format."""

    name: Optional[str] = None
    r"""An optional name for the document. If set, the document will have this name. Otherwise it will default to the current timestamp."""

    metadata: Optional[Dict[str, CreateDocumentRawParamsMetadata]] = None
    r"""Metadata for the document. Keys must be strings. Values may be strings, numbers, booleans, or lists of strings. Numbers may be integers or floating point and will be converted to 64 bit floating point. 1000 total values are allowed. Each item in an array counts towards the total. The following keys are reserved for internal use: `document_id`, `document_type`, `document_source`, `document_name`, `document_uploaded_at`."""

    external_id: OptionalNullable[str] = UNSET
    r"""An optional identifier for the document. A common value might be an id in an external system or the URL where the source file may be found."""

    partition: Optional[str] = None
    r"""An optional partition identifier. Documents can be scoped to a partition. Partitions must be lowercase alphanumeric and may only include the special characters `_` and `-`.  A partition is created any time a document is created or moved to a new partition."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["name", "metadata", "external_id", "partition"]
        nullable_fields = ["external_id"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
