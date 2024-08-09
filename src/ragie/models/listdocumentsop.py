"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .documentlist import DocumentList, DocumentListTypedDict
import pydantic
from pydantic import model_serializer
from ragie.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from ragie.utils import FieldMetadata, QueryParamMetadata
from typing import Callable, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ListDocumentsRequestTypedDict(TypedDict):
    cursor: NotRequired[Nullable[str]]
    r"""An opaque cursor for pagination"""
    page_size: NotRequired[int]
    r"""The number of items per page (must be greater than 0 and less than or equal to 100)"""
    filter_: NotRequired[Nullable[str]]
    r"""The metadata search filter on documents. Returns only documents which match the filter. The following filter operators are supported: $eq - Equal to (number, string, boolean), $ne - Not equal to (number, string, boolean), $gt - Greater than (number), $gte - Greater than or equal to (number), $lt - Less than (number), $lte - Less than or equal to (number), $in - In array (string or number), $nin - Not in array (string or number). The operators can be combined with AND and OR. Read [Metadata & Filters guide](https://docs.ragie.ai/docs/metadata-filters) for more details and examples."""
    

class ListDocumentsRequest(BaseModel):
    cursor: Annotated[OptionalNullable[str], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = UNSET
    r"""An opaque cursor for pagination"""
    page_size: Annotated[Optional[int], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 10
    r"""The number of items per page (must be greater than 0 and less than or equal to 100)"""
    filter_: Annotated[OptionalNullable[str], pydantic.Field(alias="filter"), FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = UNSET
    r"""The metadata search filter on documents. Returns only documents which match the filter. The following filter operators are supported: $eq - Equal to (number, string, boolean), $ne - Not equal to (number, string, boolean), $gt - Greater than (number), $gte - Greater than or equal to (number), $lt - Less than (number), $lte - Less than or equal to (number), $in - In array (string or number), $nin - Not in array (string or number). The operators can be combined with AND and OR. Read [Metadata & Filters guide](https://docs.ragie.ai/docs/metadata-filters) for more details and examples."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["cursor", "page_size", "filter"]
        nullable_fields = ["cursor", "filter"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
        

class ListDocumentsResponseTypedDict(TypedDict):
    result: DocumentListTypedDict
    

class ListDocumentsResponse(BaseModel):
    next: Callable[[], Optional[ListDocumentsResponse]]
    
    result: DocumentList
    