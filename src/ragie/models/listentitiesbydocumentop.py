"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .entitylist import EntityList, EntityListTypedDict
from pydantic import model_serializer
from ragie.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from ragie.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    QueryParamMetadata,
)
from typing import Callable, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ListEntitiesByDocumentRequestTypedDict(TypedDict):
    document_id: str
    r"""The id of the document."""
    cursor: NotRequired[Nullable[str]]
    r"""An opaque cursor for pagination"""
    page_size: NotRequired[int]
    r"""The number of items per page (must be greater than 0 and less than or equal to 100)"""
    partition: NotRequired[Nullable[str]]
    r"""An optional partition to scope the request to. If omitted, accounts created after 1/9/2025 will have the request scoped to the default partition, while older accounts will have the request scoped to all partitions. Older accounts may opt in to strict partition scoping by contacting support@ragie.ai. Older accounts using the partitions feature are strongly recommended to scope the request to a partition."""


class ListEntitiesByDocumentRequest(BaseModel):
    document_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The id of the document."""

    cursor: Annotated[
        OptionalNullable[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""An opaque cursor for pagination"""

    page_size: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 10
    r"""The number of items per page (must be greater than 0 and less than or equal to 100)"""

    partition: Annotated[
        OptionalNullable[str],
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = UNSET
    r"""An optional partition to scope the request to. If omitted, accounts created after 1/9/2025 will have the request scoped to the default partition, while older accounts will have the request scoped to all partitions. Older accounts may opt in to strict partition scoping by contacting support@ragie.ai. Older accounts using the partitions feature are strongly recommended to scope the request to a partition."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["cursor", "page_size", "partition"]
        nullable_fields = ["cursor", "partition"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
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


class ListEntitiesByDocumentResponseTypedDict(TypedDict):
    result: EntityListTypedDict


class ListEntitiesByDocumentResponse(BaseModel):
    next: Callable[[], Optional[ListEntitiesByDocumentResponse]]

    result: EntityList
