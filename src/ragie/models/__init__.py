"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .connection import (
    Connection,
    ConnectionMetadataMetadata,
    ConnectionMetadataMetadataTypedDict,
    ConnectionTypedDict,
)
from .connectionbase import (
    ConnectionBase,
    ConnectionBaseMetadata,
    ConnectionBaseMetadataTypedDict,
    ConnectionBaseTypedDict,
    PartitionStrategy,
)
from .connectionlist import ConnectionList, ConnectionListTypedDict
from .connectionstats import ConnectionStats, ConnectionStatsTypedDict
from .createdocumentfromurlparams import (
    CreateDocumentFromURLParams,
    CreateDocumentFromURLParamsMetadata,
    CreateDocumentFromURLParamsMetadataTypedDict,
    CreateDocumentFromURLParamsMode,
    CreateDocumentFromURLParamsTypedDict,
)
from .createdocumentparams import (
    CreateDocumentParams,
    CreateDocumentParamsMode,
    CreateDocumentParamsTypedDict,
    File,
    FileTypedDict,
    Metadata,
    MetadataTypedDict,
)
from .createdocumentrawparams import (
    CreateDocumentRawParams,
    CreateDocumentRawParamsMetadata,
    CreateDocumentRawParamsMetadataTypedDict,
    CreateDocumentRawParamsTypedDict,
    Data,
    DataTypedDict,
    Two,
    TwoTypedDict,
)
from .createinstructionparams import (
    CreateInstructionParams,
    CreateInstructionParamsFilter,
    CreateInstructionParamsFilterTypedDict,
    CreateInstructionParamsScope,
    CreateInstructionParamsTypedDict,
)
from .delete_connection_connections_connection_id_delete_postop import (
    DeleteConnectionConnectionsConnectionIDDeletePostRequest,
    DeleteConnectionConnectionsConnectionIDDeletePostRequestTypedDict,
)
from .deleteconnectionpayload import (
    DeleteConnectionPayload,
    DeleteConnectionPayloadTypedDict,
)
from .deletedocumentop import DeleteDocumentRequest, DeleteDocumentRequestTypedDict
from .document import (
    Document,
    DocumentMetadata,
    DocumentMetadataTypedDict,
    DocumentTypedDict,
)
from .documentdelete import DocumentDelete, DocumentDeleteTypedDict
from .documentfileupdate import DocumentFileUpdate, DocumentFileUpdateTypedDict
from .documentget import (
    DocumentGet,
    DocumentGetMetadata,
    DocumentGetMetadataTypedDict,
    DocumentGetTypedDict,
)
from .documentlist import DocumentList, DocumentListTypedDict
from .documentmetadataupdate import (
    DocumentMetadataUpdate,
    DocumentMetadataUpdateMetadata,
    DocumentMetadataUpdateMetadataTypedDict,
    DocumentMetadataUpdateTypedDict,
)
from .documentrawupdate import DocumentRawUpdate, DocumentRawUpdateTypedDict
from .documentsummary import DocumentSummary, DocumentSummaryTypedDict
from .entity import Entity, EntityTypedDict
from .entitylist import EntityList, EntityListTypedDict
from .errormessage import ErrorMessage, ErrorMessageData
from .get_connection_connections_connection_id_getop import (
    GetConnectionConnectionsConnectionIDGetRequest,
    GetConnectionConnectionsConnectionIDGetRequestTypedDict,
)
from .get_connection_stats_connections_connection_id_stats_getop import (
    GetConnectionStatsConnectionsConnectionIDStatsGetRequest,
    GetConnectionStatsConnectionsConnectionIDStatsGetRequestTypedDict,
)
from .getdocumentop import GetDocumentRequest, GetDocumentRequestTypedDict
from .getdocumentsummaryop import (
    GetDocumentSummaryRequest,
    GetDocumentSummaryRequestTypedDict,
)
from .httpvalidationerror import HTTPValidationError, HTTPValidationErrorData
from .instruction import (
    Filter,
    FilterTypedDict,
    Instruction,
    InstructionTypedDict,
    Scope,
)
from .list_connections_connections_getop import (
    ListConnectionsConnectionsGetRequest,
    ListConnectionsConnectionsGetRequestTypedDict,
    ListConnectionsConnectionsGetResponse,
    ListConnectionsConnectionsGetResponseTypedDict,
)
from .listdocumentsop import (
    ListDocumentsRequest,
    ListDocumentsRequestTypedDict,
    ListDocumentsResponse,
    ListDocumentsResponseTypedDict,
)
from .listentitiesbydocumentop import (
    ListEntitiesByDocumentRequest,
    ListEntitiesByDocumentRequestTypedDict,
    ListEntitiesByDocumentResponse,
    ListEntitiesByDocumentResponseTypedDict,
)
from .listentitiesbyinstructionop import (
    ListEntitiesByInstructionRequest,
    ListEntitiesByInstructionRequestTypedDict,
    ListEntitiesByInstructionResponse,
    ListEntitiesByInstructionResponseTypedDict,
)
from .oauthurlcreate import (
    Mode,
    OAuthURLCreate,
    OAuthURLCreateMetadata,
    OAuthURLCreateMetadataTypedDict,
    OAuthURLCreateTypedDict,
    Theme,
)
from .oauthurlresponse import OAuthURLResponse, OAuthURLResponseTypedDict
from .pagination import Pagination, PaginationTypedDict
from .patchdocumentmetadataop import (
    PatchDocumentMetadataRequest,
    PatchDocumentMetadataRequestTypedDict,
)
from .patchdocumentmetadataparams import (
    PatchDocumentMetadataParams,
    PatchDocumentMetadataParamsTypedDict,
)
from .retrieval import Retrieval, RetrievalTypedDict
from .retrieveparams import RetrieveParams, RetrieveParamsTypedDict
from .scoredchunk import ScoredChunk, ScoredChunkTypedDict
from .sdkerror import SDKError
from .security import Security, SecurityTypedDict
from .set_connection_enabled_connections_connection_id_enabled_putop import (
    SetConnectionEnabledConnectionsConnectionIDEnabledPutRequest,
    SetConnectionEnabledConnectionsConnectionIDEnabledPutRequestTypedDict,
)
from .setconnectionenabledpayload import (
    SetConnectionEnabledPayload,
    SetConnectionEnabledPayloadTypedDict,
)
from .update_connection_connections_connection_id_putop import (
    UpdateConnectionConnectionsConnectionIDPutRequest,
    UpdateConnectionConnectionsConnectionIDPutRequestTypedDict,
)
from .updatedocumentfileop import (
    UpdateDocumentFileRequest,
    UpdateDocumentFileRequestTypedDict,
)
from .updatedocumentfileparams import (
    UpdateDocumentFileParams,
    UpdateDocumentFileParamsFile,
    UpdateDocumentFileParamsFileTypedDict,
    UpdateDocumentFileParamsMode,
    UpdateDocumentFileParamsTypedDict,
)
from .updatedocumentrawop import (
    UpdateDocumentRawRequest,
    UpdateDocumentRawRequestTypedDict,
)
from .updatedocumentrawparams import (
    Data2,
    Data2TypedDict,
    UpdateDocumentRawParams,
    UpdateDocumentRawParamsData,
    UpdateDocumentRawParamsDataTypedDict,
    UpdateDocumentRawParamsTypedDict,
)
from .updateinstructionop import (
    UpdateInstructionRequest,
    UpdateInstructionRequestTypedDict,
)
from .updateinstructionparams import (
    UpdateInstructionParams,
    UpdateInstructionParamsTypedDict,
)
from .validationerror import (
    Loc,
    LocTypedDict,
    ValidationError,
    ValidationErrorTypedDict,
)

__all__ = [
    "Connection",
    "ConnectionBase",
    "ConnectionBaseMetadata",
    "ConnectionBaseMetadataTypedDict",
    "ConnectionBaseTypedDict",
    "ConnectionList",
    "ConnectionListTypedDict",
    "ConnectionMetadataMetadata",
    "ConnectionMetadataMetadataTypedDict",
    "ConnectionStats",
    "ConnectionStatsTypedDict",
    "ConnectionTypedDict",
    "CreateDocumentFromURLParams",
    "CreateDocumentFromURLParamsMetadata",
    "CreateDocumentFromURLParamsMetadataTypedDict",
    "CreateDocumentFromURLParamsMode",
    "CreateDocumentFromURLParamsTypedDict",
    "CreateDocumentParams",
    "CreateDocumentParamsMode",
    "CreateDocumentParamsTypedDict",
    "CreateDocumentRawParams",
    "CreateDocumentRawParamsMetadata",
    "CreateDocumentRawParamsMetadataTypedDict",
    "CreateDocumentRawParamsTypedDict",
    "CreateInstructionParams",
    "CreateInstructionParamsFilter",
    "CreateInstructionParamsFilterTypedDict",
    "CreateInstructionParamsScope",
    "CreateInstructionParamsTypedDict",
    "Data",
    "Data2",
    "Data2TypedDict",
    "DataTypedDict",
    "DeleteConnectionConnectionsConnectionIDDeletePostRequest",
    "DeleteConnectionConnectionsConnectionIDDeletePostRequestTypedDict",
    "DeleteConnectionPayload",
    "DeleteConnectionPayloadTypedDict",
    "DeleteDocumentRequest",
    "DeleteDocumentRequestTypedDict",
    "Document",
    "DocumentDelete",
    "DocumentDeleteTypedDict",
    "DocumentFileUpdate",
    "DocumentFileUpdateTypedDict",
    "DocumentGet",
    "DocumentGetMetadata",
    "DocumentGetMetadataTypedDict",
    "DocumentGetTypedDict",
    "DocumentList",
    "DocumentListTypedDict",
    "DocumentMetadata",
    "DocumentMetadataTypedDict",
    "DocumentMetadataUpdate",
    "DocumentMetadataUpdateMetadata",
    "DocumentMetadataUpdateMetadataTypedDict",
    "DocumentMetadataUpdateTypedDict",
    "DocumentRawUpdate",
    "DocumentRawUpdateTypedDict",
    "DocumentSummary",
    "DocumentSummaryTypedDict",
    "DocumentTypedDict",
    "Entity",
    "EntityList",
    "EntityListTypedDict",
    "EntityTypedDict",
    "ErrorMessage",
    "ErrorMessageData",
    "File",
    "FileTypedDict",
    "Filter",
    "FilterTypedDict",
    "GetConnectionConnectionsConnectionIDGetRequest",
    "GetConnectionConnectionsConnectionIDGetRequestTypedDict",
    "GetConnectionStatsConnectionsConnectionIDStatsGetRequest",
    "GetConnectionStatsConnectionsConnectionIDStatsGetRequestTypedDict",
    "GetDocumentRequest",
    "GetDocumentRequestTypedDict",
    "GetDocumentSummaryRequest",
    "GetDocumentSummaryRequestTypedDict",
    "HTTPValidationError",
    "HTTPValidationErrorData",
    "Instruction",
    "InstructionTypedDict",
    "ListConnectionsConnectionsGetRequest",
    "ListConnectionsConnectionsGetRequestTypedDict",
    "ListConnectionsConnectionsGetResponse",
    "ListConnectionsConnectionsGetResponseTypedDict",
    "ListDocumentsRequest",
    "ListDocumentsRequestTypedDict",
    "ListDocumentsResponse",
    "ListDocumentsResponseTypedDict",
    "ListEntitiesByDocumentRequest",
    "ListEntitiesByDocumentRequestTypedDict",
    "ListEntitiesByDocumentResponse",
    "ListEntitiesByDocumentResponseTypedDict",
    "ListEntitiesByInstructionRequest",
    "ListEntitiesByInstructionRequestTypedDict",
    "ListEntitiesByInstructionResponse",
    "ListEntitiesByInstructionResponseTypedDict",
    "Loc",
    "LocTypedDict",
    "Metadata",
    "MetadataTypedDict",
    "Mode",
    "OAuthURLCreate",
    "OAuthURLCreateMetadata",
    "OAuthURLCreateMetadataTypedDict",
    "OAuthURLCreateTypedDict",
    "OAuthURLResponse",
    "OAuthURLResponseTypedDict",
    "Pagination",
    "PaginationTypedDict",
    "PartitionStrategy",
    "PatchDocumentMetadataParams",
    "PatchDocumentMetadataParamsTypedDict",
    "PatchDocumentMetadataRequest",
    "PatchDocumentMetadataRequestTypedDict",
    "Retrieval",
    "RetrievalTypedDict",
    "RetrieveParams",
    "RetrieveParamsTypedDict",
    "SDKError",
    "Scope",
    "ScoredChunk",
    "ScoredChunkTypedDict",
    "Security",
    "SecurityTypedDict",
    "SetConnectionEnabledConnectionsConnectionIDEnabledPutRequest",
    "SetConnectionEnabledConnectionsConnectionIDEnabledPutRequestTypedDict",
    "SetConnectionEnabledPayload",
    "SetConnectionEnabledPayloadTypedDict",
    "Theme",
    "Two",
    "TwoTypedDict",
    "UpdateConnectionConnectionsConnectionIDPutRequest",
    "UpdateConnectionConnectionsConnectionIDPutRequestTypedDict",
    "UpdateDocumentFileParams",
    "UpdateDocumentFileParamsFile",
    "UpdateDocumentFileParamsFileTypedDict",
    "UpdateDocumentFileParamsMode",
    "UpdateDocumentFileParamsTypedDict",
    "UpdateDocumentFileRequest",
    "UpdateDocumentFileRequestTypedDict",
    "UpdateDocumentRawParams",
    "UpdateDocumentRawParamsData",
    "UpdateDocumentRawParamsDataTypedDict",
    "UpdateDocumentRawParamsTypedDict",
    "UpdateDocumentRawRequest",
    "UpdateDocumentRawRequestTypedDict",
    "UpdateInstructionParams",
    "UpdateInstructionParamsTypedDict",
    "UpdateInstructionRequest",
    "UpdateInstructionRequestTypedDict",
    "ValidationError",
    "ValidationErrorTypedDict",
]
