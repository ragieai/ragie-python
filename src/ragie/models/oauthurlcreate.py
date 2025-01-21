"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .connectorsource import ConnectorSource
from enum import Enum
from pydantic import model_serializer
from ragie.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from typing import Dict, List, Optional, Union
from typing_extensions import NotRequired, TypeAliasType, TypedDict


OAuthURLCreateMetadataTypedDict = TypeAliasType(
    "OAuthURLCreateMetadataTypedDict", Union[str, int, bool, List[str]]
)


OAuthURLCreateMetadata = TypeAliasType(
    "OAuthURLCreateMetadata", Union[str, int, bool, List[str]]
)


class Mode(str, Enum):
    HI_RES = "hi_res"
    FAST = "fast"


class Theme(str, Enum):
    LIGHT = "light"
    DARK = "dark"
    SYSTEM = "system"


class OAuthURLCreateTypedDict(TypedDict):
    redirect_uri: str
    source_type: NotRequired[ConnectorSource]
    metadata: NotRequired[Dict[str, OAuthURLCreateMetadataTypedDict]]
    r"""Metadata for the document. Keys must be strings. Values may be strings, numbers, booleans, or lists of strings. Numbers may be integers or floating point and will be converted to 64 bit floating point. 1000 total values are allowed. Each item in an array counts towards the total. The following keys are reserved for internal use: `document_id`, `document_type`, `document_source`, `document_name`, `document_uploaded_at`."""
    mode: NotRequired[Nullable[Mode]]
    partition: NotRequired[Nullable[str]]
    theme: NotRequired[Nullable[Theme]]
    r"""Sets the theme of the Ragie Web UI when the user lands there. Can be light, dark, or system to use whatever the system value is. If omitted, system is used."""


class OAuthURLCreate(BaseModel):
    redirect_uri: str

    source_type: Optional[ConnectorSource] = None

    metadata: Optional[Dict[str, OAuthURLCreateMetadata]] = None
    r"""Metadata for the document. Keys must be strings. Values may be strings, numbers, booleans, or lists of strings. Numbers may be integers or floating point and will be converted to 64 bit floating point. 1000 total values are allowed. Each item in an array counts towards the total. The following keys are reserved for internal use: `document_id`, `document_type`, `document_source`, `document_name`, `document_uploaded_at`."""

    mode: OptionalNullable[Mode] = UNSET

    partition: OptionalNullable[str] = UNSET

    theme: OptionalNullable[Theme] = UNSET
    r"""Sets the theme of the Ragie Web UI when the user lands there. Can be light, dark, or system to use whatever the system value is. If omitted, system is used."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["source_type", "metadata", "mode", "partition", "theme"]
        nullable_fields = ["mode", "partition", "theme"]
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
