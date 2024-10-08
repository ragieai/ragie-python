"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
import pydantic
from ragie.types import BaseModel
from typing import Any, Dict, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateInstructionParamsScope(str, Enum):
    r"""The scope of the instruction. Determines whether the instruction is applied to the entire document or to each chunk of the document. Options are `'document'` or `'chunk'`. Generally `'document'` should be used when analyzing the full document is desired, such as when generating a summary or determining sentiment, and `'chunk'` should be used when a fine grained search over a document is desired."""

    DOCUMENT = "document"
    CHUNK = "chunk"


class CreateInstructionParamsFilterTypedDict(TypedDict):
    r"""An optional metadata filter that is matched against document metadata during update and creation. The instruction will only be applied to documents with metadata matching the filter.  The following filter operators are supported: $eq - Equal to (number, string, boolean), $ne - Not equal to (number, string, boolean), $gt - Greater than (number), $gte - Greater than or equal to (number), $lt - Less than (number), $lte - Less than or equal to (number), $in - In array (string or number), $nin - Not in array (string or number). The operators can be combined with AND and OR. Read [Metadata & Filters guide](https://docs.ragie.ai/docs/metadata-filters) for more details and examples."""


class CreateInstructionParamsFilter(BaseModel):
    r"""An optional metadata filter that is matched against document metadata during update and creation. The instruction will only be applied to documents with metadata matching the filter.  The following filter operators are supported: $eq - Equal to (number, string, boolean), $ne - Not equal to (number, string, boolean), $gt - Greater than (number), $gte - Greater than or equal to (number), $lt - Less than (number), $lte - Less than or equal to (number), $in - In array (string or number), $nin - Not in array (string or number). The operators can be combined with AND and OR. Read [Metadata & Filters guide](https://docs.ragie.ai/docs/metadata-filters) for more details and examples."""


class CreateInstructionParamsTypedDict(TypedDict):
    name: str
    r"""The name of the instruction. Must be unique."""
    prompt: str
    r"""A natural language instruction which will be applied to documents as they are created and updated. The results of the `instruction_prompt` will be stored as an `entity` in the schema defined by the `entity_schema` parameter."""
    entity_schema: Dict[str, Any]
    r"""The JSON schema definition of the entity generated by an instruction. The schema must define an `object` at its root. If the instruction is expected to generate multiple items, the root object should have a key which defines an array of the expected items. An instruction which generates multiple emails may be expressed as `{\"type\": \"object\", \"properties\": {\"emails\": { \"type\": \"array\", \"items\": { \"type\": \"string\"}}}}`. Simple values may be expressed as an object with a single key. For example, a summary instruction may generate a single string value. The schema might be `{\"type\": \"object\", \"properties\": { \"summary\": { \"type\": \"string\"}}}`."""
    active: NotRequired[bool]
    r"""Whether the instruction is active. Active instructions are applied to documents when they're created or when their file is updated."""
    scope: NotRequired[CreateInstructionParamsScope]
    r"""The scope of the instruction. Determines whether the instruction is applied to the entire document or to each chunk of the document. Options are `'document'` or `'chunk'`. Generally `'document'` should be used when analyzing the full document is desired, such as when generating a summary or determining sentiment, and `'chunk'` should be used when a fine grained search over a document is desired."""
    filter_: NotRequired[CreateInstructionParamsFilterTypedDict]
    r"""An optional metadata filter that is matched against document metadata during update and creation. The instruction will only be applied to documents with metadata matching the filter.  The following filter operators are supported: $eq - Equal to (number, string, boolean), $ne - Not equal to (number, string, boolean), $gt - Greater than (number), $gte - Greater than or equal to (number), $lt - Less than (number), $lte - Less than or equal to (number), $in - In array (string or number), $nin - Not in array (string or number). The operators can be combined with AND and OR. Read [Metadata & Filters guide](https://docs.ragie.ai/docs/metadata-filters) for more details and examples."""
    partition: NotRequired[str]
    r"""An optional partition identifier. Instructions can be scoped to a partition. An instruction that defines a partition will only be executed for documents in that partition."""


class CreateInstructionParams(BaseModel):
    name: str
    r"""The name of the instruction. Must be unique."""

    prompt: str
    r"""A natural language instruction which will be applied to documents as they are created and updated. The results of the `instruction_prompt` will be stored as an `entity` in the schema defined by the `entity_schema` parameter."""

    entity_schema: Dict[str, Any]
    r"""The JSON schema definition of the entity generated by an instruction. The schema must define an `object` at its root. If the instruction is expected to generate multiple items, the root object should have a key which defines an array of the expected items. An instruction which generates multiple emails may be expressed as `{\"type\": \"object\", \"properties\": {\"emails\": { \"type\": \"array\", \"items\": { \"type\": \"string\"}}}}`. Simple values may be expressed as an object with a single key. For example, a summary instruction may generate a single string value. The schema might be `{\"type\": \"object\", \"properties\": { \"summary\": { \"type\": \"string\"}}}`."""

    active: Optional[bool] = True
    r"""Whether the instruction is active. Active instructions are applied to documents when they're created or when their file is updated."""

    scope: Optional[CreateInstructionParamsScope] = CreateInstructionParamsScope.CHUNK
    r"""The scope of the instruction. Determines whether the instruction is applied to the entire document or to each chunk of the document. Options are `'document'` or `'chunk'`. Generally `'document'` should be used when analyzing the full document is desired, such as when generating a summary or determining sentiment, and `'chunk'` should be used when a fine grained search over a document is desired."""

    filter_: Annotated[
        Optional[CreateInstructionParamsFilter], pydantic.Field(alias="filter")
    ] = None
    r"""An optional metadata filter that is matched against document metadata during update and creation. The instruction will only be applied to documents with metadata matching the filter.  The following filter operators are supported: $eq - Equal to (number, string, boolean), $ne - Not equal to (number, string, boolean), $gt - Greater than (number), $gte - Greater than or equal to (number), $lt - Less than (number), $lte - Less than or equal to (number), $in - In array (string or number), $nin - Not in array (string or number). The operators can be combined with AND and OR. Read [Metadata & Filters guide](https://docs.ragie.ai/docs/metadata-filters) for more details and examples."""

    partition: Optional[str] = None
    r"""An optional partition identifier. Instructions can be scoped to a partition. An instruction that defines a partition will only be executed for documents in that partition."""
