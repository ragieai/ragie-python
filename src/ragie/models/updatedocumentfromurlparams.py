"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from ragie.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class UpdateDocumentFromURLParamsMode(str, Enum):
    r"""Partition strategy for the document. Options are `'hi_res'` or `'fast'`. Only applicable for rich documents such as word documents and PDFs. When set to `'hi_res'`, images and tables will be extracted from the document. `'fast'` will only extract text. `'fast'` may be up to 20x faster than `'hi_res'`."""

    HI_RES = "hi_res"
    FAST = "fast"


class UpdateDocumentFromURLParamsTypedDict(TypedDict):
    url: str
    r"""Url of the file to download. Must be publicly accessible and HTTP or HTTPS scheme."""
    mode: NotRequired[UpdateDocumentFromURLParamsMode]
    r"""Partition strategy for the document. Options are `'hi_res'` or `'fast'`. Only applicable for rich documents such as word documents and PDFs. When set to `'hi_res'`, images and tables will be extracted from the document. `'fast'` will only extract text. `'fast'` may be up to 20x faster than `'hi_res'`."""


class UpdateDocumentFromURLParams(BaseModel):
    url: str
    r"""Url of the file to download. Must be publicly accessible and HTTP or HTTPS scheme."""

    mode: Optional[UpdateDocumentFromURLParamsMode] = (
        UpdateDocumentFromURLParamsMode.FAST
    )
    r"""Partition strategy for the document. Options are `'hi_res'` or `'fast'`. Only applicable for rich documents such as word documents and PDFs. When set to `'hi_res'`, images and tables will be extracted from the document. `'fast'` will only extract text. `'fast'` may be up to 20x faster than `'hi_res'`."""