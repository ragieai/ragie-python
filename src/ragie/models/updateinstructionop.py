"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .updateinstructionparams import UpdateInstructionParams, UpdateInstructionParamsTypedDict
from ragie.types import BaseModel
from ragie.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import TypedDict
from typing_extensions import Annotated


class UpdateInstructionRequestTypedDict(TypedDict):
    instruction_id: str
    r"""The ID of the instruction."""
    update_instruction_params: UpdateInstructionParamsTypedDict
    

class UpdateInstructionRequest(BaseModel):
    instruction_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The ID of the instruction."""
    update_instruction_params: Annotated[UpdateInstructionParams, FieldMetadata(request=RequestMetadata(media_type="application/json"))]
    