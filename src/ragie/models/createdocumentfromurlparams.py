"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from pydantic import model_serializer
from ragie.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from typing import Dict, List, Optional, Union
from typing_extensions import NotRequired, TypeAliasType, TypedDict


CreateDocumentFromURLParamsMetadataTypedDict = TypeAliasType(
    "CreateDocumentFromURLParamsMetadataTypedDict", Union[str, int, bool, List[str]]
)


CreateDocumentFromURLParamsMetadata = TypeAliasType(
    "CreateDocumentFromURLParamsMetadata", Union[str, int, bool, List[str]]
)


class CreateDocumentFromURLParamsMode(str, Enum):
    r"""Partition strategy for the document. Options are `'hi_res'` or `'fast'`. When set to `'hi_res'`, images and tables will be extracted from the document. `'fast'` will only extract text. `'fast'` may be up to 20x faster than `'hi_res'`. `hi_res` is only applicable for Word documents, PDFs, Images, and PowerPoints. Images will always be processed in `hi_res`. If `hi_res` is set for an unsupported document type, it will be processed and billed in `fast` mode."""

    HI_RES = "hi_res"
    FAST = "fast"


class CreateDocumentFromURLParamsTypedDict(TypedDict):
    url: str
    r"""Url of the file to download. Must be publicly accessible and HTTP or HTTPS scheme."""
    name: NotRequired[str]
    metadata: NotRequired[Dict[str, CreateDocumentFromURLParamsMetadataTypedDict]]
    r"""Metadata for the document. Keys must be strings. Values may be strings, numbers, booleans, or lists of strings. Numbers may be integers or floating point and will be converted to 64 bit floating point. 1000 total values are allowed. Each item in an array counts towards the total. The following keys are reserved for internal use: `document_id`, `document_type`, `document_source`, `document_name`, `document_uploaded_at`, `start_time`, `end_time`."""
    mode: NotRequired[CreateDocumentFromURLParamsMode]
    r"""Partition strategy for the document. Options are `'hi_res'` or `'fast'`. When set to `'hi_res'`, images and tables will be extracted from the document. `'fast'` will only extract text. `'fast'` may be up to 20x faster than `'hi_res'`. `hi_res` is only applicable for Word documents, PDFs, Images, and PowerPoints. Images will always be processed in `hi_res`. If `hi_res` is set for an unsupported document type, it will be processed and billed in `fast` mode."""
    external_id: NotRequired[Nullable[str]]
    r"""An optional identifier for the document. A common value might be an id in an external system or the URL where the source file may be found."""
    partition: NotRequired[str]
    r"""An optional partition identifier. Documents can be scoped to a partition. Partitions must be lowercase alphanumeric and may only include the special characters `_` and `-`.  A partition is created any time a document is created."""


class CreateDocumentFromURLParams(BaseModel):
    url: str
    r"""Url of the file to download. Must be publicly accessible and HTTP or HTTPS scheme."""

    name: Optional[str] = None

    metadata: Optional[Dict[str, CreateDocumentFromURLParamsMetadata]] = None
    r"""Metadata for the document. Keys must be strings. Values may be strings, numbers, booleans, or lists of strings. Numbers may be integers or floating point and will be converted to 64 bit floating point. 1000 total values are allowed. Each item in an array counts towards the total. The following keys are reserved for internal use: `document_id`, `document_type`, `document_source`, `document_name`, `document_uploaded_at`, `start_time`, `end_time`."""

    mode: Optional[CreateDocumentFromURLParamsMode] = (
        CreateDocumentFromURLParamsMode.FAST
    )
    r"""Partition strategy for the document. Options are `'hi_res'` or `'fast'`. When set to `'hi_res'`, images and tables will be extracted from the document. `'fast'` will only extract text. `'fast'` may be up to 20x faster than `'hi_res'`. `hi_res` is only applicable for Word documents, PDFs, Images, and PowerPoints. Images will always be processed in `hi_res`. If `hi_res` is set for an unsupported document type, it will be processed and billed in `fast` mode."""

    external_id: OptionalNullable[str] = UNSET
    r"""An optional identifier for the document. A common value might be an id in an external system or the URL where the source file may be found."""

    partition: Optional[str] = None
    r"""An optional partition identifier. Documents can be scoped to a partition. Partitions must be lowercase alphanumeric and may only include the special characters `_` and `-`.  A partition is created any time a document is created."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["name", "metadata", "mode", "external_id", "partition"]
        nullable_fields = ["external_id"]
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
