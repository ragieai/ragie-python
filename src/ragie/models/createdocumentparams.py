"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
import io
import pydantic
from ragie.types import BaseModel
from ragie.utils import FieldMetadata, MultipartFormMetadata
from typing import Dict, IO, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class CreateDocumentParamsMode(str, Enum):
    r"""Partition strategy for the document. Options are `'hi_res'` or `'fast'`. When set to `'hi_res'`, images and tables will be extracted from the document. `'fast'` will only extract text. `'fast'` may be up to 20x faster than `'hi_res'`. `hi_res` is only applicable for Word documents, PDFs, Images, and PowerPoints. Images will always be processed in `hi_res`. If `hi_res` is set for an unsupported document type, it will be processed and billed in `fast` mode."""

    HI_RES = "hi_res"
    FAST = "fast"


MetadataTypedDict = TypeAliasType(
    "MetadataTypedDict", Union[str, float, bool, List[str]]
)


Metadata = TypeAliasType("Metadata", Union[str, float, bool, List[str]])


class FileTypedDict(TypedDict):
    file_name: str
    content: Union[bytes, IO[bytes], io.BufferedReader]
    content_type: NotRequired[str]


class File(BaseModel):
    file_name: Annotated[
        str, pydantic.Field(alias="fileName"), FieldMetadata(multipart=True)
    ]

    content: Annotated[
        Union[bytes, IO[bytes], io.BufferedReader],
        pydantic.Field(alias=""),
        FieldMetadata(multipart=MultipartFormMetadata(content=True)),
    ]

    content_type: Annotated[
        Optional[str],
        pydantic.Field(alias="Content-Type"),
        FieldMetadata(multipart=True),
    ] = None


class CreateDocumentParamsTypedDict(TypedDict):
    file: FileTypedDict
    r"""The binary file to upload, extract, and index for retrieval. The following file types are supported: Plain Text: `.eml` `.html` `.json` `.md` `.msg` `.rst` `.rtf` `.txt` `.xml`
    Images: `.png` `.webp` `.jpg` `.jpeg` `.tiff` `.bmp` `.heic`
    Documents: `.csv` `.doc` `.docx` `.epub` `.epub+zip` `.odt` `.pdf` `.ppt` `.pptx` `.tsv` `.xlsx` `.xls`.
    """
    mode: NotRequired[CreateDocumentParamsMode]
    r"""Partition strategy for the document. Options are `'hi_res'` or `'fast'`. When set to `'hi_res'`, images and tables will be extracted from the document. `'fast'` will only extract text. `'fast'` may be up to 20x faster than `'hi_res'`. `hi_res` is only applicable for Word documents, PDFs, Images, and PowerPoints. Images will always be processed in `hi_res`. If `hi_res` is set for an unsupported document type, it will be processed and billed in `fast` mode."""
    metadata: NotRequired[Dict[str, MetadataTypedDict]]
    r"""Metadata for the document. Keys must be strings. Values may be strings, numbers, booleans, or lists of strings. Numbers may be integers or floating point and will be converted to 64 bit floating point. 1000 total values are allowed. Each item in an array counts towards the total. The following keys are reserved for internal use: `document_id`, `document_type`, `document_source`, `document_name`, `document_uploaded_at`."""
    external_id: NotRequired[str]
    r"""An optional identifier for the document. A common value might be an id in an external system or the URL where the source file may be found."""
    name: NotRequired[str]
    r"""An optional name for the document. If set, the document will have this name. Otherwise it will default to the file's name."""
    partition: NotRequired[str]
    r"""An optional partition identifier. Documents can be scoped to a partition. Partitions must be lowercase alphanumeric and may only include the special characters `_` and `-`.  A partition is created any time a document is created."""


class CreateDocumentParams(BaseModel):
    file: Annotated[File, FieldMetadata(multipart=MultipartFormMetadata(file=True))]
    r"""The binary file to upload, extract, and index for retrieval. The following file types are supported: Plain Text: `.eml` `.html` `.json` `.md` `.msg` `.rst` `.rtf` `.txt` `.xml`
    Images: `.png` `.webp` `.jpg` `.jpeg` `.tiff` `.bmp` `.heic`
    Documents: `.csv` `.doc` `.docx` `.epub` `.epub+zip` `.odt` `.pdf` `.ppt` `.pptx` `.tsv` `.xlsx` `.xls`.
    """

    mode: Annotated[
        Optional[CreateDocumentParamsMode], FieldMetadata(multipart=True)
    ] = CreateDocumentParamsMode.FAST
    r"""Partition strategy for the document. Options are `'hi_res'` or `'fast'`. When set to `'hi_res'`, images and tables will be extracted from the document. `'fast'` will only extract text. `'fast'` may be up to 20x faster than `'hi_res'`. `hi_res` is only applicable for Word documents, PDFs, Images, and PowerPoints. Images will always be processed in `hi_res`. If `hi_res` is set for an unsupported document type, it will be processed and billed in `fast` mode."""

    metadata: Annotated[
        Optional[Dict[str, Metadata]],
        FieldMetadata(multipart=MultipartFormMetadata(json=True)),
    ] = None
    r"""Metadata for the document. Keys must be strings. Values may be strings, numbers, booleans, or lists of strings. Numbers may be integers or floating point and will be converted to 64 bit floating point. 1000 total values are allowed. Each item in an array counts towards the total. The following keys are reserved for internal use: `document_id`, `document_type`, `document_source`, `document_name`, `document_uploaded_at`."""

    external_id: Annotated[Optional[str], FieldMetadata(multipart=True)] = None
    r"""An optional identifier for the document. A common value might be an id in an external system or the URL where the source file may be found."""

    name: Annotated[Optional[str], FieldMetadata(multipart=True)] = None
    r"""An optional name for the document. If set, the document will have this name. Otherwise it will default to the file's name."""

    partition: Annotated[Optional[str], FieldMetadata(multipart=True)] = None
    r"""An optional partition identifier. Documents can be scoped to a partition. Partitions must be lowercase alphanumeric and may only include the special characters `_` and `-`.  A partition is created any time a document is created."""
