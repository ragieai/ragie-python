"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ragie.types import BaseModel
from ragie.utils import FieldMetadata, PathParamMetadata
from typing_extensions import Annotated, TypedDict


class DeleteInstructionRequestTypedDict(TypedDict):
    instruction_id: str
    r"""The ID of the instruction."""


class DeleteInstructionRequest(BaseModel):
    instruction_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the instruction."""
