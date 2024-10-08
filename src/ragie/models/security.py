"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ragie.types import BaseModel
from ragie.utils import FieldMetadata, SecurityMetadata
from typing_extensions import Annotated, TypedDict


class SecurityTypedDict(TypedDict):
    auth: str


class Security(BaseModel):
    auth: Annotated[
        str,
        FieldMetadata(
            security=SecurityMetadata(
                scheme=True,
                scheme_type="http",
                sub_type="bearer",
                field_name="Authorization",
            )
        ),
    ]
