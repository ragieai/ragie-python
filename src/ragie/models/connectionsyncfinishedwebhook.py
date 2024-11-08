"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .connectionsyncfinishedwebhookpayload import (
    ConnectionSyncFinishedWebhookPayload,
    ConnectionSyncFinishedWebhookPayloadTypedDict,
)
from enum import Enum
import pydantic
from pydantic.functional_validators import AfterValidator
from ragie.types import BaseModel
from ragie.utils import validate_const
from typing_extensions import Annotated, TypedDict


class ConnectionSyncFinishedWebhookType(str, Enum):
    CONNECTION_SYNC_FINISHED = "connection_sync_finished"


class ConnectionSyncFinishedWebhookTypedDict(TypedDict):
    nonce: str
    payload: ConnectionSyncFinishedWebhookPayloadTypedDict
    type: ConnectionSyncFinishedWebhookType


class ConnectionSyncFinishedWebhook(BaseModel):
    nonce: str

    payload: ConnectionSyncFinishedWebhookPayload

    TYPE: Annotated[
        Annotated[
            ConnectionSyncFinishedWebhookType,
            AfterValidator(
                validate_const(
                    ConnectionSyncFinishedWebhookType.CONNECTION_SYNC_FINISHED
                )
            ),
        ],
        pydantic.Field(alias="type"),
    ] = ConnectionSyncFinishedWebhookType.CONNECTION_SYNC_FINISHED
