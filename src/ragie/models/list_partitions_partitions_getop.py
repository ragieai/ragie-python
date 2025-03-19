"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .partitionlist import PartitionList, PartitionListTypedDict
from pydantic import model_serializer
from ragie.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from ragie.utils import FieldMetadata, QueryParamMetadata
from typing import Callable, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ListPartitionsPartitionsGetRequestTypedDict(TypedDict):
    cursor: NotRequired[Nullable[str]]
    r"""An opaque cursor for pagination"""
    page_size: NotRequired[int]
    r"""The number of items per page (must be greater than 0 and less than or equal to 100)"""


class ListPartitionsPartitionsGetRequest(BaseModel):
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

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["cursor", "page_size"]
        nullable_fields = ["cursor"]
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


class ListPartitionsPartitionsGetResponseTypedDict(TypedDict):
    result: PartitionListTypedDict


class ListPartitionsPartitionsGetResponse(BaseModel):
    next: Callable[[], Optional[ListPartitionsPartitionsGetResponse]]

    result: PartitionList
