"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ragie.types import BaseModel
from typing_extensions import TypedDict


class SetConnectionEnabledPayloadTypedDict(TypedDict):
    enabled: bool


class SetConnectionEnabledPayload(BaseModel):
    enabled: bool
