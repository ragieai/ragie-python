"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ragie.types import BaseModel
from ragie.utils import FieldMetadata, PathParamMetadata
from typing_extensions import Annotated, TypedDict


class SyncConnectionRequestTypedDict(TypedDict):
    connection_id: str


class SyncConnectionRequest(BaseModel):
    connection_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
