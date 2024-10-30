"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .documentupdatewebhookpayload import (
    DocumentUpdateWebhookPayload,
    DocumentUpdateWebhookPayloadTypedDict,
)
from enum import Enum
import pydantic
from pydantic.functional_validators import AfterValidator
from ragie.types import BaseModel
from ragie.utils import validate_const
from typing_extensions import Annotated, TypedDict


class Type(str, Enum):
    DOCUMENT_STATUS_UPDATED = "document_status_updated"


class DocumentUpdateWebhookTypedDict(TypedDict):
    nonce: str
    payload: DocumentUpdateWebhookPayloadTypedDict
    type: Type


class DocumentUpdateWebhook(BaseModel):
    nonce: str

    payload: DocumentUpdateWebhookPayload

    TYPE: Annotated[
        Annotated[Type, AfterValidator(validate_const(Type.DOCUMENT_STATUS_UPDATED))],
        pydantic.Field(alias="type"),
    ] = Type.DOCUMENT_STATUS_UPDATED
