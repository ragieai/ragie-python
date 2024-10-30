"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .entityextractedwebhookpayload import (
    EntityExtractedWebhookPayload,
    EntityExtractedWebhookPayloadTypedDict,
)
from enum import Enum
import pydantic
from pydantic.functional_validators import AfterValidator
from ragie.types import BaseModel
from ragie.utils import validate_const
from typing_extensions import Annotated, TypedDict


class EntityExtractedWebhookType(str, Enum):
    ENTITY_EXTRACTED = "entity_extracted"


class EntityExtractedWebhookTypedDict(TypedDict):
    nonce: str
    payload: EntityExtractedWebhookPayloadTypedDict
    type: EntityExtractedWebhookType


class EntityExtractedWebhook(BaseModel):
    nonce: str

    payload: EntityExtractedWebhookPayload

    TYPE: Annotated[
        Annotated[
            EntityExtractedWebhookType,
            AfterValidator(validate_const(EntityExtractedWebhookType.ENTITY_EXTRACTED)),
        ],
        pydantic.Field(alias="type"),
    ] = EntityExtractedWebhookType.ENTITY_EXTRACTED
