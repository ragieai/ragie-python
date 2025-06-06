"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .partitionlimits import PartitionLimits, PartitionLimitsTypedDict
from .partitionstats import PartitionStats, PartitionStatsTypedDict
from datetime import datetime
from pydantic import model_serializer
from ragie.types import BaseModel, Nullable, UNSET_SENTINEL
from typing_extensions import TypedDict


class PartitionDetailTypedDict(TypedDict):
    name: str
    is_default: bool
    limit_exceeded_at: Nullable[datetime]
    limits: PartitionLimitsTypedDict
    stats: PartitionStatsTypedDict


class PartitionDetail(BaseModel):
    name: str

    is_default: bool

    limit_exceeded_at: Nullable[datetime]

    limits: PartitionLimits

    stats: PartitionStats

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["limit_exceeded_at"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
