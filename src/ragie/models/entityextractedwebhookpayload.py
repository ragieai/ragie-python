"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from pydantic import model_serializer
from ragie.types import BaseModel, Nullable, UNSET_SENTINEL
from typing_extensions import TypedDict


class EntityExtractedWebhookPayloadDocumentMetadataTypedDict(TypedDict):
    pass


class EntityExtractedWebhookPayloadDocumentMetadata(BaseModel):
    pass


class EntityExtractedWebhookPayloadDataTypedDict(TypedDict):
    pass


class EntityExtractedWebhookPayloadData(BaseModel):
    pass


class EntityExtractedWebhookPayloadTypedDict(TypedDict):
    entity_id: str
    document_id: str
    instruction_id: str
    document_metadata: EntityExtractedWebhookPayloadDocumentMetadataTypedDict
    document_external_id: Nullable[str]
    partition: str
    sync_id: Nullable[str]
    data: EntityExtractedWebhookPayloadDataTypedDict


class EntityExtractedWebhookPayload(BaseModel):
    entity_id: str

    document_id: str

    instruction_id: str

    document_metadata: EntityExtractedWebhookPayloadDocumentMetadata

    document_external_id: Nullable[str]

    partition: str

    sync_id: Nullable[str]

    data: EntityExtractedWebhookPayloadData

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["document_external_id", "sync_id"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
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
