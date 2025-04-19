"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .connectorsourcetypeinfo import (
    ConnectorSourceTypeInfo,
    ConnectorSourceTypeInfoTypedDict,
)
from ragie.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class ListConnectorSourceTypeInfoTypedDict(TypedDict):
    connectors: List[ConnectorSourceTypeInfoTypedDict]


class ListConnectorSourceTypeInfo(BaseModel):
    connectors: List[ConnectorSourceTypeInfo]
