"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .documentdeletewebhookpayload import (
    DocumentDeleteWebhookPayload,
    DocumentDeleteWebhookPayloadTypedDict,
)
from enum import Enum
import pydantic
from pydantic.functional_validators import AfterValidator
from ragie.types import BaseModel
from ragie.utils import validate_const
from typing_extensions import Annotated, TypedDict


class DocumentDeleteWebhookType(str, Enum):
    DOCUMENT_DELETED = "document_deleted"


class DocumentDeleteWebhookTypedDict(TypedDict):
    nonce: str
    payload: DocumentDeleteWebhookPayloadTypedDict
    type: DocumentDeleteWebhookType


class DocumentDeleteWebhook(BaseModel):
    nonce: str

    payload: DocumentDeleteWebhookPayload

    TYPE: Annotated[
        Annotated[
            DocumentDeleteWebhookType,
            AfterValidator(validate_const(DocumentDeleteWebhookType.DOCUMENT_DELETED)),
        ],
        pydantic.Field(alias="type"),
    ] = DocumentDeleteWebhookType.DOCUMENT_DELETED