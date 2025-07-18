"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from ragie.types import BaseModel
from typing_extensions import TypedDict


class SlackDataTypedDict(TypedDict):
    channel_id: str
    channel_name: str


class SlackData(BaseModel):
    channel_id: str

    channel_name: str
