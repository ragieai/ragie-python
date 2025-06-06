"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .setconnectionenabledpayload import (
    SetConnectionEnabledPayload,
    SetConnectionEnabledPayloadTypedDict,
)
from ragie.types import BaseModel
from ragie.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing_extensions import Annotated, TypedDict


class SetConnectionEnabledConnectionsConnectionIDEnabledPutRequestTypedDict(TypedDict):
    connection_id: str
    set_connection_enabled_payload: SetConnectionEnabledPayloadTypedDict


class SetConnectionEnabledConnectionsConnectionIDEnabledPutRequest(BaseModel):
    connection_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    set_connection_enabled_payload: Annotated[
        SetConnectionEnabledPayload,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
