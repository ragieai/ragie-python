"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from pydantic import model_serializer
from ragie.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from typing import Dict, List, Union
from typing_extensions import NotRequired, TypeAliasType, TypedDict


DocumentGetMetadataTypedDict = TypeAliasType(
    "DocumentGetMetadataTypedDict", Union[str, int, bool, List[str]]
)


DocumentGetMetadata = TypeAliasType(
    "DocumentGetMetadata", Union[str, int, bool, List[str]]
)


class DocumentGetTypedDict(TypedDict):
    id: str
    created_at: datetime
    updated_at: datetime
    status: str
    name: str
    metadata: Dict[str, DocumentGetMetadataTypedDict]
    partition: str
    errors: List[str]
    chunk_count: NotRequired[Nullable[int]]
    external_id: NotRequired[Nullable[str]]
    page_count: NotRequired[Nullable[float]]


class DocumentGet(BaseModel):
    id: str

    created_at: datetime

    updated_at: datetime

    status: str

    name: str

    metadata: Dict[str, DocumentGetMetadata]

    partition: str

    errors: List[str]

    chunk_count: OptionalNullable[int] = UNSET

    external_id: OptionalNullable[str] = UNSET

    page_count: OptionalNullable[float] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["chunk_count", "external_id", "page_count"]
        nullable_fields = ["chunk_count", "external_id", "page_count"]
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
