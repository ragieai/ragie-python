"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from ragie.types import BaseModel
from typing import Any, Dict
from typing_extensions import TypedDict


class EntityTypedDict(TypedDict):
    id: str
    created_at: datetime
    updated_at: datetime
    instruction_id: str
    r"""The ID of the instruction which generated the entity."""
    document_id: str
    r"""The ID of the document which the entity was produced from."""
    data: Dict[str, Any]


class Entity(BaseModel):
    id: str

    created_at: datetime

    updated_at: datetime

    instruction_id: str
    r"""The ID of the instruction which generated the entity."""

    document_id: str
    r"""The ID of the document which the entity was produced from."""

    data: Dict[str, Any]
